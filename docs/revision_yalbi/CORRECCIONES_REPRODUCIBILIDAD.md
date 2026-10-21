# Correcciones de reproducibilidad para la tesis de Alfredo Morales Salazar

**Qué es esto:** lista de información que la tesis **no documenta** (o documenta de forma
ambigua o distinta a lo ejecutado) y que es **necesaria para reproducir el trabajo de principio
a fin**. Cada punto indica *qué falta*, *dónde va en la tesis* y *el valor real* cuando se pudo
confirmar contra el repositorio `tesis-alfredo-morales` (rama `feat/post-humanizacion-capitulos`),
su código (`scripts/`) o sus resultados versionados (`results/`).

Alcance de la revisión: solo lectura del repositorio. Los datos crudos (`.h5ad`, ~144 mil
células) no están en el repositorio, así que nada se volvió a ejecutar; cuando un valor depende
de los datos se indica «no se puede confirmar sin los datos».

Se ordena por severidad para la reproducibilidad:
- 🔴 **Bloqueante**: sin esto no se puede reproducir la etapa.
- 🟠 **Importante**: se puede reproducir, pero con riesgo alto de divergir.
- 🟡 **Menor**: conviene para claridad y trazabilidad; no bloquea.

Todas las rutas son relativas a la raíz del repositorio.

---

## 🔴 Bloqueantes

### 1. La tabla de los 23 DEG no corresponde a ningún archivo de resultados (§Resultados, «Expresión diferencial de alta confianza»; Conclusión 2)
Es la corrección de mayor impacto científico. Se buscó en todo el historial de git: ningún archivo de resultados de ninguna corrida tiene *IL7R* con LFC −1.0416; en todas, su LFC es cercano a 0 y su padj está entre 0.39 y 0.99. El valor solo aparece en un texto narrativo (`Inmunosenescencia_ Células NK y Modelado..txt`). La tabla `@tbl-degs-23` y el texto citan *IL7R*
(−1.0416), *NKG7* (+0.8175), *KLRB1*, *GZMA*, *TRAC*, *GZMH*, *HLA-DRB1*, *KLRG1*, *XCL1*,
*XCL2* y *S100A9* (−1.6169). El archivo que produce el código para ese análisis es otro.
- **Confirmado (archivo):** `results/subtypes/deseq2_results_significant_nk_cell_general.csv`
  tiene 23 genes con padj < 0.05, pero son ABCB8, AGAP2, ATL1, CST7, FAM169A, FCHSD1, HIRA,
  KIR3DL1, KIR3DL2, MAP3K8, OSBPL3, PALLD, PLEKHO1, PORCN, PRSS23, PTGDS, RNF169, S100A9,
  SERGEF, SP2, XCL1, XCL2 y ZNF672. De los 11 genes de la tabla de la tesis solo coinciden 3
  (*XCL1*, *XCL2*, *S100A9*), y con otros valores.
- **El signo de *S100A9* está invertido:** en el archivo es log2FC = **+1.875** (padj 0.0045);
  la tesis dice −1.6169 y lo interpreta como «represión genuina». En todo el historial de git
  (28 commits revisados) *S100A9* aparece siempre con signo positivo en los archivos de DEG.
- ***TRAC* no puede ser un DEG con este código:** `scripts/22_pseudobulk_subtypes_pydeseq2.py`
  l. 117–122 elimina todos los genes que empiezan por `TRAC`, `TRBC`, `RPS`, `RPL`, `IGH`,
  `IGK`, `IGL`, etc., antes del modelo. *TRAC* no existe en ninguno de los tres archivos
  completos de resultados.
- ***IL7R*, *NKG7*, *KLRB1*, *GZMA*, *GZMH*, *HLA-DRB1*, *KLRG1* no son significativos** en
  ningún archivo (global, CD56dim, CD56bright, ni `results/pydeseq2/`); por ejemplo, *IL7R*
  global: log2FC −0.008, padj 0.44. Ningún CSV del repositorio, en ningún commit, contiene a
  *IL7R* como significativo.
- **Origen de los valores de la tesis:** solo aparecen en texto narrativo, no en salidas de
  código: `results/subtypes/Inmunosenescencia_ Células NK y Modelado..txt` (l. 106 y ss., un
  documento redactado con apoyo de un modelo de lenguaje que contiene marcas «[User prompt]»),
  `docs/reporte_integrativo_final.md` l. 313–325 y `docs/vault/decisions.md` l. 23.
- **La Figura 5 de la propia tesis contradice la tabla:** `tesis/manuscripts/figures_clean/fig5.png`
  (idéntica byte a byte a `results/figures/heatmap_23_hits_collapsed.png`) muestra los 23 genes
  del CSV (ZNF672 … PLEKHO1), no *IL7R*/*NKG7*/*GZMA*.
- **Acción:** regenerar `@tbl-degs-23` directamente del CSV (con un script que la escriba) y
  reescribir los párrafos de Resultados, Discusión (*IL7R*, *KLRG1*, granzimas, *S100A9*),
  Conclusiones 2–3 y Resumen con la lista real. Si existe otra corrida que dio la lista de la
  tesis, versionar su script, su entrada y su salida, e indicar cuál es la definitiva.

