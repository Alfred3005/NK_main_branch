import pandas as pd
import gseapy as gp
import os
import glob

def run_specialized_gsea():
    results_dir = "../../results/experiment_collinearity"
    out_dir = os.path.join(results_dir, "gsea_specialized")
    os.makedirs(out_dir, exist_ok=True)
    
    # Custom gene sets
    gmt_path = "../../data/gene_sets/custom_senescence_signatures.gmt"
    
    # We can also add standard libraries for comparison (e.g., Reactome)
    gene_sets = [gmt_path, "Reactome_2022"]
    
    files_to_process = [
        "deseq2_results_nk_cd56dim.csv",
        "deseq2_results_nk_cd56bright.csv"
    ]
    
    for file_name in files_to_process:
        file_path = os.path.join(results_dir, file_name)
        if not os.path.exists(file_path):
            print(f"No se encontró {file_path}")
            continue
            
        print(f"Procesando {file_name}...")
        df = pd.read_csv(file_path)
        
        # Renombramos la primera columna a 'gene_symbol' si no tiene nombre
        if 'feature_name' in df.columns:
            df.rename(columns={'feature_name': 'gene_symbol'}, inplace=True)
        elif 'Unnamed: 0' in df.columns:
            df.rename(columns={'Unnamed: 0': 'gene_symbol'}, inplace=True)
            
        if 'stat' not in df.columns or 'gene_symbol' not in df.columns:
            print(f"Formato no esperado en {file_name}")
            continue
            
        # Preparar ranking
        rnk = df[['gene_symbol', 'stat']].dropna().copy()
        
        # Eliminar duplicados reteniendo el estadístico absoluto más alto
        rnk['abs_stat'] = rnk['stat'].abs()
        rnk = rnk.sort_values('abs_stat', ascending=False).drop_duplicates('gene_symbol')
        rnk = rnk[['gene_symbol', 'stat']].sort_values('stat', ascending=False)
        
        # Ejecutar gseapy
        subset_name = file_name.replace("deseq2_results_", "").replace(".csv", "")
        subset_out = os.path.join(out_dir, subset_name)
        
        try:
            res = gp.prerank(rnk=rnk,
                             gene_sets=gene_sets,
                             threads=4,
                             min_size=5,
                             max_size=1000,
                             permutation_num=1000,
                             outdir=subset_out,
                             no_plot=True,
                             seed=42)
            print(f"Análisis completado para {subset_name}")
        except Exception as e:
            print(f"Error corriendo GSEA en {subset_name}: {e}")

if __name__ == "__main__":
    run_specialized_gsea()
