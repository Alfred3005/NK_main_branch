# 📊 Documento Maestro: Resultados DEA (PyDESeq2 Estricto)

Este documento consolida los resultados del análisis de expresión diferencial aislando la varianza técnica (colinealidad por ensayos desbalanceados).

## 1. NK Global (Células NK Totales)
### Genes Significativos (FDR < 0.05)
| feature_name   |   baseMean |   log2FoldChange |     lfcSE |     stat |      pvalue |       padj |
|:---------------|-----------:|-----------------:|----------:|---------:|------------:|-----------:|
| ABCB8          |    5.80799 |       0.00744296 | 0.123019  |  3.92346 | 8.72845e-05 | 0.0411934  |
| AGAP2          |   11.2951  |       0.0137014  | 0.0412668 |  4.16702 | 3.08607e-05 | 0.0290449  |
| ATL1           |    3.36264 |       0.00466882 | 0.0304803 |  3.88127 | 0.000103912 | 0.0441368  |
| CST7           | 1320.51    |       0.102809   | 0.0279735 |  4.10161 | 4.10287e-05 | 0.0290449  |
| FAM169A        |    9.58036 |       0.00837422 | 0.0272532 |  3.90377 | 9.47058e-05 | 0.0423434  |
| FCHSD1         |   12.6895  |       0.0113387  | 0.0294387 |  4.01924 | 5.83869e-05 | 0.0354283  |
| HIRA           |    7.1397  |       0.0056202  | 0.0296954 |  3.95925 | 7.51861e-05 | 0.0399191  |
| KIR3DL1        |   36.6541  |      -1.40653    | 0.239595  | -5.19836 | 2.01055e-07 | 0.00170796 |
| KIR3DL2        |   28.5928  |      -1.17599    | 0.27311   | -4.08193 | 4.46632e-05 | 0.0291857  |
| MAP3K8         |   99.8316  |      -0.365954   | 0.111543  | -3.93315 | 8.38382e-05 | 0.0411934  |
| OSBPL3         |   10.0148  |       0.6338     | 0.239625  |  3.8306  | 0.000127832 | 0.0493607  |
| PALLD          |   14.4827  |       0.842782   | 0.307319  |  4.24435 | 2.19224e-05 | 0.0264713  |
| PLEKHO1        |    1.43367 |      -0.00433139 | 0.0365606 | -3.84571 | 0.000120205 | 0.0486258  |
| PORCN          |    8.11923 |       0.010364   | 0.0357942 |  3.99135 | 6.56989e-05 | 0.0372075  |
| PRSS23         |  170.281   |       0.180455   | 0.0501561 |  4.11137 | 3.93312e-05 | 0.0290449  |
| PTGDS          |  490.469   |       0.682515   | 0.16594   |  5.00342 | 5.63222e-07 | 0.00239229 |
| RNF169         |   13.8351  |       0.747284   | 0.271506  |  4.14164 | 3.44829e-05 | 0.0290449  |
| S100A9         |    7.86776 |       1.87533    | 0.449232  |  4.7437  | 2.09848e-06 | 0.00445664 |
| SERGEF         |    7.99181 |       1.19408    | 0.44749   |  4.91256 | 8.98966e-07 | 0.00254557 |
| SP2            |    9.07093 |       0.679798   | 0.215573  |  4.21544 | 2.49288e-05 | 0.0264713  |
| XCL1           |   33.6166  |      -0.724954   | 0.164244  | -4.56675 | 4.95347e-06 | 0.00841595 |
| XCL2           |  108.027   |      -0.344555   | 0.0996213 | -3.81818 | 0.000134438 | 0.0496543  |
| ZNF672         |    3.96641 |       0.00724588 | 0.0283835 |  4.37062 | 1.23895e-05 | 0.0175415  |

## 2. NK CD56dim
**Genes Significativos (FDR < 0.05):** 0 genes detectados tras la contracción apeGLM (Señal purificada de ruido de lote).

## 3. NK CD56bright
**Genes Significativos (FDR < 0.05):** 0 genes detectados tras la contracción apeGLM.

## 🔗 Rutas a las Tablas Rankeadas Completas (Estadístico Wald)
Estas tablas fueron utilizadas como input para los análisis GSEA preranked:
- **NK Global:** [ranked_wald_stat.rnk](file:///c:/Users/PREDATOR/Documents/Antigravity_workspaces/NK_pipeline_RNA_ambient_Main_Branch/results/experiment_collinearity/gsea/global/ranked_wald_stat.rnk)
- **NK CD56dim:** [ranked_wald_stat.rnk](file:///c:/Users/PREDATOR/Documents/Antigravity_workspaces/NK_pipeline_RNA_ambient_Main_Branch/results/experiment_collinearity/gsea/cd56dim/ranked_wald_stat.rnk)
- **NK CD56bright:** [ranked_wald_stat.rnk](file:///c:/Users/PREDATOR/Documents/Antigravity_workspaces/NK_pipeline_RNA_ambient_Main_Branch/results/experiment_collinearity/gsea/cd56bright/ranked_wald_stat.rnk)