### 2. Cohorte y subpoblación de la expresión diferencial mal atribuidas (§Resultados; Resumen; Conclusión 1)
La tesis dice que los 23 DEG salen de una «matriz balanceada» de **N = 187 donantes (152 vs 35),
62,553 células**, y atribuye *IL7R*/*KLRB1*/*XCL1*/*XCL2*/*S100A9* a CD56bright y *GZMA*/*GZMH*/
*NKG7*/*KLRG1* a CD56dim.
- **Confirmado:** los 23 DEG vienen del pseudobulk **global** (`NK cell general`, todas las
  células, `22_…py` l. 149–150). Según `docs/reporte_integrativo_final.md` l. 285–290, ese
  análisis usó **420 donantes (194 vs 226), 140,930 células**, 5 ensayos.
- N = 187 / 62,553 corresponde a la cohorte del análisis **CD56dim** (`docs/…` l. 292–297) y
  coincide con la del GLM de abundancia (`results/subtypes/statistical_test_ratios.txt`: 152 vs
  35). **CD56dim y CD56bright dieron 0 DEG** (`deseq2_results_significant_nk_cd56dim.csv` y
  `…_cd56bright.csv` solo tienen encabezado).
- **No se puede confirmar sin los datos:** el número exacto de donantes y células del análisis
  global (el CSV no lo guarda; solo lo imprime en consola, `22_…py` l. 185 y 219).
- **Acción:** en §Resultados, Resumen y Conclusión 1, reportar por separado N y células de cada
  análisis (global, CD56dim, CD56bright, GLM), decir que los subtipos no dieron DEG individuales
  y quitar la atribución de genes a subtipos. Idealmente, que `22_…py` escriba un
  `pseudobulk_design_<subtipo>.csv` con donante, grupo, ensayo y n_células.

### 3. Procedencia de los datos: no hay script de extracción de CELLxGENE Census (§Metodología, «Recolección y preprocesamiento»; Anexo A.1)
La tesis da `census_version="2023-12-15"`, 45 M → 8.8 M células, 14 estudios y 13 aportantes,
pero el repositorio no tiene el código que consulta el Census.
- **Confirmado:** ningún archivo `.py` del repositorio importa `cellxgene_census`. El primer
  script de la cadena (`scripts/03-consolidate-scar.py` l. 33) ya parte de
  `data/processed/scar_denoised/adata_scar_*.h5ad`, que ningún script genera.
- Falta: el filtro exacto de `obs` (`is_primary_data`, `disease == "normal"`,
  `tissue_general == "blood"`, lista de `cell_type`, `organism`), la lista de `dataset_id` y de
  `collection_id`, y el criterio con que se excluyó el estudio 14. La tabla de estudios del
  Anexo A (aportes por estudio que suman 143,991) no tiene script que la produzca.
- La exclusión de «individuos sometidos a tratamientos farmacológicos» no tiene un campo
  correspondiente en el esquema del Census; no hay código que la aplique.
- Siete de los 13 estudios son de COVID-19, lupus, inmunodeficiencia común variable o
  hematopoyesis clonal: hay que decir que solo se tomaron sus donantes control (`disease ==
  normal`) y mostrar cómo.
- **Acción:** versionar el script de extracción (consulta al Census, lista de `dataset_id`,
  conteos por paso: 45 M → 8.8 M → NK → ≥ 34 años) y citarlo en §Metodología y Anexo A.

### 4. scAR: el paso no está en el repositorio y no tiene parámetros (§Metodología, «Diseño experimental libre de contaminación ambiental»)
- **Confirmado:** ningún script ejecuta scAR (`grep` de `scar` como módulo: sin resultados).
  `03-consolidate-scar.py` solo concatena salidas ya corregidas; por el nombre de los archivos
  (l. 59) se deduce que scAR corrió **por donante**, pero no se puede confirmar.
- Falta: versión de scAR, cómo se estimó el perfil ambiental sin gotas vacías (la tesis dice que
  no las había), `feature_type`, número de épocas, `sparsity`, semilla, CPU/GPU, y si se aplicó
  antes o después del filtro a NK.
- La afirmación «reducción estadísticamente significativa» de *HBA1* e *IGKC* (Resultados,
  Fig. 1b) no tiene prueba estadística detrás: `scripts/12_scar_ambient_validation.py`
  l. 34–55 solo compara medias crudas contra corregidas en una gráfica de barras, y depende de
  una capa `raw_counts` que ningún script crea.
- **Acción:** versionar el script de scAR con sus parámetros, o al menos documentarlos en
  §Metodología; cambiar «estadísticamente significativa» por «reducción de la media» o añadir la
  prueba.

### 5. La cadena de ejecución está rota: archivos intermedios sin productor, rutas de Windows y un orquestador parcial (§Metodología, disponibilidad de código)
- **El orquestador empieza a la mitad.** `scripts/run_final_pipeline.py` l. 55–65 solo corre
  `22 → 23 → 24 → 14 → 25 → plot_* → compile → report`. Extracción, scAR, QC, Solo y armado de
  metadatos quedan fuera. `run_pipeline.ps1` es PowerShell (solo Windows).
- **Archivos que ningún script genera:**
  - `data/NK_dataset_qc_ready.h5ad`, entrada de 22, 23, `plot_heatmap_global.py` y las tablas
    demográficas (`22_…py` l. 96; `23_…py` l. 411).
  - `scAR_python_validation/data/v20_python_gold_standard.h5ad`, entrada de 12, 13, 17, 25 y
    `apply_mass_critical_filter.py`. `05-doublets-solo.py` escribe `v20_python_final_clean.h5ad`
    (l. 24), no el `gold_standard`.
  - `data/processed/scar_denoised/adata_scar_*.h5ad` (punto 4).
  - El conjunto `REACTOME_SASP` de `custom_senescence_signatures.gmt` (punto 7).
- **Rutas absolutas de otra máquina:** `C:/Users/PREDATOR/Documents/Antigravity_workspaces/…`
  en `24_subtypes_ranked_gsea.py` l. 37 y 43, `plot_heatmap_global.py` l. 11 y
  `plot_gprofiler_style.py` l. 20. Además, `plot_heatmap_global.py` y `plot_gprofiler_style.py`
  leen de `results/experiment_collinearity`, carpeta que no existe en `results/` (está en
  `legacy/`).
- **Directorios de trabajo incompatibles:** 03–05, 12, 13, 25_extract y `apply_mass_critical_filter`
  usan rutas relativas a la raíz (`scAR_python_validation/…`); 22, 23, 14 y 25_ora usan rutas
  relativas a `scripts/` (`../data/…`). No hay forma de correr la cadena completa desde un solo
  directorio.
- **Acción:** un orquestador único (Snakemake, Makefile o `run_all.py`) desde la consulta al
  Census hasta las figuras, con rutas relativas a la raíz y un paso explícito que escriba
  `NK_dataset_qc_ready.h5ad`. Documentar en §Metodología qué archivo entra a cada etapa.

### 6. GLM binomial: el código no corrige la sobredispersión que la tesis dice corregir; el intervalo de confianza no coincide; Milo no tiene salida (§Metodología, «Modelado estadístico de abundancia»; §Resultados, «Abundancia diferencial»)
La tesis dice «prueba de Wald con corrección por sobredispersión» y reporta β = −0.4702,
p < 0.0001, RP = 0.6249, IC95 % [0.578, 0.675].
- **Confirmado (código):** `scripts/23_differential_abundance_milo.py` l. 206–207 ajusta
  `sm.GLM(y, X, family=Binomial()).fit()` con la escala por defecto. El archivo
  `results/subtypes/proportion_glm_results.txt` lo confirma: `Scale: 1.0000`,
  `Covariance Type: nonrobust`.
- **Los datos están sobredispersos:** Pearson χ² = 1,230 con 183 g.l. → φ ≈ 6.7. Con la
  corrección (`fit(scale="X2")`), el EE de β pasa de 0.075 a ≈ 0.194, z ≈ −2.42,
  **p ≈ 0.016** e IC95 % de la RP ≈ **[0.43, 0.91]** (cálculo propio a partir de los valores del
  archivo). El efecto sigue siendo significativo al 5 %, pero no «p < 0.0001».
- **IC de la tesis:** con los valores del archivo, exp(−0.618) = 0.539 y exp(−0.322) = 0.725.
  El intervalo [0.578, 0.675] no se reproduce con ningún error estándar del archivo.
- **Milo:** el script se llama «milo», el `MASTER_INDEX.md` habla de «Abundancia Diferencial
  (Milo)» y el código lo intenta (l. 231–381, `make_nhoods(prop=0.1)`, `n_neighbors=50`,
  `n_pcs=30`, diseño `~ assay + age_group`), pero no hay ningún `milo_*.csv` ni `milo_*.png` en
  `results/`, y `milopy` no está en `requirements.txt`. Si falla la importación, el script sigue
  en silencio (l. 240–243, 302–304).
- La prueba de Mann-Whitney sobre los cocientes por donante dio **p = 0.167** (152 vs 35;
  `results/subtypes/statistical_test_ratios.txt`) y la tesis no la menciona.
- **Acción:** (a) volver a ajustar con `scale="X2"` (o cuasibinomial, o un GLMM binomial con
  efecto aleatorio por donante) y reportar β, EE, p e IC de ese modelo; (b) corregir el IC; (c)
  decir en §Metodología que Milo no se usó (o versionar su salida); (d) reportar la prueba de
  Mann-Whitney y explicar por qué se prefiere el GLM.

### 7. La firma «SASP» evaluada es en realidad la firma SAHF de Reactome (§Resultados, `@tbl-sasp-exhaustion`; Discusión; Conclusión 4)
- **Confirmado (archivo):** en `results/subtypes/gsea_specialized/nk_cd56dim/gene_sets.gmt`,
  `REACTOME_SASP` (l. 3) tiene exactamente los mismos 13 genes que «Formation Of
  Senescence-Associated Heterochromatin Foci (SAHF) R-HSA-2559584» (l. 431): RB1, UBN1, ASF1A,
  H1-5, H1-2, HIRA, EP400, HMGA1, H1-4, LMNB1, TP53, H1-3, CABIN1. La SASP real de Reactome
  (R-HSA-2559582, l. 1172) es otro conjunto. Por eso los genes núcleo citados (histonas H1,
  *CABIN1*, *UBN1*) son de heterocromatina, no de secreción.
- Ningún script crea `REACTOME_SASP`: `13_build_custom_gmt.py` solo agrega CellAge (y deja
  SenMayo como `pass`, l. 27–34); `16_update_signatures.py` solo agrega GSE9650 (l. 29–34).
- **Valores en CD56bright no coinciden:** la tesis dice NES +1.503, p 0.0242, FDR 0.3168 («no
  significativo»). El archivo `gsea_specialized/nk_cd56bright/gseapy.gene_set.prerank.report.csv`
  dice NES +1.513, p 0.0196, **FDR 0.0743**, es decir, bajo el umbral exploratorio 0.25.
- La conclusión «ausencia de SASP» sí tiene apoyo en la SASP verdadera de Reactome, evaluada en
  la misma corrida: NES +0.877, FDR 1.00 (CD56bright) y NES −0.913, FDR 0.91 (CD56dim).
- **Acción:** reemplazar `REACTOME_SASP` por R-HSA-2559582 (y, si se quiere, SenMayo), versionar
  el script que arma el GMT, volver a correr `14_run_specialized_gsea.py` y rehacer la tabla.

---

## 🟠 Importantes

### 8. Solo: el umbral de la tesis no es el del código (§Metodología, «scAR y control de calidad»)
- **Tesis:** doblete si la diferencia de probabilidad doblete − singlete > 0.3 **y** la
  complejidad supera el percentil 95.
- **Código** (`scripts/05-doublets-solo.py` l. 80): `doublet_score > 0.5` y
  `doublet_score > singlet_score`; no hay ningún criterio de percentil 95.
- Otros parámetros que faltan en el texto: 5,000 HVG `flavor="seurat"` con `batch_key="donor_id"`
  (l. 58–63); scVI `n_layers=2`, `n_latent=30`, `gene_likelihood="nb"`, `batch_key="donor_id"`
  (l. 69–70); `max_epochs=None` para scVI y 400 con *early stopping* para Solo (l. 71, 75); sin
  semilla (`scvi.settings.seed` no se fija).
- `docs/reporte_integrativo_final.md` l. 168 dice que Solo no detectó dobletes por encima del
  umbral (191,903 células). La tesis no da cuántos dobletes se quitaron.
- **Acción:** describir el umbral real y reportar el número de dobletes removidos.

### 9. QC adaptativo: dos implementaciones paralelas y un filtro de masa crítica no descrito (§Metodología)
- `04-adaptive-qc.py` usa ddqc (l. 73–83: `res=1.5`, Leiden, `n_components=30`, `k=15`, MAD
  `threshold=2.5`, `n_genes_lower_bound=100`) y, **si ddqc falla, aplica en silencio** filtros
  fijos `n_genes > 200` y `% mito < 20` (l. 88–92).
- `04-purify-qc-lineage.py` es una reimplementación manual (l. 29–79: Leiden `res=0.5`,
  `n_neighbors=20`, 2,000 HVG, 30 PC; corte inferior de genes y superior de % mito a
  2.5 × 1.4826 × MAD por clúster; mínimo 100 genes; MAD = 0 se reemplaza por 1.0 o 0.5).
- Solo deriva de `04-purify` (`05-doublets-solo.py` l. 23); `05-preprocessing-metadata.py`
  deriva de `04-adaptive` (l. 20). No se puede saber cuál alimentó la cohorte final sin los
  datos.
- `apply_mass_critical_filter.py` l. 18 exige **≥ 200 células por donante**
  (`docs/vault/decisions.md` §1: «de 600+ a 547» donantes). La tesis no lo menciona, y 423
  donantes con 143,991 células (≈ 340 células/donante en promedio) hacen dudar de si se aplicó a
  la cohorte final.
- El «filtrado declarativo» que neutraliza la bimodalidad no se define en el texto. En el código
  es la exclusión por prefijo de RPS/RPL/IG/TR (`22_…py` l. 117–119).
- **Acción:** declarar cuál script de QC es el canónico, con su resolución, MAD y cortes;
  reportar cuántas células salieron en cada paso; decir si se aplicó el umbral de 200 células por
  donante; listar los prefijos excluidos.

### 10. Subtipos CD56bright/CD56dim: son la anotación de los autores originales, y la tabla demográfica cuenta NK genéricas y NKT como CD56dim (§Metodología; §Resultados, «Pureza del linaje»)
- **Confirmado:** no hay clustering ni anotación propia. Los subtipos son la columna `cell_type`
  del Census: `"CD16-negative, CD56-bright natural killer cell, human"` y
  `"CD16-positive, CD56-dim natural killer cell, human"` (`22_…py` l. 126–133; `23_…py` l. 15–16).
- `legacy/descriptive_analysis/generate_descriptive_tables.py` l. 24–28 asigna a **CD56dim**
  también `natural killer cell` (genérica) y, con `fillna('CD56dim')`, las tres categorías NKT.
  Así se obtiene «CD56dim 141,172 (98.0 %) + CD56bright 2,819 = 143,991». En DE y en el GLM, en
  cambio, CD56dim es solo la etiqueta explícita; las NK genéricas y NKT entran únicamente al
  análisis global.
- No está documentado qué estudios anotaron explícitamente bright/dim y cuáles solo «natural
  killer cell»; es justo lo que obliga a filtrar ensayos en 22 y 23.
- **Acción:** decir en §Metodología que los subtipos vienen de la anotación del Census (sin
  reanotar), y corregir la tabla demográfica para separar «CD56dim anotada», «NK sin subtipo» y
  «NKT».

### 11. Grupos de edad: umbrales inconsistentes entre texto y código (§Metodología)
- Metodología: «Adultos 34–60», «Adultos mayores > 60». Resultados: «34 a 59» y «≥ 60».
- Código: `05-doublets-solo.py` l. 45 `old` si `age >= 60` y l. 47 conserva `age > 34` (excluye
  a los de 34 años); `generate_descriptive_tables.py` l. 16 usa `age >= 34`.
- La edad se extrae con `str.extract(r'(\d+)')` de `development_stage` (l. 41). Las etiquetas del
  Census que no son «NN-year-old» (p. ej. por década, o «80 year-old and over») darían edades
  incorrectas o NaN. No se puede confirmar sin los datos.
- **Acción:** unificar en el texto «34–59 / ≥ 60» y en el código `>= 34`; documentar el
  tratamiento de etiquetas de edad no numéricas.

### 12. Pseudobulk y PyDESeq2: filtros, diseño y *shrinkage* no descritos o descritos distinto (§Metodología, «Análisis de expresión diferencial»)
Valores reales (`scripts/22_pseudobulk_subtypes_pydeseq2.py`):
- Mínimo de células por donante: **5 en CD56bright, 1 en CD56dim y global** (l. 155); al menos
  150 células por subtipo (l. 164) y 3 donantes (l. 188).
- **Filtro de ensayos:** se quitan los ensayos sin donantes de ambos grupos de edad (l. 174–183).
  El GLM usa otro filtro: ensayos con ≥ 10 células bright y ≥ 10 dim (`23_…py` l. 398–400). Y
  `docs/vault/decisions.md` l. 22 y el texto narrativo de `results/subtypes/` dicen «solo 10x 3'
  v3». Son tres descripciones distintas de la «cohorte balanceada». Los ensayos que quedan en el
  GLM son, por el archivo, «10x 3' transcription profiling», «10x 5' v1» y «10x 5' v2» (no
  3' v3).
- A cada donante se le asigna un solo ensayo (el de más células, l. 139–140).
- Prefiltro de genes: ≥ 10 cuentas en ≥ 3 donantes (l. 215–217).
- Diseño `~ assay + age_group`, degradado en silencio a `~ age_group` si hay un solo ensayo
  (l. 239–249); contraste `["age_group", "old", "adult"]` (l. 263); `refit_cooks=True`.
- **DEG = padj < 0.05 sin umbral de log2FC** (l. 281). El volcán usa |LFC| > 0.5 solo para
  colorear (l. 24). Tras el *shrinkage*, varios de los 23 DEG tienen log2FC ≈ 0.005–0.014
  (ABCB8, AGAP2, ATL1, HIRA, PLEKHO1, ZNF672…); conviene decirlo.
- ***Shrinkage*:** no es apeGLM de R. Es `DeseqStats.lfc_shrink()` de PyDESeq2 (l. 272), que
  implementa un previo de Cauchy tipo apeGLM. Los archivos muestran que sí se aplicó (p. ej.
  ABCB8: log2FC/lfcSE = 0.06 frente a `stat` = 3.92). Pero el nombre del coeficiente
  `"age_group[T.old]"` solo existe en PyDESeq2 ≥ 0.5; con la 0.4.x que permite
  `requirements.txt` (`pydeseq2>=0.4.4`), el `except` de l. 273–274 dejaría los LFC sin contraer
  sin detener el pipeline.
- La tesis afirma que la regularización apeGLM «redujo la cantidad absoluta de genes
  significativos». En PyDESeq2, el *shrinkage* solo cambia `log2FoldChange` y `lfcSE`; `padj`
  viene de la prueba de Wald sin contraer, así que no cambia el número de DEG.
- La tesis cita PyDESeq2 como Love et al. (2014); la referencia de PyDESeq2 es Muzellec et al.
  (2023, *Bioinformatics*).
- **Acción:** documentar todo lo anterior en §Metodología (con versión de PyDESeq2), unificar la
  definición de «cohorte balanceada» y quitar la frase sobre la reducción de DEG por el
  *shrinkage*.

### 13. ORA: el texto describe g:Profiler, pero se ejecutó Enrichr (§Metodología, «Enriquecimiento funcional»)
- **Tesis:** g:Profiler, fuentes GO:BP, KEGG, REAC y HP, universo = todos los genes analizados,
  p nominal < 0.05.
- **Código del que salen los archivos:** `scripts/25_subtypes_ora.py` l. 24 y 35–44 usa
  `gp.enrichr` con MSigDB_Hallmark_2020, GO_Biological_Process_2023 y Reactome_2022, **sin
  universo propio** (el de Enrichr por defecto) y con **padj < 0.05**. Las salidas son
  `results/subtypes/ora/nk_cell_general/…` (p. ej. «Neutrophil Chemotaxis», genes
  XCL2;XCL1;S100A9).
- La función g:Profiler de `24_subtypes_ranked_gsea.py` (l. 213–256, llamada en l. 533) no tiene
  salidas en `results/` (no existe `results/subtypes/gsea/*/ora/`), y `gprofiler-official` no está
  en `requirements.txt`; si no está instalada, el script la omite en silencio (l. 216–219).
- **Acción:** describir la ORA que realmente produjo los resultados (Enrichr, bibliotecas, fecha
  de consulta y universo), o bien correr g:Profiler, versionar la salida y usarla.

### 14. GSEA: parámetros ausentes del texto y reutilización silenciosa de resultados viejos (§Metodología)
- Valores reales (`24_subtypes_ranked_gsea.py` l. 50–65): ranking = estadístico de Wald de
  PyDESeq2 (l. 82); bibliotecas MSigDB_Hallmark_2020, KEGG_2021_Human, Reactome_2022 y
  GO_Biological_Process_2023, que gseapy **descarga de Enrichr en línea** (el comentario de l. 49
  dice «offline», pero no es así); `min_size=15`, `max_size=500`, **1,000 permutaciones**,
  **semilla 42**, 4 hilos.
- GSEA especializada (`14_run_specialized_gsea.py` l. 54–61): `min_size=5`, `max_size=1000`,
  1,000 permutaciones, semilla 42; GMT propio más Reactome_2022.
- Con 1,000 permutaciones, el p mínimo es 0.001; todos los «p = 0.0010» de `@tbl-vias-gsea`
  están en ese piso.
- **Reutilización:** `gsea_for_analysis` (l. 168–182) **carga el CSV previo si existe y no vuelve
  a correr GSEA**. Como `results/subtypes/gsea/*/gsea_*.csv` están versionados, volver a correr el
  pipeline con otros DEG no actualizaría el GSEA.
- **Acción:** reportar estos parámetros, la fecha o versión de las bibliotecas de Enrichr (o
  versionar los `.gmt` usados), y agregar una opción `--force` o borrar los CSV antes de correr.

### 15. Entorno sin versiones fijadas y dependencias faltantes (§Metodología, primer párrafo)
- `requirements.txt` usa solo `>=` (scanpy, anndata, scvi-tools, pydeseq2, gseapy, statsmodels…)
  e instala ddqc desde `git+https://github.com/ayshwaryas/ddqc.git` sin commit.
- Faltan: **scar**, **milopy** (y R/edgeR para Milo), **gprofiler-official**, **torch**,
  **cellxgene-census**, patsy, formulaic.
- La tesis da Python 3.12.3 y scvi-tools 1.1.5; ninguno de los dos está fijado. No hay archivo de
  bloqueo (`environment.yml`, `conda-lock`, `uv.lock` o `pip freeze`).
- Semillas: GSEA usa 42; scVI y Solo (`05-doublets-solo.py`, `26_run_single_cell_scvi.py`) no
  fijan semilla; Leiden y UMAP usan el valor por defecto de scanpy.
- **Acción:** generar un `environment.yml` o lock con versiones exactas de la corrida final,
  fijar `scvi.settings.seed` y reportar las versiones clave en §Metodología.

### 16. Afirmaciones de Discusión y Conclusiones sin análisis detrás en el repositorio (§Discusión; §Conclusiones; Resumen)
| Afirmación | ¿Qué hay en el repositorio? |
|---|---|
| El ARN ambiental de los adultos mayores (*CXCL8*, *CXCL2*, *IL1B*, *IL6*, *SERPINA1*) es una lectura del *inflammaging* (Discusión l. 44–46) | Nada. Ningún script compara el perfil ambiental por grupo de edad. `12_scar_…py` solo grafica medias globales de HBB/HBA/IG/JCHAIN/LYZ. Esos genes no están en los resultados de DE o tienen padj vacío. |
| Ausencia de SASP | La firma usada es SAHF (punto 7). La SASP real no está enriquecida, lo que sí apoya la conclusión una vez corregida. |
| Sin sobreexpresión de *PDCD1*, *HAVCR2*, *LAG3* (Discusión l. 32; Conclusión 4) | *PDCD1* **no está** en ningún archivo de resultados (se filtró por baja expresión): no se evaluó. *HAVCR2* y *LAG3* no son significativos en global ni en CD56dim y no están en CD56bright. La firma GSE9650 es de linfocitos T CD8. |
| Pérdida de reclutamiento de cDC1 por *XCL1*/*XCL2* | *XCL1* y *XCL2* sí bajan en el pool global (log2FC −0.725, padj 0.0084; −0.345, padj 0.0497), con otros valores que los de la tesis. No hay análisis de comunicación celular; mantenerlo como hipótesis (como ya hace Perspectivas), no como resultado (Conclusión 2, Resumen). |
| «Colapso absoluto» de OXPHOS / Complejo I en CD56bright (Resumen; Conclusión 4) | KEGG OXPHOS FDR 0.078, Hallmark OXPHOS FDR 0.164, GO ATP Synthesis FDR 0.210: son señales exploratorias (FDR < 0.25), no «colapso». No se evaluó un conjunto específico de Complejo I. |
| MYC induce *TERT* (Discusión l. 24) | *TERT* no está en los resultados; *MYC* no cambia (padj 0.999 en CD56dim). Solo hay GSEA (Myc Targets V1, FDR 0.037). |
| Alteraciones del citoesqueleto que impiden la polarización de gránulos (Discusión l. 40) | Solo «Actomyosin Structure Organization», NES **+1.857**, FDR 0.134, en `docs/reporte_integrativo_final.md` l. 436: es positivo y exploratorio. |
| *10x 5' v2* introduce distorsiones de hasta 55 % (Resultados) | Ningún script lo calcula; la cifra aparece en el texto narrativo de `results/subtypes/…Modelado..txt`. |
| Ineficacia de anti-PD-1; superagonistas de IL-15 | Sin análisis; es interpretación. |

