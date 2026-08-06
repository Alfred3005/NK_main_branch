import os
import base64
import re
import random
import markdown

def get_image_base64(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/png;base64,{encoded_string}"

def process_carousels(md_text):
    # Encontrar bloques ````carousel ... ````
    pattern = re.compile(r'````carousel\n(.*?)\n````', re.DOTALL)
    
    def repl(match):
        content = match.group(1)
        slides = content.split('<!-- slide -->')
        cid = f"carousel-{random.randint(10000,99999)}"
        html = f"<div class='carousel-container' id='{cid}'>\n"
        for i, slide in enumerate(slides):
            active = "active" if i == 0 else ""
            html += f"<div class='carousel-slide {active}'>\n"
            # Procesar el markdown de la diapositiva
            slide_html = markdown.markdown(slide.strip(), extensions=['tables', 'fenced_code', 'md_in_html'])
            html += slide_html
            html += "</div>\n"
        html += f"""<div class='carousel-controls'>
            <button onclick='moveCarousel("{cid}", -1)'>&#10094; Anterior</button>
            <button onclick='moveCarousel("{cid}", 1)'>Siguiente &#10095;</button>
        </div></div>\n"""
        return html

    return pattern.sub(repl, md_text)

def process_alerts_and_images(html_text):
    # Process Github style alerts that were parsed as blockquotes
    # <blockquote><p>[!NOTE]<br />text</p></blockquote>
    # or similar.
    def alert_repl(match):
        alert_type = match.group(1).lower()
        content = match.group(2)
        # Map github types to our classes
        if alert_type == "note": css_class = "note"
        elif alert_type == "important": css_class = "important"
        elif alert_type == "warning": css_class = "warning"
        elif alert_type == "tip": css_class = "tip"
        elif alert_type == "caution": css_class = "caution"
        else: css_class = "note"
        
        return f"<div class='alert alert-{css_class}'><span class='alert-title'>{alert_type.upper()}</span><div>{content}</div></div>"
    
    # Regex to catch blockquotes starting with [!TYPE]
    html_text = re.sub(r'<blockquote>\s*<p>\[!(.*?)\](?:<br\s*/?>|\n)(.*?)</p>\s*</blockquote>', alert_repl, html_text, flags=re.DOTALL | re.IGNORECASE)
    
    # Process images to add image-card and base64
    def img_repl(match):
        alt = match.group(1)
        src = match.group(2)
        if src.startswith("C:/") or src.startswith("../"):
            b64 = get_image_base64(src.replace("C:/", "C:\\"))
            if not b64: b64 = get_image_base64(src) # try raw
            if b64: src = b64
        return f"<div class='image-card'><img src='{src}' alt='{alt}'></div>"
    
    html_text = re.sub(r'<img\s+alt="(.*?)"\s+src="(.*?)"\s*/>', img_repl, html_text)
    
    # Fix captions (e.g., <p><em>Figura 1: ...</em></p> just after an image)
    html_text = re.sub(r'</p>\s*<p><em>(Figura.*?)</em></p>', r'</p><div class="image-caption" style="text-align: center; margin-top: -15px; margin-bottom: 20px;">\1</div>', html_text)

    # Color fixes for contrast
    html_text = html_text.replace('color:blue', 'color:#38bdf8').replace('color: blue', 'color:#38bdf8')
    html_text = html_text.replace('color:red', 'color:#f87171').replace('color: red', 'color:#f87171')
    
    return html_text



def parse_markdown_to_html(md_content):
    # Hide inline <details> inside tables to prevent breaking md_in_html nested parsing
    md_content = md_content.replace('<details><summary>', 'PLACEHOLDERINLINEDETAILSSTART')
    md_content = md_content.replace('</details> |', 'PLACEHOLDERINLINEDETAILSEND |')

    # Enable markdown parsing inside HTML tags
    md_content = md_content.replace('<details ', '<details markdown="1" ')
    md_content = md_content.replace('<div ', '<div markdown="1" ')
    
    # Pre-process mermaid (wrap in div.mermaid instead of pre code so mermaid js picks it up)
    def mermaid_repl(match):
        return f"<pre class='mermaid'>{match.group(1)}</pre>"
    md_content = re.sub(r'```mermaid\n(.*?)\n```', mermaid_repl, md_content, flags=re.DOTALL)
    
    # Process carousels first
    md_content = process_carousels(md_content)
    
    # Convert markdown to HTML
    html = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'md_in_html'])
    
    # Restore inline details
    html = html.replace('PLACEHOLDERINLINEDETAILSSTART', '<details><summary>')
    html = html.replace('PLACEHOLDERINLINEDETAILSEND', '</details>')
    
    # Post-process alerts and images
    html = process_alerts_and_images(html)
    
    return html

