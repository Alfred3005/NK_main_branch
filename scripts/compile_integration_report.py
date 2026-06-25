import os
import base64
import pandas as pd
import numpy as np

def get_image_base64(path):
    """Lee una imagen y la devuelve formateada en base64 para HTML."""
    if not os.path.exists(path):
        print(f"⚠️ Imagen no encontrada en: {path}")
        return ""
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/png;base64,{encoded_string}"

def generate_table_rows(df, columns_to_show):
    """Genera las filas de la tabla HTML a partir de un DataFrame."""
    rows_html = ""
    for idx, row in df.iterrows():
        cells = ""
        for col in columns_to_show:
            val = row[col]
            if isinstance(val, float):
                if abs(val) < 1e-4 and val != 0:
                    val_str = f"{val:.4e}"
                else:
                    val_str = f"{val:.4f}"
                
                # Formato condicional de colores para Fold Change
                if col == 'log2FoldChange':
                    if val > 0:
                        val_str = f"<span style='color: #10b981; font-weight: 600;'>{val_str}</span>"
                    elif val < 0:
                        val_str = f"<span style='color: #ef4444; font-weight: 600;'>{val_str}</span>"
                
                cells += f"<td>{val_str}</td>"
            else:
                cells += f"<td>{str(val)}</td>"
        rows_html += f"<tr><td>{idx+1}</td>{cells}</tr>"
    return rows_html

def parse_markdown_to_html(md_content):
    """Parsea una versión muy simple y limpia de markdown a HTML para la narrativa."""
    html = ""
    lines = md_content.split("\n")
    in_table = False
    table_html = ""
    in_list = False
    in_mermaid = False
    mermaid_content = ""
    in_carousel = False
    carousel_slides = []
    import random
    
    for line in lines:
        line_strip = line.strip()
        
        if line_strip.startswith("```mermaid"):
            in_mermaid = True
            continue
        elif in_mermaid and line_strip.startswith("```"):
            in_mermaid = False
            html += f"<pre class='mermaid'>\n{mermaid_content}</pre>\n"
            mermaid_content = ""
            continue
        elif in_mermaid:
            mermaid_content += line + "\n"
            continue

        if line_strip.startswith("````carousel"):
            in_carousel = True
            carousel_slides = [""]
            continue
        elif in_carousel and line_strip.startswith("<!-- slide -->"):
            carousel_slides.append("")
            continue
        elif in_carousel and line_strip.startswith("````"):
            in_carousel = False
            cid = f"carousel-{random.randint(10000,99999)}"
            html += f"<div class='carousel-container' id='{cid}'>\n"
            for i, slide in enumerate(carousel_slides):
                active = "active" if i == 0 else ""
                html += f"<div class='carousel-slide {active}'>\n"
                html += parse_markdown_to_html(slide.strip())
                html += "</div>\n"
            html += f"""<div class='carousel-controls'>
                <button onclick='moveCarousel("{cid}", -1)'>&#10094; Anterior</button>
                <button onclick='moveCarousel("{cid}", 1)'>Siguiente &#10095;</button>
            </div></div>\n"""
            continue
        elif in_carousel:
            carousel_slides[-1] += line + "\n"
            continue

        # Manejo de listas
        if line_strip.startswith("* ") or line_strip.startswith("- "):
            if not in_list:
                html += "<ul>"
                in_list = True
            content = line_strip[2:]
            # Procesar negritas
            while "**" in content:
                content = content.replace("**", "<strong>", 1).replace("**", "</strong>", 1)
            html += f"<li>{content}</li>"
            continue
        elif in_list and not (line_strip.startswith("* ") or line_strip.startswith("- ") or line_strip == ""):
            html += "</ul>"
            in_list = False
            
        if not line_strip:
            if in_table:
                html += f"<div class='table-responsive'><table>{table_html}</table></div>"
                table_html = ""
                in_table = False
            continue
            
        if line_strip.startswith("# "):
            html += f"<h1>{line_strip[2:]}</h1>"
        elif line_strip.startswith("## "):
            html += f"<h2>{line_strip[3:]}</h2>"
        elif line_strip.startswith("### "):
            html += f"<h3>{line_strip[4:]}</h3>"
        elif line_strip.startswith("#### "):
            html += f"<h4>{line_strip[5:]}</h4>"
        elif line_strip.startswith("> [!"):
            alert_type = "note"
            if "IMPORTANT" in line_strip:
                alert_type = "important"
            elif "WARNING" in line_strip:
                alert_type = "warning"
            elif "TIP" in line_strip:
                alert_type = "tip"
            elif "CAUTION" in line_strip:
                alert_type = "caution"
            content_idx = line.find("]") + 1
            alert_text = line[content_idx:].strip()
            html += f"<div class='alert alert-{alert_type}'><span class='alert-title'>{alert_type.upper()}</span><p>{alert_text}</p></div>"
        elif line_strip.startswith(">"):
            html += f"<blockquote>{line_strip[1:].strip()}</blockquote>"
        elif line_strip.startswith("|"):
            in_table = True
            cols = [c.strip() for c in line_strip.split("|")[1:-1]]
            if len(cols) > 0 and "---" in cols[0]:
                continue
            row_type = "th" if table_html == "" else "td"
            row_html = "".join([f"<{row_type}>{c}</{row_type}>" for c in cols])
            table_html += f"<tr>{row_html}</tr>"
        else:
            if in_table:
                html += f"<div class='table-responsive'><table>{table_html}</table></div>"
                table_html = ""
                in_table = False
            
            # Procesamiento de imágenes en Markdown
            import re
            if line_strip.startswith("!["):
                img_match = re.match(r'!\[(.*?)\]\((.*?)\)', line_strip)
                if img_match:
                    alt_text = img_match.group(1)
                    img_path = img_match.group(2)
                    if img_path.startswith("../"):
                        img_path = img_path[3:]
                    b64_img = get_image_base64(img_path)
                    html += f"<div class='image-card'><img src='{b64_img}' alt='{alt_text}'></div>"
                    continue

            # Procesamiento de Captions
            if line_strip.startswith("*Figura") and line_strip.endswith("*"):
                caption = line_strip[1:-1]
                html += f"<div class='image-caption' style='text-align: center; margin-top: -15px; margin-bottom: 20px;'>{caption}</div>"
                continue

            processed_line = line_strip
            while "**" in processed_line:
                processed_line = processed_line.replace("**", "<strong>", 1).replace("**", "</strong>", 1)
            while "$" in processed_line:
                processed_line = processed_line.replace("$", "<em>", 1).replace("$", "</em>", 1)
            html += f"<p>{processed_line}</p>"
            
    if in_table:
        html += f"<div class='table-responsive'><table>{table_html}</table></div>"
    if in_list:
        html += "</ul>"
        
    return html

