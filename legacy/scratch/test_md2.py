import markdown
import codecs

with codecs.open(r'C:\Users\PREDATOR\.gemini\antigravity-ide\brain\a7692536-367e-4c7b-b76f-4a7d478e4ebf\reporte_integrativo_final.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
table_lines = lines[408:420]
table_text = '\n'.join(table_lines)

html = markdown.markdown(table_text, extensions=['tables', 'md_in_html'])
print(html)
