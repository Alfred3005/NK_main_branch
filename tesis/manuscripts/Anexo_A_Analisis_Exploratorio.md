# Anexo A: Análisis exploratorio inicial y diagnóstico metodológico {#sec-anexo-a}

El presente anexo compila los registros técnicos, las matrices metodológicas de control de calidad y las referencias analíticas que sustentan la depuración bioinformática y la delimitación fenotípica del atlas transcriptómico presentado en el cuerpo principal de la tesis.

---

## Procedencia de muestras y validación de linaje

### Catálogo de estudios primarios integrados

La construcción de la cohorte analítica se llevó a cabo a partir de la plataforma *CZ CELLxGENE Census* (`census_version="2023-12-15"`). A partir del universo de datos primarios en tejido sanguíneo periférico provenientes de individuos sanos, se identificaron 14 estudios independientes iniciales. Tras la aplicación de los criterios de inclusión etarios ($\ge 34$ años) y los filtros adaptativos de calidad celular, 13 estudios aportaron células a la cohorte depurada final de 143,991 células Natural Killer (@tbl-anexo-estudios).

| No. | Primer Autor / Consorcio | Año | Revista | Título del Estudio / Colección | DOI | Células NK Aportadas |
|:---:|:---|:---:|:---|:---|:---|:---:|
| 1 | Kock et al. (AIDA Consortium) | 2025 | *Cell* | Asian Immune Diversity Atlas (AIDA) | [10.1016/j.cell.2025.02.017](https://doi.org/10.1016/j.cell.2025.02.017) | 59,560 |
| 2 | Yazar et al. | 2022 | *Science* | Single-cell eQTL mapping identifies cell type specific genetic control of autoimmune disease | [10.1126/science.abf3041](https://doi.org/10.1126/science.abf3041) | 57,030 |
| 3 | Perez et al. | 2022 | *Science* | Single-cell RNA-seq reveals the cell-type-specific molecular and genetic associations to lupus | [10.1126/science.abf1970](https://doi.org/10.1126/science.abf1970) | 9,133 |
| 4 | Liu et al. | 2021 | *Cell* | Time-resolved Systems Immunology Reveals a Late Juncture Linked to Fatal COVID-19 | [10.1016/j.cell.2021.02.018](https://doi.org/10.1016/j.cell.2021.02.018) | 4,406 |
| 5 | Wilk et al. | 2020 | *Nat Med* | Single-cell atlas of peripheral immune response to SARS-CoV-2 infection | [10.1038/s41591-020-0944-y](https://doi.org/10.1038/s41591-020-0944-y) | 3,058 |
| 6 | Stephenson et al. | 2021 | *Nat Med* | Single-cell multi-omics analysis of the immune response in COVID-19 | [10.1038/s41591-021-01329-2](https://doi.org/10.1038/s41591-021-01329-2) | 2,354 |
| 7 | Ren et al. | 2021 | *Cell* | COVID-19 immune features revealed by a large-scale single-cell transcriptome atlas | [10.1016/j.cell.2021.01.053](https://doi.org/10.1016/j.cell.2021.01.053) | 2,299 |
| 8 | The Tabula Sapiens Consortium | 2022 | *Science* | The Tabula Sapiens: A multiple-organ, single-cell transcriptomic atlas of humans | [10.1126/science.abl4896](https://doi.org/10.1126/science.abl4896) | 1,457 |
| 9 | Heimlich et al. | 2023 | *Blood Adv* | Multiomic Profiling of Human Clonal Hematopoiesis Reveals Genotype and Cell-Specific Inflammatory Pathway Activation | [10.1182/bloodadvances.2023011445](https://doi.org/10.1182/bloodadvances.2023011445) | 1,327 |
| 10 | Lee et al. | 2020 | *Sci Immunol* | Immunophenotyping of COVID-19 and influenza highlights the role of type I interferons in development of severe COVID-19 | [10.1126/sciimmunol.abd1554](https://doi.org/10.1126/sciimmunol.abd1554) | 1,311 |
| 11 | Rodríguez-Ubreva et al. | 2022 | *Nat Commun* | Single-cell Atlas of common variable immunodeficiency shows germinal center-associated epigenetic dysregulation in B-cell responses | [10.1038/s41467-022-29450-x](https://doi.org/10.1038/s41467-022-29450-x) | 1,135 |
| 12 | Jin et al. | 2021 | *iScience* | A Web Portal and Workbench for Biological Dissection of Single Cell COVID-19 Host Responses | [10.1016/j.isci.2021.103115](https://doi.org/10.1016/j.isci.2021.103115) | 622 |
| 13 | Travaglini et al. | 2020 | *Nature* | A molecular cell atlas of the human lung from single cell RNA sequencing | [10.1038/s41586-020-2922-4](https://doi.org/10.1038/s41586-020-2922-4) | 299 |
| **Total** | | | | | | **143,991** |

: Estudios independientes primarios integrados desde CZ CELLxGENE Discover. {#tbl-anexo-estudios}

*Nota.* Fuente: CZ CELLxGENE Census (versión 2023-12-15).

### Marcadores de validación fenotípica y pureza de linaje (ASCT+B)

Para validar la pureza de la población celular y favorecer la exclusión de dobletes heterotípicos o contaminaciones procedentes de linajes vecinos (células T y células B), se aplicó una estrategia de evaluación basada en la tabla de referencia estandarizada **ASCT+B** del *Human Reference Atlas* (Börner et al., 2021) (@tbl-anexo-marcadores).

| Linaje Celular | Criterio de Selección | Marcador Génico | Nombre Canónico / Función Biológica |
|:---|:---:|:---|:---|
| **Natural Killer (NK)** | **Inclusión** | *NCAM1* | CD56; marcador de adhesión y estadio madurativo |
| | | *FCGR3A* | CD16; receptor de Fc$\gamma$ de baja afinidad (ADCC) |
| | | *NKG7* | Proteína de gránulos citotóxicos |
| | | *GNLY* | Granulisina; péptido antimicrobiano y citolítico |
| | | *PRF1* | Perforina 1; formación de poros de membrana |
| | | *GZMA* | Granzima A; serina proteasa citotóxica |
| | | *GZMB* | Granzima B; inductor de apoptosis |
| | | *CST7* | Cistatina F; regulador de catepsinas y gránulos líticos |
| | | *KLRB1* | CD161; receptor tipo lectina C |
| | | *KLRD1* | CD94; subunidad de heterodímero HLA-E |
| | | *KLRF1* | NKp80; receptor activador de citotoxicidad |
| **Linfocitos T** | **Exclusión** | *CD3D* | Complejo CD3 (cadena $\delta$ del receptor TCR) |
| | | *CD3E* | Complejo CD3 (cadena $\epsilon$ del receptor TCR) |
| | | *CD3G* | Complejo CD3 (cadena $\gamma$ del receptor TCR) |
| | | *TRAC* | Región constante de la cadena alfa del TCR |
| | | *TRBC1* | Región constante 1 de la cadena beta del TCR |
| **Linfocitos B** | **Exclusión** | *CD19* | Correceptor canónico pan-linaje B |
| | | *MS4A1* | CD20; diferenciación de células B maduras |
| | | *CD79A* | Ig-alfa; subunidad de transducción del receptor BCR |
| | | *MZB1* | Proteína de zona marginal y diferenciación plasmática |

: Marcadores de validación de pureza de linaje celular basados en el estándar ASCT+B. {#tbl-anexo-marcadores}

*Nota.* Basado en las tablas ASCT+B (Börner et al., 2021).

---

## Diagnóstico de bimodalidad y sesgos técnicos por ensayo

Durante el procesamiento de control de calidad adaptativo (*ddqc*), se detectó una distribución marcadamente bimodal en el número de genes detectados por célula (`n_genes`). El análisis estratificado evidenció que dicha dispersión no obedecía a divergencias biológicas, sino a un sesgo tecnológico severo condicionado por la química de captura (tecnologías 10x Genomics 3' v2 frente a 10x 3' v3), donde los transcritos ribosomales (*RPS*, *RPL*) y las inmunoglobulinas residuales actuaban como los principales inductores del artefacto.

La documentación pormenorizada de este diagnóstico, incluyendo los gráficos de densidad, las particiones de varianza y la justificación del filtrado declarativo que depuró la matriz final, se encuentra consolidada en la **Sección 1.B** (*Control de Calidad, Bimodalidad y Sesgo Técnico*) del reporte metodológico maestro anexo:
* `Reporte_Integrativo_Subtipos_Abundancia_V2.html` (disponible en el repositorio del proyecto).

---

## Corrección probabilística del ARN ambiental (scAR)

La aplicación del algoritmo `scAR` modificó de forma sustancial la interpretación del envejecimiento de las células NK. En las fases iniciales del proyecto, las muestras provenientes de individuos de edad avanzada exhibían una aparente sobrerrepresentación de mediadores proinflamatorios (*CXCL8*, *IL1B*, *SERPINA1*). La modelización probabilística del ARN ambiental libre en solución reveló que estas moléculas correspondían a ruido de fondo derivado de la lisis sistémica de linajes mieloides circundantes, y no a transcripción autónoma de las células NK.

Los perfiles comparativos de expresión antes y después de scAR, la eliminación de firmas eritroides espurias (*HBA1*) y la cuantificación del ruido ambiental se detallan ampliamente en la **Sección 1.A** (*Corrección de ARN ambiental scAR*) del documento:
* `Reporte_Integrativo_Subtipos_Abundancia_V2.html`.

---

## Tablas de enriquecimiento funcional (GSEA y ORA)

Las tablas completas con el desglose exhaustivo de los conjuntos génicos evaluados mediante GSEA Preranked frente a las bases moleculares MSigDB Hallmark, KEGG, Reactome y GO Biological Process (incluyendo los tamaños de los conjuntos, los estadísticos de rango continuo de Wald, los valores de enriquecimiento normalizado NES y los umbrales FDR ajustados para ambas subpoblaciones), así como las matrices de contingencia del análisis de sobrerrepresentación (ORA) ejecutado sobre la firma de 23 genes diferencialmente expresados (destacando las vías de quimiotaxis asociadas a *XCL1*, *XCL2* y *S100A9*), se encuentran compiladas íntegramente en el repositorio analítico (`results/subtypes/gsea_ora_master_results.md`) y en las secciones finales del *Reporte Integrativo V2*.

