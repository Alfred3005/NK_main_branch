#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Análisis de sensibilidad: expresión diferencial y GSEA sin la corrección de scAR.

Repite 22_pseudobulk_subtypes_pydeseq2.py y 24_subtypes_ranked_gsea.py con la capa
`raw_counts` en lugar de `counts`, en una carpeta temporal, y compara con
results/subtypes. Requiere haber corrido antes run_reproducible_pipeline.py.

Produce en results/subtypes/:
    sensibilidad_scar_deg.tsv    los DEG del análisis global, con y sin scAR
    sensibilidad_scar_vias.tsv   las vías citadas en la tesis, con y sin scAR
"""

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "results" / "subtypes"
VIAS = [
    ("cd56bright", "MSigDB_Hallmark_2020", "UV Response Dn"),
    ("cd56dim", "MSigDB_Hallmark_2020", "UV Response Dn"),
    ("cd56dim", "MSigDB_Hallmark_2020", "Myc Targets V1"),
    ("cd56dim", "GO_Biological_Process_2023", "Positive Regulation Of Telomere Maintenance Via Telomerase"),
    ("cd56dim", "MSigDB_Hallmark_2020", "TNF-alpha Signaling via NF-kB"),
    ("cd56dim", "GO_Biological_Process_2023", "Regulation Of mRNA Splicing, Via Spliceosome"),
    ("cd56bright", "KEGG_2021_Human", "Oxidative phosphorylation"),
    ("cd56dim", "KEGG_2021_Human", "Oxidative phosphorylation"),
]


def correr_sin_scar(destino):
    """Copia los scripts, cambia solo la capa de entrada y los ejecuta."""
    scripts = destino / "scripts"
    scripts.mkdir()
    (destino / "data").mkdir()
    os.symlink((ROOT / "data" / "NK_dataset_qc_ready.h5ad").resolve(), destino / "data" / "NK_dataset_qc_ready.h5ad")
    nombres = ["22_pseudobulk_subtypes_pydeseq2.py", "24_subtypes_ranked_gsea.py"]
    for nombre in nombres:
        shutil.copy(ROOT / "scripts" / nombre, scripts / nombre)
    ruta = scripts / nombres[0]
    texto = ruta.read_bytes()
    original = b"adata.X = adata.layers['counts'].copy()"
    if texto.count(original) != 1:
        raise SystemExit("No se encontró la línea que elige la capa en el script 22.")
    ruta.write_bytes(texto.replace(original, b"adata.X = adata.layers['raw_counts'].copy()"))
    for nombre in nombres:
        subprocess.run([sys.executable, str(scripts / nombre)], cwd=destino, check=True,
                       stdout=subprocess.DEVNULL, env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    return destino / "results" / "subtypes"


def comparar_deg(sin):
    con_scar = pd.read_csv(BASE / "deseq2_results_nk_cell_general.csv").set_index("feature_name")
    sin_scar = pd.read_csv(sin / "deseq2_results_nk_cell_general.csv").set_index("feature_name")
    deg = con_scar.index[con_scar.padj < 0.05]
    tabla = pd.DataFrame({
        "lfc_con_scar": con_scar.log2FoldChange[deg], "padj_con_scar": con_scar.padj[deg],
        "lfc_sin_scar": sin_scar.log2FoldChange.reindex(deg), "padj_sin_scar": sin_scar.padj.reindex(deg),
        "stat_con_scar": con_scar.stat[deg], "stat_sin_scar": sin_scar.stat.reindex(deg),
    })
    tabla["significativo_en_ambos"] = tabla.padj_sin_scar < 0.05
    tabla["misma_direccion"] = (tabla.stat_con_scar * tabla.stat_sin_scar) > 0
    tabla.round(4).to_csv(BASE / "sensibilidad_scar_deg.tsv", sep="\t")
    print(f"DEG con scAR: {len(deg)}; sin scAR: {(sin_scar.padj < 0.05).sum()}; "
          f"en ambos: {tabla.significativo_en_ambos.sum()}; misma dirección y significativos: "
          f"{(tabla.significativo_en_ambos & tabla.misma_direccion).sum()}")


def fila_via(base, poblacion, biblioteca, via):
    datos = pd.read_csv(base / "gsea" / poblacion / biblioteca / "wald_stat" / "gseapy.gene_set.prerank.report.csv")
    fila = datos[datos.Term.str.startswith(via)]
    if fila.empty:
        return None, None
    return round(float(fila.NES.iloc[0]), 3), round(float(fila["FDR q-val"].iloc[0]), 4)


def comparar_vias(sin):
    filas = []
    for poblacion, biblioteca, via in VIAS:
        nes_c, fdr_c = fila_via(BASE, poblacion, biblioteca, via)
        nes_s, fdr_s = fila_via(sin, poblacion, biblioteca, via)
        filas.append({"poblacion": poblacion, "biblioteca": biblioteca, "via": via, "nes_con_scar": nes_c,
                      "fdr_con_scar": fdr_c, "nes_sin_scar": nes_s, "fdr_sin_scar": fdr_s})
    tabla = pd.DataFrame(filas)
    tabla.to_csv(BASE / "sensibilidad_scar_vias.tsv", sep="\t", index=False)
    print(tabla.to_string(index=False))


def main():
    with tempfile.TemporaryDirectory() as carpeta:
        sin = correr_sin_scar(Path(carpeta))
        comparar_deg(sin)
        comparar_vias(sin)


if __name__ == "__main__":
    main()
