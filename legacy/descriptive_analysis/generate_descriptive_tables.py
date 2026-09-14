import os
import scanpy as sc
import pandas as pd
import numpy as np

def run_generate_tables():
    data_path = 'data/NK_dataset_qc_ready.h5ad'
    out_dir = 'results/descriptive_analysis_v5/tables'
    os.makedirs(out_dir, exist_ok=True)
    
    print(f"Cargando dataset maestro para tablas desde {data_path}...")
    adata = sc.read_h5ad(data_path)

    # Filtrado estricto de cohortes por edad (Lehallier et al., 2019)
    # Adultos: 34 a 59 años | Adultos Mayores: 60+ años
    adata = adata[(adata.obs['age'] >= 34)].copy()
    
    # Reasignar age_group para asegurar consistencia
    adata.obs['age_group'] = np.where(adata.obs['age'] >= 60, 'old', 'adult')


    # Mapeo de Subtipos Canónicos NK
    subtypes_map = {
        'CD16-positive, CD56-dim natural killer cell, human': 'CD56dim',
        'CD16-negative, CD56-bright natural killer cell, human': 'CD56bright',
        'natural killer cell': 'CD56dim'
    }
    adata.obs['subtypes'] = adata.obs['cell_type'].map(subtypes_map).fillna('CD56dim').astype('category')
    
    # Normalizar age_group a minúsculas
    adata.obs['age_group_clean'] = adata.obs['age_group'].astype(str).str.lower()
    
    print("Calculando Métricas para Tabla 1...")
    donor_df = adata.obs[['donor_id', 'age_group_clean', 'sex', 'assay', 'age']].drop_duplicates(subset=['donor_id'])
    cell_obs = adata.obs
    
    summary_data = []
    
    # Evaluar grupos de edad ('adult' y 'old')
    group_labels = {'adult': 'Adultos (Jóvenes)', 'old': 'Adultos Mayores'}
    
    for grp_key in ['adult', 'old']:
        grp_label = group_labels[grp_key]
        sub_donors = donor_df[donor_df['age_group_clean'] == grp_key]
        sub_cells = cell_obs[cell_obs['age_group_clean'] == grp_key]
        
        n_donors = len(sub_donors)
        n_cells = len(sub_cells)
        
        age_mean = sub_donors['age'].mean() if 'age' in sub_donors.columns else np.nan
        age_std = sub_donors['age'].std() if 'age' in sub_donors.columns else np.nan
        
        n_female = (sub_donors['sex'].astype(str).str.lower().isin(['female', 'f'])).sum()
        n_male = (sub_donors['sex'].astype(str).str.lower().isin(['male', 'm'])).sum()
        
        median_umis = sub_cells['total_counts'].median()
        median_genes = sub_cells['n_genes_by_counts'].median()
        median_mito = sub_cells['pct_counts_mito'].median()
        
        n_cd56dim = (sub_cells['subtypes'] == 'CD56dim').sum()
        n_cd56bright = (sub_cells['subtypes'] == 'CD56bright').sum()
        pct_bright = (n_cd56bright / n_cells * 100) if n_cells > 0 else 0
        pct_dim = (n_cd56dim / n_cells * 100) if n_cells > 0 else 0
        
        summary_data.append({
            'Grupo de Edad': grp_label,
            'Donantes Totales': n_donors,
            'Células Totales': n_cells,
            'Edad Promedio ± DE': f"{age_mean:.1f} ± {age_std:.1f}" if not np.isnan(age_mean) else "N/A",
            'Sexo (Femenino / Masculino)': f"{n_female} / {n_male}",
            'Mediana UMIs / Célula': f"{median_umis:,.0f}",
            'Mediana Genes / Célula': f"{median_genes:,.0f}",
            'Mediana % MT': f"{median_mito:.2f}%",
            'Células CD56dim': f"{n_cd56dim:,} ({pct_dim:.1f}%)",
            'Células CD56bright': f"{n_cd56bright:,} ({pct_bright:.1f}%)"
        })
        
    tabla1_df = pd.DataFrame(summary_data)
    csv_path = os.path.join(out_dir, 'tabla1_demografia_cohorte.csv')
    tabla1_df.to_csv(csv_path, index=False, encoding='utf-8-sig')
    print(f"[OK] Tabla 1 guardada exitosamente en: {csv_path}")
    print("\nResumen Tabla 1:")
    print(tabla1_df.to_string(index=False))

if __name__ == "__main__":
    run_generate_tables()
