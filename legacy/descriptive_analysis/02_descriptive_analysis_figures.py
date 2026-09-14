import os
import scanpy as sc
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Configuración estacional y tipográfica para calidad de publicación
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'

def run_descriptive_figures():
    data_path = 'data/NK_dataset_qc_ready.h5ad'
    out_dir = 'results/descriptive_analysis_v5/figures'
    os.makedirs(out_dir, exist_ok=True)
    
    print(f"Cargando dataset preprocesado desde {data_path}...")
    adata = sc.read_h5ad(data_path)

    # Filtrado estricto de cohortes por edad (Lehallier et al., 2019)
    # Adultos: 34 a 59 años | Adultos Mayores: 60+ años
    adata = adata[(adata.obs['age'] >= 34)].copy()
    
    # Reasignar age_group y traducir al español
    adata.obs['age_group'] = np.where(adata.obs['age'] >= 60, 'Adultos Mayores', 'Adultos')
    adata.obs['age_group'] = adata.obs['age_group'].astype('category')
    adata.obs['age_group'] = adata.obs['age_group'].cat.reorder_categories(['Adultos', 'Adultos Mayores'])
    
    print(f"Dataset cargado: {adata.n_obs:,} células × {adata.n_vars:,} genes.")

    # Mapeo de Subtipos Canónicos NK
    subtypes_map = {
        'CD16-positive, CD56-dim natural killer cell, human': 'CD56dim',
        'CD16-negative, CD56-bright natural killer cell, human': 'CD56bright',
        'natural killer cell': 'CD56dim'
    }
    adata.obs['subtypes'] = adata.obs['cell_type'].map(subtypes_map).fillna('CD56dim').astype('category')
    print("Distribución de Subtipos en Dataset:")
    print(adata.obs['subtypes'].value_counts())

    # Asegurar UMAP latente en obsm
    if 'X_umap' not in adata.obsm:
        print("Generando proyección UMAP para visualización gráfica...")
        sc.pp.normalize_total(adata, target_sum=1e4)
        sc.pp.log1p(adata)
        sc.pp.highly_variable_genes(adata, n_top_genes=2000)
        sc.tl.pca(adata, svd_solver='arpack')
        sc.pp.neighbors(adata, n_neighbors=15, n_pcs=30)
        sc.tl.umap(adata)

    # --- FIGURA 1A: Demografía de Cohorte (Donantes por Edad, Sexo y Ensayo) ---
    print("\nGenerando Figura 1A: Demografía de Cohorte...")
    donor_meta = adata.obs[['donor_id', 'age_group', 'sex', 'assay', 'age']].drop_duplicates(subset=['donor_id'])
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # 1A.1: Donantes por Grupo de Edad y Sexo
    sex_counts = donor_meta.groupby(['age_group', 'sex'], observed=False).size().unstack(fill_value=0)
    sex_counts.plot(kind='bar', stacked=True, ax=axes[0], color=['#38bdf8', '#f472b6'], edgecolor='black', linewidth=0.8)
    axes[0].set_title("Distribución de Donantes por Edad y Sexo", fontsize=12, fontweight='bold')
    axes[0].set_xlabel("Grupo de Edad", fontsize=10, fontweight='bold')
    axes[0].set_ylabel("Número de Donantes", fontsize=10, fontweight='bold')
    axes[0].tick_params(axis='x', rotation=0)
    axes[0].legend(title="Sexo", frameon=True)
    for p in axes[0].patches:
        height = p.get_height()
        if height > 0:
            axes[0].annotate(f"{int(height)}", (p.get_x() + p.get_width() / 2., p.get_y() + height / 2.),
                             ha='center', va='center', fontsize=9, fontweight='bold', color='black')

    # 1A.2: Donantes por Ensayo (Plataforma 10x Genomics)
    assay_counts = donor_meta.groupby(['age_group', 'assay'], observed=False).size().unstack(fill_value=0)
    assay_counts.plot(kind='bar', stacked=True, ax=axes[1], cmap='Set2', edgecolor='black', linewidth=0.8)
    axes[1].set_title("Distribución de Donantes por Tecnología (Assay)", fontsize=12, fontweight='bold')
    axes[1].set_xlabel("Grupo de Edad", fontsize=10, fontweight='bold')
    axes[1].set_ylabel("Número de Donantes", fontsize=10, fontweight='bold')
    axes[1].tick_params(axis='x', rotation=0)
    axes[1].legend(title="Ensayo (10x)", frameon=True)
    for p in axes[1].patches:
        height = p.get_height()
        if height > 0:
            axes[1].annotate(f"{int(height)}", (p.get_x() + p.get_width() / 2., p.get_y() + height / 2.),
                             ha='center', va='center', fontsize=8, fontweight='bold', color='black')

    plt.tight_layout()
    fig1a_png = os.path.join(out_dir, "Figura_1A_Demografia_Cohorte.png")
    fig1a_svg = os.path.join(out_dir, "Figura_1A_Demografia_Cohorte.svg")
    plt.savefig(fig1a_png)
    plt.savefig(fig1a_svg)
    plt.close()
    print(f"  --> Guardada en: {fig1a_png}")

    # --- FIGURA 1B: Métricas de QC y Purificación Ambient ---
    print("\nGenerando Figura 1B: Métricas QC y Purificación...")
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))
    
    # Subplot 1: Total Counts (UMIs) por Edad
    sns.violinplot(data=adata.obs, x='age_group', y='total_counts', hue='assay', ax=axes[0], palette='Blues', inner='quartile')
    axes[0].set_title("Cuentas Totales por Célula (UMIs)", fontsize=11, fontweight='bold')
    axes[0].set_xlabel("Grupo de Edad", fontsize=9, fontweight='bold')
    axes[0].set_ylabel("UMIs Totales", fontsize=9, fontweight='bold')
    axes[0].legend(title="Ensayo", fontsize=8)

    # Subplot 2: Genes Detectados por Célula
    sns.violinplot(data=adata.obs, x='age_group', y='n_genes_by_counts', hue='assay', ax=axes[1], palette='Greens', inner='quartile')
    axes[1].set_title("Genes Detectados por Célula", fontsize=11, fontweight='bold')
    axes[1].set_xlabel("Grupo de Edad", fontsize=9, fontweight='bold')
    axes[1].set_ylabel("N° de Genes", fontsize=9, fontweight='bold')
    axes[1].legend(title="Ensayo", fontsize=8)

    # Subplot 3: Porcentaje Mitocondrial
    sns.violinplot(data=adata.obs, x='age_group', y='pct_counts_mito', hue='assay', ax=axes[2], palette='Oranges', inner='quartile')
    axes[2].set_title("Porcentaje Mitocondrial (%)", fontsize=11, fontweight='bold')
    axes[2].set_xlabel("Grupo de Edad", fontsize=9, fontweight='bold')
    axes[2].set_ylabel("% Cuentas MT", fontsize=9, fontweight='bold')
    axes[2].legend(title="Ensayo", fontsize=8)

    plt.tight_layout()
    fig1b_png = os.path.join(out_dir, "Figura_1B_QC_Purificacion_Metrics.png")
    fig1b_svg = os.path.join(out_dir, "Figura_1B_QC_Purificacion_Metrics.svg")
    plt.savefig(fig1b_png)
    plt.savefig(fig1b_svg)
    plt.close()
    print(f"  --> Guardada en: {fig1b_png}")

    # --- FIGURA 2A & 2B: UMAPs Latentes scVI ---
    print("\nGenerando Figura 2A & 2B: UMAPs Latentes scVI...")
    
    # 2A: Color por Assay
    fig, ax = plt.subplots(figsize=(6.5, 5.5))
    sc.pl.umap(adata, color='assay', title="Espacio Latente (Coloreado por Assay/Lote)",
               show=False, ax=ax, frameon=True, palette='Set2')
    ax.set_xlabel("UMAP 1", fontsize=10, fontweight='bold')
    ax.set_ylabel("UMAP 2", fontsize=10, fontweight='bold')
    fig2a_png = os.path.join(out_dir, "Figura_2A_scVI_UMAP_Assay.png")
    fig2a_svg = os.path.join(out_dir, "Figura_2A_scVI_UMAP_Assay.svg")
    plt.savefig(fig2a_png)
    plt.savefig(fig2a_svg)
    plt.close()
    print(f"  --> Guardada en: {fig2a_png}")

    # 2B: Color por Age Group
    fig, ax = plt.subplots(figsize=(6.5, 5.5))
    sc.pl.umap(adata, color='age_group', title="Espacio Latente (Coloreado por Grupo de Edad)",
               show=False, ax=ax, frameon=True, palette=['#0284c7', '#e11d48'])
    ax.set_xlabel("UMAP 1", fontsize=10, fontweight='bold')
    ax.set_ylabel("UMAP 2", fontsize=10, fontweight='bold')
    fig2b_png = os.path.join(out_dir, "Figura_2B_scVI_UMAP_AgeGroup.png")
    fig2b_svg = os.path.join(out_dir, "Figura_2B_scVI_UMAP_AgeGroup.svg")
    plt.savefig(fig2b_png)
    plt.savefig(fig2b_svg)
    plt.close()
    print(f"  --> Guardada en: {fig2b_png}")

    # --- FIGURA 3A: UMAP por Subtipos NK ---
    print("\nGenerando Figura 3A: UMAP de Subtipos NK...")
    fig, ax = plt.subplots(figsize=(6.5, 5.5))
    sc.pl.umap(adata, color='subtypes', title="Subpoblaciones NK (CD56dim vs CD56bright)",
               show=False, ax=ax, frameon=True, palette=['#2563eb', '#10b981'])
    ax.set_xlabel("UMAP 1", fontsize=10, fontweight='bold')
    ax.set_ylabel("UMAP 2", fontsize=10, fontweight='bold')
    fig3a_png = os.path.join(out_dir, "Figura_3A_UMAP_Subtipos_NK.png")
    fig3a_svg = os.path.join(out_dir, "Figura_3A_UMAP_Subtipos_NK.svg")
    plt.savefig(fig3a_png)
    plt.savefig(fig3a_svg)
    plt.close()
    print(f"  --> Guardada en: {fig3a_png}")

    # --- FIGURA 3B: Dotplot de Marcadores Canónicos ---
    print("\nGenerando Figura 3B: Dotplot de Marcadores Canónicos...")
    canonical_markers = ['NCAM1', 'FCGR3A', 'GZMB', 'NKG7', 'PRF1', 'GNLY', 'SELL', 'XCL1', 'KIR3DL1', 'KIR3DL2', 'KLRC1']
    available_markers = [g for g in canonical_markers if g in adata.var_names]
    
    dp = sc.pl.dotplot(adata, var_names=available_markers, groupby='subtypes',
                       title="Expresión de Marcadores Canónicos por Subtipo NK",
                       cmap='Blues', standard_scale='var', show=False)
    fig3b_png = os.path.join(out_dir, "Figura_3B_Dotplot_Marcadores_Canonicos.png")
    fig3b_svg = os.path.join(out_dir, "Figura_3B_Dotplot_Marcadores_Canonicos.svg")
    dp['mainplot_ax'].figure.savefig(fig3b_png, bbox_inches='tight', dpi=300)
    dp['mainplot_ax'].figure.savefig(fig3b_svg, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"  --> Guardada en: {fig3b_png}")

    # --- FIGURA 3C: Proporción de Subtipos por Donante ---
    print("\nGenerando Figura 3C: Proporciones de Subtipos por Donante...")
    props = adata.obs.groupby(['donor_id', 'age_group', 'subtypes'], observed=False).size().unstack(fill_value=0)
    props['total'] = props.sum(axis=1)
    props['pct_CD56bright'] = (props['CD56bright'] / props['total']) * 100
    props = props.reset_index()

    plt.figure(figsize=(6, 5))
    sns.boxplot(data=props, x='age_group', y='pct_CD56bright', palette=['#38bdf8', '#f87171'], width=0.4, boxprops=dict(alpha=0.8))
    sns.stripplot(data=props, x='age_group', y='pct_CD56bright', color='black', alpha=0.5, jitter=0.2, size=4)
    plt.title("Proporción de Células NK CD56bright por Donante (%)", fontsize=11, fontweight='bold')
    plt.xlabel("Grupo de Edad", fontsize=10, fontweight='bold')
    plt.ylabel("% CD56bright / Total NK", fontsize=10, fontweight='bold')
    
    fig3c_png = os.path.join(out_dir, "Figura_3C_Proporciones_CD56bright_Donante.png")
    fig3c_svg = os.path.join(out_dir, "Figura_3C_Proporciones_CD56bright_Donante.svg")
    plt.savefig(fig3c_png)
    plt.savefig(fig3c_svg)
    plt.close()
    print(f"  --> Guardada en: {fig3c_png}")

    print("\n[OK] Todas las figuras descriptivas han sido generadas con exito.")

if __name__ == "__main__":
    run_descriptive_figures()
