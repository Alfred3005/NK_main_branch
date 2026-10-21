# Resultados

## Integración de la Cohorte y Purificación del Microambiente

La extracción a partir de la plataforma *CellxGene Census* (`census_version="2023-12-15"`) permitió delimitar, sobre un universo inicial de aproximadamente 45 millones de células únicas, un subconjunto de 8.8 millones correspondientes a tejido sanguíneo periférico. La aplicación sistemática de los criterios de selección en donantes sanos primarios procedentes de 14 estudios independientes (cuya relación detallada de títulos y registros DOI se compila en los Anexos), en conjunto con la remoción del ruido del ARN ambiental mediante scAR y la remoción del sesgo transcripcional ribosomal y de inmunoglobulinas, consolidó un compendio analítico de alta pureza (@fig-1). 

::: {#fig-1 layout-ncol=2}
![Distribución de células por edad y estudio](figures_clean/fig1a.png){#fig-1a}

![Efectividad de la corrección ambiental](figures_clean/fig1b.png){#fig-1b}

Consolidación de la cohorte y purificación del microambiente NK.
:::

Este filtrado riguroso resultó en una cohorte final integrada por 143,991 células NK distribuidas en 423 donantes adultos únicos con edades iguales o superiores a 34 años (@fig-1a). La eficacia del saneamiento ambiental quedó de manifiesto mediante la reducción estadísticamente significativa de firmas espurias ajenas a la estirpe linfoide innata, destacando el silenciamiento de transcritos eritroides e inmunoglobulínicos de fondo como *HBA1* e *IGKC* (@fig-1b; reporte técnico detallado en Anexos).

## Caracterización Demográfica y Equilibrio Técnico

La estratificación por grupos de edad definió dos conjuntos biológicos contrastantes: adultos (34 a 59 años; $n = 197$ donantes, 73,434 células) y adultos mayores ($\geq 60$ años; $n = 226$ donantes, 70,557 células). Esta partición mantuvo una distribución equilibrada entre sexos, con 213 donantes de sexo femenino y 210 de sexo masculino (@tbl-demografia). La distribución continua de la variable edad garantizó una representación homogénea a lo largo de las décadas evaluadas (@fig-2a y @fig-2b).

::: {#fig-2 layout-ncol=2 layout-nrow=2}
![Histograma de edades](figures_clean/fig2a.png){#fig-2a}

![Donantes por edad y grupo](figures_clean/fig2b.png){#fig-2b}

![Donantes por tecnología de captura (assay) y grupo](figures_clean/fig2c.png){#fig-2c}

Caracterización demográfica y equilibrio técnico de la cohorte.
:::

Para descartar la influencia de efectos de lote (*batch effects*) provenientes de las plataformas de secuenciación, se validó que el uso de estas tecnologías estuviera distribuido proporcionalmente entre ambos grupos de edad (@fig-2c). Las métricas de control de calidad transcripcional (número de genes detectados, identificadores moleculares únicos y porcentaje de transcritos mitocondriales), obtenidas tras aplicar el filtrado adaptativo descrito en la metodología, se mantuvieron en umbrales óptimos para ambos grupos (@tbl-demografia); las visualizaciones y los desgloses de estas métricas técnicas se detallan en el Anexo correspondiente.

::: {#tbl-demografia tbl-colwidths="[12,9,9,14,11,9,9,9,9,9]"}
| Grupo de Edad | Donantes | Células | Edad ± DE (años) | Sexo (F / M) | UMIs (med.) | Genes (med.) | MT (%) | NK CD56dim | NK CD56bright |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Adultos** | 197 | 73,434 | 46.4 ± 7.3 | 102 / 95 | 1,961 | 1,268 | 3.83 | 71,683 (97.6%) | 1,751 (2.4%) |
| **Adultos Mayores** | 226 | 70,557 | 73.5 ± 8.8 | 111 / 115 | 759 | 500 | 3.77 | 69,489 (98.5%) | 1,068 (1.5%) |
| **Total Cohorte** | **423** | **143,991** | — | **213 / 210** | — | — | — | **141,172 (98.0%)** | **2,819 (2.0%)** |

Resumen demográfico y de control de calidad transcriptómico de la cohorte.
:::

## Pureza del Linaje NK y Distribución de Subtipos

Los análisis de subconjuntos celulares se delimitaron al estudio de las dos subpoblaciones canónicas del linaje: el compartimento efector maduro CD56dim, que concentró el 98.0% de la cohorte (141,172 células), y el nicho regulador e inmaduro CD56bright, que constituyó el 2.0% restante (2,819 células) (@tbl-demografia). Los demás subtipos linfoides, tales como las células NKT, quedaron limitados al análisis exploratorio global sin ser incorporadas como subconjunto independiente.

Con el objetivo de corroborar la identidad celular y depurar posibles contaminaciones de otros linajes linfoides, se evaluó la expresión de genes marcadores canónicos derivados de las tablas ASCT+B del Atlas de Referencia Humana (Börner et al., 2021) (*lineage scoring*; p. ej., *NCAM1*, *FCGR3A*, *NKG7*, *GNLY*, *PRF1*, *KLRB1* para el linaje NK) en contraposición a firmas de células B y T (@fig-3a). La lista completa de genes marcadores empleada para esta validación fenotípica se encuentra disponible en los Anexos.

Al proyectar las 30 componentes principales de la matriz log-normalizada sin correcciones forzadas sobre un espacio UMAP bidimensional, se evidenció una estructuración espacial orientada predominantemente por el grupo etario y sus covariables técnicas asociadas (@fig-3a). Lejos de representar un obstáculo analítico, esta dispersión ratificó la necesidad de modelar explícitamente la plataforma de captura mediante formulaciones aditivas en *pseudobulk* (`~ assay + age_group`), protegiendo la varianza biológica genuina frente a cualquier homogeneización artificial. La delimitación de ambos subtipos y la variación de sus frecuencias individuales entre donantes confirmaron la preservación de las identidades fenotípicas madura e inmadura (@fig-3b y @fig-3c).

::: {#fig-3 layout-ncol=2}
![Pureza del linaje (Marcadores NK vs B/T)](figures_clean/fig3a.png){#fig-3a}

![UMAP por grupo de edad](figures_clean/fig3b.png){#fig-3b}

![Proporción de células NK CD56bright por donante](figures_clean/fig3c.png){#fig-3c}

Pureza del linaje, proyección UMAP exploratoria y distribución de grupos de edad.
:::

## Abundancia Diferencial del Linaje e Involución del Nicho CD56bright

La dinámica demográfica de las subpoblaciones reveló una contracción pronunciada del compartimento regulador a medida que avanza la edad cronológica. El modelado mediante regresión logística generalizada (GLM) de familia binomial con corrección por sobredispersión empírica de Pearson ($\phi = 6.7248$, $\chi^2 = 1230.64$, $df = 183$) confirmó un descenso estadísticamente significativo en la probabilidad de abundancia de las células *NK CD56bright* en los adultos mayores frente al estrato adulto ($p = 0.0163$, coeficiente del grupo etario $\beta = -0.4702$, error estándar ajustado $SE = 0.1957$, estadístico $t = -2.403$).

Esta regresión cuantificó una contracción relativa del 37.51% en la representación de las células *CD56bright*, asociada a una razón de probabilidades (RP o *Odds Ratio*) de 0.6249 con un intervalo de confianza al 95% de $[0.4258, 0.9170]$ (@fig-4). Considerando que este subconjunto constituye el productor fisiológico primordial de factores inmunomoduladores e inmunoatrayentes, particularmente IFN-$\gamma$ y las quimiocinas *XCL1* y *XCL2* (Cooper et al., 2001; Poli et al., 2009), el declive numérico observado constata una involución preferencial del brazo secretor frente a la preservación cuantitativa del compartimento citotóxico maduro.

![Proporción de NK CD56bright y análisis de abundancia diferencial. Boxplots comparativos de la proporción relativa entre Adultos y Adultos Mayores.](figures_clean/fig4.png){#fig-4 width=85% fig-align="center"}

## Expresión Diferencial de Alta Confianza (PyDESeq2) y Neutralización del Sesgo Tecnológico

El análisis transcripcional de *pseudobulk* con *PyDESeq2* permitió delimitar las alteraciones génicas vinculadas a la inmunosenescencia tomando en cuenta los artefactos de captura tecnológica. La neutralización de las diferencias técnicas (donde tecnologías de secuenciación como 10x 5' v2 introducían distorsiones artificiales de hasta un 55%) llevó a generar una matriz de datos balanceada de rango completo ($N = 187$ donantes: 152 adultos vs. 35 adultos mayores, abarcando 62,553 células). La posterior contracción bayesiana de los cambios de expresión mediante el algoritmo `apeGLM` estabilizó los estimadores de dispersión y suprimió el ruido asociado a transcritos de baja abundancia.

Con un criterio de significancia estadística ajustado por tasa de falso descubrimiento ($padj < 0.05$), el análisis identificó una firma transcripcional conformada por 23 genes diferencialmente expresados (@fig-5 y @tbl-degs-23).

::: {#tbl-degs-23 tbl-colwidths="[12,12,12,12,14,40]"}
| Gen | Media Base | $Log_2\text{FC}$ (apeGLM) | Error Estándar ($SE$) | FDR ($padj$) | Función Biológica Relevante |
|:---|:---:|:---:|:---:|:---:|:---|
| *S100A9* | 7.87 | +1.8753 | 0.4492 | 0.0045 | Alarmina proinflamatoria y respuesta a estrés oxidativo / ferroptótico |
| *SERGEF* | 7.99 | +1.1941 | 0.4475 | 0.0025 | Factor intercambiador de nucleótidos de guanina, señalización intracelular |
| *PALLD* | 14.48 | +0.8428 | 0.3073 | 0.0265 | Paladina, organización citoesquelética de actina y motilidad celular |
| *RNF169* | 13.84 | +0.7473 | 0.2715 | 0.0290 | E3 ubiquitina ligasa, respuesta a roturas de doble cadena de ADN (DDR) |
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
| *HIRA* | 7.14 | +0.0056 | 0.0297 | 0.0399 | Chaperona de histonas H3.3, ensamblaje de focos SAHF en senescencia |
| *ATL1* | 3.36 | +0.0047 | 0.0305 | 0.0441 | Atlastina 1, GTPasa de fusión de membrana del retículo endoplásmico |
| *PLEKHO1* | 1.43 | -0.0043 | 0.0366 | 0.0486 | Pleckstrina con dominio de homología, regulación de cascadas AKT |
| *XCL2* | 108.03 | -0.3446 | 0.0996 | 0.0497 | Quimiocina paráloga reclutadora de células dendríticas cDC1 |
| *MAP3K8* | 99.83 | -0.3660 | 0.1115 | 0.0412 | Serina/treonina cinasa TPL2, transductor de señales MAPK/ERK y NF-$\kappa$B |
| *XCL1* | 33.62 | -0.7250 | 0.1642 | 0.0084 | Quimiocina quimioatrayente de células dendríticas cDC1 |
| *KIR3DL2* | 28.59 | -1.1760 | 0.2731 | 0.0292 | Receptor inhibidor de células asesinas, ligando HLA-A/B |
| *KIR3DL1* | 36.65 | -1.4065 | 0.2396 | 0.0017 | Receptor inhibidor de células asesinas, ligando HLA-Bw4 |

Genes expresados diferencialmente de alta confianza ($padj < 0.05$) en células NK en envejecimiento, ordenados por log2FoldChange tras contracción apeGLM.
:::

![Mapa de calor (*heatmap*) de la expresión de los 23 genes regulados diferencialmente de alta confianza (*hits* colapsados), revelando los patrones de sobreexpresión y subexpresión en el envejecimiento.](figures_clean/fig5.png){#fig-5 width=95% fig-align="center"}

La firma canónica de 23 genes encaja con dos programas funcionales (@fig-5). Se constató la caída concordante de las quimiocinas *XCL1* ($LFC = -0.7250$, $padj = 0.0084$) y *XCL2* ($LFC = -0.3446$, $padj = 0.0497$), moléculas requeridas para el reclutamiento quimiotáctico de células dendríticas convencionales de tipo 1 (*cDC1*; Böttcher et al., 2018). Esta disfunción podría interferir la cooperación innata. Concurrente con este silenciamiento, los datos sugieren la represión pronunciada de los receptores inhibidores clonotípicos *KIR3DL1* ($LFC = -1.4065$, $padj = 0.0017$) y *KIR3DL2* ($LFC = -1.1760$, $padj = 0.0292$), acompañada por la caída de la cinasa transductora *MAP3K8* ($LFC = -0.3660$, $padj = 0.0412$); alteración que compromete el reconocimiento de las moléculas HLA de clase I e inhabilita las cascadas de fosforilación intracelular de MEK y ERK que gobiernan la translocación nuclear del complejo NF-$\kappa$B. El freno inflamatorio es molecular.

En contraste, los genes inducidos sugieren una respuesta adaptativa frente al estrés crónico, en concordancia con los modelos teóricos que postulan que las alteraciones de la inmunosenescencia representan mecanismos compensatorios de remodelación celular orientados a sostener la viabilidad frente a agresiones moleculares continuas (Fulop et al., 2018; López-Otín et al., 2023). La alarmina *S100A9* exhibió la mayor sobreexpresión de toda la firma transcriptómica ($LFC = +1.8753$, $padj = 0.0045$). Este incremento se vincula con susceptibilidad a ferroptosis y daño tisular (Chen et al., 2021; Wei et al., 2026). La inducción concurrente de *SERGEF* ($LFC = +1.1941$, $padj = 0.0025$), la proteína citoesquelética *PALLD* ($LFC = +0.8428$, $padj = 0.0265$) y la prostaglandina sintasa *PTGDS* ($LFC = +0.6825$, $padj = 0.0024$) evidencia reorganización estructural y metabólica en senescencia (Gateva et al., 2014; Pundlik et al., 2024; Sjölinder et al., 2002). Finalmente, la elevación de la ubiquitina ligasa *RNF169* ($LFC = +0.7473$, $padj = 0.0290$), proteína nuclear que compite contra 53BP1 en sitios de daño genotóxico para modular la reparación de roturas de doble cadena de ADN (Panier et al., 2012; Poulsen et al., 2012), ratifica la presencia de estrés por daño genómico no resuelto en las células NK del adulto mayor.

## Enriquecimiento de Vías Transcriptómicas y Modulación Fenotípica (GSEA / ORA)

La exploración de redes biológicas y rutas moleculares se abordó mediante dos estrategias complementarias. En primer término, el análisis de enriquecimiento por conjuntos de genes (*GSEA Preranked*) evaluó el espectro continuo de todos los genes cuantificados ($N = 10,816$) ordenados por el estadístico de Wald del contraste en *pseudobulk* con *PyDESeq2*, permitiendo capturar alteraciones poligénicas sutiles y coordinadas frente a las colecciones moleculares MSigDB Hallmark, KEGG, Reactome y GO Biological Process (@fig-6, @fig-7 y @tbl-vias-gsea; tablas completas en Anexos). En segundo término, el análisis de sobre-representación (*ORA*) evaluó la concentración funcional específica sobre la firma discreta de los 23 genes diferencialmente expresados de alta confianza ($padj < 0.05$).

::: {#tbl-vias-gsea tbl-colwidths="[14,14,24,9,9,10,20]"}
| Subpoblación | Categoría | Colección y Vía Transcripcional | NES | $p$-valor | FDR ($q$) | Genes Clave de Núcleo (*Core Enrichment*) |
|:---|:---|:---|:---:|:---:|:---:|:---|
| **CD56bright** | Genotóxico | UV Response Dn (Hallmark) | +1.782 | 0.0010 | 0.0087 | *CDKN1B*, *ATRX*, *PIK3CD*, *ADD3*, *CITED2*, *SYNE1* |
| **CD56bright** | Metabolismo | Oxidative Phosphorylation (KEGG) | -1.742 | 0.0010 | 0.0778 | *NDUFA6*, *NDUFS8*, *COX5B*, *UQCRFS1*, *SDHC*, *NDUFB8* |
| **CD56bright** | Metabolismo | Mitochondrial ATP Synthesis Coupled Electron Transport (GO:BP) | -1.555 | 0.0010 | 0.2098 | *ATP5F1A*, *ATP5MC1*, *COX6C*, *NDUFA4*, *UQCRQ* |
| **CD56dim** | Genotóxico | UV Response Dn (Hallmark) | +1.834 | 0.0010 | 0.0116 | *TGFBR2*, *MAPK14*, *ADD3*, *PIK3CD*, *CDKN1B*, *CITED2* |
| **CD56dim** | Inflamación | TNF-alpha Signaling via NF-kB (Hallmark) | -1.784 | 0.0010 | 0.0177 | *MAP3K8*, *FOSL2*, *DUSP2*, *NFKBIA*, *BIRC3*, *TNFAIP3* |
| **CD56dim** | Ciclo Celular | Myc Targets V1 (Hallmark) | +1.625 | 0.0010 | 0.0366 | *G3BP1*, *KPNB1*, *XPO1*, *ODC1*, *PSMD1*, *DUT*, *NPM1* |
| **CD56dim** | Metabolismo | Oxidative Phosphorylation (KEGG) | -1.698 | 0.0010 | 0.1147 | *NDUFA6*, *NDUFS8*, *COX7B*, *UQCRFS1*, *NDUFC2*, *COX5B* |
| **CD56dim** | Procesamiento | Reg. of mRNA Splicing via Spliceosome (GO:BP) | -1.876 | 0.0010 | 0.1964 | *SRSF2*, *SRSF5*, *U2AF1*, *HNRNPA1*, *SF3B1*, *MAGOH* |
| **CD56dim** | Telómeros | Reg. of Telomere Maintenance via Telomerase (GO:BP) | +1.913 | 0.0010 | 0.1912 | *XRCC5*, *TNIP1*, *PRKCQ*, *TCP1*, *CCT3*, *NEK7*, *ATM* |

Vías transcripcionales enriquecidas representativas por categoría biológica en las subpoblaciones NK CD56bright y CD56dim.
:::

El análisis de enriquecimiento funcional (GSEA) sobre el espectro continuo del estadístico de Wald reveló patrones biológicos altamente coordinados, distinguiendo entre un reloj basal compartido de estrés transcripcional y respuestas metabólicas e inflamatorias compartimentalizadas por subtipo:

1. **Estrés Genotóxico y Transcripcional Convergente (Reloj Basal Compartido):** La vía de respuesta a daño genotóxico (`MSigDB_Hallmark_UV_Response_Dn`) emergió como la única firma funcional con enriquecimiento positivo robusto y estadísticamente significativo bajo el umbral estricto ($FDR < 0.05$) en ambas subpoblaciones celulares. Dicha vía mostró una inducción simétrica tanto en células *CD56bright* ($NES = +1.782$, $p = 0.0010$, $FDR = 0.0087$) como en células *CD56dim* ($NES = +1.834$, $p = 0.0010$, $FDR = 0.0116$). Este enriquecimiento basal sostenido, impulsado por genes reguladores del ciclo celular, la cromatina y la transducción de señales como *CDKN1B*, *ATRX*, *PIK3CD*, *ADD3* y *CITED2*, evidencia un desgaste genómico universal dependiente de la edad a lo largo de todo el linaje NK.
2. **Deterioro en el Procesamiento de ARN en Células NK CD56dim y a Nivel Global:** De manera coordinada con la acumulación de estrés genotóxico, se identificó una represión transcripcional de la maquinaria de maduración y empalme alternativo del ARN mensajero. En el subtipo maduro *CD56dim*, este fenómeno se evidenció en la subregulación del espliceosoma (`KEGG_Spliceosome`, $NES = -1.708$, $FDR = 0.1253$; `GO_Regulation_Of_mRNA_Splicing_Via_Spliceosome`, $NES = -1.876$, $FDR = 0.1964$; `Reactome_mRNA_Splicing_Major_Pathway`, $NES = -1.695$, $FDR = 0.2359$). A nivel del linaje global, dicha desestabilización alcanzó una marcada represión (`GO_Positive_Regulation_Of_mRNA_Splicing_Via_Spliceosome`, $NES = -2.160$, $FDR = 0.0660$; `KEGG_Spliceosome`, $NES = -1.624$, $FDR = 0.1841$), impulsada por genes núcleo de la ribonucleoproteína nuclear y factores de empalme como *SRSF2*, *SRSF5*, *SRSF10*, *U2AF2* y *HNRNPL*.
3. **Supresión del Metabolismo Mitocondrial y Fosforilación Oxidativa:** Ambas subpoblaciones exhibieron una tendencia coordinada a la pérdida de capacidad bioenergética oxidativa, con un perfil de mayor profundidad en las células inmaduras *CD56bright* (`KEGG_Oxidative_phosphorylation`, $NES = -1.742$, $FDR = 0.0778$; `MSigDB_Hallmark_Oxidative_Phosphorylation`, $NES = -1.463$, $FDR = 0.1637$; `GO_Mitochondrial_ATP_Synthesis_Coupled_Electron_Transport`, $NES = -1.555$, $FDR = 0.2098$). En el compartimento maduro *CD56dim*, la reducción en la fosforilación oxidativa y el desacoplamiento de la cadena de transporte electrónico se mantuvo como una tendencia consistente (`KEGG_Oxidative_phosphorylation`, $NES = -1.698$, $FDR = 0.1147$; `Reactome_Respiratory_Electron_Transport`, $NES = -1.623$, $FDR = 0.2277$).

Ambos perfiles de enriquecimiento se ilustran gráficamente en el panel comparativo (@fig-6 y @fig-7). La @fig-6 exhibe las vías que superaron el umbral estricto ($FDR < 0.05$), donde destaca la inducción convergente de `UV Response Dn` frente a respuestas discordantes como la represión inflamatoria endógena de `TNF-alpha Signaling via NF-kB` ($NES = -1.784$, $FDR = 0.0177$) observada exclusivamente en las células *CD56dim*. Por su parte, la @fig-7 integra el análisis bajo umbral exploratorio ($FDR < 0.25$), permitiendo capturar el comportamiento coordinado de la desaceleración metabólica mitocondrial y la contracción en la maquinaria de empalme transcripcional. Asimismo, el panel detalla los genes que componen cada vía, lo que facilita observar si dichos genes actúan de forma exclusiva en un subtipo o si son compartidos por ambas poblaciones.

![Gráfico comparativo GSEA bajo umbral estricto (FDR < 0.05). Muestra las vías conservadas (inducción bilateral de UV Response Dn) y los comportamientos específicos de subtipo en el envejecimiento.](figures_clean/fig6.png){#fig-6 width=100% fig-align="center"}

![Gráfico comparativo GSEA bajo umbral exploratorio (FDR < 0.25). Captura señales metabólicas (OXPHOS, transporte electrónico) y transcripcionales (espliceosoma) compartidas y diferenciales.](figures_clean/fig7.png){#fig-7 width=100% fig-align="center"}

Adicionalmente, se realizó una evaluación ortogonal para contrastar el perfil transcripcional NK contra firmas establecidas de Senescencia Secretora (SASP) y Agotamiento Inmune (@tbl-sasp-exhaustion).

::: {#tbl-sasp-exhaustion tbl-colwidths="[14,22,9,10,10,18,17]"}
| Subpoblación | Firma Especializada | NES | $p$-valor | FDR ($q$) | Genes Relevantes (*Core Enrichment*) | Estado de Significancia |
|:---|:---|:---:|:---:|:---:|:---|:---|
| **CD56bright** | SASP (Reactome) | +1.503 | 0.0242 | 0.3168 | *H1-4*, *H1-3*, *CABIN1*, *UBN1*, *H1-2* | No significativo ($FDR > 0.25$) |
| **CD56dim** | SASP (Reactome) | +1.281 | 0.1844 | 0.1836 | *H1-2*, *H1-3*, *H1-4*, *ASF1A*, *TP53*, *HMGA1* | Tendencia ($FDR = 0.18$) |
| **CD56dim** | Exhausted vs Memory CD8+ T Cell (GSE9650) | +1.331 | 0.0310 | 0.2455 | *XRCC5*, *ETS1*, *PIK3CD*, *TOB1*, *KLRC1*, *ARL6IP5* | Tendencia ($FDR = 0.24$) |

Evaluación de firmas ortogonales especializadas de senescencia secretora (SASP) y agotamiento inmune por subpoblación NK.
:::

Como ratificación ortogonal focalizada en la firma discreta de 23 DEGs (@tbl-degs-23), el análisis de sobre-representación (*ORA*) frente a la ontología de procesos biológicos (*GO Biological Process 2023*) reveló una concentración estadísticamente significativa en programas de quimiotaxis y migración leucocitaria. Destacaron las rutas *Neutrophil Chemotaxis* ($padj = 0.0045$, traslape 3/70), *Granulocyte Chemotaxis* ($padj = 0.0045$, traslape 3/73) y *Positive Regulation of T Cell Chemotaxis* ($padj = 0.0045$, traslape 2/12), impulsadas primordialmente por el silenciamiento coordinado de las quimiocinas *XCL1* y *XCL2*, en concurrencia con la alarmina *S100A9*, la prostaglandina sintasa *PTGDS* y la cistatina *CST7* (reporte extendido y tablas de contingencia compiladas en los Anexos). Esta convergencia analítica confirma que las alteraciones detectadas en el envejecimiento NK no constituyen fluctuaciones estocásticas aisladas, sino que traducen un colapso coordinado de las señales quimiotácticas de enlace intercelular acoplado a programas metabólicos compensatorios frente al estrés.

