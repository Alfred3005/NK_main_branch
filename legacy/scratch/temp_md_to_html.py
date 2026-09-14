import markdown
import codecs

with codecs.open(r'C:\Users\PREDATOR\.gemini\antigravity-ide\brain\21ad548d-65b8-4390-8b9a-1f0b804893b5\collinearity_report.md', 'r', encoding='utf-8') as f:
    text = f.read()

html = markdown.markdown(text, extensions=['tables', 'fenced_code'])

template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Reporte de Colinealidad</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 40px auto; padding: 20px; }}
        h1, h2, h3, h4 {{ color: #111; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }}
        table {{ border-collapse: collapse; width: 100%; margin: 15px 0; }}
        th, td {{ border: 1px solid #dfe2e5; padding: 8px 12px; text-align: left; }}
        th {{ background-color: #f6f8fa; }}
        blockquote {{ border-left: 4px solid #dfe2e5; color: #6a737d; padding-left: 15px; margin-left: 0; }}
        pre {{ background-color: #f6f8fa; border-radius: 6px; padding: 16px; overflow: auto; }}
        .mermaid {{ margin: 20px 0; text-align: center; }}
    </style>
</head>
<body>
{html}
<script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({{ startOnLoad: true }});
    // Replace code blocks containing mermaid with a div for rendering
    document.querySelectorAll('code.language-mermaid').forEach(el => {{
        const pre = el.parentElement;
        const div = document.createElement('div');
        div.className = 'mermaid';
        div.textContent = el.textContent;
        pre.replaceWith(div);
    }});
</script>
</body>
</html>"""

with codecs.open(r'results\Reporte_Colinealidad.html', 'w', encoding='utf-8') as f:
    f.write(template)

print('Conversión completada. HTML guardado en results\Reporte_Colinealidad.html')
