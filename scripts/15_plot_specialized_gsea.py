import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

def plot_specialized_gsea():
    results_dir = "results/subtypes/gsea_specialized"
    
    subtypes = ["nk_cd56dim", "nk_cd56bright"]
    
    data = []
    
    for subtype in subtypes:
        # Buscamos reportes de gseapy
        report_path_1 = os.path.join(results_dir, subtype, "gseapy.prerank.gene_sets.report.csv")
        report_path_2 = os.path.join(results_dir, subtype, "gseapy.gene_set.prerank.report.csv")
        
        report_path = None
        if os.path.exists(report_path_1):
            report_path = report_path_1
        elif os.path.exists(report_path_2):
            report_path = report_path_2
            
        if report_path:
            df = pd.read_csv(report_path)
            df['Subtype'] = subtype
            data.append(df)
            
    if not data:
        print("No se encontraron resultados de GSEA para graficar.")
        return
        
    df_all = pd.concat(data, ignore_index=True)
    
    # Filtrar todas nuestras custom gene sets
    df_custom = df_all[df_all['Term'].str.contains("custom_senescence_signatures.gmt__", na=False)].copy()
    
    if df_custom.empty:
        print("No se encontraron las vías de CellAge en los reportes.")
        return
        
    # Crear Dotplot Comparativo
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df_custom,
        x='Subtype',
        y='Term',
        size='FDR q-val',
        hue='NES',
        sizes=(50, 500),
        palette='vlag'
    )
    plt.title('GSEA: CellAge Senescence Signatures')
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, "cellage_comparative_dotplot.png"), dpi=300)
    print("Gráfica guardada exitosamente.")

if __name__ == "__main__":
    plot_specialized_gsea()
