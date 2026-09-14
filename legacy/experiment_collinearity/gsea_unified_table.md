# Tablas Unificadas GSEA por Subpoblación (FDR < 0.25) - Experiment Collinearity Strict

> **Modelo Depurado:** Los datos en esta tabla reflejan la corrida inmaculada usando exclusivamente el Estadístico de Wald, tras filtrar ensayos desbalanceados por colinealidad (~ assay + age_group estricto).

> **Guía Visual:** Los valores con significancia estadística sólida (**FDR < 0.05**) se marcan en **negrita**. El color <span style='color:red'>rojo</span> indica inducción (NES > 0) y el <span style='color:blue'>azul</span> represión (NES < 0).

## GLOBAL GSEA Results

### Inflamación y Respuesta Inmune

| Collection | Term | NES | NOM p-val | FDR q-val |
|:-----------|:-----|:----|:----------|:----------|
| MSigDB_Hallmark_2020 | **<span style="color:blue">TNF-alpha Signaling via NF-kB</span>** | **<span style="color:blue">-2.333</span>** | **0.0010** | **0.0010** |
| MSigDB_Hallmark_2020 | <span style="color:blue">Inflammatory Response</span> | <span style="color:blue">-1.486</span> | 0.0189 | 0.0566 |
| MSigDB_Hallmark_2020 | <span style="color:blue">IL-2/STAT5 Signaling</span> | <span style="color:blue">-1.376</span> | 0.0010 | 0.0979 |
| KEGG_2021_Human | <span style="color:blue">Viral protein interaction with cytokine and cytokine receptor</span> | <span style="color:blue">-1.751</span> | 0.0133 | 0.1020 |
| MSigDB_Hallmark_2020 | <span style="color:blue">IL-6/JAK/STAT3 Signaling</span> | <span style="color:blue">-1.292</span> | 0.0536 | 0.1348 |
| KEGG_2021_Human | <span style="color:blue">Antigen processing and presentation</span> | <span style="color:blue">-1.619</span> | 0.0010 | 0.1517 |
| KEGG_2021_Human | <span style="color:blue">Graft-versus-host disease</span> | <span style="color:blue">-1.544</span> | 0.0202 | 0.1763 |
| GO_Biological_Process_2023 | <span style="color:blue">Positive Regulation Of T Cell Cytokine Production (GO:0002726)</span> | <span style="color:blue">-1.842</span> | 0.0070 | 0.2067 |
| GO_Biological_Process_2023 | <span style="color:blue">Regulation Of Type II Interferon Production (GO:0032649)</span> | <span style="color:blue">-1.806</span> | 0.0010 | 0.2332 |

### Metabolismo y Bioenergética

| Collection | Term | NES | NOM p-val | FDR q-val |
|:-----------|:-----|:----|:----------|:----------|
| KEGG_2021_Human | <span style="color:blue">Oxidative phosphorylation</span> | <span style="color:blue">-1.484</span> | 0.0010 | 0.2345 |

### Muerte Celular y Estrés

| Collection | Term | NES | NOM p-val | FDR q-val |
|:-----------|:-----|:----|:----------|:----------|
| MSigDB_Hallmark_2020 | <span style="color:blue">Apoptosis</span> | <span style="color:blue">-1.222</span> | 0.0244 | 0.1968 |
| GO_Biological_Process_2023 | <span style="color:blue">Regulation Of Necroptotic Process (GO:0060544)</span> | <span style="color:blue">-1.854</span> | 0.0085 | 0.2273 |

### Ciclo Celular y Genética

| Collection | Term | NES | NOM p-val | FDR q-val |
|:-----------|:-----|:----|:----------|:----------|
| GO_Biological_Process_2023 | <span style="color:blue">Positive Regulation Of mRNA Splicing, Via Spliceosome (GO:0048026)</span> | <span style="color:blue">-2.160</span> | 0.0010 | 0.0660 |
| MSigDB_Hallmark_2020 | <span style="color:blue">Myc Targets V1</span> | <span style="color:blue">-1.313</span> | 0.0435 | 0.1313 |
| KEGG_2021_Human | <span style="color:blue">Spliceosome</span> | <span style="color:blue">-1.624</span> | 0.0010 | 0.1841 |