- **Acción:** reformular cada una como hipótesis o como interpretación de la literatura, o
  agregar el análisis que la sostenga (p. ej. comparar el perfil ambiental estimado por scAR
  entre grupos de edad).

---

## 🟡 Menores (claridad y trazabilidad)

### 17. Etiquetas de términos GSEA que no corresponden exactamente al término del archivo
- `@tbl-vias-gsea`, CD56dim: «Reg. of Telomere Maintenance via Telomerase» NES +1.913, FDR
  0.1912 corresponde en el archivo a **Positive** Regulation… (GO:0032212). El término sin
  «Positive» (GO:0032210) tiene NES 1.372 y FDR 0.619.
- «Reactome_Respiratory_Electron_Transport» NES −1.623, FDR 0.2277 corresponde a R-HSA-163200
  (*…ATP Synthesis By Chemiosmotic Coupling, And Heat Production…*). El término R-HSA-611105
  tiene NES −1.730 y FDR 0.265.
- GSE9650 es el conjunto **_DN** (genes bajos en agotadas frente a memoria). Un NES positivo
  indica parecido al perfil de memoria, no al de agotamiento; conviene escribir el nombre
  completo.

### 18. Interpretación de la cifra de 37.51 %
37.51 % = 1 − e^β es una reducción de **momios** (odds), no de «probabilidad de captura». Con
proporciones de ~2–3 % la aproximación es razonable, pero debe decirse así.

