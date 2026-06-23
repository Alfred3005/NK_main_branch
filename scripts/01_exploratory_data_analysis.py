import scanpy as sc
import pandas as pd
import os

def run_exploratory_analysis():
    data_path = '../data/NK_dataset_qc_ready.h5ad'
    print(f"Cargando dataset desde {data_path}...")
    
    if not os.path.exists(data_path):
        print("Error: No se encontró el dataset.")
        return

    adata = sc.read_h5ad(data_path)
    
    print("\n--- RESUMEN DEL DATASET ---")
    print(adata)
    
    print("\n--- DISTRIBUCIÓN DE SUBTIPOS (si existe) ---")
    if 'subtypes' in adata.obs.columns:
        print(adata.obs['subtypes'].value_counts())
    elif 'leiden' in adata.obs.columns:
        print("Clusters de Leiden:")
        print(adata.obs['leiden'].value_counts())
    else:
        print("No se encontraron anotaciones de subtipos directas en 'subtypes' o 'leiden'.")

    print("\n--- GRUPOS DE EDAD ---")
    if 'age_group' in adata.obs.columns:
        print(adata.obs['age_group'].value_counts())
        
    print("\n--- INFORMACIÓN DE ENSAYOS (Lotes) ---")
    if 'assay' in adata.obs.columns:
        print(adata.obs['assay'].value_counts())

    print("\nAnálisis exploratorio finalizado.")

if __name__ == "__main__":
    run_exploratory_analysis()
