import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.patches as patches

# ==========================================
# 1. Configuración de Rutas
# ==========================================
BASE_DIR = r"C:\Users\PREDATOR\Documents\Antigravity_workspaces\NK_pipeline_RNA_ambient_Main_Branch\results\subtypes"

GSEA_DIM = os.path.join(BASE_DIR, "gsea", "cd56dim", "gsea_MSigDB_Hallmark_2020.csv")
GSEA_BRIGHT = os.path.join(BASE_DIR, "gsea", "cd56bright", "gsea_MSigDB_Hallmark_2020.csv")

DEA_DIM = os.path.join(BASE_DIR, "deseq2_results_nk_cd56dim.csv")
DEA_BRIGHT = os.path.join(BASE_DIR, "deseq2_results_nk_cd56bright.csv")

OUTPUT_PATH = os.path.join(BASE_DIR, "gProfiler_Style_Comparative_Plot_v6.png")

# ==========================================
# 2. Carga y Preparación
# ==========================================
print("Cargando datos...")
gsea_dim = pd.read_csv(GSEA_DIM)
gsea_bright = pd.read_csv(GSEA_BRIGHT)

dea_dim = pd.read_csv(DEA_DIM).rename(columns={'feature_name': 'gene'})
dea_bright = pd.read_csv(DEA_BRIGHT).rename(columns={'feature_name': 'gene'})

# ==========================================
# 3. Definir Firmas y Seleccionar Vías
# ==========================================
# Seleccionamos todas las vías que superen FDR < 0.25 en CUALQUIERA de los subtipos
sig_dim = set(gsea_dim[gsea_dim['FDR'].astype(float) < 0.25]['Term']) if 'FDR' in gsea_dim.columns else set()
if not sig_dim and 'FDR q-val' in gsea_dim.columns:
    sig_dim = set(gsea_dim[gsea_dim['FDR q-val'].astype(float) < 0.25]['Term'])

sig_bright = set(gsea_bright[gsea_bright['FDR'].astype(float) < 0.25]['Term']) if 'FDR' in gsea_bright.columns else set()
if not sig_bright and 'FDR q-val' in gsea_bright.columns:
    sig_bright = set(gsea_bright[gsea_bright['FDR q-val'].astype(float) < 0.25]['Term'])

shared = sig_dim.intersection(sig_bright)
exclusive_dim = sig_dim - sig_bright
exclusive_bright = sig_bright - sig_dim

# Union de todas las vías significativas
unordered_pathways = list(sig_dim.union(sig_bright))

# Ordenarlas por mayor ABS(NES) para que el gráfico luzca organizado
pathway_max_nes = {}
fdr_col_dim = 'FDR' if 'FDR' in gsea_dim.columns else 'FDR q-val'
fdr_col_bright = 'FDR' if 'FDR' in gsea_bright.columns else 'FDR q-val'

for term in unordered_pathways:
    val_dim = gsea_dim[gsea_dim['Term']==term]['NES'].abs().max() if not gsea_dim[gsea_dim['Term']==term].empty else 0
    val_bright = gsea_bright[gsea_bright['Term']==term]['NES'].abs().max() if not gsea_bright[gsea_bright['Term']==term].empty else 0
    pathway_max_nes[term] = max(val_dim, val_bright)

ordered_pathways = sorted(unordered_pathways, key=lambda x: pathway_max_nes[x], reverse=True)

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
    # In newer gseapy it might be Lead_genes or core_enrichment
    lead_col_d = 'Lead_genes' if 'Lead_genes' in row_d.columns else 'core_enrichment'
    if not row_d.empty and pd.notna(row_d.iloc[0].get(lead_col_d)):
        genes_d.update(str(row_d.iloc[0][lead_col_d]).split(';'))
        
    row_b = gsea_bright[gsea_bright['Term'] == term]
    lead_col_b = 'Lead_genes' if 'Lead_genes' in row_b.columns else 'core_enrichment'
    if not row_b.empty and pd.notna(row_b.iloc[0].get(lead_col_b)):
        genes_b.update(str(row_b.iloc[0][lead_col_b]).split(';'))
        
    # Extraer top genes limpios (a veces separan por slash)
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
# 6. Renderizado (Complejo)
# ==========================================
print("Generando Gráfico Estilo g:Profiler v6 (Español)...")
fig = plt.figure(figsize=(40, max(8, len(ordered_pathways) * 0.5 + 5)))