### Otros / Estructural

| Collection | Term | NES | NOM p-val | FDR q-val |
|:-----------|:-----|:----|:----------|:----------|
| MSigDB_Hallmark_2020 | **<span style="color:blue">Apical Surface</span>** | **<span style="color:blue">-1.774</span>** | **0.0080** | **0.0189** |
| MSigDB_Hallmark_2020 | **<span style="color:blue">Estrogen Response Late</span>** | **<span style="color:blue">-1.640</span>** | **0.0154** | **0.0294** |
| MSigDB_Hallmark_2020 | <span style="color:blue">Estrogen Response Early</span> | <span style="color:blue">-1.436</span> | 0.0010 | 0.0747 |
| KEGG_2021_Human | <span style="color:blue">Hematopoietic cell lineage</span> | <span style="color:blue">-1.803</span> | 0.0061 | 0.1047 |
| GO_Biological_Process_2023 | <span style="color:red">Actomyosin Structure Organization (GO:0031032)</span> | <span style="color:red">1.857</span> | 0.0010 | 0.1337 |
| KEGG_2021_Human | <span style="color:blue">Legionellosis</span> | <span style="color:blue">-1.585</span> | 0.0079 | 0.1606 |
| KEGG_2021_Human | <span style="color:blue">Protein export</span> | <span style="color:blue">-1.817</span> | 0.0010 | 0.1896 |
| MSigDB_Hallmark_2020 | <span style="color:blue">KRAS Signaling Up</span> | <span style="color:blue">-1.207</span> | 0.0602 | 0.1972 |
| GO_Biological_Process_2023 | <span style="color:red">Protein Secretion (GO:0009306)</span> | <span style="color:red">1.873</span> | 0.0010 | 0.2043 |
| Reactome_2022 | <span style="color:blue">Immunoregulatory Interactions Between A Lymphoid And A non-Lymphoid Cell R-HSA-198933</span> | <span style="color:blue">-1.961</span> | 0.0010 | 0.2092 |

## CD56DIM GSEA Results

### Inflamación y Respuesta Inmune

| Collection | Term | NES | NOM p-val | FDR q-val |
|:-----------|:-----|:----|:----------|:----------|
| MSigDB_Hallmark_2020 | **<span style="color:blue">TNF-alpha Signaling via NF-kB</span>** | **<span style="color:blue">-1.784</span>** | **0.0010** | **0.0177** |
| GO_Biological_Process_2023 | **<span style="color:red">Regulation Of Lymphocyte Differentiation (GO:0045619)</span>** | **<span style="color:red">2.131</span>** | **0.0010** | **0.0252** |
| KEGG_2021_Human | <span style="color:blue">Non-alcoholic fatty liver disease</span> | <span style="color:blue">-1.823</span> | 0.0010 | 0.0882 |
| KEGG_2021_Human | <span style="color:blue">Chemokine signaling pathway</span> | <span style="color:blue">-1.535</span> | 0.0081 | 0.1772 |
| Specialized | <span style="color:red">custom_senescence_signatures.gmt__REACTOME_SASP</span> | <span style="color:red">1.281</span> | 0.1844 | 0.1836 |
| KEGG_2021_Human | <span style="color:blue">Huntington disease</span> | <span style="color:blue">-1.554</span> | 0.0015 | 0.1845 |
| KEGG_2021_Human | <span style="color:blue">Alzheimer disease</span> | <span style="color:blue">-1.542</span> | 0.0010 | 0.1889 |
| KEGG_2021_Human | <span style="color:blue">Parkinson disease</span> | <span style="color:blue">-1.500</span> | 0.0047 | 0.2025 |
| KEGG_2021_Human | <span style="color:blue">Vibrio cholerae infection</span> | <span style="color:blue">-1.477</span> | 0.0493 | 0.2122 |
| GO_Biological_Process_2023 | <span style="color:red">Receptor Signaling Pathway Via JAK-STAT (GO:0007259)</span> | <span style="color:red">1.749</span> | 0.0021 | 0.2239 |
| Reactome_2022 | <span style="color:blue">Antigen Presentation: Folding, Assembly, Peptide Loading Of Class I MHC R-HSA-983170</span> | <span style="color:blue">-1.619</span> | 0.0160 | 0.2280 |
| GO_Biological_Process_2023 | <span style="color:red">Receptor Signaling Pathway Via STAT (GO:0097696)</span> | <span style="color:red">1.763</span> | 0.0044 | 0.2307 |

