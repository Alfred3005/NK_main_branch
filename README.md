# 🧬 NK Aging Pipeline: RNA Ambient Correction + PyDESeq2 Shrinkage

Este repositorio contiene la arquitectura bioinformática avanzada para el análisis transcriptómico de células NK (Natural Killer) humanas, con un enfoque estricto en el estudio de la inmunosenescencia.

Tras aplicar técnicas rigurosas de corrección de RNA ambiental y filtrado adaptativo, este pipeline aísla la señal biológica del ruido técnico (sesgos de secuenciación, contaminación ribosomal e inmunoglobulinas), logrando un estándar de pureza genética y funcional sin precedentes.

### 🏁 Estado del Dataset Maestro
- **Archivo Base**: `data/NK_dataset_qc_ready.h5ad`
- **Volumen**: 143,991 células NK purificadas × 60,530 genes.
- **Balance Demográfico**: 73,434 células de adultos jóvenes (`adult`) vs 70,557 de adultos mayores (`old`).
- **Resultados Clave**: La integración de múltiples plataformas de secuenciación (10x 3' v2, 10x 5' v2, Seq-Well) se neutraliza mediante el modelo aditivo `~ assay + age_group` en PyDESeq2. Hemos demostrado que una vasta proporción de la firma de envejecimiento reportada clásicamente era ruido de lote, redefiniendo la narrativa hacia un modelo de **Inflammaging (Hiper-reactividad Inflamatoria)** en CD56dim y una drástica **Contracción Poblacional** en progenitores CD56bright.

---

## 🏛️ Estructura del Proyecto

El repositorio está diseñado para ser lineal, limpio y portátil:

- `scripts/`: Pipeline numerado de ejecución secuencial.
  - `01_exploratory_data_analysis.py`: Diagnóstico del h5ad.
  - `10-pydeseq2-pseudobulk-clean.py`: Expresión Diferencial Global.
  - `22_pseudobulk_subtypes_pydeseq2.py`: Extracción de subpoblaciones (CD56dim/bright).
  - `23_differential_abundance_milo.py`: Modelado de abundancia (GLM Binomial).
  - `24_subtypes_ranked_gsea.py`: Enriquecimiento GSEA Tricéfalo (Hallmark, KEGG, Reactome).
  - `compile_integration_report.py`: Ensamblaje del reporte interactivo HTML.
- `results/`: Contiene el reporte interactivo HTML final, tablas CSV de genes diferencialmente expresados y gráficas Volcano/GSEA.
- `data/`: (Ignorado en git) Carpeta destino para el `.h5ad`.

---

## 🤖 AI Onboarding (Para Claude Code / Antigravity / Agentic Tools)
Si eres una IA encargada de auditar, automatizar o continuar este proyecto, es imperativo que leas los siguientes documentos de memoria y contexto en la raíz del proyecto:
1. `AGENT_INSTRUCTIONS.md`: Guía de ejecución del pipeline paso a paso y asunciones estadísticas.
2. `walkthrough.md`: Resumen narrativo y metodológico de los hallazgos biológicos (Conclusiones).
3. `task.md`: El Task Tracker con el historial de módulos completados.

---

## 🛠️ Requerimientos y Entorno
- **Entorno**: Se recomienda usar el entorno virtual preconfigurado `.venv_wsl` (No usar conda por incompatibilidades de drivers).
- **Dependencias Principales**: `scanpy`, `pydeseq2`, `anndata`, `gseapy`, `statsmodels`.

**Investigador Principal:** Alfred3005  
**Soporte de IA:** Antigravity (Advanced Agentic Coding Agent)
