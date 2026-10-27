# Resultados

## Integración de la cohorte y purificación del microambiente

La extracción a partir de la plataforma *CellxGene Census* (`census_version="2023-12-15"`) permitió delimitar, sobre un universo inicial de aproximadamente 45 millones de células únicas, un subconjunto de 8.8 millones correspondientes a tejido sanguíneo periférico. La aplicación sistemática de los criterios de selección en donantes sanos primarios procedentes de 13 estudios independientes (@tbl-anexo-estudios), en conjunto con la eliminación del ARN ambiental mediante scAR y la depuración del sesgo transcripcional ribosomal y de inmunoglobulinas, consolidó la cohorte analítica (@fig-1). 

::: {#fig-1 layout-ncol=2}
![Distribución de células por edad y estudio](figures_clean/fig1a.png){#fig-1a}

![Efectividad de la corrección ambiental](figures_clean/fig1b.png){#fig-1b}

Consolidación de la cohorte y purificación del microambiente NK.
:::

*Nota.* Datos de CZ CELLxGENE Census (versión 2023-12-15). (a) Células por grupo de edad y estudio. (b) Conteo medio por célula de marcadores de ARN ambiental antes y después de la corrección con scAR.

Este filtrado riguroso resultó en una cohorte final integrada por 143,991 células NK distribuidas en 423 donantes adultos únicos con edades iguales o superiores a 34 años (@fig-1a). La eficacia del saneamiento ambiental quedó de manifiesto mediante la reducción de la expresión media de firmas espurias ajenas a la estirpe linfoide innata, destacando el silenciamiento de transcritos eritroides e inmunoglobulínicos de fondo como *HBA1* e *IGKC* (@fig-1b; Anexo A, sección A.3).

## Caracterización demográfica y distribución técnica

La estratificación por grupos de edad definió dos conjuntos biológicos contrastantes: adultos (34 a 59 años; $n = 197$ donantes, 73,434 células) y adultos mayores ($\geq 60$ años; $n = 226$ donantes, 70,557 células). Esta partición mantuvo una distribución equilibrada entre sexos, con 213 donantes de sexo femenino y 210 de sexo masculino (@tbl-demografia; @fig-2b). La distribución continua de la variable edad abarcó de forma continua el intervalo de edades evaluado (@fig-2a).

::: {#fig-2 layout-ncol=2 layout-nrow=2}
![Histograma de edades](figures_clean/fig2a.png){#fig-2a}

![Donantes por sexo y grupo de edad](figures_clean/fig2b.png){#fig-2b}

![Donantes por tecnología de captura (assay) y grupo](figures_clean/fig2c.png){#fig-2c}

Caracterización demográfica y distribución técnica de la cohorte.
:::

*Nota.* Cohorte completa: 197 adultos y 226 adultos mayores. Datos de CZ CELLxGENE Census (versión 2023-12-15).

Para evaluar la influencia de efectos de lote (*batch effects*) provenientes de las plataformas de secuenciación, se examinó la distribución de las tecnologías entre grupos de edad (@fig-2c). La distribución mostró un fuerte desbalance: 10x 5' v2 predominó en los adultos (143 de 197 donantes) y 10x 3' v2 en los adultos mayores (182 de 226); por ello, el ensayo se incluyó como covariable en los modelos. Las métricas de control de calidad transcripcional (número de genes detectados, identificadores moleculares únicos (UMI, del inglés *unique molecular identifiers*) y porcentaje de transcritos mitocondriales), obtenidas tras aplicar el filtrado adaptativo descrito en la metodología, difirieron entre grupos, en concordancia con la tecnología de captura (@tbl-demografia); las visualizaciones y los desgloses de estas métricas técnicas se detallan en el Anexo A.

::: {#tbl-demografia tbl-colwidths="[12,9,9,14,11,9,9,9,9,9]"}
| Grupo de Edad | Donantes | Células | Edad ± DE (años) | Sexo (F / M) | UMIs (med.) | Genes (med.) | MT (%) | NK CD56^dim^ | NK CD56^bright^ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Adultos** | 197 | 73,434 | 46.4 ± 7.3 | 102 / 95 | 1,961 | 1,268 | 3.83 | 71,683 (97.6%) | 1,751 (2.4%) |
| **Adultos Mayores** | 226 | 70,557 | 73.5 ± 8.8 | 111 / 115 | 759 | 500 | 3.77 | 69,489 (98.5%) | 1,068 (1.5%) |
| **Total Cohorte** | **423** | **143,991** | — | **213 / 210** | — | — | — | **141,172 (98.0%)** | **2,819 (2.0%)** |

Resumen demográfico y de control de calidad transcriptómico de la cohorte.
:::

*Nota.* DE: desviación estándar; UMI: identificadores moleculares únicos; MT: porcentaje de transcritos mitocondriales; med.: mediana. La columna NK CD56^dim^ incluye también las células NK sin subtipo anotado y las células NKT. Datos de CZ CELLxGENE Census (versión 2023-12-15).

## Pureza del linaje NK y distribución de subtipos

Los análisis de subconjuntos celulares se delimitaron al estudio de las dos subpoblaciones canónicas del linaje: el compartimento efector maduro CD56^dim^, que concentró el 98.0% de la cohorte (141,172 células), y el nicho regulador e inmaduro CD56^bright^, que constituyó el 2.0% restante (2,819 células) (@tbl-demografia). Los demás subtipos linfoides, tales como las células T asesinas naturales (NKT), quedaron limitados al análisis exploratorio global sin ser incorporados como subconjuntos independientes.

Con el objetivo de corroborar la identidad celular y depurar posibles contaminaciones de otros linajes linfoides, se evaluó la expresión de genes marcadores canónicos derivados de las tablas de estructuras anatómicas, tipos celulares y biomarcadores (ASCT+B, del inglés *Anatomical Structures, Cell Types plus Biomarkers*) del Atlas de Referencia Humana (Börner et al., 2021): *NKG7*, *GNLY*, *CST7*, *GZMA*, *PRF1*, *KLRD1* y *KLRF1* para el linaje NK, frente a *CD3D*, *CD3E*, *CD3G* y *TRAC* (linfocitos T) y *CD79A*, *MS4A1* y *CD19* (linfocitos B) (@fig-3a). La lista completa de genes marcadores empleada para esta validación fenotípica se presenta en la @tbl-anexo-marcadores del Anexo A.

Al proyectar los 30 componentes principales de la matriz log-normalizada sin correcciones forzadas sobre un espacio bidimensional de aproximación y proyección uniforme de variedades (UMAP, del inglés *uniform manifold approximation and projection*), se evidenció una estructuración espacial orientada predominantemente por el grupo etario y sus covariables técnicas asociadas (@fig-3b). Lejos de representar un obstáculo analítico, esta dispersión indicó la necesidad de modelar explícitamente la plataforma de captura mediante formulaciones aditivas en *pseudobulk* (`~ assay + age_group`), protegiendo la varianza biológica genuina frente a cualquier homogeneización artificial. La delimitación de ambos subtipos y la variación de sus frecuencias individuales entre donantes son compatibles con la preservación de las identidades fenotípicas madura e inmadura (@fig-3c).

::: {#fig-3 layout-ncol=2}
![Pureza del linaje (marcadores NK frente a B/T)](figures_clean/fig3a.png){#fig-3a}

![UMAP por grupo de edad](figures_clean/fig3b.png){#fig-3b}

![Proporción de células NK CD56^bright^ por donante](figures_clean/fig3c.png){#fig-3c}

Pureza del linaje, proyección UMAP exploratoria y proporción de células CD56^bright^ por donante.
:::

*Nota.* (a) Expresión de marcadores de linaje NK, T y B. (b) Proyección UMAP coloreada por grupo de edad. (c) Proporción de células NK CD56^bright^ en cada donante de la cohorte completa (197 adultos y 226 adultos mayores); el modelo de abundancia usa el subconjunto de 187 donantes con ensayos balanceados.

## Abundancia diferencial de las células CD56^bright^

La dinámica demográfica de las subpoblaciones reveló una contracción pronunciada del compartimento regulador a medida que avanza la edad cronológica. El modelado mediante GLM de familia binomial con corrección por sobredispersión empírica de Pearson ($\phi = 6.7248$, $\chi^2 = 1230.64$, $df = 183$) mostró un descenso estadísticamente significativo en la probabilidad de abundancia de las células NK CD56^bright^ en los adultos mayores frente al estrato adulto ($p = 0.0163$, coeficiente del grupo etario $\beta = -0.4702$, error estándar ajustado $SE = 0.1957$, estadístico $t = -2.403$). La comparación complementaria del cociente CD56^bright^/CD56^dim^ por donante (152 adultos y 35 adultos mayores) mostró la misma dirección, sin alcanzar significancia (prueba U de Mann-Whitney, $U = 3059$, $p = 0.167$).

Esta regresión cuantificó una reducción del 37.51% en los momios de que una célula NK fuera CD56^bright^, asociada a una OR de 0.6249 con un intervalo de confianza al 95% de $[0.4258, 0.9170]$ (@fig-4). Considerando que este subconjunto constituye el productor fisiológico primordial de factores inmunomoduladores e inmunoatrayentes, particularmente IFN-$\gamma$ y las quimiocinas *XCL1* y *XCL2* (Cooper et al., 2001; Poli et al., 2009), el declive numérico observado es compatible con una involución preferencial del brazo secretor frente a la preservación cuantitativa del compartimento citotóxico maduro.

![Proporción de células NK CD56^bright^ y abundancia diferencial entre adultos y adultos mayores: cociente CD56^bright^/CD56^dim^ por donante (diagramas de caja), composición media y conteos medios por grupo.](figures_clean/fig4.png){#fig-4 width=85% fig-align="center"}

*Nota.* El valor de *p* anotado en el primer panel corresponde al GLM sin corrección por sobredispersión; con la corrección, *p* = 0.0163 (véase el texto). Modelo con 187 donantes (152 adultos y 35 adultos mayores).

## Expresión diferencial (PyDESeq2) y control del sesgo tecnológico

El análisis transcripcional de *pseudobulk* con PyDESeq2 permitió delimitar las alteraciones génicas vinculadas a la inmunosenescencia tomando en cuenta los artefactos de captura tecnológica. Para controlar las diferencias técnicas, en cada análisis se excluyeron los ensayos sin donantes de ambos grupos de edad. El análisis global retuvo 420 donantes (194 adultos y 226 adultos mayores) y 140,930 células de cinco ensayos; el de CD56^dim^, 187 donantes (152 y 35) y 62,553 células de tres ensayos, y el de CD56^bright^, 354 donantes (170 y 184) y 2,814 células de cuatro ensayos. La contracción de los cambios logarítmicos (`lfc_shrink` de PyDESeq2) moderó las estimaciones de log2FC de los transcritos de baja abundancia.

Con un criterio de significancia estadística ajustado por tasa de falso descubrimiento ($padj < 0.05$), el análisis global identificó una firma transcripcional conformada por 23 genes diferencialmente expresados (@fig-5 y @tbl-degs-23); los análisis de CD56^dim^ y CD56^bright^ no identificaron genes significativos. Como no se aplicó un umbral de log2FC, varios de los 23 genes tienen cambios contraídos cercanos a 0.01.

::: {#tbl-degs-23 tbl-colwidths="[12,12,12,12,14,40]"}
| Gen | Media Base | $Log_2\text{FC}$ (contraído) | Error Estándar ($SE$) | FDR ($padj$) | Función Biológica Relevante |
|:---|:---:|:---:|:---:|:---:|:---|
| *S100A9* | 7.87 | +1.8753 | 0.4492 | 0.0045 | Alarmina proinflamatoria y respuesta a estrés oxidativo / ferroptótico |
| *SERGEF* | 7.99 | +1.1941 | 0.4475 | 0.0025 | Factor intercambiador de nucleótidos de guanina, señalización intracelular |
| *PALLD* | 14.48 | +0.8428 | 0.3073 | 0.0265 | Paladina, organización citoesquelética de actina y motilidad celular |
| *RNF169* | 13.84 | +0.7473 | 0.2715 | 0.0290 | E3 ubiquitina ligasa, respuesta a respuesta al daño en el ADN |
| *PTGDS* | 490.47 | +0.6825 | 0.1659 | 0.0024 | Prostaglandina D2 sintasa, biosíntesis lipídica y chaperona en senescencia |
| *SP2* | 9.07 | +0.6798 | 0.2156 | 0.0265 | Factor de transcripción con dedos de zinc Sp2, regulación transcripcional |
| *OSBPL3* | 10.01 | +0.6338 | 0.2396 | 0.0494 | Proteína transportadora de oxisteroles en membrana |
| *PRSS23* | 170.28 | +0.1805 | 0.0502 | 0.0290 | Serina proteasa pericelular |
| *CST7* | 1320.51 | +0.1028 | 0.0280 | 0.0290 | Cistatina F, regulador endógeno de granzimas y catepsinas citolíticas |
| *AGAP2* | 11.30 | +0.0137 | 0.0413 | 0.0290 | Proteína activadora de GTPasa Arf, tráfico vesicular y supervivencia |
| *FCHSD1* | 12.69 | +0.0113 | 0.0294 | 0.0354 | Proteína con dominio F-BAR, dinámica citoesquelética |
| *PORCN* | 8.12 | +0.0104 | 0.0358 | 0.0372 | O-aciltransferasa esencial para la maduración y secreción de ligandos Wnt |
| *FAM169A* | 9.58 | +0.0084 | 0.0273 | 0.0423 | Proteína nuclear de función homeostática |
| *ABCB8* | 5.81 | +0.0074 | 0.1230 | 0.0412 | Transportador ABC mitocondrial, homeostasis de hierro y estrés redox |
| *ZNF672* | 3.97 | +0.0072 | 0.0284 | 0.0175 | Factor transcripcional nuclear de dedos de zinc |
| *HIRA* | 7.14 | +0.0056 | 0.0297 | 0.0399 | Chaperona de histonas H3.3, ensamblaje de focos de heterocromatina asociados a la senescencia (SAHF) |
| *ATL1* | 3.36 | +0.0047 | 0.0305 | 0.0441 | Atlastina 1, GTPasa de fusión de membrana del retículo endoplásmico |
| *PLEKHO1* | 1.43 | -0.0043 | 0.0366 | 0.0486 | Pleckstrina con dominio de homología, regulación de cascadas AKT |
| *XCL2* | 108.03 | -0.3446 | 0.0996 | 0.0497 | Quimiocina paráloga reclutadora de células dendríticas cDC1 |
| *MAP3K8* | 99.83 | -0.3660 | 0.1115 | 0.0412 | Serina/treonina cinasa TPL2, transductor de señales MAPK/ERK y NF-$\kappa$B |
| *XCL1* | 33.62 | -0.7250 | 0.1642 | 0.0084 | Quimiocina quimioatrayente de células dendríticas cDC1 |
| *KIR3DL2* | 28.59 | -1.1760 | 0.2731 | 0.0292 | Receptor inhibidor de células asesinas, ligando HLA-A/B |
| *KIR3DL1* | 36.65 | -1.4065 | 0.2396 | 0.0017 | Receptor inhibidor de células asesinas, ligando HLA-Bw4 |

Genes expresados diferencialmente de alta confianza ($padj < 0.05$) en el análisis global de células NK, ordenados por log2FC contraído con PyDESeq2.
:::

*Nota.* Análisis global *pseudobulk* con PyDESeq2 (420 donantes; diseño `~ assay + age_group`). log2FC contraído con `lfc_shrink`; padj: valor de *p* ajustado por el método de Benjamini-Hochberg.

![Mapa de calor (*heatmap*) de la expresión de los 23 genes regulados diferencialmente de alta confianza (*hits* colapsados), revelando los patrones de sobreexpresión y subexpresión en el envejecimiento.](figures_clean/fig5.png){#fig-5 width=95% fig-align="center"}

*Nota.* Expresión *pseudobulk* estandarizada (puntaje *z*) de los 23 genes de la @tbl-degs-23, resumida por grupo de edad.

La firma canónica de 23 genes encaja con dos programas funcionales (@fig-5). Se observó la disminución concordante de las quimiocinas *XCL1* ($LFC = -0.7250$, $padj = 0.0084$) y *XCL2* ($LFC = -0.3446$, $padj = 0.0497$), moléculas requeridas para el reclutamiento quimiotáctico de células dendríticas cDC1 (Böttcher et al., 2018). Esta disfunción podría interferir la cooperación innata. Concurrente con este silenciamiento, los datos sugieren la represión pronunciada de los receptores inhibidores de distribución clonal *KIR3DL1* ($LFC = -1.4065$, $padj = 0.0017$) y *KIR3DL2* ($LFC = -1.1760$, $padj = 0.0292$), acompañada por la caída de la cinasa transductora *MAP3K8* ($LFC = -0.3660$, $padj = 0.0412$); alteración que podría modificar el reconocimiento de las moléculas HLA de clase I y atenuar las cascadas de fosforilación intracelular de MEK y ERK que gobiernan la translocación nuclear del factor nuclear κB (NF-$\kappa$B).

En contraste, los genes inducidos sugieren una respuesta adaptativa frente al estrés crónico, en concordancia con los modelos teóricos que postulan que las alteraciones de la inmunosenescencia representan mecanismos compensatorios de remodelación celular orientados a sostener la viabilidad frente a agresiones moleculares continuas (Fulop et al., 2018; López-Otín et al., 2023). La alarmina *S100A9* exhibió la mayor sobreexpresión de toda la firma transcriptómica ($LFC = +1.8753$, $padj = 0.0045$). Este incremento se vincula con susceptibilidad a ferroptosis y daño tisular (Chen et al., 2021; Wei et al., 2026). La inducción concurrente de *SERGEF* ($LFC = +1.1941$, $padj = 0.0025$), la proteína citoesquelética *PALLD* ($LFC = +0.8428$, $padj = 0.0265$) y la prostaglandina sintasa *PTGDS* ($LFC = +0.6825$, $padj = 0.0024$) sugiere una reorganización estructural y metabólica en senescencia (Gateva et al., 2014; Pundlik et al., 2024; Sjölinder et al., 2002). Finalmente, la elevación de la ubiquitina ligasa *RNF169* ($LFC = +0.7473$, $padj = 0.0290$), proteína nuclear que compite contra 53BP1 en sitios de daño genotóxico para modular la reparación de roturas de doble cadena de ADN (Panier et al., 2012; Poulsen et al., 2012), es compatible con estrés por daño genómico en las células NK del adulto mayor.

## Enriquecimiento de vías transcripcionales (GSEA y ORA)

La exploración de redes biológicas y rutas moleculares se abordó mediante dos estrategias complementarias. En primer término, el análisis de enriquecimiento por conjuntos de genes (*GSEA Preranked*) evaluó el espectro continuo de todos los genes cuantificados ($N = 10,057$ en el análisis global; 9,644 en CD56^dim^ y 1,872 en CD56^bright^) ordenados por el estadístico de Wald del contraste en *pseudobulk* con PyDESeq2, permitiendo capturar alteraciones poligénicas sutiles y coordinadas frente a las colecciones moleculares MSigDB Hallmark, KEGG, Reactome y GO Biological Process (@fig-6, @fig-7 y @tbl-vias-gsea; Anexo A, sección A.4). En segundo término, el ORA evaluó la concentración funcional específica sobre la firma discreta de los 23 genes diferencialmente expresados de alta confianza ($padj < 0.05$).

::: {#tbl-vias-gsea tbl-colwidths="[14,14,24,9,9,10,20]"}
| Subpoblación | Categoría | Colección y Vía Transcripcional | NES | Valor de $p$ | FDR ($q$) | Genes Clave de Núcleo (*Core Enrichment*) |
|:---|:---|:---|:---:|:---:|:---:|:---|
| *CD56^bright^* | Genotóxico | UV Response Dn (Hallmark) | +1.781 | 0.0010 | 0.0087 | *CDKN1B*, *ATRX*, *PIK3CD*, *ADD3*, *CITED2*, *SYNE1* |
| *CD56^bright^* | Metabolismo | Oxidative Phosphorylation (KEGG) | -1.742 | 0.0010 | 0.0778 | *NDUFA6*, *NDUFS8*, *COX5B*, *UQCRFS1*, *SDHC*, *NDUFB8* |
| *CD56^bright^* | Metabolismo | Mitochondrial ATP Synthesis Coupled Electron Transport (GO:BP) | -1.555 | 0.0010 | 0.2098 | *NDUFA6*, *UQCRFS1*, *SDHC*, *NDUFS8*, *COX5B*, *UQCRC2* |
| *CD56^dim^* | Genotóxico | UV Response Dn (Hallmark) | +1.834 | 0.0010 | 0.0116 | *TGFBR2*, *MAPK14*, *ADD3*, *PIK3CD*, *CDKN1B*, *CITED2* |
| *CD56^dim^* | Inflamación | TNF-alpha Signaling via NF-kB (Hallmark) | -1.784 | 0.0010 | 0.0177 | *MAP3K8*, *GADD45B*, *MAFF*, *BCL6*, *FOSL2*, *DUSP2* |
| *CD56^dim^* | Ciclo Celular | Myc Targets V1 (Hallmark) | +1.625 | 0.0010 | 0.0366 | *G3BP1*, *KPNB1*, *XPO1*, *ODC1*, *PSMD1*, *DUT*, *NPM1* |
| *CD56^dim^* | Metabolismo | Oxidative Phosphorylation (KEGG) | -1.698 | 0.0010 | 0.1147 | *ATP5MC1*, *TCIRG1*, *NDUFB7*, *ATP6V1H*, *NDUFA1*, *NDUFC2* |
| *CD56^dim^* | Procesamiento | Reg. of mRNA Splicing via Spliceosome (GO:BP) | -1.876 | 0.0010 | 0.1964 | *U2AF2*, *RBM8A*, *RBM3*, *JMJD6*, *MAGOH*, *SRSF10* |
| *CD56^dim^* | Telómeros | Positive Reg. of Telomere Maintenance via Telomerase (GO:BP) | +1.913 | 0.0010 | 0.1912 | *XRCC5*, *TNIP1*, *PRKCQ*, *TCP1*, *CCT3*, *NEK7*, *ATM* |

Vías transcripcionales enriquecidas representativas por categoría biológica en las subpoblaciones NK CD56^bright^ y CD56^dim^.
:::

*Nota.* GSEA preordenado por el estadístico de Wald de PyDESeq2, con 1,000 permutaciones; el valor de *p* mínimo posible es 0.001. Se muestran vías representativas de cada categoría con FDR < 0.25. NES: puntuación de enriquecimiento normalizada.

El análisis de enriquecimiento funcional (GSEA) sobre el espectro continuo del estadístico de Wald reveló patrones biológicos altamente coordinados, distinguiendo una señal compartida de estrés transcripcional y respuestas metabólicas e inflamatorias compartimentalizadas por subtipo:

1. **Estrés Genotóxico y Transcripcional Convergente:** La vía de respuesta a daño genotóxico (`MSigDB_Hallmark_UV_Response_Dn`) emergió como la única firma funcional con enriquecimiento positivo robusto y estadísticamente significativo bajo el umbral estricto ($FDR < 0.05$) en ambas subpoblaciones celulares. Dicha vía mostró una inducción simétrica tanto en células CD56^bright^ ($NES = +1.781$, $p = 0.0010$, $FDR = 0.0087$) como en células CD56^dim^ ($NES = +1.834$, $p = 0.0010$, $FDR = 0.0116$). Este enriquecimiento basal sostenido, impulsado por genes reguladores del ciclo celular, la cromatina y la transducción de señales como *CDKN1B*, *ATRX*, *PIK3CD*, *ADD3* y *CITED2*, sugiere un efecto de la edad compartido por todo el linaje NK.
2. **Deterioro en el Procesamiento de ARN en Células NK CD56^dim^ y a Nivel Global:** De manera coordinada con la acumulación de estrés genotóxico, se identificó una represión transcripcional de la maquinaria de maduración y empalme alternativo del ARN mensajero. En el subtipo maduro CD56^dim^, este fenómeno se evidenció en la subregulación del espliceosoma (`KEGG_Spliceosome`, $NES = -1.708$, $FDR = 0.1253$; `GO_Regulation_Of_mRNA_Splicing_Via_Spliceosome`, $NES = -1.876$, $FDR = 0.1964$; `Reactome_mRNA_Splicing_Major_Pathway`, $NES = -1.695$, $FDR = 0.2359$). A nivel del linaje global, la represión fue mayor (`GO_Positive_Regulation_Of_mRNA_Splicing_Via_Spliceosome`, $NES = -2.160$, $FDR = 0.0660$; `KEGG_Spliceosome`, $NES = -1.624$, $FDR = 0.1841$). En CD56^dim^, los genes núcleo de la regulación del empalme incluyeron factores como *U2AF2*, *SRSF10* y *HNRNPL*.
3. **Supresión del Metabolismo Mitocondrial y Fosforilación Oxidativa:** Ambas subpoblaciones exhibieron una tendencia coordinada a la pérdida de capacidad bioenergética oxidativa, con un perfil de mayor profundidad en las células inmaduras CD56^bright^ (`KEGG_Oxidative_phosphorylation`, $NES = -1.742$, $FDR = 0.0778$; `MSigDB_Hallmark_Oxidative_Phosphorylation`, $NES = -1.463$, $FDR = 0.1637$; `GO_Mitochondrial_ATP_Synthesis_Coupled_Electron_Transport`, $NES = -1.555$, $FDR = 0.2098$). En el compartimento maduro CD56^dim^, la reducción en la fosforilación oxidativa y el desacoplamiento de la cadena de transporte electrónico se mantuvo como una tendencia consistente (`KEGG_Oxidative_phosphorylation`, $NES = -1.698$, $FDR = 0.1147$; `Reactome_Respiratory_Electron_Transport_ATP_Synthesis_By_Chemiosmotic_Coupling`, $NES = -1.623$, $FDR = 0.2277$).

Ambos perfiles de enriquecimiento se ilustran gráficamente en el panel comparativo (@fig-6 y @fig-7). La @fig-6 exhibe las vías que superaron el umbral estricto ($FDR < 0.05$), donde destaca la inducción convergente de `UV Response Dn` frente a respuestas discordantes como la represión inflamatoria endógena de `TNF-alpha Signaling via NF-kB` ($NES = -1.784$, $FDR = 0.0177$) observada exclusivamente en las células CD56^dim^. Por su parte, la @fig-7 integra el análisis bajo umbral exploratorio ($FDR < 0.25$), permitiendo capturar el comportamiento coordinado de la desaceleración metabólica mitocondrial y la contracción en la maquinaria de empalme transcripcional. Asimismo, el panel detalla los genes que componen cada vía, lo que facilita observar si dichos genes actúan de forma exclusiva en un subtipo o si son compartidos por ambas poblaciones.

![Gráfico comparativo GSEA bajo umbral estricto (FDR < 0.05). Muestra las vías conservadas (inducción bilateral de UV Response Dn) y los comportamientos específicos de subtipo en el envejecimiento.](figures_clean/fig6.png){#fig-6 width=100% fig-align="center"}

*Nota.* NES: puntuación de enriquecimiento normalizada; FDR: tasa de descubrimientos falsos. GSEA preordenado por subpoblación.

![Gráfico comparativo GSEA bajo umbral exploratorio (FDR < 0.25). Captura señales metabólicas (fosforilación oxidativa, transporte electrónico) y transcripcionales (espliceosoma) compartidas y diferenciales.](figures_clean/fig7.png){#fig-7 width=100% fig-align="center"}

*Nota.* NES: puntuación de enriquecimiento normalizada; FDR: tasa de descubrimientos falsos. GSEA preordenado por subpoblación.

Adicionalmente, se realizó una evaluación ortogonal para contrastar el perfil transcripcional NK contra firmas establecidas del SASP y Agotamiento Inmune (@tbl-sasp-exhaustion). La firma de Reactome para el fenotipo secretor asociado a la senescencia (R-HSA-2559582) no mostró enriquecimiento en ninguna subpoblación. El conjunto GSE9650 utilizado reúne los genes con menor expresión en linfocitos T CD8+ agotados que en los de memoria (*DN*, del inglés *down*); por ello, su enriquecimiento positivo en CD56^dim^ indica un parecido con el perfil de memoria y no con el de agotamiento.

::: {#tbl-sasp-exhaustion tbl-colwidths="[14,22,9,10,10,18,17]"}
| Subpoblación | Firma Especializada | NES | Valor de $p$ | FDR ($q$) | Genes Relevantes (*Core Enrichment*) | Estado de Significancia |
|:---|:---|:---:|:---:|:---:|:---|:---|
| *CD56^bright^* | SASP (Reactome, R-HSA-2559582) | +0.877 | 0.6651 | 1.0000 | *CDKN1B*, *UBA52*, *MAPK1*, *ANAPC16*, *EHMT1* | No significativo ($FDR > 0.25$) |
| *CD56^dim^* | SASP (Reactome, R-HSA-2559582) | -0.913 | 0.5954 | 0.9098 | *H2AJ*, *ANAPC15*, *H2AX*, *CDKN2D*, *ANAPC11*, *H3-3B* | No significativo ($FDR > 0.25$) |
| *CD56^dim^* | Exhausted vs Memory CD8+ T Cell, DN (GSE9650) | +1.331 | 0.0310 | 0.2455 | *XRCC5*, *ETS1*, *PIK3CD*, *TOB1*, *KLRC1*, *ARL6IP5* | Tendencia ($FDR = 0.2455$) |

Evaluación de firmas ortogonales especializadas de SASP y agotamiento inmune por subpoblación NK.
:::

*Nota.* SASP: firma R-HSA-2559582 de Reactome 2022. GSE9650 DN: genes con menor expresión en linfocitos T CD8+ agotados que en los de memoria.

Como análisis complementario sobre la firma de 23 genes diferencialmente expresados (@tbl-degs-23), el ORA frente a la ontología de procesos biológicos (*GO Biological Process 2023*) reveló una concentración estadísticamente significativa en programas de quimiotaxis y migración leucocitaria. Destacaron las rutas *Neutrophil Chemotaxis* ($padj = 0.0045$, traslape 3/70), *Granulocyte Chemotaxis* ($padj = 0.0045$, traslape 3/73) y *Positive Regulation of T Cell Chemotaxis* ($padj = 0.0045$, traslape 2/12), impulsadas por la disminución de las quimiocinas *XCL1* y *XCL2*, junto con la alarmina *S100A9* en las dos primeras (Anexo A, sección A.4). Esta convergencia sugiere que las alteraciones detectadas en el envejecimiento NK se concentran en las señales quimiotácticas de enlace intercelular, junto con programas compensatorios frente al estrés.