def main():
    print("🚀 Iniciando la compilación del Reporte Integrativo Premium V2 (Con Pestañas)...")
    
    report_md = r"C:\Users\PREDATOR\.gemini\antigravity-ide\brain\a7692536-367e-4c7b-b76f-4a7d478e4ebf\reporte_integrativo_final.md"
    
    with open(report_md, "r", encoding="utf-8") as f:
        full_md = f.read()

    # Split the markdown into sections
    narrative_raw = re.split(r'## (?:.*? )?2\.\s+Abundancia Diferencial', full_md)[0]
    
    rem_1 = re.split(r'## (?:.*? )?2\.\s+Abundancia Diferencial', full_md)[1]
    abundance_raw = "## 2. Abundancia Diferencial\n" + re.split(r'## (?:.*? )?3\.\s+Expresión Diferencial \(DEGs\)', rem_1)[0]
    
    rem_2 = re.split(r'## (?:.*? )?3\.\s+Expresión Diferencial \(DEGs\)', rem_1)[1]
    degs_raw = "## 3. Expresión Diferencial (DEGs)\n" + re.split(r'## (?:.*? )?4\.\s+Enriquecimiento de Vías \(ORA y GSEA\)', rem_2)[0]
    
    rem_3 = re.split(r'## (?:.*? )?4\.\s+Enriquecimiento de Vías \(ORA y GSEA\)', rem_2)[1]
    gsea_raw = "## 4. Enriquecimiento de Vías (ORA y GSEA)\n" + re.split(r'## (?:.*? )?5\.\s+Conclusiones Integrativas', rem_3)[0]
    
    conclusions_raw = "## 5. Conclusiones Integrativas\n" + re.split(r'## (?:.*? )?5\.\s+Conclusiones Integrativas', rem_3)[1]

    # Parse each section
    narrative_html = parse_markdown_to_html(narrative_raw)
    abundance_html = parse_markdown_to_html(abundance_raw)
    degs_html = parse_markdown_to_html(degs_raw)
    gsea_html = parse_markdown_to_html(gsea_raw)
    conclusions_html = parse_markdown_to_html(conclusions_raw)

    full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte Integrativo: CD56dim vs CD56bright y Abundancia NK V2</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ startOnLoad: true, theme: 'dark' }});
    </script>
    <style>
        :root {{
            --primary: #4f46e5;
            --primary-light: #818cf8;
            --background: #0f172a;
            --surface: #1e293b;
            --surface-hover: #334155;
            --text: #f8fafc;
            --text-muted: #94a3b8;
            --border: #334155;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --card-bg: rgba(30, 41, 59, 0.7);
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Inter', sans-serif; background-color: var(--background); color: var(--text); line-height: 1.6; padding: 1.5rem 1rem; }}
        .wrapper {{ max-width: 1200px; margin: 0 auto; }}

        header {{
            text-align: center; margin-bottom: 2.5rem; padding: 2.5rem;
            background: linear-gradient(135deg, rgba(79, 70, 229, 0.15) 0%, rgba(129, 140, 248, 0.05) 100%);
            border-radius: 16px; border: 1px solid var(--border); box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2); backdrop-filter: blur(5px);
        }}
        header h1 {{ font-family: 'Outfit', sans-serif; font-size: 2.5rem; font-weight: 700; background: linear-gradient(135deg, #e0e7ff, #a5b4fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem; }}
        header p {{ color: var(--text-muted); font-size: 1.1rem; }}
        
        /* Navigation Tabs */
        .nav-tabs {{ display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 2rem; border-bottom: 1px solid var(--border); padding-bottom: 0.75rem; }}
        .nav-btn {{ padding: 0.75rem 1.25rem; cursor: pointer; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; font-family: 'Outfit', sans-serif; font-weight: 600; font-size: 0.95rem; color: var(--text-muted); transition: all 0.3s ease; }}
        .nav-btn:hover {{ background: var(--surface-hover); color: var(--text); }}
        .nav-btn.active {{ background: var(--primary); color: #ffffff; border-color: var(--primary); box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3); }}

        /* Section Panel */
        .panel {{ display: none; background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; padding: 2.5rem; margin-bottom: 2rem; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3); backdrop-filter: blur(10px); }}
        .panel.active {{ display: block; }}
        
        h1, h2, h3, h4 {{ font-family: 'Outfit', sans-serif; font-weight: 600; color: #e2e8f0; margin-top: 1.5rem; margin-bottom: 0.75rem; }}
        .panel > h1 {{ font-size: 2.2rem; color: #ffffff; border-bottom: 2px solid var(--border); padding-bottom: 0.75rem; margin-top: 0; margin-bottom: 1.5rem; }}
        h2 {{ font-size: 1.6rem; color: var(--primary-light); margin-top: 2rem; border-bottom: 1px solid var(--border); padding-bottom: 0.4rem; }}
        
        p {{ margin-bottom: 1.2rem; color: #cbd5e1; font-size: 1.05rem; }}
        ul {{ margin-bottom: 1.5rem; }}
        li {{ margin-left: 2rem; margin-bottom: 0.5rem; color: #cbd5e1; }}
        blockquote {{ padding: 0.75rem 1.25rem; border-left: 4px solid var(--primary-light); background: rgba(30, 41, 59, 0.4); border-radius: 0 8px 8px 0; margin: 1.5rem 0; font-style: italic; }}
        
        .table-responsive {{ width: 100%; overflow-x: auto; margin: 1.5rem 0; border-radius: 10px; border: 1px solid var(--border); }}
        table {{ width: 100%; border-collapse: collapse; font-size: 0.95rem; text-align: left; }}
        th, td {{ padding: 12px 16px; border-bottom: 1px solid var(--border); }}
        th {{ background-color: #0f172a; color: #ffffff; font-weight: 600; }}
        tr:nth-child(even) {{ background-color: rgba(15, 23, 42, 0.3); }}
        tr:hover {{ background-color: rgba(79, 70, 229, 0.1); }}
        
        .alert {{ padding: 1.25rem 1.5rem; border-radius: 8px; margin: 1.5rem 0; border-left: 4px solid var(--primary); background-color: rgba(79, 70, 229, 0.1); color: #e2e8f0; }}
        .alert-important {{ border-left-color: var(--primary); background-color: rgba(79, 70, 229, 0.08); }}
        .alert-warning {{ border-left-color: var(--warning); background-color: rgba(245, 158, 11, 0.08); }}
        .alert-tip {{ border-left-color: var(--success); background-color: rgba(16, 185, 129, 0.08); }}
        .alert-caution {{ border-left-color: var(--danger); background-color: rgba(239, 68, 68, 0.08); }}
        .alert-title {{ font-weight: 700; font-size: 0.8rem; letter-spacing: 0.05em; display: block; margin-bottom: 0.25rem; }}
        .alert-important .alert-title {{ color: var(--primary-light); }}
        
        .image-card {{ background: #0f172a; padding: 1rem; border-radius: 12px; border: 1px solid var(--border); text-align: center; margin: 1.5rem 0; }}
        .image-card img {{ max-width: 100%; height: auto; border-radius: 6px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5); }}
        .image-caption {{ color: var(--text-muted); font-size: 0.85rem; margin-top: 0.75rem; font-style: italic; }}

        .carousel-container {{ position: relative; background: #0f172a; border: 1px solid var(--border); border-radius: 12px; padding: 1rem; margin: 1.5rem 0; text-align: center; }}
        .carousel-slide {{ display: none; animation: fade 0.5s; }}
        .carousel-slide.active {{ display: block; }}
        .carousel-controls {{ margin-top: 1rem; display: flex; justify-content: space-between; }}
        .carousel-controls button {{ background: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 6px; cursor: pointer; font-family: 'Inter', sans-serif; font-weight: 500; }}
        .carousel-controls button:hover {{ background: var(--primary-light); }}
        @keyframes fade {{ from {{opacity: .4}} to {{opacity: 1}} }}

        /* Modal for Image Zoom */
        .modal {{ display: none; position: fixed; z-index: 1000; padding-top: 50px; left: 0; top: 0; width: 100%; height: 100%; overflow: auto; background-color: rgba(0,0,0,0.9); backdrop-filter: blur(10px); }}
        .modal-content {{ margin: auto; display: block; width: 80%; max-width: 1200px; transition: transform 0.25s ease; cursor: zoom-in; border-radius: 8px; box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5); }}
        .modal-content.zoomed {{ transform: scale(1.5); cursor: zoom-out; }}
        .close {{ position: absolute; top: 15px; right: 35px; color: #f1f1f1; font-size: 40px; font-weight: bold; transition: 0.3s; cursor: pointer; z-index: 1001; }}
        .close:hover, .close:focus {{ color: var(--primary-light); text-decoration: none; cursor: pointer; }}
        .image-card img, .carousel-slide img {{ cursor: pointer; transition: 0.3s; }}
        .image-card img:hover, .carousel-slide img:hover {{ opacity: 0.7; box-shadow: 0 0 15px var(--primary-light); }}
        
        details > summary {{ list-style: none; outline: none; }}
        details > summary::-webkit-details-marker {{ display: none; }}
    </style>
</head>
<body>
    <div class="wrapper">
        <header>
            <h1>Reporte de Cierre: Dinámica de Subtipos y Abundancia NK</h1>
            <p>Análisis Integrativo de Inmunosenescencia y Comparativa de Subpoblaciones</p>
        </header>

        <nav class="nav-tabs">
            <button class="nav-btn active" onclick="switchPanel('narrative-panel')">📖 Narrativa de Cierre</button>
            <button class="nav-btn" onclick="switchPanel('abundance-panel')">📊 Abundancia Diferencial</button>
            <button class="nav-btn" onclick="switchPanel('expression-panel')">🧬 Expresión Diferencial (DEGs)</button>
            <button class="nav-btn" onclick="switchPanel('gsea-panel')">🖼️ Perfiles GSEApy</button>
            <button class="nav-btn" onclick="switchPanel('conclusions-panel')">🎯 Conclusiones</button>
        </nav>

        <div id="narrative-panel" class="panel active">
            {narrative_html}
        </div>
        
        <div id="abundance-panel" class="panel">
            {abundance_html}
        </div>
        
        <div id="expression-panel" class="panel">
            {degs_html}
        </div>
        
        <div id="gsea-panel" class="panel">
            {gsea_html}
        </div>
        
        <div id="conclusions-panel" class="panel">
            {conclusions_html}
        </div>

        <footer>
            <p style="text-align: center; color: var(--text-muted); padding: 20px;">Generado por Antigravity · Proyecto de Inmunosenescencia de Células NK · 2026</p>
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

    out_path = os.path.abspath("results/Reporte_Integrativo_Subtipos_Abundancia_V2.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"🎉 ¡Reporte HTML V2 guardado con éxito en: {out_path}!")

if __name__ == '__main__':
    main()
