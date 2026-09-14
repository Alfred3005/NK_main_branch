import re
import markdown

with open(r'C:\Users\PREDATOR\.gemini\antigravity-ide\brain\a7692536-367e-4c7b-b76f-4a7d478e4ebf\reporte_integrativo_final.md', "r", encoding="utf-8") as f:
    full_md = f.read()

narrative_raw = re.split(r'## (?:.*? )?2\.\s+Abundancia Diferencial', full_md)[0]
rem_1 = re.split(r'## (?:.*? )?2\.\s+Abundancia Diferencial', full_md)[1]
rem_2 = re.split(r'## (?:.*? )?3\.\s+Expresión Diferencial \(DEGs\)', rem_1)[1]
rem_3 = re.split(r'## (?:.*? )?4\.\s+Enriquecimiento de Vías \(ORA y GSEA\)', rem_2)[1]
gsea_raw = "## 4. Enriquecimiento de Vías (ORA y GSEA)\n" + re.split(r'## (?:.*? )?5\.\s+Conclusiones Integrativas', rem_3)[0]

md_content = gsea_raw.replace('<details ', '<details markdown="1" ')
md_content = md_content.replace('<div ', '<div markdown="1" ')

html = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'md_in_html'])

idx2 = html.find("MSigDB_Hallmark_2020")
print("\nHTML CONTENT AROUND TABLE:")
print(html[idx2-200:idx2+400])

