import codecs

with codecs.open(r'C:\Users\PREDATOR\.gemini\antigravity-ide\brain\a7692536-367e-4c7b-b76f-4a7d478e4ebf\reporte_integrativo_final.md', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.split('\n'):
    if line.startswith('##'):
        print(line)
