import os
import markdown
import io

src_dir = r'c:\Users\PREDATOR\Documents\Antigravity_workspaces\TESIS_NK_2\manuscripts'
files = ['01_Introduccion.md', '02_Marco_Teorico.md', '03_Pregunta_Hipotesis_Objetivos.md', '04_Metodologia.md', '08_Bibliografia.md']

md_content = ''
for fname in files:
    fpath = os.path.join(src_dir, fname)
    if os.path.exists(fpath):
        with io.open(fpath, 'r', encoding='utf-8') as f:
            md_content += f.read() + '\n\n---\n\n'

html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

full_html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Borrador Tesis NK</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 900px; margin: 0 auto; padding: 2rem; line-height: 1.6; color: #333; }}
        code {{ background: #f4f4f4; padding: 2px 4px; border-radius: 4px; }}
        pre {{ background: #f4f4f4; padding: 1rem; overflow-x: auto; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; }}
        th {{ background: #f2f2f2; }}
    </style>
</head>
<body>
{html_content}
</body>
</html>'''

out_path = os.path.join(src_dir, 'Borrador_Tesis_Actual.html')
with io.open(out_path, 'w', encoding='utf-8') as f:
    f.write(full_html)

print('HTML guardado en:', out_path)
