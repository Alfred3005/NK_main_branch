import os
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.patches as patches

parser = argparse.ArgumentParser()
parser.add_argument('--fdr_cutoff', type=float, default=0.25, help="FDR threshold for pathways")
parser.add_argument('--max_pathways', type=int, default=25, help="Max pathways to plot")
parser.add_argument('--output', type=str, required=True, help="Output path")
args = parser.parse_args()

# ==========================================
# 1. Configuración de Rutas
# ==========================================
BASE_DIR = r"C:\Users\PREDATOR\Documents\Antigravity_workspaces\NK_pipeline_RNA_ambient_Main_Branch\results\experiment_collinearity"

GSEA_DIR_DIM = os.path.join(BASE_DIR, "gsea", "cd56dim")
GSEA_DIR_BRIGHT = os.path.join(BASE_DIR, "gsea", "cd56bright")

DEA_DIM = os.path.join(BASE_DIR, "deseq2_results_nk_cd56dim.csv")
DEA_BRIGHT = os.path.join(BASE_DIR, "deseq2_results_nk_cd56bright.csv")

OUTPUT_PATH = os.path.join(BASE_DIR, args.output)

# Bases de datos
DB_NAMES = [
    'MSigDB_Hallmark_2020',
    'KEGG_2021_Human',
    'Reactome_2022',
    'GO_Biological_Process_2023'
]

# ==========================================
# 2. Carga y Preparación
# ==========================================
print("Cargando datos GSEA...")
def load_all_gsea(base_dir):
    dfs = []
    for db in DB_NAMES:
        path = os.path.join(base_dir, f"gsea_{db}.csv")
        if os.path.exists(path):
            df = pd.read_csv(path)
            df['DB'] = db
            dfs.append(df)
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    return pd.DataFrame()

gsea_dim = load_all_gsea(GSEA_DIR_DIM)
gsea_bright = load_all_gsea(GSEA_DIR_BRIGHT)

dea_dim = pd.read_csv(DEA_DIM).rename(columns={'feature_name': 'gene'}) if os.path.exists(DEA_DIM) else pd.DataFrame()
if 'Unnamed: 0' in dea_dim.columns and 'gene' not in dea_dim.columns:
    dea_dim = dea_dim.rename(columns={'Unnamed: 0': 'gene'})

dea_bright = pd.read_csv(DEA_BRIGHT).rename(columns={'feature_name': 'gene'}) if os.path.exists(DEA_BRIGHT) else pd.DataFrame()
if 'Unnamed: 0' in dea_bright.columns and 'gene' not in dea_bright.columns:
    dea_bright = dea_bright.rename(columns={'Unnamed: 0': 'gene'})

# ==========================================
# 3. Definir Firmas y Seleccionar Vías
# ==========================================
fdr_col_dim = 'FDR' if 'FDR' in gsea_dim.columns else 'FDR q-val'
fdr_col_bright = 'FDR' if 'FDR' in gsea_bright.columns else 'FDR q-val'

# Filtrar por cutoff
sig_dim_df = gsea_dim[gsea_dim[fdr_col_dim].astype(float) < args.fdr_cutoff]
sig_bright_df = gsea_bright[gsea_bright[fdr_col_bright].astype(float) < args.fdr_cutoff]

sig_dim = set(sig_dim_df['Term'])
sig_bright = set(sig_bright_df['Term'])

shared = sig_dim.intersection(sig_bright)
exclusive_dim = sig_dim - sig_bright
exclusive_bright = sig_bright - sig_dim

unordered_pathways = list(sig_dim.union(sig_bright))

# Ordenar por ABS(NES)
pathway_max_nes = {}
for term in unordered_pathways:
    val_dim = gsea_dim[gsea_dim['Term']==term]['NES'].abs().max() if not gsea_dim[gsea_dim['Term']==term].empty else 0
    val_bright = gsea_bright[gsea_bright['Term']==term]['NES'].abs().max() if not gsea_bright[gsea_bright['Term']==term].empty else 0
    pathway_max_nes[term] = max(val_dim, val_bright)

# Si el límite es < len(unordered_pathways), priorizar shared, luego los de mayor NES
# Para versión exploratoria
ordered_pathways = []
shared_sorted = sorted(list(shared), key=lambda x: pathway_max_nes[x], reverse=True)
dim_sorted = sorted(list(exclusive_dim), key=lambda x: pathway_max_nes[x], reverse=True)
bright_sorted = sorted(list(exclusive_bright), key=lambda x: pathway_max_nes[x], reverse=True)

