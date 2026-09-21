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
  - `22_pseudobulk_subtypes_pydeseq2.py`: Expresión Diferencial por subtipos.
  - `23_differential_abundance_milo.py`: Modelado de abundancia (GLM Binomial).
  - `24_subtypes_ranked_gsea.py`: Enriquecimiento GSEA Tricéfalo.
  - `14_run_specialized_gsea.py`: GSEA especializado (CellAge, Reactome SASP, Inmunosenescencia).
  - `25_subtypes_ora.py`: Análisis de sobrerrepresentación (ORA).
  - `plot_gprofiler_style.py`: Visualizaciones comparativas.
  - `plot_heatmap_global.py`: Heatmap de la firma de 23 genes alterados.
  - `compile_gsea_table.py`: Compilador de tablas unificadas.
  - `generate_report_v2.py`: Ensamblaje autónomo del reporte interactivo HTML.
  - `run_final_pipeline.py`: Automatizador de la suite completa.
- `results/`:
  - `Reporte_Integrativo_Subtipos_Abundancia_V2.html`: Entregable maestro.
  - `subtypes/`: Tablas maestras.
  - `figures/`: Repositorio local de figuras.
- `tesis/`: **Manuscrito y Compilación de Tesis**
  - `manuscripts/`: Documentos Markdown organizados por capítulos.
  - `figures/`: Figuras canónicas de la tesis.
  - `_quarto.yml`: Archivo de configuración del motor Quarto.
  - Para compilar el documento en PDF, ingresar a esta carpeta y ejecutar: `quarto render --to pdf`.
- `docs/`: Documentación metodológica.
- `legacy/`: Cuarentena y resguardo de versiones históricas.
- `data/`: (Ignorado en git) Carpeta destino para el `.h5ad`.

---

## 🤖 AI Onboarding (Para Claude Code / Antigravity / Agentic Tools)
Si eres una IA encargada de auditar, automatizar o continuar este proyecto, es imperativo que leas los siguientes documentos de memoria y contexto en el proyecto:
1. `AGENT_INSTRUCTIONS.md`: Guía de ejecución del pipeline paso a paso.
2. `AGENTS.md`: **REGLA CRÍTICA** Instrucciones de validación de contexto, redacción académica y nuevo paradigma biológico (V4-Clean).
3. `docs/vault/decisions.md`: Justificación biológica y matemática.
4. `docs/vault/log.md`: Bitácora histórica completa.
5. `results/Reporte_Integrativo_Subtipos_Abundancia_V2.html`: Fuente única de la verdad científica final.

---

## 🛠️ Requerimientos y Entorno
- **Entorno**: Se recomienda usar el entorno virtual preconfigurado `.venv_wsl` (No usar conda por incompatibilidades de drivers).
- **Dependencias Principales**: `scanpy`, `pydeseq2`, `anndata`, `gseapy`, `statsmodels`.

**Investigador Principal:** Alfred3005  
**Soporte de IA:** Antigravity (Advanced Agentic Coding Agent)