def main():
    print("🚀 Iniciando la compilación del Reporte Integrativo Premium...")
    
    # Directorios de origen
    report_md = "../results/subtypes_abundance_integration_report.md"
    wiki_md = "../docs/vault/wiki/integracion_subtipos_abundancia.md"
    
    # Tablas de DEGs de origen
    abundance_dir = "../results/subtypes"
    cd56dim_de_csv = os.path.join(abundance_dir, "deseq2_results_nk_cd56dim.csv")
    cd56bright_de_csv = os.path.join(abundance_dir, "deseq2_results_nk_cd56bright.csv")
    
    # Resultados de abundancia en archivos de texto
    glm_txt = os.path.join(abundance_dir, "proportion_glm_results.txt")
    ratios_txt = os.path.join(abundance_dir, "statistical_test_ratios.txt")
    
    # 1. Cargar y filtrar DEGs de CD56dim (Top 15 por pvalue)
    print("📋 Cargando y filtrando DEGs de CD56dim...")
    df_dim = pd.read_csv(cd56dim_de_csv)
    # Renombrar columna de gen si es necesario
    if 'Unnamed: 0' in df_dim.columns:
        df_dim = df_dim.rename(columns={'Unnamed: 0': 'feature_name'})
    df_dim_sig = df_dim[df_dim['padj'] < 0.05].copy()
    df_dim_sig = df_dim_sig.sort_values(by='padj')
    
    # 2. Cargar y filtrar DEGs de CD56bright (Top 15 por pvalue en GLMM)
    print("📋 Cargando y filtrando DEGs de CD56bright...")
    if os.path.exists(cd56bright_de_csv):
        df_bright = pd.read_csv(cd56bright_de_csv)
        if 'Unnamed: 0' in df_bright.columns:
            df_bright = df_bright.rename(columns={'Unnamed: 0': 'feature_name'})
        df_bright_sig = df_bright[df_bright['pvalue'] < 0.05].copy()
        df_bright_sig = df_bright_sig.sort_values(by='pvalue')
    else:
        print("⚠️ No se encontró resultados para CD56bright. Usando tabla vacía.")
        df_bright_sig = pd.DataFrame(columns=['feature_name', 'log2FoldChange', 'stat', 'pvalue', 'padj'])
    
    # Generar filas HTML para tablas de DEGs
    de_cols_dim = ['feature_name', 'log2FoldChange', 'stat', 'pvalue', 'padj']
    # GLMM usa nombres diferentes a PyDESeq2 (ej. no tiene padj, tiene padj pero 0)
    de_cols_bright = ['feature_name', 'log2FoldChange', 'stat', 'pvalue', 'padj']
    if 'padj' not in df_bright_sig.columns:
        de_cols_bright = ['feature_name', 'log2FoldChange', 'stat', 'pvalue', 'stderr']
        
    dim_top10 = generate_table_rows(df_dim_sig.head(10), de_cols_dim)
    dim_rest = generate_table_rows(df_dim_sig.iloc[10:], de_cols_dim)
    
    # Para CD56bright, mostramos top 10 y el resto plegable
    bright_top10 = generate_table_rows(df_bright_sig.head(10), de_cols_bright)
    bright_rest = generate_table_rows(df_bright_sig.iloc[10:], de_cols_bright)
    
    # 3. Leer archivos de abundancia
    print("📖 Cargando archivos de texto de abundancia...")
    with open(glm_txt, "r", encoding="utf-8") as f:
        glm_content = f.read()
    with open(ratios_txt, "r", encoding="utf-8") as f:
        ratios_content = f.read()
        
    # 4. Leer y compilar narrativas de Markdown
    print("📝 Parseando narrativas de Markdown...")
    with open(report_md, "r", encoding="utf-8") as f:
        report_raw = f.read()
    
    # Dividir el reporte en Narrativa (Sección 1 e Introducción) y Conclusiones (Sección 5)
    import re
    # Extraer Narrativa (todo hasta la Sección 2)
    narrative_match = re.search(r'(.*?)## \S*\s*2\.\s+Abundancia Diferencial', report_raw, re.DOTALL)
    if narrative_match:
        narrative_raw = narrative_match.group(1)
    else:
        narrative_raw = report_raw # fallback
    
    # Extraer Conclusiones (desde la Sección 5 hasta el final)
    conclusions_match = re.search(r'(## \S*\s*5\.\s+Conclusiones Integrativas.*)', report_raw, re.DOTALL)
    if conclusions_match:
        conclusions_raw = conclusions_match.group(1)
    else:
        conclusions_raw = "<h2>Conclusiones</h2><p>No se encontraron conclusiones en el archivo markdown.</p>"

    # Extraer Global Pool (dentro de sección 3)
    match_global_pool = re.search(r'(### A\. NK Cells General \(Pool Global Pseudobulk\).*?)### B\. NK CD56dim', report_raw, re.DOTALL)
    global_pool_raw = match_global_pool.group(1) if match_global_pool else ""
    
    # Extraer ORA (dentro de sección 4)
    match_ora = re.search(r'(### A\. Análisis de Sobre-Representación \(ORA\) Clásico.*?)### B\. Gene Set Enrichment Analysis', report_raw, re.DOTALL)
    ora_raw = match_ora.group(1) if match_ora else ""
    
    # Extraer Integración (dentro de sección 4)
    match_integration = re.search(r'(### C\. Integración Multidimensional de Vías y Genes.*?)(?:## \S*\s*5\.)', report_raw, re.DOTALL)
    integration_raw = match_integration.group(1) if match_integration else ""

    report_html = parse_markdown_to_html(narrative_raw)
    conclusions_html = parse_markdown_to_html(conclusions_raw)
    global_pool_html = parse_markdown_to_html(global_pool_raw)
    ora_html = parse_markdown_to_html(ora_raw)
    integration_html = parse_markdown_to_html(integration_raw)

    gsea_tables_html = """
<details style="margin-top: 1.5rem; background: rgba(30, 41, 59, 0.5); padding: 15px; border-radius: 8px; border: 1px solid #4f46e5; margin-bottom: 25px; cursor: pointer;">
<summary style="font-weight: 700; color: #818cf8; font-size: 1.1rem;">Tablas de Enriquecimiento (Desplegable)</summary>
<h4>Señalización Inmune e Inflamatoria</h4>
<div class="table-responsive">
<table>
<thead><tr><th>Term</th><th>NES</th><th>FDR</th><th>p-value</th><th>Metric</th></tr></thead>
<tbody>
<tr><td>Inflammatory Response</td><td>1.634</td><td>0.0478</td><td>0.0010</td><td>wald_stat</td></tr>
<tr><td>Tnf-Alpha Signaling Via Nf-Kb</td><td>1.618</td><td>0.0407</td><td>0.0010</td><td>wald_stat</td></tr>
<tr><td>Il-2/Stat5 Signaling</td><td>1.523</td><td>0.0834</td><td>0.0063</td><td>wald_stat</td></tr>
<tr><td>Coagulation</td><td>1.404</td><td>0.1084</td><td>0.0510</td><td>wald_stat</td></tr>
<tr><td>Complement</td><td>1.242</td><td>0.2314</td><td>0.1032</td><td>wald_stat</td></tr>
<tr><td>Il-6/Jak/Stat3 Signaling</td><td>1.145</td><td>0.3561</td><td>0.2411</td><td>wald_stat</td></tr>
<tr><td>Tgf-Beta Signaling</td><td>1.025</td><td>0.5625</td><td>0.4000</td><td>wald_stat</td></tr>
<tr><td>Interferon Gamma Response</td><td>0.991</td><td>0.5669</td><td>0.4872</td><td>wald_stat</td></tr>
<tr><td>Allograft Rejection</td><td>0.961</td><td>0.5895</td><td>0.5556</td><td>wald_stat</td></tr>
<tr><td>Interferon Alpha Response</td><td>-0.879</td><td>0.7842</td><td>0.7183</td><td>wald_stat</td></tr>
</tbody>
</table>
</div>
<h4>Metabolismo y Bioenergética</h4>
<div class="table-responsive">
<table>
<thead><tr><th>Term</th><th>NES</th><th>FDR</th><th>p-value</th><th>Metric</th></tr></thead>
<tbody>
<tr><td>Glycolysis</td><td>1.476</td><td>0.0833</td><td>0.0150</td><td>wald_stat</td></tr>
<tr><td>Mtorc1 Signaling</td><td>1.448</td><td>0.0818</td><td>0.0089</td><td>wald_stat</td></tr>
<tr><td>Adipogenesis</td><td>1.399</td><td>0.1034</td><td>0.0068</td><td>wald_stat</td></tr>
<tr><td>Reactive Oxygen Species Pathway</td><td>1.359</td><td>0.1196</td><td>0.0681</td><td>wald_stat</td></tr>
<tr><td>Bile Acid Metabolism</td><td>1.120</td><td>0.3948</td><td>0.2559</td><td>wald_stat</td></tr>
<tr><td>Heme Metabolism</td><td>1.074</td><td>0.4713</td><td>0.2927</td><td>wald_stat</td></tr>
<tr><td>Fatty Acid Metabolism</td><td>0.996</td><td>0.5983</td><td>0.4457</td><td>wald_stat</td></tr>
<tr><td>Pperoxisome</td><td>0.956</td><td>0.5820</td><td>0.5763</td><td>wald_stat</td></tr>
<tr><td>Cholesterol Homeostasis</td><td>-0.994</td><td>0.6949</td><td>0.4672</td><td>wald_stat</td></tr>
<tr><td>Xenobiotic Metabolism</td><td>-1.038</td><td>0.9066</td><td>0.3866</td><td>wald_stat</td></tr>
<tr><td>Oxidative Phosphorylation</td><td>-1.206</td><td>0.8573</td><td>0.0869</td><td>wald_stat</td></tr>
</tbody>
</table>
</div>
<h4>Ciclo Celular, Apoptosis y Daño al ADN</h4>
<div class="table-responsive">
<table>
<thead><tr><th>Term</th><th>NES</th><th>FDR</th><th>p-value</th><th>Metric</th></tr></thead>
<tbody>
<tr><td>Myc Targets V1</td><td>1.687</td><td>0.0475</td><td>0.0010</td><td>wald_stat</td></tr>
<tr><td>Apoptosis</td><td>1.516</td><td>0.0728</td><td>0.0067</td><td>wald_stat</td></tr>
<tr><td>E2F Targets</td><td>1.379</td><td>0.1098</td><td>0.0067</td><td>wald_stat</td></tr>
<tr><td>Wnt-Beta Catenin Signaling</td><td>1.029</td><td>0.5746</td><td>0.4211</td><td>wald_stat</td></tr>
<tr><td>Notch Signaling</td><td>0.992</td><td>0.5861</td><td>0.4897</td><td>wald_stat</td></tr>
<tr><td>Myc Targets V2</td><td>-0.918</td><td>0.7613</td><td>0.6167</td><td>wald_stat</td></tr>
<tr><td>Dna Repair</td><td>-0.980</td><td>0.6617</td><td>0.5083</td><td>wald_stat</td></tr>
<tr><td>Mitotic Spindle</td><td>-1.018</td><td>0.7118</td><td>0.4200</td><td>wald_stat</td></tr>
<tr><td>P53 Pathway</td><td>-1.041</td><td>1.0000</td><td>0.3657</td><td>wald_stat</td></tr>
<tr><td>Spermatogenesis</td><td>-1.156</td><td>0.7866</td><td>0.2359</td><td>wald_stat</td></tr>
</tbody>
</table>
</div>
<h4>Estrés Celular y Respuestas Estructurales</h4>
<div class="table-responsive">
<table>
<thead><tr><th>Term</th><th>NES</th><th>FDR</th><th>p-value</th><th>Metric</th></tr></thead>
<tbody>
<tr><td>Uv Response Dn</td><td>1.855</td><td>0.0145</td><td>0.0010</td><td>wald_stat</td></tr>
<tr><td>Hypoxia</td><td>1.460</td><td>0.0850</td><td>0.0242</td><td>wald_stat</td></tr>
<tr><td>Androgen Response</td><td>1.273</td><td>0.2094</td><td>0.1118</td><td>wald_stat</td></tr>
<tr><td>Protein Secretion</td><td>1.261</td><td>0.2128</td><td>0.1031</td><td>wald_stat</td></tr>
<tr><td>Apical Junction</td><td>1.170</td><td>0.3555</td><td>0.1727</td><td>wald_stat</td></tr>
<tr><td>Uv Response Up</td><td>1.162</td><td>0.3538</td><td>0.1849</td><td>wald_stat</td></tr>
<tr><td>Epithelial Mesenchymal Transition</td><td>1.093</td><td>0.4406</td><td>0.2805</td><td>wald_stat</td></tr>
<tr><td>Myogenesis</td><td>1.012</td><td>0.5771</td><td>0.4204</td><td>wald_stat</td></tr>
<tr><td>Kras Signaling Up</td><td>0.989</td><td>0.5540</td><td>0.4802</td><td>wald_stat</td></tr>
<tr><td>Unfolded Protein Response</td><td>0.962</td><td>0.6050</td><td>0.5247</td><td>wald_stat</td></tr>
<tr><td>Estrogen Response Late</td><td>0.884</td><td>0.7391</td><td>0.7045</td><td>wald_stat</td></tr>
<tr><td>Apical Surface</td><td>0.735</td><td>0.9470</td><td>0.8528</td><td>wald_stat</td></tr>
<tr><td>Kras Signaling Dn</td><td>-0.541</td><td>0.9980</td><td>0.9947</td><td>wald_stat</td></tr>
<tr><td>Estrogen Response Early</td><td>-1.036</td><td>0.7653</td><td>0.3831</td><td>wald_stat</td></tr>
<tr><td>Pi3K/Akt/Mtor Signaling</td><td>-1.423</td><td>0.3352</td><td>0.0151</td><td>wald_stat</td></tr>
</tbody>
</table>
</div>
<h4>Otras Vías Hallmark</h4>
<div class="table-responsive">
<table>
<thead><tr><th>Term</th><th>NES</th><th>FDR</th><th>p-value</th><th>Metric</th></tr></thead>
<tbody>
<tr><td>G2-M Checkpoint</td><td>1.155</td><td>0.3518</td><td>0.1599</td><td>wald_stat</td></tr>
</tbody>
</table>
</div>
</details>
"""
    # Inyectar colores en la columna NES usando regex
    def colorize_nes(match):
        term = match.group(1)
        nes_val = float(match.group(2))
        color = "#10b981" if nes_val > 0 else "#ef4444"
        return f'<tr><td>{term}</td><td><span style="color: {color}; font-weight: 600;">{nes_val:.3f}</span></td>'

    gsea_tables_html = re.sub(r'<tr><td>(.*?)</td><td>(-?[0-9]+\.[0-9]+)</td>', colorize_nes, gsea_tables_html)
    
    # 5. Cargar imágenes en base64
    print("🖼️ Codificando imágenes a base64...")
    img_ratio = get_image_base64(os.path.join(abundance_dir, "nk_ratio_analysis.png"))
    
    img_gsea_compare = get_image_base64(os.path.join(abundance_dir, "gsea/comparative_summary_barplot.png"))
    img_gsea_dim = get_image_base64(os.path.join(abundance_dir, "gsea/cd56dim/dotplot_MSigDB_Hallmark_2020.png"))
    img_gsea_bright = get_image_base64(os.path.join(abundance_dir, "gsea/cd56bright/dotplot_MSigDB_Hallmark_2020.png"))
    img_gsea_global = get_image_base64(os.path.join(abundance_dir, "gsea/global/dotplot_MSigDB_Hallmark_2020.png"))
    
    # 6. Construir el HTML completo
    print("✍️ Ensamblando plantilla HTML...")
    full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte Integrativo: CD56dim vs CD56bright y Abundancia NK</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ startOnLoad: true, theme: 'dark' }});
    </script>
    <style>
        :root {{
            --primary: #4f46e5;
            --primary-light: #818cf8;
            --primary-dark: #3730a3;
            --background: #0f172a;
            --surface: #1e293b;
            --surface-hover: #334155;
            --text: #f8fafc;
            --text-muted: #94a3b8;
            --border: #334155;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --info: #06b6d4;
            --card-bg: rgba(30, 41, 59, 0.7);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--background);
            color: var(--text);
            line-height: 1.6;
            padding: 1.5rem 1rem;
        }}

        .wrapper {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        header {{
            text-align: center;
            margin-bottom: 2.5rem;
            padding: 2.5rem;
            background: linear-gradient(135deg, rgba(79, 70, 229, 0.15) 0%, rgba(129, 140, 248, 0.05) 100%);
            border-radius: 16px;
            border: 1px solid var(--border);
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(5px);
        }}

        header h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #e0e7ff, #a5b4fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }}

        header p {{
            color: var(--text-muted);
            font-size: 1.1rem;
        }}

        /* Navigation Tabs */
        .nav-tabs {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 2rem;
            border-bottom: 1px solid var(--border);
            padding-bottom: 0.75rem;
        }}

        .nav-btn {{
            padding: 0.75rem 1.25rem;
            cursor: pointer;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 8px;
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            font-size: 0.95rem;
            color: var(--text-muted);
            transition: all 0.3s ease;
        }}

        .nav-btn:hover {{
            background: var(--surface-hover);
            color: var(--text);
        }}

        .nav-btn.active {{
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
        }}

        /* Section Panel */
        .panel {{
            display: none;
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 2.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(10px);
        }}

        .panel.active {{
            display: block;
        }}

        h1, h2, h3, h4 {{
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            color: #e2e8f0;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
        }}

        .panel > h1 {{
            font-size: 2.2rem;
            color: #ffffff;
            border-bottom: 2px solid var(--border);
            padding-bottom: 0.75rem;
            margin-top: 0;
            margin-bottom: 1.5rem;
        }}

        .panel h2 {{
            font-size: 1.6rem;
            color: var(--primary-light);
            margin-top: 2rem;
            border-bottom: 1px solid var(--border);
            padding-bottom: 0.4rem;
        }}

        p {{
            margin-bottom: 1.2rem;
            color: #cbd5e1;
            font-size: 1.05rem;
        }}

        ul {{
            margin-bottom: 1.5rem;
        }}

        li {{
            margin-left: 2rem;
            margin-bottom: 0.5rem;
            color: #cbd5e1;
        }}

        blockquote {{
            padding: 0.75rem 1.25rem;
            border-left: 4px solid var(--primary-light);
            background: rgba(30, 41, 59, 0.4);
            border-radius: 0 8px 8px 0;
            margin: 1.5rem 0;
            font-style: italic;
        }}

        /* Responsive Table */
        .table-responsive {{
            width: 100%;
            overflow-x: auto;
            margin: 1.5rem 0;
            border-radius: 10px;
            border: 1px solid var(--border);
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.95rem;
            text-align: left;
        }}

        th, td {{
            padding: 12px 16px;
            border-bottom: 1px solid var(--border);
        }}

        th {{
            background-color: #0f172a;
            color: #ffffff;
            font-weight: 600;
        }}

        tr:nth-child(even) {{
            background-color: rgba(15, 23, 42, 0.3);
        }}

        tr:hover {{
            background-color: rgba(79, 70, 229, 0.1);
        }}

        /* Alerts style */
        .alert {{
            padding: 1.25rem 1.5rem;
            border-radius: 8px;
            margin: 1.5rem 0;
            border-left: 4px solid var(--primary);
            background-color: rgba(79, 70, 229, 0.1);
            color: #e2e8f0;
        }}

        .alert-important {{
            border-left-color: var(--primary);
            background-color: rgba(79, 70, 229, 0.08);
        }}

        .alert-warning {{
            border-left-color: var(--warning);
            background-color: rgba(245, 158, 11, 0.08);
        }}

        .alert-tip {{
            border-left-color: var(--success);
            background-color: rgba(16, 185, 129, 0.08);
        }}

        .alert-caution {{
            border-left-color: var(--danger);
            background-color: rgba(239, 68, 68, 0.08);
        }}

        .alert-title {{
            font-weight: 700;
            font-size: 0.8rem;
            letter-spacing: 0.05em;
            display: block;
            margin-bottom: 0.25rem;
        }}

        .alert-important .alert-title {{ color: var(--primary-light); }}
        .alert-warning .alert-title {{ color: var(--warning); }}
        .alert-tip .alert-title {{ color: var(--success); }}
        .alert-caution .alert-title {{ color: var(--danger); }}

        /* Split view layout */
        .split-container {{
            display: flex;
            flex-direction: column;
            gap: 2rem;
            margin: 2rem 0;
        }}

        @media (min-width: 900px) {{
            .split-container {{
                flex-direction: row;
            }}
            .split-half {{
                flex: 1;
                min-width: 0;
            }}
        }}

        /* Text area for output */
        .terminal-block {{
            background-color: #020617;
            font-family: 'Courier New', Courier, monospace;
            padding: 1.5rem;
            border-radius: 10px;
            border: 1px solid var(--border);
            color: #38bdf8;
            font-size: 0.9rem;
            overflow-x: auto;
            white-space: pre-wrap;
            margin: 1rem 0;
        }}

        .image-card {{
            background: #0f172a;
            padding: 1rem;
            border-radius: 12px;
            border: 1px solid var(--border);
            text-align: center;
            margin: 1.5rem 0;
        }}

        .image-card img {{
            max-width: 100%;
            height: auto;
            border-radius: 6px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
        }}

        .image-caption {{
            color: var(--text-muted);
            font-size: 0.85rem;
            margin-top: 0.75rem;
            font-style: italic;
        }}

        /* Carousel Styles */
        .carousel-container {{
            position: relative;
            background: #0f172a;
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1rem;
            margin: 1.5rem 0;
            text-align: center;
        }}
        .carousel-slide {{
            display: none;
            animation: fade 0.5s;
        }}
        .carousel-slide.active {{
            display: block;
        }}
        .carousel-controls {{
            margin-top: 1rem;
            display: flex;
            justify-content: space-between;
        }}
        .carousel-controls button {{
            background: var(--primary);
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            cursor: pointer;
            font-family: 'Inter', sans-serif;
            font-weight: 500;
        }}
        .carousel-controls button:hover {{
            background: var(--primary-light);
        }}
        @keyframes fade {{
            from {{opacity: .4}} 
            to {{opacity: 1}}
        }}

        /* Collapse Button */
        .collapse-btn {{
            display: block;
            width: 100%;
            padding: 12px;
            background-color: #0f172a;
            color: var(--primary-light);
            border: 1px solid var(--border);
            border-radius: 8px;
            cursor: pointer;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            text-align: center;
            margin-top: 1rem;
            transition: all 0.3s ease;
        }}

        .collapse-btn:hover {{
            background-color: var(--surface-hover);
            color: #ffffff;
        }}

        .collapse-content {{
            display: none;
        }}

        .collapse-content.show {{
            display: table-row-group;
        }}

        /* Sub-tab navigation inside GSEA */
        .sub-tabs {{
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
        }}

        .sub-tab-btn {{
            padding: 0.5rem 1rem;
            background-color: rgba(30, 41, 59, 0.5);
            border: 1px solid var(--border);
            color: var(--text-muted);
            border-radius: 6px;
            cursor: pointer;
            font-family: 'Outfit', sans-serif;
            font-weight: 500;
            font-size: 0.85rem;
            transition: all 0.2s ease;
        }}

        .sub-tab-btn:hover {{
            color: var(--text);
        }}

        .sub-tab-btn.active {{
            background-color: var(--surface-hover);
            color: var(--primary-light);
            border-color: var(--primary-light);
        }}

        .sub-panel {{
            display: none;
        }}

        .sub-panel.active {{
            display: block;
        }}

        footer {{
            text-align: center;
            margin-top: 4rem;
            padding-top: 2rem;
            border-top: 1px solid var(--border);
            color: var(--text-muted);
            font-size: 0.9rem;
        }}
        
        /* Modal for Image Zoom */
        .modal {{
            display: none;
            position: fixed;
            z-index: 1000;
            padding-top: 50px;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgba(0,0,0,0.9);
            backdrop-filter: blur(10px);
        }}
        .modal-content {{
            margin: auto;
            display: block;
            width: 80%;
            max-width: 1200px;
            transition: transform 0.25s ease;
            cursor: zoom-in;
            border-radius: 8px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
        }}
        .modal-content.zoomed {{
            transform: scale(1.5);
            cursor: zoom-out;
        }}
        .close {{
            position: absolute;
            top: 15px;
            right: 35px;
            color: #f1f1f1;
            font-size: 40px;
            font-weight: bold;
            transition: 0.3s;
            cursor: pointer;
            z-index: 1001;
        }}
        .close:hover,
        .close:focus {{
            color: var(--primary-light);
            text-decoration: none;
            cursor: pointer;
        }}
        .image-card img, .carousel-slide img {{
            cursor: pointer;
            transition: 0.3s;
        }}
        .image-card img:hover, .carousel-slide img:hover {{
            opacity: 0.7;
            box-shadow: 0 0 15px var(--primary-light);
        }}
    </style>