ordered_pathways.extend(shared_sorted)
# Intercalar dim y bright para llenar hasta max_pathways
idx_d, idx_b = 0, 0
while len(ordered_pathways) < args.max_pathways and (idx_d < len(dim_sorted) or idx_b < len(bright_sorted)):
    if idx_d < len(dim_sorted):
        ordered_pathways.append(dim_sorted[idx_d])
        idx_d += 1
    if len(ordered_pathways) >= args.max_pathways:
        break
    if idx_b < len(bright_sorted):
        ordered_pathways.append(bright_sorted[idx_b])
        idx_b += 1

# Recortar estrictamente al máximo
ordered_pathways = ordered_pathways[:args.max_pathways]

if len(ordered_pathways) == 0:
    print("No hay vías significativas para graficar.")
    exit(0)

pathway_signatures = []
for p in ordered_pathways:
    if p in exclusive_dim:
        pathway_signatures.append('Dim Exclusive')
    elif p in exclusive_bright:
        pathway_signatures.append('Bright Exclusive')
    else:
        pathway_signatures.append('Shared')

# ==========================================
# 4. Extracción de Genes
# ==========================================
gene_pool = set()
pathway_genes_dim = {}
pathway_genes_bright = {}

for term in ordered_pathways:
    genes_d = set()
    genes_b = set()
    
    row_d = gsea_dim[gsea_dim['Term'] == term]
    lead_col_d = 'Lead_genes' if 'Lead_genes' in row_d.columns else 'core_enrichment'
    if not row_d.empty and pd.notna(row_d.iloc[0].get(lead_col_d)):
        genes_d.update(str(row_d.iloc[0][lead_col_d]).split(';'))
        
    row_b = gsea_bright[gsea_bright['Term'] == term]
    lead_col_b = 'Lead_genes' if 'Lead_genes' in row_b.columns else 'core_enrichment'
    if not row_b.empty and pd.notna(row_b.iloc[0].get(lead_col_b)):
        genes_b.update(str(row_b.iloc[0][lead_col_b]).split(';'))
        
    genes_d = [g.split('/')[0] for g in genes_d if g]
    genes_b = [g.split('/')[0] for g in genes_b if g]

    genes_d = list(set(genes_d))[:8]
    genes_b = list(set(genes_b))[:8]
    
    pathway_genes_dim[term] = genes_d
    pathway_genes_bright[term] = genes_b
    
    gene_pool.update(genes_d)
    gene_pool.update(genes_b)

ordered_genes = sorted(list(gene_pool))

# ==========================================
# 5. Construcción de Matrices
# ==========================================
presence_matrix = np.zeros((len(ordered_pathways), len(ordered_genes)))
for i, term in enumerate(ordered_pathways):
    for j, gene in enumerate(ordered_genes):
        in_dim = gene in pathway_genes_dim[term]
        in_bright = gene in pathway_genes_bright[term]
        if in_dim and in_bright:
            presence_matrix[i, j] = 3
        elif in_dim:
            presence_matrix[i, j] = 1
        elif in_bright:
            presence_matrix[i, j] = 2

lfc_matrix = np.zeros((2, len(ordered_genes)))
for j, gene in enumerate(ordered_genes):
    row_d = dea_dim[dea_dim['gene'] == gene]
    lfc_matrix[0, j] = row_d.iloc[0]['log2FoldChange'] if not row_d.empty else 0
    
    row_b = dea_bright[dea_bright['gene'] == gene]
    lfc_matrix[1, j] = row_b.iloc[0]['log2FoldChange'] if not row_b.empty else 0

nes_dim = []
nes_bright = []
fdr_dim = []
fdr_bright = []

for term in ordered_pathways:
    row_d = gsea_dim[gsea_dim['Term'] == term]
    row_b = gsea_bright[gsea_bright['Term'] == term]
    
    nes_dim.append(row_d.iloc[0]['NES'] if not row_d.empty else 0)
    nes_bright.append(row_b.iloc[0]['NES'] if not row_b.empty else 0)
    
    fdr_dim.append(row_d.iloc[0][fdr_col_dim] if not row_d.empty else 1.0)
    fdr_bright.append(row_b.iloc[0][fdr_col_bright] if not row_b.empty else 1.0)

# ==========================================
# 6. Renderizado
# ==========================================
print(f"Generando Gráfico Estilo g:Profiler (FDR < {args.fdr_cutoff})...")
fig = plt.figure(figsize=(30, max(8, len(ordered_pathways) * 0.5 + 5)))

gs = GridSpec(3, 4, 
              height_ratios=[0.12, 0.03, 1], 
              width_ratios=[1.5, 1.5, 1.0, 13], 
              wspace=0.05, hspace=0.0)