### Metabolismo y Bioenergética

| Collection | Term | NES | NOM p-val | FDR q-val |
|:-----------|:-----|:----|:----------|:----------|
| GO_Biological_Process_2023 | <span style="color:blue">Regulation Of Peptidyl-Threonine Phosphorylation (GO:0010799)</span> | <span style="color:blue">-2.045</span> | 0.0010 | 0.0977 |
| KEGG_2021_Human | <span style="color:blue">Oxidative phosphorylation</span> | <span style="color:blue">-1.698</span> | 0.0010 | 0.1147 |
| MSigDB_Hallmark_2020 | <span style="color:blue">PI3K/AKT/mTOR  Signaling</span> | <span style="color:blue">-1.504</span> | 0.0100 | 0.1488 |
| MSigDB_Hallmark_2020 | <span style="color:red">Glycolysis</span> | <span style="color:red">1.295</span> | 0.0505 | 0.2146 |
| Reactome_2022 | <span style="color:blue">Respiratory Electron Transport, ATP Synthesis By Chemiosmotic Coupling, Heat Production By Uncoupling Proteins R-HSA-163200</span> | <span style="color:blue">-1.623</span> | 0.0016 | 0.2277 |
| Reactome_2022 | <span style="color:blue">Mitochondrial Protein Import R-HSA-1268020</span> | <span style="color:blue">-1.654</span> | 0.0034 | 0.2423 |

### Muerte Celular y Estrés

| Collection | Term | NES | NOM p-val | FDR q-val |
|:-----------|:-----|:----|:----------|:----------|
| MSigDB_Hallmark_2020 | **<span style="color:red">UV Response Dn</span>** | **<span style="color:red">1.834</span>** | **0.0010** | **0.0116** |
| Specialized | <span style="color:red">custom_senescence_signatures.gmt__GSE9650_EXHAUSTED_VS_MEMORY_CD8_TCELL_DN</span> | <span style="color:red">1.331</span> | 0.0310 | 0.2455 |

### Ciclo Celular y Genética

| Collection | Term | NES | NOM p-val | FDR q-val |
|:-----------|:-----|:----|:----------|:----------|
| MSigDB_Hallmark_2020 | **<span style="color:red">Myc Targets V1</span>** | **<span style="color:red">1.625</span>** | **0.0010** | **0.0366** |
| KEGG_2021_Human | <span style="color:blue">Spliceosome</span> | <span style="color:blue">-1.708</span> | 0.0010 | 0.1253 |
| GO_Biological_Process_2023 | <span style="color:red">Positive Regulation Of Telomere Maintenance Via Telomerase (GO:0032212)</span> | <span style="color:red">1.913</span> | 0.0010 | 0.1912 |
| GO_Biological_Process_2023 | <span style="color:red">Positive Regulation Of Telomere Maintenance Via Telomere Lengthening (GO:1904358)</span> | <span style="color:red">1.867</span> | 0.0010 | 0.1940 |
| GO_Biological_Process_2023 | <span style="color:blue">Regulation Of mRNA Splicing, Via Spliceosome (GO:0048024)</span> | <span style="color:blue">-1.876</span> | 0.0010 | 0.1964 |
| MSigDB_Hallmark_2020 | <span style="color:red">E2F Targets</span> | <span style="color:red">1.324</span> | 0.0305 | 0.2169 |
| GO_Biological_Process_2023 | <span style="color:red">Positive Regulation Of Transcription By RNA Polymerase III (GO:0045945)</span> | <span style="color:red">1.775</span> | 0.0067 | 0.2251 |
| Reactome_2022 | <span style="color:blue">mRNA Splicing - Major Pathway R-HSA-72163</span> | <span style="color:blue">-1.695</span> | 0.0010 | 0.2359 |
| GO_Biological_Process_2023 | <span style="color:red">Regulation Of Telomerase RNA Localization To Cajal Body (GO:1904872)</span> | <span style="color:red">1.727</span> | 0.0064 | 0.2371 |
| Reactome_2022 | <span style="color:blue">mRNA Splicing R-HSA-72172</span> | <span style="color:blue">-1.673</span> | 0.0010 | 0.2405 |
| GO_Biological_Process_2023 | <span style="color:red">Positive Regulation Of Telomerase Activity (GO:0051973)</span> | <span style="color:red">1.790</span> | 0.0023 | 0.2411 |
| Reactome_2022 | <span style="color:blue">SRP-dependent Cotranslational Protein Targeting To Membrane R-HSA-1799339</span> | <span style="color:blue">-1.860</span> | 0.0017 | 0.2443 |
| GO_Biological_Process_2023 | <span style="color:red">Regulation Of Telomerase Activity (GO:0051972)</span> | <span style="color:red">1.716</span> | 0.0163 | 0.2467 |

