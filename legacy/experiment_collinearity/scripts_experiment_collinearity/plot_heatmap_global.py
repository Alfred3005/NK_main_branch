import os
import scanpy as sc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. Configuración de Rutas
# ==========================================
BASE_DIR = r"C:\Users\PREDATOR\Documents\Antigravity_workspaces\NK_pipeline_RNA_ambient_Main_Branch"
DATA_PATH = os.path.join(BASE_DIR, "data", "NK_dataset_qc_ready.h5ad")
RESULTS_DIR = os.path.join(BASE_DIR, "results", "experiment_collinearity")
DEA_RESULTS = os.path.join(RESULTS_DIR, "deseq2_results_significant_nk_cell_general.csv")

OUTPUT_SC = os.path.join(RESULTS_DIR, "heatmap_23_hits_single_cell.png")
OUTPUT_PB = os.path.join(RESULTS_DIR, "heatmap_23_hits_pseudobulk.png")

os.makedirs(RESULTS_DIR, exist_ok=True)

# ==========================================
# 2. Cargar Genes Significativos (Hits)
# ==========================================
print(f"Cargando DEGs desde: {DEA_RESULTS}")
try:
    dea_df = pd.read_csv(DEA_RESULTS)
    # Dependiendo de la versión de script, la columna puede ser feature_name o Unnamed: 0
    gene_col = 'feature_name' if 'feature_name' in dea_df.columns else dea_df.columns[0]
    hits = dea_df[gene_col].tolist()
    print(f"[OK] Se encontraron {len(hits)} genes significativos.")
except Exception as e:
    print(f"[ERROR] Error al cargar los resultados DEA: {e}")
    exit(1)

# ==========================================
# 3. Cargar Dataset Single-Cell y Filtrar
# ==========================================
print(f"Cargando dataset: {DATA_PATH}")
adata = sc.read_h5ad(DATA_PATH)

# Filtrar para retener solo los ensayos válidos que se usaron en el DEA estricto
# Replicando el filtrado del script 22:
bright_name = 'CD16-negative, CD56-bright natural killer cell, human'
dim_name = 'CD16-positive, CD56-dim natural killer cell, human'
counts = adata.obs.groupby(['assay', 'cell_type']).size().unstack(fill_value=0)
valid_assays = []
for assay in counts.index:
    n_bright = counts.loc[assay, bright_name] if bright_name in counts.columns else 0
    n_dim = counts.loc[assay, dim_name] if dim_name in counts.columns else 0
    if n_bright >= 10 and n_dim >= 10:
        valid_assays.append(assay)

adata = adata[adata.obs['assay'].isin(valid_assays)].copy()
print(f"[OK] Dataset filtrado por colinealidad (ensayos: {valid_assays}). Células restantes: {adata.n_obs}")

# Asegurar que los genes Hits están en el dataset
hits = [g for g in hits if g in adata.var_names]
print(f"Genes disponibles para heatmap: {len(hits)}")

# Asegurarse de tener una capa log1p normalizada para el single-cell
if 'log1p' not in adata.uns:
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)

# ==========================================
# 4. Heatmap Pseudobulk (Agrupado por Donante)
# ==========================================
print("Generando Heatmap Pseudobulk (por Donante)...")
# Agrupar conteos puros por donante para replicar PyDESeq2
df_counts = pd.DataFrame(adata.X.toarray() if hasattr(adata.X, "toarray") else adata.X, 
                         index=adata.obs_names, columns=adata.var_names)
df_counts['donor_id'] = adata.obs['donor_id'].values

# Sumar conteos por donante
pb_counts = df_counts.groupby('donor_id').sum()

# Filtrar solo los genes significativos
pb_counts = pb_counts[hits]

# Normalización por tamaño de biblioteca (CPM) para visualización
lib_size = pb_counts.sum(axis=1)
pb_cpm = pb_counts.div(lib_size, axis=0) * 1e6
# Aplicar log2(CPM + 1)
pb_log = np.log2(pb_cpm + 1)

