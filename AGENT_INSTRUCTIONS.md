# NK Subtypes RNA-seq Pipeline - Agentic Execution Guide

## Context & Objectives
This repository contains the "Main_Branch" version of the NK cell transcriptomics pipeline (V4-Clean). It has been optimized to isolate the pure biological signal of immunosenescence from technical noise (ambient RNA, sequencing bias, and ribosomal contamination). 

The goal of this pipeline is to analyze 187 healthy donors to identify differentially expressed genes (DEGs) and functional enrichment (GSEA) across the NK CD56dim and CD56bright subsets, as well as to measure the population contraction of the CD56bright subset via a Binomial Generalized Linear Model (GLM).

## Execution Environment
- **OS**: WSL (Ubuntu) on Windows.
- **Python Environment**: You MUST use the pre-configured virtual environment located at `../.venv_wsl/bin/activate` or install dependencies matching the pipeline needs. No conda environments are used due to Docker/Nvidia driver incompatibilities.
- **Paths**: All scripts inside the `scripts/` folder use relative paths pointing to `../data/` and `../results/`.

## Execution Steps (Sequential)

Execute the scripts sequentially from the `scripts/` directory or run `python scripts/run_final_pipeline.py`:

1. **`22_pseudobulk_subtypes_pydeseq2.py`**
   - **Purpose**: Runs Differential Expression by Subtype (CD56dim, CD56bright, and Global NK) with strict assay balance per age group (`10x 3' v3`, N=187 donantes).
   - **Model**: `~ assay + age_group` with `apeGLM` shrinkage.
   - **Output**: Generates CSVs in `../results/subtypes/` and identifies 23 significant DEGs globally (*IL7R* down, *S100A9* down, *NKG7* up).

2. **`23_differential_abundance_milo.py`**
   - **Purpose**: Differential Abundance.
   - **Mechanism**: Calculates a Binomial GLM of the ratio between CD56bright and Total NK cells. 
   - **Result**: Log Odds Ratio around -0.47 (OR=0.62), p-val < 0.0001, confirming the significant loss of CD56bright progenitors with age.

3. **`24_subtypes_ranked_gsea.py`**
   - **Purpose**: Performs Gene Set Enrichment Analysis (GSEA) using MSigDB Hallmark, KEGG, and Reactome based on Wald stats from PyDESeq2.
   - **Output**: Generates reports and dotplots in `../results/subtypes/gsea/`.

4. **`14_run_specialized_gsea.py`**
   - **Purpose**: Runs specialized GSEA on orthogonal senescence signatures (CellAge, Reactome SASP, Immune Exhaustion).
   - **Output**: `../results/subtypes/gsea_specialized/`.

5. **`25_subtypes_ora.py`**
   - **Purpose**: Over-Representation Analysis (ORA) on high-confidence DEG sets.
   - **Output**: `../results/subtypes/ora/`.

6. **`plot_gprofiler_style.py` & `plot_heatmap_global.py`**
   - **Purpose**: Generates publication-grade figures: comparative gProfiler-style plots (FDR < 0.05 and FDR < 0.25) and clustered heatmaps.
   - **Output**: `../results/subtypes/`.

7. **`compile_gsea_table.py`**
   - **Purpose**: Consolidates GSEA results into a unified semantic table (`gsea_unified_table.md`) categorizing pathways by biological process.

8. **`generate_report_v2.py`**
   - **Purpose**: Compiles all narrative sections, 21 data tables, and 20 figures into the standalone interactive HTML report.
   - **Output**: `../results/Reporte_Integrativo_Subtipos_Abundancia_V2.html`.

## Agent Guidelines
- If a step fails, do not arbitrarily change the statistical model. Check for missing dependencies or file path issues.
- All visualizations and tables are output to `results/subtypes/` and `results/figures/`.
- All legacy, exploratory or historical versions are isolated in `legacy/`. Do not run or modify files in `legacy/` during standard pipeline execution.
