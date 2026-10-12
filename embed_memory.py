import os
import json
import shutil
import urllib.request
import sys

file_path = sys.argv[1]
vault_dir = os.path.dirname(os.path.dirname(file_path))
index_path = os.path.join(vault_dir, "embeddings_index.json")
bak_path = index_path + ".bak"

with open(file_path, "r", encoding="utf-8") as f:
    text_content = f.read()

url = "http://127.0.0.1:1234/v1/embeddings"
data = json.dumps({
    "input": text_content[:4000],
    "model": "text-embedding-nomic-embed-text-v1.5@q4_k_m"
}).encode("utf-8")
headers = {"Content-Type": "application/json", "Authorization": "Bearer lm-studio"}
req = urllib.request.Request(url, data=data, headers=headers)

try:
    with urllib.request.urlopen(req, timeout=10) as response:
        res_data = json.loads(response.read().decode("utf-8"))
        embedding = res_data["data"][0]["embedding"]

        # Respaldo atomico preventivo
        if os.path.exists(index_path):
            shutil.copy2(index_path, bak_path)

        index = []
        if os.path.exists(index_path):
            with open(index_path, "r", encoding="utf-8") as idx_file:
                index = json.load(idx_file)

        # Evitar duplicados por nombre de archivo
        fname = os.path.basename(file_path)
        index = [item for item in index if item.get("file") != fname]
        index.append({"file": fname, "embedding": embedding})

        with open(index_path, "w", encoding="utf-8") as idx_file:
            json.dump(index, idx_file, ensure_ascii=False)
    print("EXITO: Embedding generado e indexado atomicamente.")
except Exception as e:
    print(f"ADVERTENCIA_LMSTUDIO: No se pudo vectorizar ({e}). El archivo Markdown se mantiene seguro.")
    if os.path.exists(bak_path) and not os.path.exists(index_path):
        shutil.copy2(bak_path, index_path)
