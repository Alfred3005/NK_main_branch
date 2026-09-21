# Resultados

## Integración de la Cohorte y Purificación del Microambiente

De los aproximadamente 45 millones de células únicas disponibles en la plataforma *CellxGene Census* (`census_version="2023-12-15"`) al momento de realizar la extracción, 8.8 millones correspondían a tejido sanguíneo periférico. Tras la aplicación de los criterios de inclusión y exclusión (donantes sanos primarios procedentes de 14 estudios distintos), y posterior a la limpieza bioinformática (corrección de fondo ambiental mediante scAR, remoción de ruido ribosomal e inmunoglobulinas), se consolidó un conjunto de datos final de alta pureza (Figura 1). Cabe mencionar que la relación de los títulos y DOIs de los 14 estudios originarios se detalla en los Anexos. De manera análoga, los resultados completos sobre las validaciones técnicas y controles de calidad aplicados para la remoción del fondo ambiental se documentan en un reporte separado disponible en los Anexos.

La cohorte purificada incluyó un total de 143,991 células NK a lo largo de 423 donantes adultos únicos ($\geq 34$ años) (Figura 1A). Adicionalmente, el análisis de efectividad de la corrección ambiental ratificó la calidad inicial de las células purificadas, evidenciando una reducción estadísticamente significativa en la expresión de genes de otros linajes (ej. *HBA1*, *IGKC*) (Figura 1B).

## Caracterización Demográfica y Equilibrio Técnico

Para caracterizar el perfil de senescencia, la población se estratificó en dos grupos biológicos: adultos (34 a 59 años; $n = 197$ donantes, 73,434 células) y adultos mayores ($\geq 60$ años; $n = 226$ donantes, 70,557 células), manteniendo un equilibrio proporcional entre los sexos femenino y masculino (213 y 210 donantes, respectivamente) (Tabla 1). La distribución continua de las edades proporcionó un panorama representativo de la evolución cronológica en la cohorte (Figura 2A y 2B).

Para descartar la influencia de efectos de lote (*batch effects*) provenientes de las plataformas de secuenciación, se validó que el uso de estas tecnologías estuviera distribuido proporcionalmente entre ambos grupos de edad (Figura 2C). Las métricas de control de calidad transcripcional (número de genes detectados, identificadores moleculares únicos y porcentaje de transcritos mitocondriales), obtenidas tras aplicar el filtrado adaptativo descrito en la metodología, se mantuvieron en umbrales óptimos para ambos grupos (Tabla 1); las visualizaciones y los desgloses de estas métricas técnicas se detallan en el Anexo correspondiente.

