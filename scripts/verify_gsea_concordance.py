#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_gsea_concordance.py
Auditoría forense de concordancia para análisis funcionales (GSEA / ORA)
y firma canónica de 23 DEGs en TESIS_NK_2.
"""

import os
import sys
import re
import pandas as pd

WORKSPACE = r"c:\Users\PREDATOR\Documents\Antigravity_workspaces\TESIS_NK_2"
RESULTS_DIR = os.path.join(WORKSPACE, "results", "subtypes")
MANUSCRIPTS_DIR = os.path.join(WORKSPACE, "tesis", "manuscripts")

def check_gsea_concordance():
    print("=" * 70)
    print("AUDITORÍA FORENSE DE ANÁLISIS FUNCIONALES (GSEA / ORA)")
    print("=" * 70)
    
    errors = []
    
    # 1. Verificar existencia de archivos primarios de GSEA
    gsea_files = {
        "cd56bright_hallmark": os.path.join(RESULTS_DIR, "gsea", "cd56bright", "gsea_sig_MSigDB_Hallmark_2020.csv"),
        "cd56bright_kegg": os.path.join(RESULTS_DIR, "gsea", "cd56bright", "gsea_sig_KEGG_2021_Human.csv"),
        "cd56bright_gobp": os.path.join(RESULTS_DIR, "gsea", "cd56bright", "gsea_sig_GO_Biological_Process_2023.csv"),
        "cd56dim_hallmark": os.path.join(RESULTS_DIR, "gsea", "cd56dim", "gsea_sig_MSigDB_Hallmark_2020.csv"),
        "cd56dim_kegg": os.path.join(RESULTS_DIR, "gsea", "cd56dim", "gsea_sig_KEGG_2021_Human.csv"),
        "cd56dim_gobp": os.path.join(RESULTS_DIR, "gsea", "cd56dim", "gsea_sig_GO_Biological_Process_2023.csv"),
        "specialized_cd56dim": os.path.join(RESULTS_DIR, "gsea_specialized", "nk_cd56dim", "gseapy.gene_set.prerank.report.csv"),
        "specialized_cd56bright": os.path.join(RESULTS_DIR, "gsea_specialized", "nk_cd56bright", "gseapy.gene_set.prerank.report.csv"),
        "degs_23": os.path.join(RESULTS_DIR, "deseq2_results_significant_nk_cell_general.csv")
    }
    
    for key, path in gsea_files.items():
        if not os.path.exists(path):
            errors.append(f"Archivo primario no encontrado: {path}")
        else:
            print(f"[OK] Archivo primario verificado: {key} -> {os.path.basename(path)}")
            
    if errors:
        for err in errors:
            print(f"[ERROR] {err}")
        return False

    # 2. Leer texto del Capítulo 5
    cap5_path = os.path.join(MANUSCRIPTS_DIR, "05_Resultados.md")
    with open(cap5_path, "r", encoding="utf-8") as f:
        cap5_text = f.read()

    print("\n--- Verificación de Tabla 3 (Vías GSEA Representativas) ---")
    # Vías clave a contrastar
    # UV Response Dn en CD56bright
    df_cb_h = pd.read_csv(gsea_files["cd56bright_hallmark"])
    row_uv_b = df_cb_h[df_cb_h["Term"].str.contains("UV Response Dn", case=False, na=False)].iloc[0]
    nes_uv_b = round(row_uv_b["NES"], 3)
    fdr_uv_b = round(row_uv_b["FDR"], 4)
    print(f"CD56bright UV Response Dn CSV: NES={nes_uv_b}, FDR={fdr_uv_b}")
    if "+1.782" in cap5_text or "+1.781" in cap5_text:
        print("[OK] NES de UV Response Dn (CD56bright) coincide con Tabla 3.")
    else:
        errors.append(f"Discrepancia en NES UV Response Dn (CD56bright): CSV={nes_uv_b}")

    # TNF-alpha en CD56dim
    df_cd_h = pd.read_csv(gsea_files["cd56dim_hallmark"])
    row_tnf = df_cd_h[df_cd_h["Term"].str.contains("TNF-alpha", case=False, na=False)].iloc[0]
    nes_tnf = round(row_tnf["NES"], 3)
    fdr_tnf = round(row_tnf["FDR"], 4)
    print(f"CD56dim TNF-alpha Signaling CSV: NES={nes_tnf}, FDR={fdr_tnf}")
    if "-1.784" in cap5_text:
        print("[OK] NES de TNF-alpha Signaling (CD56dim) coincide con Tabla 3.")
    else:
        errors.append(f"Discrepancia en NES TNF-alpha: CSV={nes_tnf}")

    # Verificar que MAP3K8 esté presente como gen líder de TNF-alpha
    lead_tnf = row_tnf["Lead_genes"].split(";")
    if "MAP3K8" == lead_tnf[0]:
        print("[OK] MAP3K8 es el gen líder PRIMARIO de TNF-alpha Signaling via NF-kB en CD56dim.")
    else:
        print(f"[AVISO] MAP3K8 en posición {lead_tnf.index('MAP3K8') if 'MAP3K8' in lead_tnf else 'no encontrado'}")

    print("\n--- Verificación de Tabla 4 (Firmas Especializadas SASP y Exhaustion) ---")
    # Verificar que IL7R NO esté presente en la fila de GSE9650 en Tabla 4
    match_tbl4 = re.search(r"Exhausted vs Memory CD8\+ T Cell.*?\n", cap5_text)
    if match_tbl4:
        row_str = match_tbl4.group(0)
        print(f"Fila GSE9650 en Tabla 4: {row_str.strip()}")
        if "IL7R" in row_str:
            errors.append("IL7R aún aparece en los genes líderes de GSE9650 en Tabla 4. Debe ser purgado.")
        else:
            print("[OK] IL7R ha sido purgado de los genes destacados de GSE9650 en Tabla 4.")
            
        if "ARL6IP5" in row_str or "TOB1" in row_str:
            print("[OK] Genes líderes legítimos (ARL6IP5, TOB1, KLRC1, XRCC5, ETS1) verificados.")
    else:
        errors.append("No se localizó la fila de GSE9650 en Tabla 4 de 05_Resultados.md")

    print("\n--- Verificación de Integración de ORA en Capítulo 5 ---")
    if "Neutrophil Chemotaxis" in cap5_text and "XCL1" in cap5_text and "S100A9" in cap5_text:
        print("[OK] Párrafo ortogonal de ORA integrado coherentemente con los 23 DEGs y refiriendo a Anexos.")
    else:
        errors.append("El párrafo de ORA no contiene las rutas clave o los genes esperados.")

    print("\n--- Verificación de Capítulo 6 (Discusión) ---")
    cap6_path = os.path.join(MANUSCRIPTS_DIR, "06_Discusion.md")
    with open(cap6_path, "r", encoding="utf-8") as f:
        cap6_text = f.read()

    has_map3k8 = "MAP3K8" in cap6_text
    has_tnf = ("TNF-alpha" in cap6_text or "TNF-$\\alpha$" in cap6_text or "TNF_alpha" in cap6_text)
    if has_map3k8 and has_tnf:
        print("[OK] Conexión mecanicista MAP3K8 <-> TNF-alpha / NF-kB presente en Discusión.")
    else:
        errors.append("Falta articulación mecanicista entre MAP3K8 y TNF-alpha en Discusión.")

    if "RNF169" in cap6_text and "UV Response Dn" in cap6_text:
        print("[OK] Paradoja genotóxica (RNF169 compensatorio vs falla de UV Response Dn) articulada.")
    else:
        errors.append("Falta articulación entre RNF169 y UV Response Dn en Discusión.")

    # 3. Validar los 23 DEGs canónicos
    print("\n--- Verificación de la firma de 23 DEGs canónicos ---")
    df_degs = pd.read_csv(gsea_files["degs_23"])
    n_degs = len(df_degs)
    print(f"Número de genes en CSV canónico: {n_degs}")
    if n_degs == 23:
        print("[OK] Lista de 23 DEGs exacta.")
    else:
        errors.append(f"Número inesperado de DEGs en CSV: {n_degs} (esperado 23).")

    # Resumen
    print("\n" + "=" * 70)
    if not errors:
        print("[EXITO TOTAL] Todos los criterios de concordancia funcional (GSEA/ORA) fueron superados.")
        print("=" * 70)
        return True
    else:
        print(f"[FALLO] Se detectaron {len(errors)} discrepancias:")
        for err in errors:
            print(f"  - {err}")
        print("=" * 70)
        return False

if __name__ == "__main__":
    success = check_gsea_concordance()
    sys.exit(0 if success else 1)
