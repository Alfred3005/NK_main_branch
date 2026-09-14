# 📜 Registro de Actividad (Chronos)

Todas las decisiones y cambios significativos del proyecto se registran aquí.

## 2026-09-07
- **01:00 AM**: 🧹 **Gran Limpieza, Consolidación Canónica y Alineación Definitiva con Reporte V2**.
    - **Auditoría Forense:** Se comprobó que el reporte `Reporte_Integrativo_Subtipos_Abundancia_V2.html` (20 de julio de 2026) es el entregable final canónico, superando al borrador previo e incompleto V3.
    - **Promoción Canónica:** Se promovieron los scripts de la solución de colinealidad (`experiment_collinearity`) a la raíz de `scripts/` (`22_pseudobulk_subtypes_pydeseq2.py`, `24_subtypes_ranked_gsea.py`, `14_run_specialized_gsea.py`, `25_subtypes_ora.py`, `plot_gprofiler_style.py`, `plot_heatmap_global.py`).
    - **Sincronización de Resultados:** La carpeta `results/subtypes/` se consolidó con la totalidad de tablas de DEGs, GSEA unificado, ORA y figuras maestras en Base64.
    - **Independencia y Portabilidad:** Se importó el documento maestro `docs/reporte_integrativo_final.md` y se recopilaron todas las 20 figuras en `results/figures/`, permitiendo que `generate_report_v2.py` compile de forma 100% autónoma sin depender de rutas externas del sistema.
    - **Aislamiento a Legacy:** Se movieron a `legacy/` los reportes históricos (V1, V3 trunca, Colinealidad), los scripts descriptivos de agosto (`02_...`, `results/descriptive_analysis_v5/`), los scripts temporales de depuración (`scratch/`) y los respaldos previos.
    - **Automatización Unificada:** Se actualizaron `run_final_pipeline.py` y `run_pipeline.ps1` para orquestar linealmente la ejecución canónica.

## 2026-08-19
- **02:00 PM**: 📊 **Generación de Figuras y Tablas Descriptivas para Manuscrito de Tesis**.
    - Creación de scripts descriptivos (`02_descriptive_analysis_figures.py`, `02b_descriptive_figures_individual.py`, `generate_descriptive_tables.py`, `compile_descriptive_report.py`) y generación de `results/descriptive_analysis_v5/` para alimentar específicamente las secciones 5.1 y 5.2 del manuscrito de tesis.
    - Aislados posteriormente a `legacy/descriptive_analysis/` para preservar la pureza del pipeline transcriptómico central.

## 2026-07-20
- **03:05 PM**: 🧬 **Cierre del Hito de Colinealidad Estricta y Compilación del Reporte V2**.
    - **Resolución de Colinealidad:** Filtrado riguroso por química balanceada (`10x 3' v3`, N=187 donantes: 152 adultos vs 35 ancianos, 62,553 células).
    - **Firma Molecular Pura:** Identificación del colapso de *IL7R* (CD127, log2FC = -1.0416, FDR = 0.0003) como marcador maestro de atrofia del nicho secretor, junto con el silenciamiento de *XCL1/2* y la verdadera represión de *S100A9* (-1.6169).
    - **Reporte Integrativo V2:** Creación de `scripts/generate_report_v2.py` con navegación por pestañas (`Narrativa`, `Abundancia`, `DEGs`, `Perfiles GSEApy`, `Conclusiones`), 21 tablas interactivas completas y gráficos estilo gProfiler v7.