### 19. Scripts sin uso reportado y salidas ausentes
`26_run_single_cell_scvi.py`, `27_run_single_cell_mixedlm.py` y `28_subtypes_mixed_gsea.py`
(scVI-DE y modelo mixto `expression ~ age_group + assay` con donante aleatorio; `27_…py` l. 23)
trabajan en `scAR_python_validation_v4_clean_subtypes_mixed_models/` y no tienen salidas en
`results/`. La tesis no los menciona; `docs/vault/decisions.md` §4 dice que el modelo mixto dio
0 DEG. Lo mismo ocurre con `17_*`, `17b_*` y `20_functional_enrichment.py` (este último menciona
«86 genes significativos», l. 94). **Acción:** reportarlos como análisis de sensibilidad o
moverlos a `legacy/`.

### 20. Documentos narrativos guardados como resultados
`results/subtypes/Inmunosenescencia_ Células NK y Modelado..txt` no es una salida de código (tiene
marcas «[User prompt]» y fuentes web) y es la fuente de varias cifras de la tesis. El Anexo A
remite a `Reporte_Integrativo_Subtipos_Abundancia_V2.html` para el diagnóstico de bimodalidad y
scAR. **Acción:** sacar el `.txt` de `results/` y citar en los anexos los scripts y tablas que
sostienen cada diagnóstico.

