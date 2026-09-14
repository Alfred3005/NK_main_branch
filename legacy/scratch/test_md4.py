import codecs

with codecs.open(r'C:\Users\PREDATOR\Documents\Antigravity_workspaces\NK_pipeline_RNA_ambient_Main_Branch\results\Reporte_Integrativo_Subtipos_Abundancia_V2.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("Inflammatory Response")
print(text[idx-200:idx+400])