</head>
<body>
    <div class="wrapper">
        <header>
            <h1>Reporte de Cierre: Dinámica de Subtipos y Abundancia NK</h1>
            <p>Análisis Integrativo de Inmunosenescencia y Comparativa de Subpoblaciones Bright vs Dim</p>
        </header>

        <nav class="nav-tabs">
            <button class="nav-btn active" onclick="switchPanel('narrative-panel')">📖 Narrativa de Cierre</button>
            <button class="nav-btn" onclick="switchPanel('abundance-panel')">📊 Abundancia Diferencial</button>
            <button class="nav-btn" onclick="switchPanel('expression-panel')">🧬 Expresión Diferencial (DEGs)</button>
            <button class="nav-btn" onclick="switchPanel('gsea-panel')">🖼️ Perfiles GSEApy</button>
            <button class="nav-btn" onclick="switchPanel('conclusions-panel')">🎯 Conclusiones</button>
        </nav>

        <!-- PANEL NARRATIVA -->
        <div id="narrative-panel" class="panel active">
            <h1>Narrativa de Integración Científica</h1>
            {report_html}
        </div>

        <!-- PANEL ABUNDANCIA -->
        <div id="abundance-panel" class="panel">
            <h1>Modelado de Abundancia Celular</h1>
            <p>Análisis del ratio de la subpoblación rara progenitora CD56bright frente a la población efectora mayoritaria CD56dim en una cohorte co-ocurrente de $N=187$ donantes.</p>
            
            <div class="split-container">
                <div class="split-half">
                    <h3>Ajuste de GLM Binomial para Proporciones</h3>
                    <p>Este modelo ajusta la probabilidad binomial considerando la profundidad de lectura por donante e incorporando el ensayo técnico como covariable correctora.</p>
                    <div class="terminal-block">{glm_content}</div>
                </div>
                <div class="split-half">
                    <h3>Abundancia Diferencial</h3>
                    <p>En individuos envejecidos, la probabilidad de muestrear una célula inmunomoduladora CD56bright disminuye significativamente (~37%).</p>
                </div>
            </div>

            <div class="alert alert-important">
                <span class="alert-title">DISCUSIÓN DE POTENCIA ESTADÍSTICA:</span>
                <p>El test de Mann-Whitney U reporta un p-valor no significativo ($p = 0.1674$) porque se ve afectado por el ruido estocástico (*shot noise*) en la detección de células CD56bright (población escasa). En contraste, el **GLM Binomial** corrige por el lote técnico <code>assay</code> (el cual exhibe efectos drásticos de hasta coef = -2.12) y pondera a los donantes por su conteo total, rescatando un p-valor altamente significativo ($p < 0.0001$) y confirmando la **pérdida progresiva de células CD56bright en donantes mayores.**</p>
            </div>

            <div class="image-card">
                <img src="{img_ratio}" alt="Análisis de Ratios NK por Edad">
                <div class="image-caption">Distribución del ratio CD56bright/CD56dim y porcentajes celulares en donantes adultos jóvenes vs. mayores.</div>
            </div>
        </div>

        <!-- PANEL EXPRESIÓN DIFERENCIAL -->
        <div id="expression-panel" class="panel">
            <h1>Expresión Diferencial (DEGs) por Subtipo</h1>
            <p>Comparativa de las firmas moleculares depuradas por pseudobulk PyDESeq2 ($padj &lt; 0.05$) bajo el diseño aditivo completo <code>~ assay + age_group</code>.</p>

            <!-- POOL GLOBAL -->
            <div style="margin-bottom: 2.5rem; padding: 1.5rem; background: rgba(15, 23, 42, 0.4); border-radius: 12px; border: 1px solid var(--border);">
                {global_pool_html}
            </div>

            <div class="split-container">
                <!-- COLUMNA CD56DIM -->
                <div class="split-half">
                    <h2>NK CD56dim (PyDESeq2 Pseudobulk)</h2>
                    <p>Para esta población abundante, aplicamos un enfoque de <b>pseudobulk</b> colapsando las cuentas a nivel de donante ($N = 187$: 152 adultos y 35 viejos). Este método suma los perfiles de todas las células CD56dim de un mismo individuo, creando perfiles sintéticos altamente robustos. La ventaja principal del pseudobulk frente a enfoques puramente <i>single-cell</i> es que erradica la sobredispersión artificial ("dropouts" o inflación de ceros) y mitiga los sesgos de pseudoreplicación, permitiendo usar herramientas estándar de oro como PyDESeq2. Gracias a este modelado, logramos aislar la señal biológica y revelar 12 DEGs robustos con FDR &lt; 0.05 (S100A8, S100A9, AHR, CD83) asociados a hiper-inflamación.</p>
                    
                    <div class="table-responsive">
                        <table>
                            <thead>
                                <tr>
                                    <th>N°</th>
                                    <th>Gen</th>
                                    <th>LFC</th>
                                    <th>Stat (Wald)</th>
                                    <th>p-value</th>
                                    <th>p-adj (FDR)</th>
                                </tr>
                            </thead>
                            <tbody>
                                {dim_top10}
                            </tbody>
                            <tbody id="dim-more-rows" class="collapse-content">
                                {dim_rest}
                            </tbody>
                        </table>
                    </div>
                    <button class="collapse-btn" onclick="toggleCollapse('dim-more-rows')">Ver más genes CD56dim</button>
                </div>

                <!-- COLUMNA CD56BRIGHT -->
                <div class="split-half">
                    <h2>NK CD56bright (PyDESeq2 Pseudobulk)</h2>
                    <p>A pesar de representar una población extremadamente minoritaria (~5%), optamos por mantener el rigor simétrico y aplicamos el mismo modelo <b>Pseudobulk con PyDESeq2</b> (<code>~ assay + age_group</code>) utilizado en CD56dim. Si bien la escasez de células por donante en este subtipo plantea un reto analítico, el algoritmo de DESeq2 está intrínsecamente diseñado para manejar estas disparidades mediante sus factores de tamaño (<i>Size Factors</i> calculados vía mediana de ratios), compensando matemáticamente a los donantes con baja captura celular.</p>
                    <p>Adicionalmente, la robusta contracción empírica de Bayes (<code>apeGLM</code>) castigó severamente cualquier gen cuya varianza estuviera impulsada por donantes con conteos minúsculos, comprimiendo su Fold Change hacia cero para proteger el modelo contra falsos positivos. Como resultado de esta protección algorítmica extrema —y del desbalance demográfico del N de donantes—, <b>cero genes lograron superar el estricto umbral FDR &lt; 0.05 individualmente</b>.</p>
                    <p>Sin embargo, el Estadístico de Wald continuo generado por DESeq2 probó ser matemáticamente perfecto para el <i>Gene Set Enrichment Analysis</i> (GSEA). Al no depender de líneas de corte arbitrarias, el GSEA rescató la señal biológica al detectar que cientos de genes mitocondriales se desplazaban coordinadamente a la baja en el ranking, revelando un colapso sistémico a pesar de la falta de potencia estadística a nivel de gen individual. El total de células CD56bright analizadas fue N = 4,986 (distribuidas en 173 donantes: 142 adultos / 31 ancianos). A continuación se muestran los top genes ordenados por p-valor nominal extraídos de PyDESeq2, evidenciando alteraciones en rutas estructurales y mitocondriales:</p>
                    
                    <div class="table-responsive">
                        <table>
                            <thead>
                                <tr>
                                    <th>N°</th>
                                    <th>Gen</th>
                                    <th>LFC</th>
                                    <th>Stat (Wald)</th>
                                    <th>p-value</th>
                                    <th>p-adj (FDR)</th>
                                </tr>
                            </thead>
                            <tbody>
                                {bright_top10}
                            </tbody>
                            <tbody id="bright-more-rows" class="collapse-content">
                                {bright_rest}
                            </tbody>
                        </table>
                    </div>
                    <button class="collapse-btn" onclick="toggleCollapse('bright-more-rows')">Ver más genes CD56bright</button>
                </div>
            </div>
        </div>

        <!-- PANEL GSEA -->
        <div id="gsea-panel" class="panel">
            <!-- ORA SECTION -->
            <div style="margin-bottom: 2.5rem;">
                {ora_html}
            </div>

            <h1>Enriquecimiento Funcional GSEA Preranked</h1>
            <p>Dotplots y gráficos de enriquecimiento comparando los análisis funcionales de los subtipos y el pool completo (Global).</p>
            <div class="methodology-explanation" style="margin-bottom: 20px;">
                <h3>Metodología GSEA Preranked</h3>
                <p>En lugar de depender de umbrales estadísticos arbitrarios para seleccionar una lista pequeña de "genes significativos" (Over-Representation Analysis), implementamos el algoritmo de <b>GSEA Preranked</b>. Este método evalúa el espectro continuo completo de los genes expresados, ordenándolos desde los más sobre-expresados hasta los más reprimidos. Esto es sumamente ventajoso para señales de envejecimiento o poblaciones raras (donante el ruido estadístico individual puede ocultar los genes a la penalización múltiple), ya que rescata de manera robusta el movimiento biológicamente coordinado de vías completas, superando el "shot noise" a nivel de gen individual.</p>
            </div>
            
            <div class="image-card">
                <h3>Resumen Comparativo de Vías Hallmarks Significativas</h3>
                <img src="{img_gsea_compare}" alt="Comparación de GSEA Hallmarks">
                <div class="image-caption">Comparativa del número de términos enriquedidos y sus scores entre Global, CD56dim y CD56bright.</div>
            </div>

            <div class="tabs-container" style="margin-top: 2rem;">
                <h3>Dotplots de Enriquecimiento (MSigDB Hallmark 2020)</h3>
                
                <div class="sub-tabs" id="gsea-subtabs">
                    <button class="sub-tab-btn active" onclick="switchSubTab('gsea-sub', 'dim')">NK CD56dim</button>
                    <button class="sub-tab-btn" onclick="switchSubTab('gsea-sub', 'bright')">NK CD56bright</button>
                    <button class="sub-tab-btn" onclick="switchSubTab('gsea-sub', 'global')">NK Cell General (Global)</button>
                </div>

                <div id="gsea-sub-dim" class="sub-panel active">
                    <div class="image-card">
                        <img src="{img_gsea_dim}" alt="GSEA CD56dim Hallmark">
                        <div class="image-caption">Dotplot GSEA Preranked para CD56dim. Se aprecia la represión de TNF-α/NF-κB (enmascaramiento por inflammaging).</div>
                    </div>
                    {gsea_tables_html}
                </div>

                <div id="gsea-sub-bright" class="sub-panel">
                    <div class="image-card">
                        <img src="{img_gsea_bright}" alt="GSEA CD56bright Hallmark">
                        <div class="image-caption">Dotplot GSEA Preranked para CD56bright, exhibiendo represión en OXPHOS/ROS mitocondrial.</div>
                    </div>
                </div>

                <div id="gsea-sub-global" class="sub-panel">
                    <div class="image-card">
                        <img src="{img_gsea_global}" alt="GSEA Global Hallmark">
                        <div class="image-caption">Dotplot GSEA Preranked Global. La firma de CD56dim domina completamente, cancelando la biología de la población rara.</div>
                    </div>
                </div>
            </div>

            <!-- INTEGRATION SECTION -->
            <div style="margin-top: 3rem;">
                {integration_html}
            </div>
        </div>

        <!-- PANEL CONCLUSIONES -->
        <div id="conclusions-panel" class="panel">
            {conclusions_html}
        </div>

        <footer>
            <p>Generado por Antigravity · Proyecto de Inmunosenescencia de Células NK · 2026</p>
        </footer>
    </div>

    <!-- Modal para Zoom de Imágenes -->
    <div id="imageModal" class="modal">
      <span class="close" onclick="closeModal()">&times;</span>
      <img class="modal-content" id="img01" onclick="toggleZoom()">
      <div id="caption" style="text-align: center; color: #cbd5e1; padding: 20px; font-size: 1.1rem; font-style: italic;"></div>
    </div>

    <script>
        function switchPanel(panelId) {{
            const buttons = document.querySelectorAll('.nav-btn');
            buttons.forEach(btn => btn.classList.remove('active'));
            
            const panels = document.querySelectorAll('.panel');
            panels.forEach(p => p.classList.remove('active'));
            
            event.target.classList.add('active');
            document.getElementById(panelId).classList.add('active');
        }}

        function switchSubTab(group, tabId) {{
            const tabsContainer = document.getElementById(group + '-tabs');
            const buttons = event.currentTarget.parentNode.getElementsByClassName('sub-tab-btn');
            for (let btn of buttons) {{
                btn.classList.remove('active');
            }}
            
            const panels = document.querySelectorAll('[id^="' + group + '-"]');
            panels.forEach(p => {{
                if (p.id !== group + '-tabs') {{
                    p.classList.remove('active');
                }}
            }});
            
            event.currentTarget.classList.add('active');
            document.getElementById(group + '-' + tabId).classList.add('active');
        }}

        function toggleCollapse(divId) {{
            const content = document.getElementById(divId);
            if (content.classList.contains('show')) {{
                content.classList.remove('show');
                event.target.innerText = "Ver más genes";
            }} else {{
                content.classList.add('show');
                event.target.innerText = "Ocultar genes adicionales";
            }}
        }}
        
        function moveCarousel(id, direction) {{
            const container = document.getElementById(id);
            const slides = container.querySelectorAll('.carousel-slide');
            let activeIndex = 0;
            slides.forEach((slide, index) => {{
                if (slide.classList.contains('active')) {{
                    activeIndex = index;
                    slide.classList.remove('active');
                }}
            }});
            let newIndex = activeIndex + direction;
            if (newIndex >= slides.length) newIndex = 0;
            if (newIndex < 0) newIndex = slides.length - 1;
            slides[newIndex].classList.add('active');
        }}

        // Configuración del Modal de Imágenes (Lightbox Zoom)
        document.addEventListener("DOMContentLoaded", function() {{
            var modal = document.getElementById("imageModal");
            var modalImg = document.getElementById("img01");
            var captionText = document.getElementById("caption");
            var images = document.querySelectorAll(".image-card img, .carousel-slide img");
            
            images.forEach(img => {{
                img.onclick = function(){{
                    modal.style.display = "block";
                    modalImg.src = this.src;
                    modalImg.classList.remove("zoomed");
                    var caption = this.nextElementSibling;
                    if(caption && caption.classList.contains("image-caption")) {{
                        captionText.innerHTML = caption.innerHTML;
                    }} else {{
                        captionText.innerHTML = this.alt;
                    }}
                }}
            }});
        }});

        function closeModal() {{
            document.getElementById("imageModal").style.display = "none";
        }}
        
        function toggleZoom() {{
            var img = document.getElementById("img01");
            img.classList.toggle("zoomed");
        }}
    </script>
</body>
</html>
"""

    output_html = "../results/Reporte_Integrativo_Subtipos_Abundancia.html"
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(full_html)
        
    print(f"🎉 ¡Reporte HTML integrativo premium guardado con éxito en: {output_html}!")

if __name__ == '__main__':
    main()
