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

def run_individual_figures():
    data_path = 'data/NK_dataset_qc_ready.h5ad'
    out_dir = 'results/descriptive_analysis_v5/figures_individual'
    os.makedirs(out_dir, exist_ok=True)
    
    print(f"Cargando dataset preprocesado desde {data_path}...")
    adata = sc.read_h5ad(data_path)

    # Filtrado estricto de cohortes por edad (Lehallier et al., 2019)
    adata = adata[(adata.obs['age'] >= 34)].copy()
    
    # Reasignar age_group y traducir al español
    adata.obs['age_group'] = np.where(adata.obs['age'] >= 60, 'Adultos Mayores', 'Adultos')
    adata.obs['age_group'] = adata.obs['age_group'].astype('category')
    adata.obs['age_group'] = adata.obs['age_group'].cat.reorder_categories(['Adultos', 'Adultos Mayores'])
    
    print("Dataset cargado y metadata limpia.")

    # --- DATAFRAME DE DONANTES ---
    donor_meta = adata.obs[['donor_id', 'age_group', 'sex', 'assay', 'age']].drop_duplicates(subset=['donor_id'])

    # Paleta de colores para Edad
    color_adultos = '#f97316' # Naranja
    color_mayores = '#b91c1c' # Rojo Ladrillo
    age_palette = {'Adultos': color_adultos, 'Adultos Mayores': color_mayores}

    # --- FIGURA 1C: Distribución Cronológica de Edad (Histograma Coloreado) ---
    print("Generando Histograma Bimodal de Edad...")
    plt.figure(figsize=(8, 5))
    
    # Separar por grupo para colorear el histograma
    adults_age = donor_meta[donor_meta['age_group'] == 'Adultos']['age']
    old_age = donor_meta[donor_meta['age_group'] == 'Adultos Mayores']['age']
    
    sns.histplot(adults_age, bins=np.arange(34, 61, 1), color=color_adultos, edgecolor='black', alpha=0.8, label='Adultos (34-59)')
    sns.histplot(old_age, bins=np.arange(60, 96, 1), color=color_mayores, edgecolor='black', alpha=0.8, label='Adultos Mayores (60+)')
    
    # KDE global
    sns.kdeplot(donor_meta['age'], color='#0284c7', linewidth=2)
    
    plt.axvline(60, color='black', linestyle='--', linewidth=1.5, label='Umbral Bimodal (60 años)')
    
    plt.title("Distribución Cronológica de Edad de Donantes (Densidad)", fontsize=14, fontweight='bold')
    plt.xlabel("Edad Cronológica (Años)", fontsize=12, fontweight='bold')
    plt.ylabel("N° de Donantes", fontsize=12, fontweight='bold')
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "Figura_1C_Distribucion_Cronologica_Edad.png"))
    plt.close()

    # --- FIGURA 1D: Boxplot Bimodal de Edad ---
    print("Generando Boxplot de Estratificación...")
    plt.figure(figsize=(6, 5))
    sns.boxplot(data=donor_meta, x='age_group', y='age', palette=age_palette, width=0.5, boxprops=dict(alpha=0.7))
    sns.stripplot(data=donor_meta, x='age_group', y='age', color='black', alpha=0.6, jitter=0.2, size=4)
    plt.title("Estratificación Bimodal Robusta (Adult vs Old)", fontsize=13, fontweight='bold')
    plt.xlabel("Grupo Estratificado", fontsize=11, fontweight='bold')
    plt.ylabel("Edad (Años)", fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "Figura_1C_Estratificacion_Bimodal.png")) # Respetando el nombre antiguo o dándole uno nuevo
    plt.close()

    # --- FIGURA 1A: Demografía por Sexo (Individual) ---
    print("Generando barras de Demografía por Sexo...")
    plt.figure(figsize=(6, 5))
    sex_counts = donor_meta.groupby(['age_group', 'sex'], observed=False).size().unstack(fill_value=0)
    ax = sex_counts.plot(kind='bar', stacked=True, color=['#38bdf8', '#f472b6'], edgecolor='black', linewidth=0.8)
    plt.title("Distribución de Donantes por Edad y Sexo", fontsize=12, fontweight='bold')
    plt.xlabel("Grupo de Edad", fontsize=10, fontweight='bold')
    plt.ylabel("Número de Donantes", fontsize=10, fontweight='bold')
    plt.xticks(rotation=0)
    plt.legend(title="Sexo", frameon=True)
    for p in ax.patches:
        height = p.get_height()
        if height > 0:
            ax.annotate(f"{int(height)}", (p.get_x() + p.get_width() / 2., p.get_y() + height / 2.),
                        ha='center', va='center', fontsize=10, fontweight='bold', color='black')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "Figura_1A_Distribucion_Sexo.png"))
    plt.close()

    # --- FIGURA 1A.2: Demografía por Assay (Individual) ---
    print("Generando barras de Demografía por Assay...")
    plt.figure(figsize=(6, 5))
    assay_counts = donor_meta.groupby(['age_group', 'assay'], observed=False).size().unstack(fill_value=0)
    ax = assay_counts.plot(kind='bar', stacked=True, cmap='Set2', edgecolor='black', linewidth=0.8)
    plt.title("Distribución de Donantes por Tecnología (Assay)", fontsize=12, fontweight='bold')
    plt.xlabel("Grupo de Edad", fontsize=10, fontweight='bold')
    plt.ylabel("Número de Donantes", fontsize=10, fontweight='bold')
    plt.xticks(rotation=0)
    plt.legend(title="Ensayo (10x)", frameon=True)
    for p in ax.patches:
        height = p.get_height()
        if height > 0:
            ax.annotate(f"{int(height)}", (p.get_x() + p.get_width() / 2., p.get_y() + height / 2.),
                        ha='center', va='center', fontsize=8, fontweight='bold', color='black')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "Figura_1A_Distribucion_Assay.png"))
    plt.close()

    # --- FIGURAS 1B: Métricas QC (Individuales) ---
    print("Generando Violines QC individuales...")
    # UMIs
    plt.figure(figsize=(5, 5))
    sns.violinplot(data=adata.obs, x='age_group', y='total_counts', hue='assay', palette='Blues', inner='quartile')
    plt.title("Cuentas Totales por Célula (UMIs)", fontsize=11, fontweight='bold')
    plt.xlabel("Grupo de Edad", fontsize=10, fontweight='bold')
    plt.ylabel("UMIs Totales", fontsize=10, fontweight='bold')
    plt.legend(title="Ensayo", fontsize=8)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "Figura_1B_QC_UMIs.png"))
    plt.close()

    # Genes
    plt.figure(figsize=(5, 5))
    sns.violinplot(data=adata.obs, x='age_group', y='n_genes_by_counts', hue='assay', palette='Greens', inner='quartile')
    plt.title("Genes Detectados por Célula", fontsize=11, fontweight='bold')
    plt.xlabel("Grupo de Edad", fontsize=10, fontweight='bold')
    plt.ylabel("N° de Genes", fontsize=10, fontweight='bold')
    plt.legend(title="Ensayo", fontsize=8)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "Figura_1B_QC_Genes.png"))
    plt.close()

    # Mito
    plt.figure(figsize=(5, 5))
    sns.violinplot(data=adata.obs, x='age_group', y='pct_counts_mito', hue='assay', palette='Oranges', inner='quartile')
    plt.title("Porcentaje Mitocondrial (%)", fontsize=11, fontweight='bold')
    plt.xlabel("Grupo de Edad", fontsize=10, fontweight='bold')
    plt.ylabel("% Cuentas MT", fontsize=10, fontweight='bold')
    plt.legend(title="Ensayo", fontsize=8)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "Figura_1B_QC_Mito.png"))
    plt.close()

    print("\n[OK] Figuras individuales generadas y guardadas.")

if __name__ == "__main__":
    run_individual_figures()
