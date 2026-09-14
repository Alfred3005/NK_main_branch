import codecs

md_path = r'C:\Users\PREDATOR\.gemini\antigravity-ide\brain\a7692536-367e-4c7b-b76f-4a7d478e4ebf\reporte_integrativo_final.md'
with codecs.open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix mermaid
text = text.replace('C --> D{¿El Assay tiene Adultos > 0\nY Ancianos > 0?}', 'C --> D{"¿El Assay tiene Adultos > 0<br/>Y Ancianos > 0?"}')

with codecs.open(md_path, 'w', encoding='utf-8') as f:
    f.write(text)

py_path = r'C:\Users\PREDATOR\Documents\Antigravity_workspaces\NK_pipeline_RNA_ambient_Main_Branch\scripts\generate_report_v2.py'
with codecs.open(py_path, 'r', encoding='utf-8') as f:
    py_text = f.read()

# Add placeholder logic for tables
new_logic = """
def parse_markdown_to_html(md_content):
    # Hide inline <details> inside tables to prevent breaking md_in_html nested parsing
    md_content = md_content.replace('<details><summary>', '___INLINE_DETAILS_START___')
    md_content = md_content.replace('</details> |', '___INLINE_DETAILS_END___ |')
    md_content = md_content.replace('</details></details>', '___INLINE_DETAILS_END___</details>')

    # Enable markdown parsing inside HTML tags
    md_content = md_content.replace('<details ', '<details markdown="1" ')
    md_content = md_content.replace('<div ', '<div markdown="1" ')
    
    # Pre-process mermaid (wrap in div.mermaid instead of pre code so mermaid js picks it up)
    def mermaid_repl(match):
        return f"<pre class='mermaid'>{match.group(1)}</pre>"
    md_content = re.sub(r'```mermaid\\n(.*?)\\n```', mermaid_repl, md_content, flags=re.DOTALL)
    
    # Process carousels first
    md_content = process_carousels(md_content)
    
    # Convert markdown to HTML
    html = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'md_in_html'])
    
    # Restore inline details
    html = html.replace('___INLINE_DETAILS_START___', '<details><summary>')
    html = html.replace('___INLINE_DETAILS_END___', '</details>')
    
    # Post-process alerts and images
    html = process_alerts_and_images(html)
    
    return html
"""

import re
py_text = re.sub(r'def parse_markdown_to_html\(md_content\):.*?return html\n', new_logic, py_text, flags=re.DOTALL)

with codecs.open(py_path, 'w', encoding='utf-8') as f:
    f.write(py_text)

print("Done replacements")
