# NK Subtypes RNA-seq Pipeline - Agentic Execution Guide

## Context & Objectives
This repository contains the "Main_Branch" version of the NK cell transcriptomics pipeline (V4-Clean). It has been optimized to isolate the pure biological signal of immunosenescence from technical noise (ambient RNA, sequencing bias, and ribosomal contamination). 

The goal of this pipeline is to analyze 187 healthy donors to identify differentially expressed genes (DEGs) and functional enrichment (GSEA) across the NK CD56dim and CD56bright subsets, as well as to measure the population contraction of the CD56bright subset via a Binomial Generalized Linear Model (GLM).

## Execution Environment
- **OS**: WSL (Ubuntu) on Windows.
- **Python Environment**: You MUST use the pre-configured virtual environment located at `../.venv_wsl/bin/activate` or install dependencies matching the pipeline needs. No conda environments are used due to Docker/Nvidia driver incompatibilities.
- **Paths**: All scripts inside the `scripts/` folder use relative paths pointing to `../data/` and `../results/`.

## Execution Steps (Sequential)

Execute the scripts sequentially from the `scripts/` directory:

1. **`01_exploratory_data_analysis.py`**
   - **Purpose**: Validates the input `NK_dataset_qc_ready.h5ad` file. Verifies dimensions (~143,991 cells × 60,530 genes) and age group balancing. 
   - **Note**: The large number of genes is intentional. Ribosomal (RPS/RPL) and IG genes are filtered *dynamically* at runtime by PyDESeq2 to preserve count matrices for stochastic assumption validity.

2. **`10-pydeseq2-pseudobulk-clean.py`**
   - **Purpose**: Runs Global Differential Expression (Baseline) using PyDESeq2 with pseudobulk aggregation.
   - **Model**: `~ assay + age_group`
   - **Output**: Identifies purely significant global DEGs after LFC Shrinkage (`apeGLM`).

3. **`22_pseudobulk_subtypes_pydeseq2.py`**
   - **Purpose**: Runs Differential Expression by Subtype (CD56dim and CD56bright).
   - **Model**: Degrades to `~ age_group` for CD56dim to avoid collinearity. CD56bright might skip DEG output if cell mass is insufficient (this is an expected statistical control).

4. **`23_differential_abundance_milo.py`**
   - **Purpose**: Differential Abundance.
   - **Mechanism**: Calculates a Binomial GLM of the ratio between CD56bright and Total NK cells. 
   - **Expected Result**: Log Odds Ratio around -0.47 (OR=0.62), p-val = 0.000000, confirming the loss of CD56bright progenitors with age.

5. **`24_subtypes_ranked_gsea.py`**
   - **Purpose**: Performs Gene Set Enrichment Analysis (GSEA) using MSigDB Hallmark, KEGG, and Reactome based on the Wald stats from PyDESeq2.

6. **`compile_integration_report.py`**
   - **Purpose**: Compiles all CSVs, text results, and generated PNGs into a final, self-contained base64 HTML report.
   - **Output**: `../results/Reporte_Integrativo_Subtipos_Abundancia.html`

## Agent Guidelines
- If a step fails, do not arbitrarily change the statistical model. Check for missing dependencies or file path issues.
- The absence of a CD56bright results CSV is handled gracefully by the compilation script. Do not attempt to force false-positive DEG extraction for sparse populations.
- All visualizations are output to `results/subtypes/gsea/` and `results/subtypes/`.
