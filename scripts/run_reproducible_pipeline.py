#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
ORQUESTADOR MAESTRO REPRODUCIBLE: PIPELINE V4-CLEAN (TESIS NK)
===============================================================================
Este script automatiza las etapas posteriores al control de calidad, a partir de
data/NK_dataset_qc_ready.h5ad. No incluye la extracción del Census, scAR, SOLO ni el
control de calidad, que dieron origen a ese archivo y usan otro entorno
(environment-qc.yml). Etapas:
  1. Construcción de firmas moleculares especializadas (CellAge, Reactome SASP, GSE9650).
  2. Modelado de abundancia diferencial y proporciones de subtipos (GLM Cuasibinomial).
  3. Expresión diferencial pseudobulk por subtipo (PyDESeq2 + contracción apeGLM).
  4. Generación de mapas de calor y visualizaciones de los 23 DEGs canónicos.
  5. Análisis de enriquecimiento funcional por rangos (GSEA Hallmarks/KEGG/Reactome/GO).
  6. Evaluación GSEA de firmas especializadas de senescencia, SASP y agotamiento linfoide.
  7. Análisis de sobre-representación (ORA).
  8. Compilación de tablas maestras unificadas GSEA.
  9. Generación del reporte integrativo maestro auto-contenido en HTML.
===============================================================================
"""

import os
import sys
import time
import subprocess
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

PROJECT_ROOT = Path(__file__).resolve().parent.parent

def run_step(script_relative_path, description):
    script_full = PROJECT_ROOT / script_relative_path
    if not script_full.exists():
        print(f"\n[ERROR] No se localizó el script: {script_full}")
        return False

    print(f"\n{'='*75}")
    print(f">> ETAPA: {description}")
    print(f">> EJECUTANDO: {script_relative_path}")
    print(f"{'='*75}")

    start_time = time.time()
    cmd = [sys.executable, str(script_full)]
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONPATH"] = str(PROJECT_ROOT)

    try:
        proc = subprocess.Popen(
            cmd,
            cwd=str(PROJECT_ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            bufsize=1,
            universal_newlines=True,
            env=env
        )
        for line in proc.stdout:
            print(f"   {line}", end="")
        proc.wait()
        elapsed = time.time() - start_time

        if proc.returncode == 0:
            print(f"\n[OK] Completado exitosamente en {elapsed:.2f} s")
            return True
        else:
            print(f"\n[ERROR] Falló {script_relative_path} con código de salida {proc.returncode}")
            return False
    except Exception as e:
        print(f"\n[EXCEPCIÓN] Error al iniciar {script_relative_path}: {e}")
        return False

def main():
    print("\n" + "#"*75)
    print("   INICIANDO EJECUCIÓN DEL PIPELINE REPRODUCIBLE: TESIS NK V4-CLEAN")
    print(f"   Raíz del repositorio: {PROJECT_ROOT}")
    print("#"*75)

    # 1. Verificación de prerrequisitos de datos
    data_h5ad = PROJECT_ROOT / "data" / "NK_dataset_qc_ready.h5ad"
    if not data_h5ad.exists():
        print(f"\n[ERROR] No se detectó el dataset base en: {data_h5ad}")
        print("Coloca o vincula el archivo H5AD en la carpeta 'data/' y vuelve a correr.")
        sys.exit(1)

    # 2. Definición del flujo de etapas
    pipeline_stages = [
        ("scripts/13_build_custom_gmt.py", "1. Construcción de Firmas Especializadas GMT"),
        ("scripts/22_pseudobulk_subtypes_pydeseq2.py", "2. Expresión Diferencial Pseudobulk por Subtipo (PyDESeq2)"),
        ("scripts/23_differential_abundance_milo.py", "3. Modelado de Abundancia GLM y Ratio de Subtipos"),
        ("scripts/29_figura4_abundancia.py", "4. Figura 4 de la Tesis (Abundancia de Subtipos)"),
        ("scripts/30_figuras_cohorte.py", "4b. Figuras y Tablas de la Cohorte (Figuras 1a a 3b)"),
        ("scripts/plot_heatmap_global.py", "5. Visualización de Heatmaps (23 DEGs Canónicos)"),
        ("scripts/14_run_specialized_gsea.py", "6. GSEA de Firmas Especializadas (SASP R-HSA-2559582)"),
        ("scripts/15_plot_specialized_gsea.py", "7. Generación de Dotplot de Senescencia Especializada"),
        ("scripts/24_subtypes_ranked_gsea.py", "8. GSEA Multibase por Subtipos (Hallmark, KEGG, Reactome)"),
        ("scripts/25_subtypes_ora.py", "9. Análisis de Sobre-representación (ORA)"),
        ("scripts/plot_gprofiler_style.py", "10. Dotplot Estilo g:Profiler"),
        ("scripts/compile_gsea_table.py", "11. Compilación de Tablas Maestras Unificadas GSEA"),
        ("scripts/generate_report_v2.py", "12. Generación del Reporte Integrativo HTML V2"),
    ]

    total_start = time.time()
    completed = 0

    for script_rel, desc in pipeline_stages:
        success = run_step(script_rel, desc)
        if not success:
            print(f"\n[ABORTADO] Se interrumpió la tubería debido a un error en: {script_rel}")
            sys.exit(1)
        completed += 1

    total_time = (time.time() - total_start) / 60.0
    print("\n" + "#"*75)
    print(f"   PIPELINE FINALIZADO CON ÉXITO: {completed}/{len(pipeline_stages)} etapas completadas.")
    print(f"   Tiempo total de cómputo: {total_time:.2f} minutos.")
    print("#"*75 + "\n")

if __name__ == "__main__":
    main()
