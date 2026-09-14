import codecs

with codecs.open(r'C:\Users\PREDATOR\.gemini\antigravity-ide\brain\a7692536-367e-4c7b-b76f-4a7d478e4ebf\reporte_integrativo_final.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Agotamiento Inmune' in line or 'SASP & Exhaustion' in line:
        print(f"Line {i+1}: {line.strip()}")
        print("".join(lines[i+1:i+20]))