gs = GridSpec(3, 4, 
              height_ratios=[0.12, 0.03, 1], 
              width_ratios=[1.5, 1.5, 1.0, 13], 
              wspace=0.05, hspace=0.0)

# ---- PANEL SUPERIOR: Anotación LFC ----
ax_lfc = fig.add_subplot(gs[0, 3])
sns.heatmap(lfc_matrix, cmap="RdBu_r", center=0, vmin=-3, vmax=3, 
            cbar=False, ax=ax_lfc, xticklabels=False, yticklabels=['LFC CD56dim', 'LFC CD56bright'],
            linewidths=0.5, linecolor='white')
ax_lfc.tick_params(axis='y', rotation=0, labelsize=10)
ax_lfc.set_title("Anotación de Expresión Génica (LogFoldChange)", pad=15, fontsize=14, fontweight='bold')

# ---- PANEL CENTRAL-DERECHO: Matriz de Presencia ----
ax_mat = fig.add_subplot(gs[2, 3])
cmap_presence = ListedColormap(['#f4f4f4', '#007bff', '#ffc107', '#28a745'])
bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
norm = BoundaryNorm(bounds, cmap_presence.N)

sns.heatmap(presence_matrix, cmap=cmap_presence, norm=norm, 
            cbar=False, ax=ax_mat, 
            xticklabels=ordered_genes, yticklabels=False,
            linewidths=0.5, linecolor='white')

ax_mat.tick_params(axis='x', rotation=90, labelsize=9)

# ---- PANEL CENTRAL-IZQUIERDO: Barplot ----
ax_bar = fig.add_subplot(gs[2, 1])
y_pos = np.arange(len(ordered_pathways))
height = 0.35

ax_bar.barh(y_pos - height/2, nes_dim, height, color='#007bff', label='CD56dim NES', edgecolor='white')
ax_bar.barh(y_pos + height/2, nes_bright, height, color='#ffc107', label='CD56bright NES', edgecolor='white')

ax_bar.set_yticks(y_pos)
ax_bar.set_yticklabels([])
ax_bar.invert_yaxis()
ax_bar.axvline(0, color='black', linewidth=1)
ax_bar.set_xlabel("Puntaje de Enriquecimiento Normalizado (NES)")
ax_bar.legend(loc='upper left', bbox_to_anchor=(0, 1.15), frameon=False)

# ---- PANEL CENTRAL-MEDIO: Valores FDR ----
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
    
    # Diferenciar los robustos (FDR < 0.05) con negritas
    fw_d = 'bold' if fd < 0.05 else 'normal'
    fw_b = 'bold' if fb < 0.05 else 'normal'
    
    ax_fdr.text(0.2, i, text_d, ha='center', va='center', fontsize=10, color='black', fontweight=fw_d)
    ax_fdr.text(0.8, i, text_b, ha='center', va='center', fontsize=10, color='black', fontweight=fw_b)

# ---- PANEL IZQUIERDO: Labels y Agrupaciones ----
ax_labels = fig.add_subplot(gs[2, 0])
ax_labels.axis('off')
ax_labels.set_ylim(ax_bar.get_ylim())

for i, (term, sig) in enumerate(zip(ordered_pathways, pathway_signatures)):
    clean_term = term.replace("HALLMARK_", "").replace("_", " ")
    
    if sig == 'Dim Exclusive':
        color = '#007bff'
    elif sig == 'Bright Exclusive':
        color = '#d4a000'
    else:
        color = '#28a745'
        
    ax_labels.text(0.95, i, clean_term, va='center', ha='right', 
                   fontsize=10, fontweight='bold', color=color,
                   transform=ax_labels.transData)

import matplotlib.patches as mpatches
legend_patches = [
    mpatches.Patch(color='#007bff', label='Gen Líder en CD56dim'),
    mpatches.Patch(color='#ffc107', label='Gen Líder en CD56bright'),
    mpatches.Patch(color='#28a745', label='Gen Líder en Ambos')
]
fig.legend(handles=legend_patches, loc='upper center', ncol=3, bbox_to_anchor=(0.5, 0.05), frameon=False)

plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches='tight', pad_inches=0.5)
print(f"Gráfico guardado en: {OUTPUT_PATH}")