::: {#tbl-demografia tbl-colwidths="[12,9,9,14,11,9,9,9,9,9]"}
| Grupo de Edad | Donantes | Células | Edad ± DE (años) | Sexo (F / M) | UMIs (med.) | Genes (med.) | MT (%) | NK CD56dim | NK CD56bright |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Adultos** | 197 | 73,434 | 46.4 ± 7.3 | 102 / 95 | 1,961 | 1,268 | 3.83 | 71,683 (97.6%) | 1,751 (2.4%) |
| **Adultos Mayores** | 226 | 70,557 | 73.5 ± 8.8 | 111 / 115 | 759 | 500 | 3.77 | 69,489 (98.5%) | 1,068 (1.5%) |
| **Total Cohorte** | **423** | **143,991** | — | **213 / 210** | — | — | — | **141,172 (98.0%)** | **2,819 (2.0%)** |

Resumen demográfico y de control de calidad transcriptómico de la cohorte.
:::

## Pureza del Linaje NK y Distribución de Subtipos

El análisis por subtipo se restringió exclusivamente a las dos poblaciones principales del linaje: células NK maduras CD56dim (98.0%, 141,172 células) y células NK inmaduras/secretoras CD56bright (2.0%, 2,819 células) (Tabla 1). Otros subtipos como los linfocitos NKT maduros solamente se estudiaron de manera indirecta a través de los análisis del grupo celular NK general como un conjunto global.

Con el objetivo de corroborar la identidad celular y depurar posibles contaminaciones de otros linajes linfoides, se evaluó la expresión de genes marcadores canónicos derivados de las tablas ASCT+B del Atlas de Referencia Humana (Börner et al., 2021) (*lineage scoring*, ej. *NCAM1*, *FCGR3A*, *NKG7*, *GNLY*, *PRF1*, *KLRB1* para el linaje NK) en contraposición a firmas de células B y T (Figura 3A). La lista completa de genes marcadores empleada para esta validación fenotípica se encuentra disponible en los Anexos.

El análisis topológico del espacio latente demostró que la estructura global del linaje celular NK se mantiene estable e independiente de la edad cronológica (Figura 3B). Sin embargo, la evaluación de las proporciones poblacionales evidenció cambios basales a nivel inter-donante en las subpoblaciones. En particular, la proporción de las células inmaduras CD56bright presentó una variabilidad cuantificable entre adultos y adultos mayores (Figura 3C), sentando las bases fenotípicas previas al análisis de expresión diferencial.

## Abundancia Diferencial del Linaje e Involución del Nicho CD56bright

Para evaluar la dinámica poblacional del nicho inmaduro e inmunomodulador (*NK CD56bright*) frente al compartimento efector citotóxico (*NK CD56dim*) a lo largo del envejecimiento cronológico, se implementó un Modelo Lineal Generalizado (GLM) de familia Binomial ajustado por sobredispersión. El modelo cuantificó la probabilidad de abundancia celular en función de la estratificación por grupo de edad ("Adultos", 34–59 años vs. "Adultos Mayores", $\ge 60$ años).

El modelado binomial determinó una contracción estadísticamente significativa en la probabilidad de abundancia del subconjunto *NK CD56bright* en el grupo de adultos mayores ($p < 0.0001$, coeficiente de edad $\beta = -0.4702$), evidenciando una reducción relativa del 37.51% en comparación con la cohorte de adultos. La razón de probabilidades estimada fue de 0.6249 ($IC_{95\%} = [0.578, 0.675]$) (Figura 4). Dado que las células *CD56bright* constituyen la fuente primaria de citocinas inmunomoduladoras (tales como IFN-$\gamma$ y quimiocinas *XCL1*/*XCL2*) (Cooper et al., 2001; Poli et al., 2009), su declive numérico representa una alteración en el compartimento celular.

## Expresión Diferencial de Alta Confianza (PyDESeq2) y Neutralización del Sesgo Tecnológico

Para evaluar las alteraciones transcripcionales asociadas a la inmunosenescencia neutralizando los artefactos técnicos, se utilizó la paquetería *PyDESeq2* sobre datos agregados por donante (*pseudobulk*). Con el fin de eliminar el sesgo de captura entre químicas de secuenciación (donde tecnologías como 10x 5' v2 introducían sobreestimaciones transcriptómicas de hasta un 55%) y evitar la colinealidad técnica, el análisis se restringió a matrices balanceadas de rango completo ($N = 187$ donantes: 152 adultos vs. 35 adultos mayores, 62,553 células). Al aplicar la contracción de tasas de cambio logarítmico mediante el algoritmo `apeGLM`, se aisló la varianza transcripcional pura.

Bajo un umbral estricto de Tasa de Descubrimiento Falso ($padj < 0.05$), se aisló una firma transcripcional limpia constituida por 23 genes regulados diferencialmente de alta confianza (Figura 5 y Tabla 2).

::: {#tbl-degs-23 tbl-colwidths="[12,12,12,14,50]"}
| Gen | $Log_2\text{FC}$ | $p$-valor | FDR ($padj$) | Función Biológica y Linaje |
|:---|:---:|:---:|:---:|:---|
| *IL7R* | -1.0416 | 0.0000 | 0.0003 | Receptor de supervivencia y homeostasis inmadura (*CD56bright*) |
| *NKG7* | +0.8175 | 0.0001 | 0.0163 | Regulador de degranulación citotóxica efectora |
| *KLRB1* | -0.9161 | 0.0001 | 0.0163 | Receptor CD161, coestimulador y coinhibidor madurativo |
| *GZMA* | +0.9419 | 0.0003 | 0.0381 | Granzima A, serina proteasa citolítica pro-apoptótica |
| *TRAC* | -1.1398 | 0.0004 | 0.0381 | Cadena constante del receptor T (marcador negativo de pureza) |
| *GZMH* | +0.7063 | 0.0004 | 0.0381 | Granzima H, proteasa citotóxica lítica |
| *HLA-DRB1* | -1.0776 | 0.0004 | 0.0381 | Molécula de histocompatibilidad MHC clase II |
| *KLRG1* | +0.7583 | 0.0004 | 0.0381 | Marcador de diferenciación terminal y senescencia efectora |
| *XCL1* | -1.0967 | 0.0005 | 0.0401 | Quimiocina quimioatrayente de células dendríticas cDC1 |
| *XCL2* | -1.0827 | 0.0005 | 0.0401 | Quimiocina paráloga reclutadora de células cDC1 |
| *S100A9* | -1.6169 | 0.0006 | 0.0460 | Alarmina proinflamatoria y moduladora de estrés celular |

Genes expresados diferencialmente de alta confianza (FDR < 0.05) representativos en la cohorte de células NK, aislando la colinealidad técnica.
:::

Entre los hallazgos transcripcionales, se observó la represión coordinada del receptor de interleucina-7 (*IL7R*, $LFC = -1.0416$, $padj = 0.0003$) y de la lectina *KLRB1* ($LFC = -0.9161$, $padj = 0.0163$) en la subpoblación *CD56bright*. Asimismo, se evidenció una subexpresión significativa de las quimiocinas *XCL1* ($LFC = -1.0967$, $padj = 0.0401$) y *XCL2* ($LFC = -1.0827$, $padj = 0.0401$), moléculas responsables del reclutamiento de células dendríticas convencionales de tipo 1 (*cDC1*) (Böttcher et al., 2018). Adicionalmente, tras depurar el sesgo de lote, se confirmó la represión genuina de la alarmina *S100A9* ($LFC = -1.6169$, $padj = 0.0460$), descartando el artefacto previo de hiperinflamación global.

En contraste, se detectó la sobreexpresión de proteasas citotóxicas como *GZMA* ($LFC = +0.9419$, $padj = 0.0381$) y *GZMH* ($LFC = +0.7063$, $padj = 0.0381$), junto con el regulador *NKG7* ($LFC = +0.8175$, $padj = 0.0163$) y el marcador de diferenciación terminal *KLRG1* ($LFC = +0.7583$, $padj = 0.0381$), indicando una acumulación de estos transcritos efectores en las células *CD56dim*.

## Enriquecimiento de Vías Transcriptómicas y Modulación Fenotípica (GSEA / ORA)

Para evaluar las alteraciones funcionales a nivel de vías y redes génicas, se ejecutó el Análisis de Enriquecimiento por Conjuntos de Genes (*GSEA Preranked*) utilizando los estadísticos de Wald derivados del modelado en *pseudobulk* frente a colecciones canónicas (MSigDB Hallmark, KEGG, GO Biological Process, Reactome) estratificando por subpoblación celular (*NK CD56bright* vs. *NK CD56dim*) (Figuras 6 y 7). Cabe destacar que las tablas completas con la totalidad de los resultados del análisis GSEA se encuentran disponibles para su consulta en los anexos correspondientes.

::: {#tbl-vias-gsea tbl-colwidths="[14,14,24,9,9,10,20]"}
| Subpoblación | Categoría | Colección y Vía Transcripcional | NES | $p$-valor | FDR ($q$) | Genes Clave de Núcleo (*Core Enrichment*) |
|:---|:---|:---|:---:|:---:|:---:|:---|
| **CD56bright** | Metabolismo | Oxidative Phosphorylation (KEGG) | -1.698 | 0.0010 | 0.1147 | *NDUFA6*, *NDUFS8*, *COX5B*, *UQCRFS1*, *SDHC*, *NDUFB8* |
| **CD56bright** | Metabolismo | Respiratory Electron Transport (Reactome) | -1.623 | 0.0016 | 0.2277 | *NDUFA6*, *NDUFS8*, *COX7B*, *UQCRFS1*, *NDUFC2*, *COX5B* |
| **CD56bright** | Señalización | PI3K / AKT / mTOR Signaling (Hallmark) | -1.504 | 0.0100 | 0.1488 | *AKT1*, *GRK2*, *RAC1*, *SLC2A1*, *MAPK9*, *PRKAG1* |
| **CD56dim** | Genotóxico | UV Response Dn (Hallmark) | +1.782 | 0.0010 | 0.0087 | *ATRX*, *SYNE1*, *PIK3CD*, *CDKN1B*, *FYN*, *CITED2*, *NIPBL* |
| **CD56dim** | Procesamiento | Reg. of mRNA Splicing via Spliceosome (GO:BP) | -2.160 | 0.0010 | 0.0660 | *U2AF1*, *MAGOH*, *SRSF5*, *HNRNPA1*, *SRSF2*, *SF3B1* |
| **CD56dim** | Ciclo Celular | Myc Targets V1 (Hallmark) | +1.625 | 0.0010 | 0.0366 | *G3BP1*, *KPNB1*, *XPO1*, *ODC1*, *PSMD1*, *DUT*, *NPM1* |
| **CD56dim** | Telómeros | Reg. of Telomere Maintenance (GO:BP) | +1.913 | 0.0010 | 0.1912 | *XRCC5*, *TNIP1*, *PRKCQ*, *TCP1*, *CCT3*, *NEK7*, *ATM* |

Vías transcripcionales enriquecidas representativas por categoría biológica en las subpoblaciones NK CD56bright y CD56dim.
:::

El análisis de enriquecimiento detectó los siguientes patrones funcionales por subtipo:

1. **Supresión del Metabolismo Mitocondrial en Células NK CD56bright:** En el subtipo inmaduro *CD56bright*, se observó una subregulación de vías asociadas a la cadena de transporte de electrones y fosforilación oxidativa (`KEGG_Oxidative_phosphorylation`, $NES = -1.698$, $FDR = 0.1147$; `Reactome_Respiratory_Electron_Transport`, $NES = -1.623$, $FDR = 0.2277$).
2. **Respuesta al Daño y Procesamiento de ARN en Células NK CD56dim:** En el subtipo maduro *CD56dim*, se identificó un enriquecimiento de señales de respuesta a daño genotóxico (`MSigDB_Hallmark_UV_Response_Dn`, $NES = +1.782$, $FDR = 0.0087$). Simultáneamente, se detectó la represión de mecanismos asociados al espliceosoma y maduración de ARNm (`GO_Positive_Regulation_Of_mRNA_Splicing_Via_Spliceosome`, $NES = -2.160$, $FDR = 0.0660$; `KEGG_Spliceosome`, $NES = -1.624$, $FDR = 0.1841$), impulsada por genes núcleo como *SRSF2*, *SRSF5*, *U2AF1* y *HNRNPA1*.

Ambos perfiles de enriquecimiento se ilustran gráficamente en el panel comparativo (Figuras 6 y 7). Estas figuras permiten visualizar la direccionalidad de la expresión de las vías transcripcionales por subtipo celular para identificar si concuerdan o se comportan de manera diferente. Asimismo, el panel detalla los genes que componen cada vía, lo que facilita observar si dichos genes actúan de forma exclusiva en un subtipo o si se comparten entre ambas poblaciones.

Adicionalmente, se realizó una evaluación ortogonal para contrastar el perfil transcripcional NK contra firmas establecidas de Senescencia Secretora (SASP) y Agotamiento Inmune (Tabla 4).

::: {#tbl-sasp-exhaustion tbl-colwidths="[14,22,9,10,10,18,17]"}
| Subpoblación | Firma Especializada | NES | $p$-valor | FDR ($q$) | Genes Relevantes (*Core Enrichment*) | Estado de Significancia |
|:---|:---|:---:|:---:|:---:|:---|:---|
| **CD56bright** | SASP (Reactome) | +1.503 | 0.0242 | 0.3168 | *H1-4*, *H1-3*, *CABIN1*, *UBN1*, *H1-2* | No significativo ($FDR > 0.25$) |
| **CD56dim** | SASP (Reactome) | +1.281 | 0.1844 | 0.1836 | *H1-2*, *H1-3*, *H1-4*, *ASF1A*, *TP53*, *HMGA1* | Tendencia ($FDR = 0.18$) |
| **CD56dim** | Exhausted vs Memory CD8+ T Cell (GSE9650) | +1.331 | 0.0310 | 0.2455 | *XRCC5*, *ETS1*, *PIK3CD*, *TOB1*, *KLRC1*, *IL7R* | Tendencia ($FDR = 0.24$) |

Evaluación de firmas ortogonales especializadas de senescencia secretora (SASP) y agotamiento inmune por subpoblación NK.
:::

La evaluación no detectó significancia estadística fuerte ($FDR < 0.05$) para las firmas de agotamiento inmune clásico en el compartimento celular estudiado.