### Otros / Estructural

| Collection | Term | NES | NOM p-val | FDR q-val |
|:-----------|:-----|:----|:----------|:----------|
| MSigDB_Hallmark_2020 | **<span style="color:blue">Epithelial Mesenchymal Transition</span>** | **<span style="color:blue">-1.726</span>** | **0.0017** | **0.0221** |
| Specialized | <span style="color:blue">Reactome_2022__Sema3A PAK Dependent Axon Repulsion R-HSA-399954</span> | <span style="color:blue">-1.966</span> | 0.0010 | 0.0898 |
| Reactome_2022 | <span style="color:blue">RHO GTPases Activate PAKs R-HSA-5627123</span> | <span style="color:blue">-1.971</span> | 0.0010 | 0.0966 |
| KEGG_2021_Human | <span style="color:blue">Retrograde endocannabinoid signaling</span> | <span style="color:blue">-1.876</span> | 0.0010 | 0.0971 |
| KEGG_2021_Human | <span style="color:blue">Parathyroid hormone synthesis, secretion and action</span> | <span style="color:blue">-1.681</span> | 0.0017 | 0.1066 |
| KEGG_2021_Human | <span style="color:blue">Long-term depression</span> | <span style="color:blue">-1.691</span> | 0.0089 | 0.1083 |
| KEGG_2021_Human | <span style="color:blue">GnRH signaling pathway</span> | <span style="color:blue">-1.661</span> | 0.0037 | 0.1156 |
| KEGG_2021_Human | <span style="color:blue">Morphine addiction</span> | <span style="color:blue">-1.718</span> | 0.0053 | 0.1379 |
| KEGG_2021_Human | <span style="color:blue">Circadian entrainment</span> | <span style="color:blue">-1.743</span> | 0.0070 | 0.1467 |
| KEGG_2021_Human | <span style="color:blue">Protein export</span> | <span style="color:blue">-1.622</span> | 0.0175 | 0.1503 |
| MSigDB_Hallmark_2020 | <span style="color:red">Apical Junction</span> | <span style="color:red">1.408</span> | 0.0459 | 0.1536 |
| KEGG_2021_Human | <span style="color:blue">Melanogenesis</span> | <span style="color:blue">-1.601</span> | 0.0123 | 0.1634 |
| Specialized | <span style="color:blue">Reactome_2022__RHO GTPases Activate PAKs R-HSA-5627123</span> | <span style="color:blue">-1.971</span> | 0.0010 | 0.1650 |
| KEGG_2021_Human | <span style="color:blue">Diabetic cardiomyopathy</span> | <span style="color:blue">-1.568</span> | 0.0016 | 0.1738 |
| KEGG_2021_Human | <span style="color:blue">Gastric acid secretion</span> | <span style="color:blue">-1.531</span> | 0.0372 | 0.1746 |
| KEGG_2021_Human | <span style="color:blue">Glycosylphosphatidylinositol (GPI)-anchor biosynthesis</span> | <span style="color:blue">-1.576</span> | 0.0320 | 0.1756 |
| KEGG_2021_Human | <span style="color:blue">Adherens junction</span> | <span style="color:blue">-1.541</span> | 0.0165 | 0.1795 |
| KEGG_2021_Human | <span style="color:blue">Insulin signaling pathway</span> | <span style="color:blue">-1.582</span> | 0.0078 | 0.1798 |
| GO_Biological_Process_2023 | <span style="color:red">Positive Regulation Of Erythrocyte Differentiation (GO:0045648)</span> | <span style="color:red">1.839</span> | 0.0022 | 0.1914 |
| KEGG_2021_Human | <span style="color:blue">Pathways of neurodegeneration</span> | <span style="color:blue">-1.492</span> | 0.0014 | 0.1975 |
| Reactome_2022 | <span style="color:blue">Semaphorin Interactions R-HSA-373755</span> | <span style="color:blue">-1.798</span> | 0.0010 | 0.2008 |
| KEGG_2021_Human | <span style="color:blue">Apelin signaling pathway</span> | <span style="color:blue">-1.495</span> | 0.0229 | 0.2021 |
| GO_Biological_Process_2023 | <span style="color:red">Positive Regulation Of DNA Biosynthetic Process (GO:2000573)</span> | <span style="color:red">1.847</span> | 0.0010 | 0.2056 |
| KEGG_2021_Human | <span style="color:blue">Thermogenesis</span> | <span style="color:blue">-1.503</span> | 0.0016 | 0.2085 |
| GO_Biological_Process_2023 | <span style="color:red">Establishment Of Protein Localization To Extracellular Region (GO:0035592)</span> | <span style="color:red">1.761</span> | 0.0136 | 0.2173 |
| Reactome_2022 | <span style="color:blue">NR1H2 And NR1H3-mediated Signaling R-HSA-9024446</span> | <span style="color:blue">-1.632</span> | 0.0144 | 0.2183 |
| Reactome_2022 | <span style="color:blue">Signaling By FGFR R-HSA-190236</span> | <span style="color:blue">-1.619</span> | 0.0085 | 0.2202 |
| Reactome_2022 | <span style="color:blue">Extracellular Matrix Organization R-HSA-1474244</span> | <span style="color:blue">-1.614</span> | 0.0066 | 0.2209 |
| GO_Biological_Process_2023 | <span style="color:red">Regulation Of Organelle Organization (GO:0033043)</span> | <span style="color:red">1.788</span> | 0.0010 | 0.2215 |
| KEGG_2021_Human | <span style="color:blue">mRNA surveillance pathway</span> | <span style="color:blue">-1.441</span> | 0.0249 | 0.2227 |
| Reactome_2022 | <span style="color:blue">Signaling By FGFR3 R-HSA-5654741</span> | <span style="color:blue">-1.632</span> | 0.0163 | 0.2269 |
| GO_Biological_Process_2023 | <span style="color:blue">Regulation Of Cardiac Muscle Contraction (GO:0055117)</span> | <span style="color:blue">-1.884</span> | 0.0019 | 0.2271 |
| KEGG_2021_Human | <span style="color:blue">Neurotrophin signaling pathway</span> | <span style="color:blue">-1.443</span> | 0.0240 | 0.2275 |
| GO_Biological_Process_2023 | <span style="color:red">Positive Regulation Of Establishment Of Protein Localization (GO:1904951)</span> | <span style="color:red">1.873</span> | 0.0021 | 0.2278 |
| Reactome_2022 | <span style="color:blue">Formation Of HIV-1 Elongation Complex Containing HIV-1 Tat R-HSA-167200</span> | <span style="color:blue">-1.644</span> | 0.0083 | 0.2310 |
| Reactome_2022 | <span style="color:blue">FGFR2 Mutant Receptor Activation R-HSA-1839126</span> | <span style="color:blue">-1.648</span> | 0.0142 | 0.2314 |
| Reactome_2022 | <span style="color:blue">Signaling By FGFR2 IIIa TM R-HSA-8851708</span> | <span style="color:blue">-1.648</span> | 0.0142 | 0.2314 |
| KEGG_2021_Human | <span style="color:blue">Cytosolic DNA-sensing pathway</span> | <span style="color:blue">-1.445</span> | 0.0415 | 0.2320 |
| KEGG_2021_Human | <span style="color:blue">Glycosaminoglycan biosynthesis</span> | <span style="color:blue">-1.430</span> | 0.0606 | 0.2334 |
| Reactome_2022 | <span style="color:blue">RHOJ GTPase Cycle R-HSA-9013409</span> | <span style="color:blue">-1.633</span> | 0.0051 | 0.2337 |
| Reactome_2022 | <span style="color:blue">Complex I Biogenesis R-HSA-6799198</span> | <span style="color:blue">-1.669</span> | 0.0034 | 0.2341 |
| GO_Biological_Process_2023 | <span style="color:red">Positive Regulation Of Myeloid Cell Differentiation (GO:0045639)</span> | <span style="color:red">1.736</span> | 0.0022 | 0.2349 |
| Reactome_2022 | <span style="color:blue">Collagen Formation R-HSA-1474290</span> | <span style="color:blue">-1.703</span> | 0.0129 | 0.2357 |
| KEGG_2021_Human | <span style="color:blue">Vascular smooth muscle contraction</span> | <span style="color:blue">-1.446</span> | 0.0287 | 0.2387 |
| Reactome_2022 | <span style="color:blue">VEGFR2 Mediated Vascular Permeability R-HSA-5218920</span> | <span style="color:blue">-1.635</span> | 0.0130 | 0.2394 |
| KEGG_2021_Human | <span style="color:blue">Vasopressin-regulated water reabsorption</span> | <span style="color:blue">-1.455</span> | 0.0402 | 0.2395 |
| Reactome_2022 | <span style="color:blue">mRNA 3-End Processing R-HSA-72187</span> | <span style="color:blue">-1.801</span> | 0.0010 | 0.2429 |
| KEGG_2021_Human | <span style="color:blue">Olfactory transduction</span> | <span style="color:blue">-1.447</span> | 0.0605 | 0.2446 |

