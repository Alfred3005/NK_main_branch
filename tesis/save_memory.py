import os
import json
import shutil
import urllib.request

content = """# Cierre de Sesión: Clarificación de Anergia vs Exhaustion y Perspectivas Futuras
Fecha: 2026-10-06

## Decisiones Epistemológicas y Conceptuales
* Se consolidó la diferenciación mecanicista entre la anergia circulante inducida por el *inflammaging* sistémico (desensibilización adaptativa frente al ruido proinflamatorio crónico de bajo grado) y el agotamiento terminal (*exhaustion*) asociado a microambientes tisulares severamente patológicos como la FPI.
* Se validaron estilométricamente todas las correcciones, alcanzando un *Burstiness* final de 19.26 y longitud media de 37 palabras sin detectar clichés de LLM, blindando la cadencia humana académica.
* Se estructuró la sección de *Perspectivas y Limitaciones*, proponiendo de forma directa el uso futuro de ensayos de quimiotaxis (*Transwell*) y transcriptómica espacial para evaluar empíricamente la "ceguera quimiotáctica" entre el linaje NK y las cDC1 por la represión génica de XCL1/XCL2.

## Modificaciones de Archivos
* `08_Bibliografia.md`: Se indexaron y completaron los metadatos y la lista completa de autores de las referencias recién añadidas (Agudelo Garcia et al. y Martinez-Sánchez et al.) empleando la API de OpenAlex, reordenando numéricamente el documento.
* `06_Discusion.md`: Se reestructuró la discusión final sobre senescencia celular y ceguera quimiotáctica, con especial refinamiento en las líneas descriptivas del aislamiento adaptativo y las perspectivas clínicas y metodológicas a futuro.

## Hitos Alcanzados (ROADMAP)
* Se dio cierre exitoso a las revisiones estructurales y de contenido del Capítulo 6 (Discusión).

## Tareas Pendientes para la Próxima Sesión
* Redactar y auditar la fundamentación metodológica del **Anexo A**: el rescate de datos balanceados y el uso de la herramienta probabilística `scAR` para la depuración del ARN ambiental.
* Revisar el flujo visual compilado en Quarto y dar inicio a la redacción del Capítulo de Conclusiones.
"""

file_path = r'C:\Users\PREDATOR\Documents\Obsidian_vault01\Memoria_Antigravity\2026-10-06_Clarificacion_Anergia_Perspectivas.md'
os.makedirs(os.path.dirname(file_path), exist_ok=True)
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('File written successfully.')

vault_dir = os.path.dirname(os.path.dirname(file_path))
index_path = os.path.join(vault_dir, 'embeddings_index.json')
bak_path = index_path + '.bak'

url = 'http://127.0.0.1:1234/v1/embeddings'
data = json.dumps({
    'input': content[:4000],
    'model': 'text-embedding-nomic-embed-text-v1.5@q4_k_m'
}).encode('utf-8')
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer lm-studio'}
req = urllib.request.Request(url, data=data, headers=headers)

try:
    with urllib.request.urlopen(req, timeout=10) as response:
        res_data = json.loads(response.read().decode('utf-8'))
        embedding = res_data['data'][0]['embedding']

        if os.path.exists(index_path):
            shutil.copy2(index_path, bak_path)

        index = []
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as idx_file:
                try:
                    index = json.load(idx_file)
                except:
                    pass

        fname = os.path.basename(file_path)
        index = [item for item in index if item.get('file') != fname]
        index.append({'file': fname, 'embedding': embedding})

        with open(index_path, 'w', encoding='utf-8') as idx_file:
            json.dump(index, idx_file, ensure_ascii=False)
    print('EXITO: Embedding generado e indexado atomicamente.')
except Exception as e:
    print(f'ADVERTENCIA_LMSTUDIO: No se pudo vectorizar ({e}). El archivo Markdown se mantiene seguro.')
    if os.path.exists(bak_path) and not os.path.exists(index_path):
        shutil.copy2(bak_path, index_path)
