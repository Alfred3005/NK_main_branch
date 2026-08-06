# -*- coding: utf-8 -*-
import os
import glob
import pandas as pd

def categorize_term(term):
    t = term.lower()
    
    # Muerte Celular y Estrés
    if any(k in t for k in ["apoptosis", "ferroptosis", "pyroptosis", "necroptosis", "death", "uv response", "oxidative stress", "ros", "stress", "senescence", "p53", "dna damage", "exhaust"]):
        return "Muerte Celular y Estrés"
        
    # Inflamación y Respuesta Inmune
    if any(k in t for k in ["inflam", "immune", "tnf", "nf-kb", "nfkb", "il-", "stat", "interferon", "cytokine", "sasp", "toll", "myd88", "chemokine", "antigen", "t cell", "b cell", "leukocyte", "macrophage", "nk cell", "nod-like", "rig-i", "complement", "infection", "lupus", "disease", "graft", "fc receptor"]):
        return "Inflamación y Respuesta Inmune"
        
    # Metabolismo y Bioenergética
    if any(k in t for k in ["metabol", "glycolysis", "oxphos", "oxidative phosphorylation", "respiratory", "electron transport", "mtorc1", "mtor", "hypoxia", "lipid", "fatty acid", "cholesterol", "atp", "mitochondria", "tca", "citric acid", "pi3k", "akt"]):
        return "Metabolismo y Bioenergética"
        
    # Ciclo Celular y Genética
    if any(k in t for k in ["cell cycle", "g2m", "mitotic", "e2f", "myc", "dna repair", "chromosome", "telomere", "epigenetic", "methylation", "histone", "chromatin", "splicing", "translation", "ribosome", "transcription", "rna", "smad", "notch", "wnt"]):
        return "Ciclo Celular y Genética"
        
    return "Otros / Estructural"

def format_cell(row, col):
    val = row[col]
    fdr = row['FDR q-val_raw']
    nes = row['NES_raw']
    
    # Bold if FDR < 0.05
    is_sig = fdr < 0.05
    
    if col == 'Term':
        color = "red" if nes > 0 else "blue"
        term_clean = val.split("__")[-1] if "__" in val else val
        formatted = f'<span style="color:{color}">{term_clean}</span>'
        if is_sig:
            formatted = f'**{formatted}**'
        return formatted
        
    if col == 'NES':
        color = "red" if nes > 0 else "blue"
        formatted = f'<span style="color:{color}">{val:.3f}</span>'
        if is_sig:
            formatted = f'**{formatted}**'
        return formatted
        
    if col in ['NOM p-val', 'FDR q-val']:
        formatted = f'{val:.4f}'
        if is_sig:
            formatted = f'**{formatted}**'
        return formatted
        
    return val

def compile_gsea_table():
    base_dir = r"C:\Users\PREDATOR\Documents\Antigravity_workspaces\NK_pipeline_RNA_ambient_Main_Branch\results\subtypes"
    search_pattern = os.path.join(base_dir, "**", "gseapy.gene_set.prerank.report.csv")
    csv_files = glob.glob(search_pattern, recursive=True)
    
    all_data = []
    for f in csv_files:
        # Ignore combined_metric if it still exists somehow, we only want wald_stat or specialized
        if "combined_metric" in f:
            continue
            
        parts = f.split(os.sep)
        if "gsea_specialized" in f:
            subset = parts[-2].replace("nk_", "")
            collection = "Specialized"
        else:
            subset = parts[-4]
            collection = parts[-3]
            
        try:
            df = pd.read_csv(f)
            df['Subset'] = subset.upper()
            df['Collection'] = collection
            all_data.append(df)
        except Exception as e:
            pass
            
    if not all_data:
        print("No data found.")
        return
        
    combined = pd.concat(all_data, ignore_index=True)
    filtered = combined[combined['FDR q-val'] < 0.25].copy()
    
    # Add raw columns for formatting logic
    filtered['FDR q-val_raw'] = filtered['FDR q-val']
    filtered['NES_raw'] = filtered['NES']
    
    # Categorize
    filtered['Categoría Biológica'] = filtered['Term'].apply(categorize_term)
    
    # Sort
    filtered = filtered.sort_values(by=['Subset', 'Categoría Biológica', 'NES_raw'], ascending=[True, True, False])
    
    # Format columns
    filtered['Term'] = filtered.apply(lambda row: format_cell(row, 'Term'), axis=1)
    filtered['NES'] = filtered.apply(lambda row: format_cell(row, 'NES'), axis=1)
    filtered['NOM p-val'] = filtered.apply(lambda row: format_cell(row, 'NOM p-val'), axis=1)
    filtered['FDR q-val'] = filtered.apply(lambda row: format_cell(row, 'FDR q-val'), axis=1)
    
    out_path = r"C:\Users\PREDATOR\.gemini\antigravity-ide\brain\5ba349c3-eedc-4062-b7e2-62eac9b671ec\gsea_unified_table.md"
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Tablas Unificadas GSEA por Subpoblación (FDR < 0.25)\n\n")
        f.write("> **Guía Visual:** Los valores con significancia estadística sólida (**FDR < 0.05**) se marcan en **negrita**. El color <span style='color:red'>rojo</span> indica inducción (NES > 0) y el <span style='color:blue'>azul</span> represión (NES < 0).\n\n")
        
        for subset in ['CD56BRIGHT', 'CD56DIM', 'GLOBAL']:
            subset_df = filtered[filtered['Subset'] == subset]
            if subset_df.empty:
                continue
                
            f.write(f"## {subset} GSEA Results\n\n")
            
            # Group by category
            for cat in ["Inflamación y Respuesta Inmune", "Metabolismo y Bioenergética", "Muerte Celular y Estrés", "Ciclo Celular y Genética", "Otros / Estructural"]:
                cat_df = subset_df[subset_df['Categoría Biológica'] == cat]
                if cat_df.empty:
                    continue
                    
                f.write(f"### {cat}\n\n")
                out_df = cat_df[['Collection', 'Term', 'NES', 'NOM p-val', 'FDR q-val']]
                f.write(out_df.to_markdown(index=False))
                f.write("\n\n")
                
        f.write("## Archivos CSV Fuente (Versiones Finales)\n")
        for fpath in csv_files:
            if "combined_metric" not in fpath:
                f.write(f"- `{fpath}`\n")
            
    print("Tables generated successfully.")

if __name__ == '__main__':
    compile_gsea_table()