### 21. Marcadores de pureza: la tabla del Anexo A no es la lista del código
El Anexo A lista 11 marcadores NK, 5 T y 4 B. `04-purify-qc-lineage.py` l. 23–27 puntúa 6 NK
(NCAM1, FCGR3A, NKG7, GNLY, PRF1, KLRB1), 3 B (CD19, MS4A1, MZB1) y 3 T (CD3E, TRAC, TRBC1). El
*dotplot* de la Fig. 3a no tiene script que lo genere. Tampoco se dice si el puntaje se usó para
excluir células o solo para mostrar.

### 22. Errores menores de código
- `05-doublets-solo.py` l. 32 llama a `sys.exit(1)` sin `import sys`.
- `03-consolidate-scar.py` asigna `donor_id` desde el nombre del archivo solo si falta (l. 58–60);
  no se dice si los `donor_id` del Census son únicos entre estudios.
- El flujo de `figura2_flujo_metodologico.png` es un esquema, no una salida de datos; conviene
  versionar su fuente (Mermaid o SVG).

---

## Cifras de la tesis contra los archivos de resultados

| Cifra | Dice la tesis | Dice el archivo (ruta) | ¿Coincide? |
|---|---|---|---|
| Cohorte total | 423 donantes, 143,991 células | 197 + 226 donantes; 73,434 + 70,557 células (`legacy/descriptive_analysis/results_descriptive_analysis_v5/tables/tabla1_demografia_cohorte.csv`) | Sí (el archivo está en `legacy/`) |
| Edad, sexo, UMIs, genes, % MT por grupo | 46.4 ± 7.3 / 73.5 ± 8.8; 102/95, 111/115; 1,961 / 759 UMIs… | Mismos valores (mismo CSV) | Sí |
| CD56dim / CD56bright | 141,172 (98.0 %) / 2,819 (2.0 %) | Mismos valores, pero «CD56dim» incluye NK genéricas y NKT (`generate_descriptive_tables.py` l. 24–28) | Sí la cifra, no la definición |
| Cohorte de los 23 DEG | N = 187 (152/35), 62,553 células | Global: 420 (194/226), 140,930 células; 187/62,553 es la cohorte CD56dim (`docs/reporte_integrativo_final.md` l. 285–297) | **No** |
| Número de DEG FDR < 0.05 (global) | 23 | 23 (`results/subtypes/deseq2_results_significant_nk_cell_general.csv`) | Sí |
| Lista de DEG | IL7R, NKG7, KLRB1, GZMA, TRAC, GZMH, HLA-DRB1, KLRG1, XCL1, XCL2, S100A9 | 23 genes distintos; solo coinciden XCL1, XCL2, S100A9 (mismo CSV) | **No** |
| *IL7R* | −1.0416, padj 0.0003 | −0.008, padj 0.44 (`deseq2_results_nk_cell_general.csv`) | **No** |
| *NKG7* | +0.8175, padj 0.0163 | +0.034, padj 0.55 (ídem) | **No** |
| *KLRB1* | −0.9161, padj 0.0163 | −0.004, padj 0.94 (ídem) | **No** |
| *GZMA* | +0.9419, padj 0.0381 | −0.021, padj 0.71 (ídem) | **No** (signo opuesto) |
| *TRAC* | −1.1398, padj 0.0381 | Ausente: el filtro de l. 117–119 de `22_…py` lo excluye | **No** |
| *GZMH* | +0.7063, padj 0.0381 | +0.021, padj 0.60 (ídem) | **No** |
| *HLA-DRB1* | −1.0776, padj 0.0381 | −0.0006, padj 0.90 (ídem) | **No** |
| *KLRG1* | +0.7583, padj 0.0381 | −0.005, padj 0.88 (ídem) | **No** (signo opuesto) |
| *XCL1* | −1.0967, padj 0.0401 | −0.7250, padj 0.0084 (ídem) | Signo sí; valor no |
| *XCL2* | −1.0827, padj 0.0401 | −0.3446, padj 0.0497 (ídem) | Signo sí; valor no |
| *S100A9* | −1.6169, padj 0.0460 | **+1.8753**, padj 0.0045 (ídem) | **No** (signo opuesto) |
| DEG en CD56dim / CD56bright | Genes atribuidos a cada subtipo | 0 y 0 (`deseq2_results_significant_nk_cd56dim.csv`, `…_cd56bright.csv`) | **No** |
| β edad (GLM) | −0.4702 | −0.4702, EE 0.075 (`results/subtypes/proportion_glm_results.txt`) | Sí |
| p del GLM | < 0.0001, «con corrección por sobredispersión» | z = −6.231, p < 0.001, **sin corrección** (Scale 1.0, nonrobust); con corrección ≈ 0.016 | Cifra sí; método **no** |
| RP | 0.6249 | e^−0.4702 = 0.6249 | Sí |
| IC95 % de la RP | [0.578, 0.675] | [0.539, 0.725] desde el IC de β del archivo | **No** |
| Contracción | 37.51 % | 1 − 0.6249 = 37.51 % (reducción de momios) | Sí (cifra) |
| N del GLM | — (se presenta como cohorte balanceada) | 187 donantes (152/35) (`statistical_test_ratios.txt`; GLM `No. Observations: 187`) | Sí |
| Mann-Whitney | No se reporta | p = 0.1674 (`statistical_test_ratios.txt`) | — |
| UV Response Dn, CD56bright | NES +1.782, p 0.0010, FDR 0.0087 | 1.7815, p 0.001, FDR 0.0087 (`results/subtypes/gsea/cd56bright/gsea_MSigDB_Hallmark_2020.csv`) | Sí |
| UV Response Dn, CD56dim | +1.834, FDR 0.0116 | 1.8343, FDR 0.0116 (`gsea/cd56dim/gsea_MSigDB_Hallmark_2020.csv`) | Sí |
| TNF-α/NF-κB, CD56dim | −1.784, FDR 0.0177 | −1.7838, FDR 0.0177 (ídem) | Sí |
| Myc Targets V1, CD56dim | +1.625, FDR 0.0366 | 1.6246, FDR 0.0366 (ídem) | Sí |
| E2F Targets, CD56dim (Discusión) | +1.324 | 1.3237, FDR 0.217 (ídem) | Sí (exploratorio) |
| OXPHOS KEGG, CD56bright | −1.742, FDR 0.0778 | −1.7421, FDR 0.0778 (`gsea/cd56bright/gsea_KEGG_2021_Human.csv`) | Sí |
| OXPHOS Hallmark, CD56bright | −1.463, FDR 0.1637 | −1.4630, FDR 0.1637 | Sí |
| Mito ATP Synthesis (GO), CD56bright | −1.555, FDR 0.2098 | −1.5550, FDR 0.2098 | Sí |
| OXPHOS KEGG, CD56dim | −1.698, FDR 0.1147 | −1.6983, FDR 0.1147 | Sí |
| Spliceosome KEGG, CD56dim | −1.708, FDR 0.1253 | −1.7082, FDR 0.1253 | Sí |
| Reg. mRNA Splicing via Spliceosome (GO), CD56dim | −1.876, FDR 0.1964 | −1.8762, FDR 0.1964 | Sí |
| mRNA Splicing Major Pathway (Reactome), CD56dim | −1.695, FDR 0.2359 | −1.6948, FDR 0.2359 | Sí |
| Respiratory Electron Transport (Reactome), CD56dim | −1.623, FDR 0.2277 | −1.6225, FDR 0.2276, pero es R-HSA-163200 | Valor sí; etiqueta no |
| Telomere Maintenance via Telomerase, CD56dim | +1.913, FDR 0.1912 | 1.9132, FDR 0.1912, término «**Positive** Regulation…» | Valor sí; etiqueta incompleta en la tabla |
| Pos. Reg. Telomerase Activity / DNA Biosynthetic, CD56dim | +1.790 / +1.847 | 1.7902 / 1.8468 | Sí |
| Pos. Reg. mRNA Splicing (GO), global | −2.160, FDR 0.0660 | −2.1598, FDR 0.0660 (`gsea/global/gsea_GO_Biological_Process_2023.csv`) | Sí |
| Spliceosome KEGG, global | −1.624, FDR 0.1841 | −1.6240, FDR 0.1841 | Sí |
| «SASP», CD56bright | +1.503, p 0.0242, FDR 0.3168 | 1.513, p 0.0196, **FDR 0.0743**; además el conjunto es SAHF (`gsea_specialized/nk_cd56bright/gseapy.gene_set.prerank.report.csv`) | **No** |
| «SASP», CD56dim | +1.281, p 0.1844, FDR 0.1836 | 1.281, p 0.1844, FDR 0.1836 (conjunto SAHF) | Cifra sí; conjunto **no** |
| GSE9650 Exhausted vs Memory, CD56dim | +1.331, p 0.0310, FDR 0.2455 | 1.331, p 0.0310, FDR 0.2455, conjunto `_DN` | Sí |
| Células analizadas tras QC | — | 191,903 según `docs/reporte_integrativo_final.md` l. 168; sin archivo de conteos por paso | No se puede confirmar sin los datos |