# Extraer el age_group de cada donante
age_dict = adata.obs.groupby('donor_id')['age_group'].first().to_dict()
# Ordenar donantes primero por grupo de edad para mejor visualización
pb_log['age_group'] = pb_log.index.map(age_dict)
pb_log = pb_log.sort_values('age_group')
age_series = pb_log['age_group']
pb_log = pb_log.drop(columns=['age_group'])

# Asignar colores a los grupos de edad
age_groups = age_series.unique()
colors = sns.color_palette("Set1", len(age_groups))
lut = dict(zip(age_groups, colors))
row_colors = age_series.map(lut)

# Crear Clustermap jerárquico
g = sns.clustermap(
    pb_log,
    row_colors=row_colors,
    row_cluster=False, # Ya ordenados por grupo de edad
    col_cluster=True,  # Agrupar genes por co-expresión
    cmap="RdBu_r",
    z_score=1, # Z-score verdadero por columna (gen)
    center=0,
    vmin=-2.5,
    vmax=2.5,
    figsize=(12, 10),
    cbar_pos=(0.02, 0.8, 0.03, 0.18),
    linewidths=0.5,
    xticklabels=True,
    yticklabels=False,
    tree_kws=dict(linewidths=1.5)
)

g.fig.suptitle("Heatmap Pseudobulk - 23 Hits Globales (Z-Score)", y=1.02, fontsize=14, weight='bold')
g.ax_cbar.set_title("Z-Score\n(Log2 CPM)")

# Añadir leyenda manual
from matplotlib.patches import Patch
handles = [Patch(facecolor=lut[name]) for name in lut]
plt.legend(handles, lut, title='Age Group',
           bbox_to_anchor=(1.05, 1), bbox_transform=plt.gcf().transFigure, loc='upper left')

plt.savefig(OUTPUT_PB, dpi=300, bbox_inches='tight')
plt.close()
print(f"[OK] Guardado en: {OUTPUT_PB}")

# ==========================================
# 5. Matriz Colapsada de Z-Scores Promedio
# ==========================================
print("Generando Heatmap Colapsado (Promedio de Z-Scores Pseudobulk)...")

OUTPUT_COLLAPSED = os.path.join(RESULTS_DIR, "heatmap_23_hits_collapsed.png")

from scipy.stats import zscore

# Calcular Z-score por columna (gen) a través de todos los donantes
pb_zscore = pb_log.apply(zscore)

# Añadir grupo de edad para agrupar
pb_zscore['age_group'] = age_series

# Calcular el Z-score mediano por grupo de edad (robusto frente a outliers)
pb_zscore_median = pb_zscore.groupby('age_group').median()

# Asegurar que adult quede arriba y old abajo
if 'adult' in pb_zscore_median.index and 'old' in pb_zscore_median.index:
    pb_zscore_median = pb_zscore_median.reindex(['adult', 'old'])

# Agrupar genes usando el orden del clustermap anterior (g.dendrogram_col.reordered_ind)
ordered_genes = pb_log.columns[g.dendrogram_col.reordered_ind]
pb_zscore_median = pb_zscore_median[ordered_genes]

# Determinar límites simétricos dinámicos basados en los valores reales para no tener colores deslavados
max_val = np.abs(pb_zscore_median.values).max()

plt.figure(figsize=(14, 3))
sns.heatmap(
    pb_zscore_median,
    cmap="RdBu_r",
    center=0,
    vmin=-max_val,
    vmax=max_val,
    annot=False,
    cbar_kws={'label': 'Z-Score Mediano'},
    linewidths=1,
    linecolor='black'
)
plt.title("Z-Score Mediano de Pseudobulk (23 Hits Globales)", weight='bold', pad=15)
plt.yticks(rotation=0, weight='bold', size=12)
plt.xticks(rotation=45, ha='right', size=10)
plt.tight_layout()
plt.savefig(OUTPUT_COLLAPSED, dpi=300)
plt.close()
print(f"[OK] Guardado en: {OUTPUT_COLLAPSED}")
