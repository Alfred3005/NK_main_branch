# 🧬 NK Aging Pipeline: RNA Ambient Correction + PyDESeq2 Shrinkage

Este repositorio contiene la arquitectura bioinformática avanzada para el análisis transcriptómico de células NK (Natural Killer) humanas, con un enfoque estricto en el estudio de la inmunosenescencia.

Tras aplicar técnicas rigurosas de corrección de RNA ambiental y filtrado adaptativo, este pipeline aísla la señal biológica del ruido técnico (sesgos de secuenciación, contaminación ribosomal e inmunoglobulinas), logrando un estándar de pureza genética y funcional sin precedentes.

### 🏁 Estado del Dataset Maestro
- **Archivo Base**: `data/NK_dataset_qc_ready.h5ad`
- https://drive.google.com/drive/folders/16QNDSToKWhiTFHAS-opsTl_1MYSuI2tV?usp=sharing
- **Volumen**: 143,991 células NK purificadas × 60,530 genes.
- **Balance Demográfico**: 73,434 células de adultos jóvenes (`adult`) vs 70,557 de adultos mayores (`old`).
- **Resultados Clave**: La integración de múltiples plataformas de secuenciación (10x 3' v2, 10x 5' v2, Seq-Well) se neutraliza mediante el modelo aditivo `~ assay + age_group` en PyDESeq2. Hemos demostrado que una vasta proporción de la firma de envejecimiento reportada clásicamente era ruido de lote, redefiniendo la narrativa hacia un modelo de **Inflammaging (Hiper-reactividad Inflamatoria)** en CD56dim y una drástica **Contracción Poblacional** en progenitores CD56bright.

---

## 🏛️ Estructura del Proyecto

El repositorio está diseñado para ser lineal, limpio, reproducible y portable:

- `scripts/`: Pipeline de ejecución secuencial canónico.
  - `22_pseudobulk_subtypes_pydeseq2.py`: Expresión Diferencial por subtipos (CD56dim/bright/general) con control estricto de colinealidad.
  - `23_differential_abundance_milo.py`: Modelado de abundancia (GLM Binomial).
  - `24_subtypes_ranked_gsea.py`: Enriquecimiento GSEA Tricéfalo (Hallmark, KEGG, Reactome).
  - `14_run_specialized_gsea.py`: GSEA especializado (CellAge, Reactome SASP, Inmunosenescencia).
  - `25_subtypes_ora.py`: Análisis de sobrerrepresentación (ORA).
  - `plot_gprofiler_style.py`: Visualizaciones comparativas estilo gProfiler (FDR < 0.05 y FDR < 0.25).
  - `plot_heatmap_global.py`: Heatmap de la firma de 23 genes alterados.
  - `compile_gsea_table.py`: Compilador de tablas unificadas por categorías funcionales.
  - `generate_report_v2.py`: Ensamblaje autónomo del reporte interactivo HTML final.
  - `run_final_pipeline.py`: Automatizador que corre la suite completa.
- `results/`:
  - `Reporte_Integrativo_Subtipos_Abundancia_V2.html`: **Entregable maestro definitivo e interactivo**.
  - `subtypes/`: Tablas maestras de DEGs, GSEA, ORA, volcanos y reportes CSV finales.
  - `figures/`: Repositorio local de todas las 20 figuras canónicas en alta resolución.
- `docs/`: Documentación metodológica, memoria en Obsidian (`docs/vault/`) y el markdown maestro `reporte_integrativo_final.md`.
- `legacy/`: Cuarentena y resguardo de versiones históricas (V1, V3 trunca, análisis descriptivo exploratorio).
- `data/`: (Ignorado en git) Carpeta destino para `NK_dataset_qc_ready.h5ad`.

---

## 🤖 AI Onboarding (Para Claude Code / Antigravity / Agentic Tools)
Si eres una IA encargada de auditar, automatizar o continuar este proyecto, es imperativo que leas los siguientes documentos de memoria y contexto en el proyecto:
1. `AGENT_INSTRUCTIONS.md`: Guía de ejecución del pipeline paso a paso y asunciones estadísticas.
2. `docs/vault/decisions.md`: Justificación biológica y matemática (depuración de lote, efecto cancelación, colinealidad).
3. `docs/vault/log.md`: Bitácora histórica completa (Chronos).
4. `results/Reporte_Integrativo_Subtipos_Abundancia_V2.html`: Fuente única de la verdad científica final.

---

## 🛠️ Requerimientos y Entorno
- **Entorno**: Se recomienda usar el entorno virtual preconfigurado `.venv_wsl` (No usar conda por incompatibilidades de drivers).
- **Dependencias Principales**: `scanpy`, `pydeseq2`, `anndata`, `gseapy`, `statsmodels`.

**Investigador Principal:** Alfred3005  
**Soporte de IA:** Antigravity (Advanced Agentic Coding Agent)
