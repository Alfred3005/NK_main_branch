import os
import json

def update_signatures():
    data_dir = "data/gene_sets"
    json_path = os.path.join(data_dir, "custom_senescence_signatures.json")
    gmt_path = os.path.join(data_dir, "custom_senescence_signatures.gmt")
    
    # Cargar el diccionario actual
    if os.path.exists(json_path):
        with open(json_path, 'r') as f:
            custom_gmt = json.load(f)
    else:
        custom_gmt = {}

    print(f"Firmas actuales antes de actualizar: {list(custom_gmt.keys())}")

    # Buscar y extraer firmas de Exhaustion de c7.gmt
    c7_path = "c7.gmt"
    if os.path.exists(c7_path):
        print("Extrayendo firmas de Exhaustion de C7...")
        with open(c7_path, 'r') as f:
            for line in f:
                parts = line.strip().split('\t')
                term = parts[0]
                genes = parts[2:]
                
                # Vamos a tomar las firmas principales de agotamiento (Exhaustion) GSE9650
                if term in [
                    "GSE9650_EXHAUSTED_VS_MEMORY_CD8_TCELL_UP",
                    "GSE9650_EXHAUSTED_VS_MEMORY_CD8_TCELL_DN",
                    "GSE9650_EFFECTOR_VS_EXHAUSTED_CD8_TCELL_UP",
                    "GSE9650_EFFECTOR_VS_EXHAUSTED_CD8_TCELL_DN"
                ]:
                    custom_gmt[term] = genes
                    print(f"Agregado {term} con {len(genes)} genes.")
    else:
        print(f"Advertencia: No se encontró {c7_path}")

    # Guardar
    with open(json_path, 'w') as f:
        json.dump(custom_gmt, f, indent=4)
        
    with open(gmt_path, 'w') as f:
        for term, genes in custom_gmt.items():
            f.write(f"{term}\t\t" + "\t".join(genes) + "\n")
            
    print(f"Firmas totales en el diccionario: {len(custom_gmt)}")
    print(f"Diccionario guardado en {json_path} y {gmt_path}")

if __name__ == "__main__":
    update_signatures()