Resumen de la tabla: los valores de abundancia (salvo el IC y el método) y casi todos los de GSEA
coinciden con `results/`. Los de expresión diferencial génica no coinciden.

---

## Tablas y figuras de la tesis: script que las produce

| Elemento | Archivo en la tesis | Script que lo produce | Observación |
|---|---|---|---|
| Fig. 2 (flujo metodológico) | `figures/figura2_flujo_metodologico.png` | Ninguno | Esquema; versionar su fuente |
| Fig. 1a (células por edad y estudio) | `figures_clean/fig1a.png` = `legacy/…/Figura_distribucion_por_estudios.png` | **Ninguno** encontrado | Sin script |
| Fig. 1b (efecto de scAR) | `fig1b.png` = `results/figures/06_scAR_Ambient_RNA_Correction.png` | `scripts/12_scar_ambient_validation.py` (escribe en `scAR_python_validation_v4_clean/…`) | Entrada `gold_standard` sin productor |
| Fig. 2a/2b/2c (edad, sexo, ensayo) | `fig2a–c.png` = `legacy/…/figures_individual/Figura_1C…`, `1A_Distribucion_Sexo`, `1A_Distribucion_Assay` | `legacy/descriptive_analysis/02b_descriptive_figures_individual.py` | Está en `legacy/`, fuera del orquestador |
| Fig. 3a (pureza de linaje) | `fig3a.png` = `results/figures/02_Lineage_Purity_DotPlot.png` | **Ninguno** | Sin script |
| Fig. 3b (UMAP por edad) | `fig3b.png` = `results/figures/04_UMAP_Age_Group.png` | **Ninguno** | Sin script (30 PC, sin corrección, según el texto) |
| Fig. 3c (proporción CD56bright por donante) | `fig3c.png` = `legacy/…/Figura_3C_Proporciones_CD56bright_Donante.png` | `legacy/descriptive_analysis/02_descriptive_analysis_figures.py` l. 187 y ss. | En `legacy/` |
| Fig. 4 (abundancia) | `fig4.png` = `tesis/figures/…/nk_ratio_analysis.png` | `scripts/23_differential_abundance_milo.py` (`run_cell_ratio_analysis`) | La p anotada es la del GLM sin corrección |
| Fig. 5 (heatmap 23 DEG) | `fig5.png` = `results/figures/heatmap_23_hits_collapsed.png` | `scripts/plot_heatmap_global.py` l. 137 | Ruta de Windows; muestra genes distintos a los de `@tbl-degs-23` |
| Fig. 6 y 7 (GSEA comparativo) | `fig6.png`, `fig7.png` = `results/figures/gProfiler_Style_Comparative_Plot_v7_*.png` | `scripts/plot_gprofiler_style.py` (nombre por argumento, l. 28) | Ruta de Windows; lee `results/experiment_collinearity` |
| `@tbl-demografia` | — | `legacy/descriptive_analysis/generate_descriptive_tables.py` | En `legacy/`; cuenta NK genéricas y NKT como CD56dim |
| `@tbl-degs-23` | — | **Ninguno**: valores de texto narrativo | Ver punto 1 |
| `@tbl-vias-gsea` | — | `24_subtypes_ranked_gsea.py` (valores); `compile_gsea_table.py` (tabla unificada) | Selección de filas manual; dos etiquetas inexactas |
| `@tbl-sasp-exhaustion` | — | `14_run_specialized_gsea.py` | Conjunto «SASP» = SAHF; valores de CD56bright distintos |
| Tabla de estudios (Anexo A) | — | **Ninguno** | Sin script |
| Tabla de marcadores ASCT+B (Anexo A) | — | Ninguno (lista del código distinta, punto 21) | — |

---

## Resumen de prioridad
Si solo se corrigen unas pocas cosas en la tesis, el orden de impacto es:
**#1 (tabla de 23 DEG ≠ archivo; *S100A9* con signo opuesto; *TRAC* imposible) > #2 (cohorte
N = 187 mal atribuida y genes asignados a subtipos sin DEG) > #6 (GLM sin la corrección de
sobredispersión que dice el texto; IC; Milo) > #7 (SASP = SAHF) > #5 (cadena rota: entradas sin
productor, rutas de Windows) > #3/#4 (Census y scAR sin código) > #13 (ORA Enrichr ≠ g:Profiler)
> #8 (umbral de Solo) > #12 (pseudobulk y *shrinkage*) > #16 (afirmaciones sin análisis).**

Las siete primeras son las que hoy impiden una reproducción fiel o hacen que el texto diga algo
distinto de lo que muestran los archivos. Los resultados de GSEA de subtipos y la cifra
β = −0.4702 sí se reproducen desde `results/`, lo que da una base sólida para corregir el resto.