## CD56BRIGHT GSEA Results

### Inflamación y Respuesta Inmune

| Collection | Term | NES | NOM p-val | FDR q-val |
|:-----------|:-----|:----|:----------|:----------|
| Specialized | <span style="color:red">custom_senescence_signatures.gmt__REACTOME_SASP</span> | <span style="color:red">1.513</span> | 0.0196 | 0.0743 |
| KEGG_2021_Human | <span style="color:blue">Huntington disease</span> | <span style="color:blue">-1.688</span> | 0.0010 | 0.0816 |
| KEGG_2021_Human | <span style="color:blue">Parkinson disease</span> | <span style="color:blue">-1.526</span> | 0.0010 | 0.1421 |
| KEGG_2021_Human | <span style="color:blue">Non-alcoholic fatty liver disease</span> | <span style="color:blue">-1.453</span> | 0.0010 | 0.1635 |
| KEGG_2021_Human | <span style="color:blue">Neutrophil extracellular trap formation</span> | <span style="color:blue">-1.342</span> | 0.0610 | 0.1967 |
| KEGG_2021_Human | <span style="color:blue">Vibrio cholerae infection</span> | <span style="color:blue">-1.291</span> | 0.1317 | 0.2244 |
| KEGG_2021_Human | <span style="color:blue">Bacterial invasion of epithelial cells</span> | <span style="color:blue">-1.261</span> | 0.1210 | 0.2307 |
| KEGG_2021_Human | <span style="color:blue">Alzheimer disease</span> | <span style="color:blue">-1.265</span> | 0.0010 | 0.2402 |