# PANEL LFC
ax_lfc = fig.add_subplot(gs[0, 3])
sns.heatmap(lfc_matrix, cmap="RdBu_r", center=0, vmin=-3, vmax=3, 
            cbar=False, ax=ax_lfc, xticklabels=False, yticklabels=['LFC CD56dim', 'LFC CD56bright'],
            linewidths=0.5, linecolor='white')
ax_lfc.tick_params(axis='y', rotation=0, labelsize=10)
ax_lfc.set_title(f"Anotación de Expresión Génica (LogFoldChange) - Corte FDR < {args.fdr_cutoff}", pad=15, fontsize=14, fontweight='bold')

# PANEL MATRIZ
ax_mat = fig.add_subplot(gs[2, 3])
cmap_presence = ListedColormap(['#f4f4f4', '#007bff', '#ffc107', '#28a745'])
bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
norm = BoundaryNorm(bounds, cmap_presence.N)

sns.heatmap(presence_matrix, cmap=cmap_presence, norm=norm, 
            cbar=False, ax=ax_mat, 
            xticklabels=ordered_genes, yticklabels=False,
            linewidths=0.5, linecolor='white')
ax_mat.tick_params(axis='x', rotation=90, labelsize=9)

# PANEL BARPLOT
ax_bar = fig.add_subplot(gs[2, 1])
y_pos = np.arange(len(ordered_pathways))
height = 0.35

ax_bar.barh(y_pos - height/2, nes_dim, height, color='#007bff', label='CD56dim NES', edgecolor='white')
ax_bar.barh(y_pos + height/2, nes_bright, height, color='#ffc107', label='CD56bright NES', edgecolor='white')

ax_bar.set_yticks(y_pos)
ax_bar.set_yticklabels([])
ax_bar.invert_yaxis()
ax_bar.axvline(0, color='black', linewidth=1)
ax_bar.set_xlabel("NES")
ax_bar.legend(loc='upper left', bbox_to_anchor=(0, 1.15), frameon=False)

# PANEL FDR
ax_fdr = fig.add_subplot(gs[2, 2])
ax_fdr.axis('off')
ax_fdr.set_ylim(ax_bar.get_ylim())

ax_fdr.text(0.2, -0.7, "FDR\n(Dim)", ha='center', va='bottom', fontsize=10, fontweight='bold', color='#007bff')
ax_fdr.text(0.8, -0.7, "FDR\n(Bright)", ha='center', va='bottom', fontsize=10, fontweight='bold', color='#d4a000')

for i, (fd, fb) in enumerate(zip(fdr_dim, fdr_bright)):
    text_d = f"{fd:.1e}" if fd < 0.001 else f"{fd:.3f}"
    text_b = f"{fb:.1e}" if fb < 0.001 else f"{fb:.3f}"
    if fd >= 1.0: text_d = "-"
    if fb >= 1.0: text_b = "-"
    fw_d = 'bold' if fd < 0.05 else 'normal'
    fw_b = 'bold' if fb < 0.05 else 'normal'
    ax_fdr.text(0.2, i, text_d, ha='center', va='center', fontsize=10, color='black', fontweight=fw_d)
    ax_fdr.text(0.8, i, text_b, ha='center', va='center', fontsize=10, color='black', fontweight=fw_b)

# PANEL LABELS
ax_labels = fig.add_subplot(gs[2, 0])
ax_labels.axis('off')
ax_labels.set_ylim(ax_bar.get_ylim())

for i, (term, sig) in enumerate(zip(ordered_pathways, pathway_signatures)):
    clean_term = term.replace("HALLMARK_", "").replace("_", " ")
    if len(clean_term) > 35:
        clean_term = clean_term[:32] + "..."
    color = '#007bff' if sig == 'Dim Exclusive' else '#d4a000' if sig == 'Bright Exclusive' else '#28a745'
    ax_labels.text(0.95, i, clean_term, va='center', ha='right', fontsize=9, fontweight='bold', color=color, transform=ax_labels.transData)

legend_patches = [
    patches.Patch(color='#007bff', label='Gen Líder CD56dim'),
    patches.Patch(color='#ffc107', label='Gen Líder CD56bright'),
    patches.Patch(color='#28a745', label='Gen Líder Ambos')
]
fig.legend(handles=legend_patches, loc='upper center', ncol=3, bbox_to_anchor=(0.5, 0.05), frameon=False)

plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches='tight', pad_inches=0.5)
print(f"Gráfico guardado en: {OUTPUT_PATH}")
