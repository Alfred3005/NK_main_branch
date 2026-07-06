import pandas as pd
import gseapy as gp
import os
import json

def build_custom_gmt(output_dir="data/gene_sets"):
    os.makedirs(output_dir, exist_ok=True)
    custom_gmt = {}

    # 1. Procesar CellAge
    cellage_path = "docs/cellAge/cellage3.tsv"
    if os.path.exists(cellage_path):
        df_cellage = pd.read_csv(cellage_path, sep="\t")
        
        # El archivo parece contener sólo genes humanos y la columna direccional es 'Senescence Effect'
        # Los valores son 'Induces', 'Inhibits', 'Unclear'
        
        genes_promotores = df_cellage[df_cellage['Senescence Effect'] == 'Induces']['Gene symbol'].dropna().unique().tolist()
        genes_inhibidores = df_cellage[df_cellage['Senescence Effect'] == 'Inhibits']['Gene symbol'].dropna().unique().tolist()
        
        custom_gmt["CELLAGE_SENESCENCE_INDUCES"] = genes_promotores
        custom_gmt["CELLAGE_SENESCENCE_INHIBITS"] = genes_inhibidores
        print(f"CellAge cargado: {len(genes_promotores)} Inductores, {len(genes_inhibidores)} Inhibidores.")
    else:
        print(f"Advertencia: No se encontró {cellage_path}")

    # 2. Obtener SenMayo desde MSigDB (MAYES_SENESCENCE_SIGNATURE)
    try:
        # Extraer usando el nombre directo si está disponible en la librería MSigDB C2
        # gseapy get_library no extrae firmas específicas individuales, extrae la librería completa
        # Alternativa: cargar el gmt manualmente si tuviésemos el de MSigDB. 
        # Dado que SenMayo es un gen set, lo podemos obtener a través del MSigDB gmt file.
        # Por robustez, si no queremos descargar todo MSigDB, dejaremos un espacio para inyectarlo.
        pass
    except Exception as e:
        print(f"Error obteniendo SenMayo: {e}")

    # Guardaremos el diccionario en formato JSON y también generaremos el archivo .gmt
    json_path = os.path.join(output_dir, "custom_senescence_signatures.json")
    with open(json_path, 'w') as f:
        json.dump(custom_gmt, f, indent=4)
        
    gmt_path = os.path.join(output_dir, "custom_senescence_signatures.gmt")
    with open(gmt_path, 'w') as f:
        for term, genes in custom_gmt.items():
            f.write(f"{term}\t\t" + "\t".join(genes) + "\n")
            
    print(f"Diccionario guardado en {json_path} y {gmt_path}")
    return custom_gmt

if __name__ == "__main__":
    build_custom_gmt()