### Metabolismo y Bioenergética

| Collection | Term | NES | NOM p-val | FDR q-val |
|:-----------|:-----|:----|:----------|:----------|
| KEGG_2021_Human | <span style="color:blue">Oxidative phosphorylation</span> | <span style="color:blue">-1.742</span> | 0.0010 | 0.0778 |
| MSigDB_Hallmark_2020 | <span style="color:blue">Oxidative Phosphorylation</span> | <span style="color:blue">-1.463</span> | 0.0010 | 0.1637 |
| GO_Biological_Process_2023 | <span style="color:blue">Mitochondrial Respiratory Chain Complex I Assembly (GO:0032981)</span> | <span style="color:blue">-1.521</span> | 0.0171 | 0.1821 |
| GO_Biological_Process_2023 | <span style="color:blue">Mitochondrial ATP Synthesis Coupled Electron Transport (GO:0042775)</span> | <span style="color:blue">-1.555</span> | 0.0010 | 0.2098 |
| GO_Biological_Process_2023 | <span style="color:blue">Mitochondrial Electron Transport, NADH To Ubiquinone (GO:0006120)</span> | <span style="color:blue">-1.532</span> | 0.0379 | 0.2113 |
| GO_Biological_Process_2023 | <span style="color:blue">Aerobic Electron Transport Chain (GO:0019646)</span> | <span style="color:blue">-1.567</span> | 0.0010 | 0.2281 |