## 2026-06-10
- **06:30 PM**: 🧬 **Reporte Integrativo y Cierre de Tesis (CD56dim vs CD56bright + Abundancia)**.
    - **Reporte Científico:** Redactado [subtypes_abundance_integration_report.md](file:///c:/Users/PREDATOR/Documents/Antigravity_workspaces/NK_pipeline_RNA_ambient/results/subtypes_abundance_integration_report.md) contrastando las subpoblaciones NK, la abundancia celular y el efecto cancelación en Global NK.
    - **Obsidian Wiki:** Creada la nota enciclopédica [[wiki/integracion_subtipos_abundancia.md|integracion_subtipos_abundancia.md]] con mapa conceptual Mermaid, paradoja de TNF-α/NF-κB, mismatch mito-nuclear de CD56bright y la ruta de validaciones futuras (`scVelo`, `AUCell`, `scFEA`).
    - **Compilador HTML Premium:** Creado y ejecutado [compile_integration_report.py](file:///c:/Users/PREDATOR/Documents/Antigravity_workspaces/NK_pipeline_RNA_ambient/scripts/compile_integration_report.py) para ensamblar el reporte interactivo premium auto-contenido en [Reporte_Integrativo_Subtipos_Abundancia.html](file:///c:/Users/PREDATOR/Documents/Antigravity_workspaces/NK_pipeline_RNA_ambient/results/Reporte_Integrativo_Subtipos_Abundancia.html) con gráficos y tablas embebidos.
- **01:35 AM**: 🧬 **Análisis de Modelos Mixtos y scVI en Célula Única (NK CD56bright)**.
    - **Pipeline scVI:** Ejecución de `26_run_single_cell_scvi.py` en WSL con la RTX 4060, modelando counts crudos y controlando por donante/lote. Identificó **413 genes significativos** con Bayes Factor > 3.0.
    - **Pipeline MixedLM Paralelizado:** Implementación y ejecución de `27_run_single_cell_mixedlm.py` gen por gen en paralelo (joblib, n_jobs=-2), normalizando a 10,000 counts + log1p. Se identificaron **0 genes significativos con padj < 0.05** tras FDR (BH), evidenciando la pérdida de poder del LMM tradicional a nivel de célula única en poblaciones escasas.
    - **GSEA Preranked Comparativo:** Ejecución de `28_subtypes_mixed_gsea.py` para Hallmark, KEGG, Reactome y GO:BP. Logró "rescatar" 31 vías en MixedLM y 143 en scVI, revelando consistencia molecular en la firma pro-inflamatoria (TNF-alpha/NF-kB, IL-17) y el declive bioenergético mitocondrial de las CD56bright viejas.
    - **Reporte Interactivo y Tablas:** Generación de `Reporte_Comparativo_Modelos_Mixtos.html` incorporando tablas interactivas con el Top 100 de genes y las perspectivas de investigación futuras recomendadas por el Consejo Académico Titan.

## 2026-05-29
- **03:42 PM**: 🧬 **Validación de LFC Shrinkage en Nueva Rama Aislada (`v4_shrinkage`)**.
    - **Aislamiento de la Rama:** Se creó la nueva estructura de directorios `scAR_python_validation_v4_shrinkage/` para documentar de forma independiente este análisis comparativo.
    - **Benchmark de Shrinkage:** Implementado y ejecutado `22_pydeseq2_shrinkage_benchmark.py` en WSL. Se extrajeron LFCs Raw y Shrunken (apeGLM) para el Modelo Conjunto (`~ assay + age_group`) y Modelos Divididos (`~ age_group` en 3' y 5').
    - **Auditoría de Genes de Interés:** Se analizaron en detalle marcadores clave como `KIR3DL1/2` (estables, apenas cambian LFC), falsos positivos mieloides (`LYZ`, colapsado) y genes de bajo conteo solicitados (`SERPINA1`, `DUOX1`, `CST3`), validando que su aparente significancia o alto LFC en crudo se debía a variabilidad estadística y bajo conteo.
    - **Reporte Comparativo HTML:** Implementado `convert_shrinkage_report_to_html.py`, compilando un reporte interactivo final y auto-contenido con las 4 figuras complejas embebidas en Base64 en `scAR_python_validation_v4_shrinkage/docs/Reporte_Comparativo_Shrinkage.html`.

## 2026-05-28
- **01:15 AM**: 🧬 **Comparativa de Modelos (Opción A vs Opción B) y Depuración del Reporte de Tesis (V4-Clean)**.
    - **Evaluación Comparativa:** Se ejecutó una re-evaluación sistemática de los datos purificados bajo la Opción A (Modelo Conjunto aditivo `~ assay + age_group`) y la Opción B (Modelos aislados por lote `~ age_group`) en carpetas exploratorias independientes. Se clasificaron los genes significativos en umbrales escalonados de LFC (0.25, 0.50, 1.00).
    - **Trazabilidad en Heatmap:** Se corrigió la generación de conteos normalizados en [17_differential_expression_figures.py](file:///c:/Users/PREDATOR/Documents/Antigravity_workspaces/NK_pipeline_RNA_ambient/scAR_python_validation_v4_clean/scripts/17_differential_expression_figures.py) para utilizar los resultados de 10,230 genes de DESeq2 en lugar del subset de 5,000 HVGs. Se re-ejecutó el clustering visual en [17b_pydeseq2_visualizations.py](file:///c:/Users/PREDATOR/Documents/Antigravity_workspaces/NK_pipeline_RNA_ambient/scAR_python_validation_v4_clean/scripts/17b_pydeseq2_visualizations.py) logrando que el heatmap `Heatmap_sig_genes.png` muestre los **12 genes** de la firma completa en vez de 4.
    - **Depuración de Formatos:** Se eliminaron los caracteres de math-blocks crudos (`$`) de los p-valores/LFC en el reporte y se escaparon los caracteres de valor absoluto en las cabeceras de las tablas (`\|LFC\|`), logrando un renderizado web de tablas nativas sin errores. Se re-compiló el reporte final a HTML auto-contenido en [Reporte_Integral_PyDESeq2_V4.html](file:///c:/Users/PREDATOR/Documents/Antigravity_workspaces/NK_pipeline_RNA_ambient/scAR_python_validation_v4_clean/docs/Reporte_Integral_PyDESeq2_V4.html).
    - **Documentación de Cierre:** Se integraron todos los hallazgos comparativos de kits (Opción A vs B) como una nueva Sección 4 oficial en el reporte integral de tesis.

## 2026-05-26
- **09:15 PM**: 🔄 **Ajuste de Umbrales en Visualizaciones y Reporte (Firma Completa)**.
    - **Volcano Plot:** Se ajustó el umbral biológico a $|LFC| > 0.5$ (en lugar de $1.0$) y $padj < 0.05$, destacando y anotando exactamente a los 10 genes clave.
    - **Heatmap:** Se expandió el clustered heatmap para mostrar la firma completa de 12 genes (reduciendo el umbral biológico a $|LFC| > 0.25$ y $padj < 0.05$) para asegurar que todos los genes significativos modulados estén representados. Se añadieron los genes `MAP3K8` y `XCL2`.
    - **Reporte e HTML:** Se actualizaron `Reporte_Integral_PyDESeq2_V4.md` y el HTML compilado para documentar estos nuevos umbrales, incorporar las figuras regeneradas y documentar las funciones de los 12 genes significativos.
- **07:50 PM**: 📊 **Actualización de Visualizaciones y Reporte Integral (Fase 17)**.
    - **Gráficos:** Se modificó el MA-plot (`MA_plot_v4_final.png`) para colorear los puntos significativos basándose únicamente en `padj < 0.05` (removiendo el filtro de LFC), permitiendo ver todos los genes estadísticamente significativos.
    - **Heatmap:** Se implementó la generación de un clustered heatmap (`Heatmap_sig_genes.png`) que representa la expresión Z-score de la firma relajada de 10 genes ($|LFC| > 0.5$, $padj < 0.05$) ordenados por edad.
    - **Reporte:** Se reescribió y actualizó completamente [[wiki/Reporte_Integral_PyDESeq2_V4.md|📄 Reporte Integral PyDESeq2 V4]] con las cifras corregidas (4 y 10 genes), las tres nuevas figuras y las interpretaciones biológicas de UniProt.
    - **Compilación:** Se compiló el reporte a un archivo HTML premium auto-contenido con las figuras embebidas en base64 en `scAR_python_validation_v4_clean/docs/Reporte_Integral_PyDESeq2_V4.html`.

## 2026-05-25
- **03:45 PM**: 🧬 **Corrección de Entrada PyDESeq2 y Firma Molecular**.
    - **Diagnóstico:** La Fase 04 (`04-purify-qc-lineage.py`) guardaba valores log-normalizados flotantes en `adata.X` en lugar de cuentas enteras discretas, lo que invalidaba el modelo binomial negativo de DESeq2 y producía falsos significativos (como genes con LFC = 0.0000 y padj < 0.05).
    - **Corrección:** Se modificó la Fase 04 para mantener conteos discretos de scAR en `adata.X` y se resolvieron singularidades de LOESS en la selección de HVGs.
    - **Impacto:** Firma depurada de 86 supuestos genes a **4 genes de alta confianza ($|LFC| > 1$)** y **10 genes de firma relajada ($|LFC| > 0.5$)**.
    - **Gráficos:** Corregida lógica en `17b_pydeseq2_visualizations.py` para requerir simultáneamente `padj < 0.05` y `|LFC| > 1` en el Volcano Plot, añadiendo líneas límite.
    - **Wiki:** Destilado conocimiento en [[wiki/REVISION_COMPARATIVA_DE|🔍 Revisión Comparativa DE]].
    - **DotPlot de Pureza:** Se corrigió el error visual en `11_visual_validation.py` donde `standard_scale='var'` sobre solo 2 grupos (Adult vs Old) distorsionaba la escala y hacía que los adultos parecieran tener expresión nula de marcadores NK y expresión espuria de T-cell (como CD8A). Se eliminó el escalamiento variable, se normalizaron y log-transformaron los datos del plot, y se regeneró el reporte HTML auto-contenido `VISUAL_VALIDATION_AUDIT.html`.

## 2026-04-23
- **02:55 AM**: 🚀 **Éxito en Prueba Piloto scAR (Donante IGTB469)**.
    - Instalación de `scar` (Novartis) en `.v20_venv` vía GitHub.
    - Implementación de optimizaciones de memoria (categorías + float32).
    - Entrenamiento exitoso en GPU (100 épocas).
    - Generación de `adata_scar_IGTB469.h5ad`.
- **02:15 AM**: 🚀 **Inicialización de Memoria Híbrida (Shadowing Protocol)**.
    - Creación de estructura de Vault en `docs/vault/`.
    - Configuración de `CLAUDE.md` y `.editorconfig`.
    - Migración de logs históricos de la V20 a la `wiki/` con metadatos YAML.
    - Creación de `index.md` y `log.md`.
- **02:00 AM**: Auditoría de salud del entorno. Dataset maestro validado (225k células, 6/6 marcadores NK).

## 2026-04-18
- Cierre de la Fase 07: Validación de firma molecular mediante Pseudobulk + DESeq2. Descubrimiento de la anergia por caída de `LCP2`.

## 2026-04-17
- Consolidación del dataset maestro V20. Éxito en el rescate de identidad genética (HGNC).

---
*Fin del Registro Actual*
 - 2026-04-23: �xito total en el Benchmark de scAR. Se demostr� superioridad t�cnica (3-4 min/donante en GPU) y biol�gica (reducci�n de contaminantes >50% vs flujo anterior). Se establece el plan para el procesamiento masivo del dataset V20.

## 2026-04-28
- **01:15 AM**: 🛡️ **Creación del Dataset Gold Standard (Pure Python)**.
    - Aplicación de filtros de purificación estricta: `B_CELL_score < 0.1` y `NK_score > T_CELL_score`.
    - Implementación de filtro de **Masa Crítica**: `n_cells >= 200` por donante para mitigar ruido estadístico.
    - Resultado: **547 donantes** validados (alineación con la referencia original de 502 + 45 rescatados).
    - Volumen final: **191,903 células** de alta pureza.
    - Objeto final: `scAR_python_validation/data/v20_python_gold_standard.h5ad`.