### Muerte Celular y Estrés

| Collection | Term | NES | NOM p-val | FDR q-val |
|:-----------|:-----|:----|:----------|:----------|
| MSigDB_Hallmark_2020 | **<span style="color:red">UV Response Dn</span>** | **<span style="color:red">1.781</span>** | **0.0010** | **0.0087** |
| MSigDB_Hallmark_2020 | <span style="color:blue">Reactive Oxygen Species Pathway</span> | <span style="color:blue">-1.562</span> | 0.0280 | 0.1508 |
| KEGG_2021_Human | <span style="color:blue">Amyotrophic lateral sclerosis</span> | <span style="color:blue">-1.469</span> | 0.0010 | 0.1702 |

### Ciclo Celular y Genética

| Collection | Term | NES | NOM p-val | FDR q-val |
|:-----------|:-----|:----|:----------|:----------|
| MSigDB_Hallmark_2020 | <span style="color:blue">DNA Repair</span> | <span style="color:blue">-1.377</span> | 0.0488 | 0.1798 |

### Otros / Estructural

| Collection | Term | NES | NOM p-val | FDR q-val |
|:-----------|:-----|:----|:----------|:----------|
| KEGG_2021_Human | <span style="color:blue">Cytosolic DNA-sensing pathway</span> | <span style="color:blue">-1.949</span> | 0.0010 | 0.0689 |
| KEGG_2021_Human | <span style="color:blue">Thermogenesis</span> | <span style="color:blue">-1.746</span> | 0.0010 | 0.1037 |
| KEGG_2021_Human | <span style="color:blue">Cardiac muscle contraction</span> | <span style="color:blue">-1.792</span> | 0.0010 | 0.1250 |
| KEGG_2021_Human | <span style="color:blue">Lysosome</span> | <span style="color:blue">-1.537</span> | 0.0258 | 0.1530 |
| KEGG_2021_Human | <span style="color:blue">Pertussis</span> | <span style="color:blue">-1.446</span> | 0.0855 | 0.1545 |
| KEGG_2021_Human | <span style="color:blue">Adherens junction</span> | <span style="color:blue">-1.418</span> | 0.0774 | 0.1628 |
| GO_Biological_Process_2023 | <span style="color:blue">Cell-Matrix Adhesion (GO:0007160)</span> | <span style="color:blue">-1.509</span> | 0.0633 | 0.1752 |
| GO_Biological_Process_2023 | <span style="color:blue">NADH Dehydrogenase Complex Assembly (GO:0010257)</span> | <span style="color:blue">-1.521</span> | 0.0171 | 0.1821 |
| GO_Biological_Process_2023 | <span style="color:blue">Regulation Of Actin Cytoskeleton Organization (GO:0032956)</span> | <span style="color:blue">-1.487</span> | 0.0503 | 0.1826 |
| KEGG_2021_Human | <span style="color:blue">Retrograde endocannabinoid signaling</span> | <span style="color:blue">-1.368</span> | 0.0471 | 0.1955 |
| KEGG_2021_Human | <span style="color:blue">Diabetic cardiomyopathy</span> | <span style="color:blue">-1.351</span> | 0.0385 | 0.1989 |
| GO_Biological_Process_2023 | <span style="color:blue">Response To UV (GO:0009411)</span> | <span style="color:blue">-1.645</span> | 0.0296 | 0.2097 |
| KEGG_2021_Human | <span style="color:blue">Phagosome</span> | <span style="color:blue">-1.315</span> | 0.0690 | 0.2129 |

