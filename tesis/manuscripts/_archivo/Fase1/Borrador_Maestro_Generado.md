# ![](data:image/jpeg;base64...)![](data:image/jpeg;base64...)

![UNAM](data:image/jpeg;base64...)

**UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO**

**POSGRADO EN CIENCIAS BIOLÓGICAS**

FACULTAD DE MEDICINA

BIOMEDICINA

**Análisis transcriptómico de células asesinas naturales en el contexto de la inmunosenescencia**

**TESIS**

QUE PARA OPTAR POR EL GRADO DE:

**MAESTRO(A) EN CIENCIAS BIOLÓGICAS**

PRESENTA:

**ALFREDO MORALES SALAZAR**

**TUTOR(A) PRINCIPAL DE TESIS: DRA. YALBI ITZEL BALDERAS MARTÍNEZ**

**INSTITUTO NACIONAL DE ENFERMEDADES RESPIRATORIAS ISMAEL COSÍO VILLEGAS**

**COMITÉ TUTOR: DRA. MARIEL SOFÍA MALDONADO BONILLA**

**INSTITUTO NACIONAL DE ENFERMEDADES RESPIRATORIAS ISMAEL COSÍO VILLEGAS**

**DR. JESÚS ESPINAL ENRIQUEZ**

**INSTITUTO NACIONAL DE MEDICINA GENÓMICA**

# **CIUDAD UNIVERSITARIA, CD. MX., ABRIL DE 2026**

#

## AGRADECIMIENTOS

**Al Posgrado en Ciencias Biológicas de la Universidad Nacional Autónoma de México (UNAM)**, por brindarme la oportunidad de realizar mis estudios de maestría y por el apoyo académico recibido durante mi formación.

**Al Consejo Nacional de Humanidades, Ciencias y Tecnologías (CONAHCYT)** que ha pasado a ser **la Secretaría de Ciencia, Humanidades, Tecnología e Innovación (SECIHTI)**, por el apoyo económico otorgado para la realización de mis estudios a través de la Beca Nacional (Tradicional) 2023-1, con número de solicitud **2023-000002-01NACF-06265** y CVU **1272954**. Asimismo, se agradece el financiamiento otorgado a través del proyecto de **Ciencia de Frontera con clave CF-2023-I-1653**, el cual fue fundamental para el desarrollo de esta investigación.

**Al Instituto Nacional de Enfermedades Respiratorias "Ismael Cosío Villegas" (INER)**, por las facilidades otorgadas para la realización de mi estancia de investigación y el desarrollo de esta tesis. De manera especial, agradezco al **Laboratorio de Bioinformática y Biología Computacional (LABBIC)** por el entorno científico proporcionado. Se reconoce el apoyo del Comité de Investigación y del Comité de Ética en Investigación del INER por la aprobación del protocolo con código de asignación **B10-24**, titulado: "Generación de redes de regulación de factores de transcripción y miRNAs asociados al envejecimiento a partir de la integración de datos de secuenciación de transcriptomas de células individuales".

**Al Laboratorio de Cómputo de Alto Rendimiento (LCAR)** de la Coordinación del Departamento de Matemáticas de la Facultad de Ciencias, UNAM, y a **Miguel Ángel Pérez León**, por el soporte técnico especializado y el acceso a los recursos computacionales. Se agradece también al **Laboratorio Nacional de Soluciones Biomiméticas para Diagnóstico y Terapia (LaNSBioDyT)**, Facultad de Ciencias, UNAM, por el apoyo en infraestructura tecnológica.

**A Wellcome Connecting Science (WCS)**, por la beca otorgada para participar en el curso "Single Cell Genomic Approaches to Study the Immune System" en Medellín, Colombia. El apoyo en hospedaje y alimentación, así como la formación recibida, fueron piezas clave para los análisis bioinformáticos de este trabajo.

**A mi tutora principal, la Dra. Yalbi Itzel Balderas Martínez**, por su guía académica, su confianza y por la oportunidad de colaborar en sus proyectos de investigación. A mi **Comité Tutoral, el Dr. Jesús Espinal Enriquez y la Dra. Mariel Sofía Maldonado Bonilla**, por sus valiosas observaciones y el seguimiento constante a este proyecto.

#

#

# Índices

## 1.1 Índice de capítulos

[**1. Índices 5**](#_fxwtyhbbvg1t)

[1.1 Índice de capítulos 5](#_uo7eosj2oduy)

[1.2 Índice de figuras 7](#_o8kyh7s3erfh)

[● Tabla S2. Genes inflamatorios y proteostasis: modelos y breakpoints……………………………77 8](#_og2i6fy5u9pd)

[● Tabla S3. Comparación de cambios transcriptómicos entre subtipos de NK……………………..78 8](#_4rc45jmsw53l)

[**2. Resumen 9**](#_3hgf2v5ygbpu)

[**3. Summary 10**](#_tsrx7u75p7n7)

[**4. Introducción 10**](#_kvl1iky584br)

[**5. Pregunta de Investigación y Objetivos 12**](#_ybyn1bktw04x)

[5.1 Pregunta de Investigación 12](#_ks5w5iwdjkz2)

[5.2 Hipótesis Principal 12](#_pgnyqyy78uhg)

[5.3 Objetivo General 12](#_es0enllo2xnw)

[5.4 Objetivos Específicos 12](#_wuuf4btpfhlm)

[**6. Marco Teórico 12**](#_5nw1ooofro4z)

[6.1 Propósito, alcance y delimitación del marco teórico 12](#_xqobi25wv613)

[6.2 Conceptos del Envejecimiento relevantes 13](#_zhwvwqkzduar)

[ 13](#_6k825dlwwf9g)

[Los Pilares del Envejecimiento como marco conceptual 13](#_tkynz4j3t2nw)

[Pilares primarios: Causas del daño celular 14](#_nb1zmx6ydy29)

[Pérdida de la proteostasis 14](#_cpvz1ofytu9a)

[Pilares antagónicos: Respuestas compensatorias al daño 15](#_cipsodrz2gj2)

[Disfunción mitocondrial y estrés oxidativo 15](#_xgeshk5magzx)

[Senescencia celular 15](#_f4hynhe69gek)

[Pilares integrativos: Consecuencias sistémicas del envejecimiento 15](#_z1tsj1ckpuch)

[Inflammaging: inflamación crónica de bajo grado 15](#_66av6qsptf7u)

[6.3 El sistema inmune y su papel durante el envejecimiento 16](#_g0vz38n6uxne)

[Descripción general del sistema inmune y sus componentes clave 16](#_a81no6e28g77)

[Cambios relacionados con la edad en el sistema inmune 17](#_ekfigdkrt3ix)

[Alteraciones en las respuestas inmunes innatas y adaptativas 18](#_s0x6p1627zpf)

[Inflamación crónica de bajo grado: inflammaging 18](#_o7ymi0tlemlc)

[6.4 Células Natural Killer y su relación con la senescencia 19](#_8gpz7priyb6o)

[ 19](#_ii0b54hz75wz)

[Papel de las células NK en la eliminación de células senescentes 19](#_xyzzn8lselp8)

[Poblaciones de células NK y sus roles específicos 20](#_h1w4ip9x9y18)

[Cambios fenotípicos y funcionales 21](#_660g4sug1r75)

[6.5. Secuenciación de RNA de célula única en células NK durante el envejecimiento 22](#_rb5qxl9s7qat)

[La secuenciación de RNA de célula única y el estudio del envejecimiento de las células inmunes 23](#_28qxjxytwcih)

[**7. Metodología 24**](#_8fpxj1toz7k0)

[7.1 Recolección y preprocesamiento de datos 24](#_bxs9m7ymt0sy)

[Estratificación por grupos de edad 24](#_zfp5fswn6fux)

[Identificación de las poblaciones de células NK 24](#_w8oninxuvdpc)

[7.2 Control de calidad 25](#_t5vke06162jo)

[Detección y eliminación de células dobletes 25](#_jfxk8qu2m0hr)

[Métricas de calidad celular 25](#_39ooyyksdjfj)

[7.3 Normalización y Escalado 25](#_qiuvnw69yxfn)

[7.4 Comprobación de los marcadores canónicos para tipos celulares 26](#_5e3g3n1d1vvf)

[7.5 Integración de Datos 26](#_yofqtvdyk5wj)

[Arquitectura del modelo scVI 26](#_be60m8i3j57f)

[Integración Refinada con scANVI 26](#_6neexikvchjd)

[7.6 Análisis de Expresión Diferencial 27](#_lnvxbw95hxng)

[Diseño del Análisis 27](#_v3fqjihzoyo2)

[Parámetros del análisis 27](#_2ns8l1km9d1n)

[7.7 Análisis de patrones temporales 28](#_89x52sbwetvz)

[7.8 Análisis de Enriquecimiento Funcional 28](#_dj79b6vmx0o3)

[**8. Resultados 29**](#_5bmx3onfsy3t)

[8.1 Recolección de datos 29](#_by7x8ux1i82a)

[8.2 Análisis descriptivos 29](#_mp5sg7dcn7wl)

[Frecuencia y distribución de subtipos de células NK 31](#_avwp291xq21g)

[8.3 Validación de Tipos Celulares 31](#_jbdi3ewmaeik)

[Expresión de marcadores NK canónicos 31](#_nq8alfvmxp7e)

[Evaluación de contaminación celular 32](#_jzqcwddzraz)

[8.4 Integración de datos y reducción de efectos batch 32](#_usq9mg7szqmo)

[8.5 Análisis de expresión diferencial 34](#_sy7slb7ncybz)

[Análisis de expresión diferencial entre células NK 34](#_ibhcoxy8o3ho)

[Sub-expresión de genes: declive de la inmunovigilancia 36](#_sdor5n6ngku1)

[Sobre-expresión de genes: Inflamación sostenida 37](#_nctpkpvqpqrg)

[8.6 Patrones temporales de Expresión Génica Durante el Envejecimiento 38](#_s9w3ltrgvv1s)

[Tabla 4. Análisis de patrones temporales y modelos de trayectoria 39](#_10nftblxvver)

[Genes Inflamatorios y de Proteostasis 41](#_ta6jnklga3hr)

[Inmunoglobulinas y Declive de la Respuesta Adaptativa 41](#_yifxy6ge6n79)

[Validación y Robustez de Resultados 41](#_q4757f743sj8)

[8.7 Análisis de patrones de expresión génica en subtipos de células NK durante el envejecimiento 41](#_rqqu1z72y1pe)

[8.8 Perfil Transcripcional de Células NK Envejecidas 43](#_x7p7edkwnpku)

[Tabla 1. Perfil de sobre-expresión génica diferencial en células NK envejecidas 44](#_xla8i39bh3ym)

[Tabla 2. Perfil de sub-expresión génica diferencial en células NK envejecidas 46](#_qqubnowa21az)

[Tabla 3. Enriquecimiento funcional y regulación transcripcional 48](#_yw0a0e84zl13)

[**9. Discusión 51**](#_mm5pg52rdwrk)

[9.1 Marcadores Moleculares del Envejecimiento de Células NK 51](#_u0i1xamn238w)

[*SERPINA1*: Marcador más prominente 51](#_iodz7inxifvz)

[Mediadores inflamatorios como panel coordinado 52](#_gbv8aovqvwsc)

[*CST3* un biomarcador local y sistémico convergente 52](#_hbkle0hfz02n)

[Validación como biomarcadores de envejecimiento 52](#_drzzw5pmwrsj)

[9.2 Pérdida de Componentes de Reconocimiento Molecular 53](#_wm26lelcqjqt)

[Validación de pureza y autenticidad del hallazgo 53](#_6wbovvg6g4k6)

[Pérdida de la vigilancia 53](#_lu8ws3nyf237)

[9.3 Modelos Integrativos del Envejecimiento de NK 54](#_jf8u4b22l4yu)

[Modelo I: El Ciclo Oxidativo-Inflamatorio 54](#_6sydq09nepw3)

[Modelo II: Posible papel del zinc en la inmunosenescencia de células NK 56](#_7vnh4f9zz8vm)

[9.4 De vigilantes a promotores de inflamación 58](#_ccdfg8lk3gc8)

[9.5 Implicaciones Biomédicas y Direcciones Futuras 59](#_rp7oq9fgwl5k)

[Potencial terapéutico: múltiples niveles de intervención 59](#_bbm6cdotvnj5)

[Hacia la medicina personalizada del envejecimiento 60](#_qehmvg5er2sa)

[9.7 Fortalezas del estudio 60](#_t9c4vp5njqxm)

[9.8 Limitaciones 61](#_kweac0dl89ds)

[9.9 Conclusiones 61](#_6l0g3vs7hmhz)

[9.10 Perspectivas 61](#_cpdruimkrdct)

[Declaración de uso de la IA 62](#_551a4x27t6f1)

[**11. Bibliografía 63**](#_wjeoopzhs6rm)

[**12. Figuras Suplementarias 73**](#_ccsg0ovlu5v3)

[Tabla S1. Genes con correlaciones significativas con edad (top 10 positivas y negativas) 73](#_ntkzerwqk5s)

[Tabla S2. Genes inflamatorios y proteostasis: modelos y breakpoints 74](#_euqla15o21mz)

[Tabla S3. Comparación de cambios transcriptómicos entre subtipos de NK 75](#_v5s5nyj926fe)

## 1.2 Índice de figuras

|  |
| --- |
| * **Figura 1.** Pilares (*hallmarks*) del envejecimiento………………………………………………….. 14 * **Figura 2.** Distribución de grupos de edad, frecuencias de subtipos celulares y validación de clasificación mediante marcadores canónicos. ………………………………………………….….31 * **Figura 3.** Evaluación de la integración de datos (scIB) y proyección de tipos celulares en espacio latente (UMAP). ……………………………………………………………………………………..….34 * **Figura 4.** Distribución de la muestra por grupos de edad y estudio de procedencia en proyección dimensional. ………………………………………………………………………………………….....37 * **Figura 5.** Perfil transcripcional diferencial (*heatmap*) en células NK ordenado por cronología. 38 * **Figura 6.** Dinámicas de expresión de genes sobre-regulados (*up-regulated*) durante el envejecimiento. …………………………………………………………………………………………39 * **Tabla 4.** Análisis de patrones temporales y modelos de trayectoria………………………………41 * **Figura 7.** Descenso progresivo en la expresión de segmentos variables de inmunoglobulinas asociados a la edad. …………………………………..………………………………………………..43 * **Figura 8.** Proporción de modelos matemáticos (lineales y cuadráticos) óptimos para la descripción de genes diferencialmente expresados. ……………………………………………….45 * **Tabla 1.** Perfil de expresión génica diferencial en células NK envejecidas por módulos funcionales. ………………………………………………………………………………………..…… 48 * **Tabla 2.** Genes subexpresados relacionados con la pérdida de componentes de reconocimiento molecular. ………………………………………………………………………………………..….….. 49 * **Tabla 3.** Enriquecimiento funcional y reguladores transcripcionales identificados en la inmunosenescencia de NK. ………………………………………………………………..…….…… 51 * **Figura 9.** Modelo integrativo del ciclo oxidativo-inflamatorio auto-perpetuante en células NK envejecidas. ……………………………………………………………………..………………………58 * **Figura 10.** Representación del mecanismo del zinc y su impacto en el control transcripcional de la inflamación. ………………………………………………………………………..…………..……..60 * **Tabla S1.** Genes con correlaciones significativas con edad (top 10 positivas y negativas)........78  Tabla S2. Genes inflamatorios y proteostasis: modelos y breakpoints……………………………79Tabla S3. Comparación de cambios transcriptómicos entre subtipos de NK……………………..80 |

Análisis transcriptómico de células asesinas naturales en el contexto de la inmunosenescencia.

# Resumen

El envejecimiento causa un deterioro gradual de la función del sistema inmunológico, llamado inmunosenescencia, que incluye la disfunción de las células asesinas naturales (NK). Estas células son esenciales para la vigilancia inmunitaria y la eliminación de células senescentes. Aunque tienen un papel clave, todavía no se entiende bien por qué dejan de funcionar correctamente con la edad, especialmente según sus distintos subtipos celulares. En este estudio se analizó cómo cambian las células NK en términos de expresión durante el envejecimiento en adultos, mediante un análisis bioinformático a gran escala. Se recopilaron y analizaron datos de secuenciación de RNA de célula única de 14 estudios transversales, lo que permitió crear un mapa de 193,701 células de donantes sanos, divididas en adultos (34-60 años, n=384) y adultos mayores (>60 años, n=118).

Al combinar modelos de inferencia variacional (scVI/scANVI) y análisis de expresión diferencial (pseudo-bulk), se identificó una firma molecular de 83 genes con cambios significativos (∣log2​FC∣>1,padj​<0.05). Los resultados muestran una activación coordinada de programas proinflamatorios y de respuesta al estrés celular, con mayor expresión de quimiocinas CXC (*CXCL8*, *CXCL2*), citoquinas (*IL1B*, *IL6*) y mediadores de la proteostasis como *SERPINA1* y *CST3*. También se observó una disminución progresiva en la expresión de componentes de reconocimiento molecular, especialmente en segmentos variables de inmunoglobulinas (*IGLV2-8*, *IGHV3-23*), lo que sugiere una reducción del repertorio de receptores y una menor vigilancia inmunológica. El análisis por subtipos mostró que las células NK CD56 dim son el principal motor de esta transición, con trayectorias de expresión cuadráticas que indican una aceleración del deterioro en etapas avanzadas de la vida.

Se propone un modelo en el que las células NK dejan de ser vigilantes inmunológicos y pasan a promover activamente la inflamación debido a una hiperactivación disfuncional. Este estado se mantiene por un ciclo continuo de oxidación e inflamación, con mayor producción de especies reactivas de oxígeno (*DUOX1*) y un posible secuestro de zinc dentro de la célula, lo que afecta los mecanismos antiinflamatorios después de la transcripción. Los resultados identifican a *SERPINA1* como un biomarcador clave de la inmunosenescencia y sugieren que restaurar la función de las células NK, ya sea mediante la modulación de las vías NF-κB o con suplementos de zinc, podría ser una estrategia prometedora para reducir el impacto del envejecimiento en el sistema inmunitario.

**Palabras clave:** envejecimiento, células asesinas naturales, células Natural Killer, NK, transcriptómica de célula única, *inflammaging*, biomarcadores, inmunosenescencia.

# Summary

As people age, their immune system weakens, a process known as immunosenescence, which includes problems with natural killer (NK) cells. NK cells play a key role in immune defense and removing old cells. However, it is still unclear why these cells lose function with age, especially among different subtypes. In this study, we examined how NK cells change as adults get older by analyzing large-scale genetic data. We combined single-cell RNA sequencing data from 14 studies, creating a dataset of 193,701 cells from healthy donors, divided into adults (34-60 years, n=384) and older adults (>60 years, n=118).

Using advanced statistical models and gene expression analysis, we found 83 genes that changed significantly with age (∣log2​FC∣>1, padj​<0.05). The data showed that pro-inflammatory and stress response genes were more active, including higher levels of CXC chemokines (*CXCL8*, *CXCL2*), cytokines (*IL1B*, *IL6*), and proteins like *SERPINA1* and *CST3*. At the same time, there was a steady drop in genes involved in recognizing threats, especially certain immunoglobulin segments (*IGLV2-8*, *IGHV3-23*), which may mean the immune system's ability to detect problems is reduced. Further analysis showed that CD56 dim NK cells are mainly responsible for these changes, with their gene expression patterns declining faster in later life.

We suggest that as NK cells age, they move from protecting the body to promoting inflammation because they become overactive in a dysfunctional way. This ongoing state is driven by a cycle of oxidation and inflammation, with more reactive oxygen species (*DUOX1*) and possible zinc being trapped inside cells, which weakens anti-inflammatory processes. Our results highlight *SERPINA1* as an important marker of immune aging and suggest that improving NK cell function, either by adjusting NF-κB pathways or by giving targeted zinc supplements, could help reduce the effects of aging on the immune system.

**Keywords:** aging, Natural Killer cells, NK, single-cell transcriptomics, inflammaging, biomarkers, immunosenescence.

# Introducción

El envejecimiento adulto se define como un proceso biológico progresivo caracterizado por la pérdida gradual de la regulación homeostática del organismo, con cambios moleculares y celulares que se aceleran en las etapas avanzadas de la vida (Del Bosque Plata, 2016). Esta transición marca el paso desde la estabilidad funcional hacia la acumulación progresiva de disfunciones, resultando en un período prolongado de morbilidad (Keheler, 2021) y convirtiéndose en un factor de riesgo primario para numerosas patologías que aparecen predominantemente en la segunda mitad de la vida (Niccoli & Partridge, 2012). Comprender los mecanismos moleculares detrás de esta transición resulta esencial para desarrollar intervenciones que promuevan un envejecimiento saludable.

Antes se creía que el envejecimiento no podía revertirse, pero algunos estudios recientes han cuestionado esta idea. Por ejemplo, la parabiosis heterocrónica es un modelo experimental en el que se conectan dos organismos de diferentes edades para que compartan factores circulantes y ha demostrado que la sangre de individuos jóvenes puede revertir ciertos signos de deterioro en organismos envejecidos (Conboy et al., 2005; Mayack et al., 2011). Estos resultados indican que el envejecimiento puede modificarse mediante factores sistémicos presentes en la sangre. Este descubrimiento sobre la flexibilidad del envejecimiento adulto ha llevado a prestar más atención a los componentes circulantes. En especial, esto nos lleva a comparar el potencial rejuvenecedor del plasma joven con la nueva evidencia sobre terapias celulares adoptivas y sugiere una hipótesis en la que las células NK, que toman el protagonismo como componentes clave del sistema inmune, podrían ser uno de los factores que median o producen estas propiedades rejuvenecedoras.

Esta perspectiva sitúa a las células asesinas naturales (NK) en el centro de interés. Estas células, que constituyen aproximadamente el 5-10% de los linfocitos en sangre periférica (Blum et al., 2007) y pertenecen a la familia de células linfoides innatas del grupo 1 (ILC1) (Zhang et al., 2017), desempeñan funciones que las posicionan como centinelas críticos. Las células NK poseen la capacidad única de reconocer y eliminar células senescentes sin sensibilización previa, mientras coordinan respuestas inmunitarias más amplias mediante la secreción de citocinas como el interferón gamma (IFNγ) y el factor de necrosis tumoral alfa (TNFα) (Paul & Lal, 2017).

El potencial de las células NK para modular el envejecimiento se ha explorado en estudios recientes sobre terapia adoptiva, los cuales refuerzan la conexión con los efectos observados en la parabiosis. A diferencia de los enfoques senolíticos tradicionales, las células NK activadas ex vivo pueden eliminar selectivamente células senescentes acumuladas, con efectos sostenidos tras una sola administración (Chelyapov et al., 2022; Deng & Terunuma, 2024). Estudios preclínicos han demostrado que la infusión de células NK reduce marcadores de senescencia en múltiples órganos y mejora la función cardíaca y cognitiva (Cheng et al., 2020), mientras que ensayos clínicos en poblaciones geriátricas confirman la viabilidad y seguridad de estas estrategias (Björklund et al., 2016).

No obstante, esta capacidad de limpiar las células senescentes de los tejidos se ve comprometida con la edad, donde la vigilancia inmunológica decae progresivamente. Añadido a esto, se han reportado cambios en la proporción de subtipos (CD56 bright/CD56 dim) y modificaciones en perfiles funcionales que se acentúan con la edad (Brauning et al., 2022). A nivel molecular, se identifican biomarcadores de disfunción como el acortamiento telomérico progresivo y la reducción de la actividad telomerasa (Fali et al., 2019), así como cambios en la expresión de receptores específicos como NKp30, NKp46 (Hazeldine et al., 2012) y KLRG1 (Muller-Durovic et al., 2016). Estos cambios sugieren que las células NK transitan de ser vigilantes inmunológicos a un estado disfuncional que podría contribuir activamente a la disminución de la función inmune global.

Para mejorar las terapias con células NK y comprender cómo contribuyen a rejuvenecer la sangre, es importante estudiar los cambios en los genes que activan estas células. Las tecnologías que permiten analizar el RNA de una sola célula han cambiado la forma en que se estudian los procesos biológicos, ya que permiten identificar diferentes tipos de células y seguir sus trayectorias con gran detalle (Tang et al., 2009; Altschuler & Wu, 2010). Esta precisión es clave para investigar lo que ocurre durante el envejecimiento del sistema inmunológico, en el que algunas subpoblaciones pueden seguir caminos de senescencia divergentes.

En este estudio, analizamos datos de secuenciación de RNA de célula única a gran escala para describir los cambios en la expresión génica que acompañan el envejecimiento de las células NK humanas. Al combinar varios conjuntos de datos y emplear métodos computacionales avanzados, buscamos crear un atlas transcriptómico detallado. Este enfoque nos permitirá identificar los cambios clave entre subpoblaciones durante esta transición y encontrar biomarcadores predictivos y posibles objetivos terapéuticos. Queremos entender cómo las células NK modifican su expresión génica durante la inmunosenescencia, pasando de ser células vigilantes inmunológicas que reconocen y coordinan la respuesta inmune a convertirse en promotores activos de la inflamación.

# Marco Teórico

## 6.1 Propósito, alcance y delimitación del marco teórico

Este marco teórico ofrece la base para analizar cómo cambian los genes de las células Natural Killer (NK) a medida que envejecemos mediante scRNA-seq y sitúa el estudio en el contexto de la inmunosenescencia. El trabajo cubre tres temas principales: cómo envejece el sistema inmune, qué son las células NK y cómo cambian con la edad, y cómo se utiliza la scRNA-seq para estudiar estos cambios. El objetivo es analizar los cambios en la expresión de genes de las células NK para identificar patrones que nos permitan seguir estudiando el envejecimiento del sistema inmune.

## 6.2 Conceptos del Envejecimiento relevantes



El envejecimiento es el deterioro progresivo de la integridad fisiológica que ocurre con el paso del tiempo, resultando en una función alterada y mayor vulnerabilidad a la muerte. A nivel molecular, el envejecimiento se caracteriza por la acumulación de alteraciones celulares en múltiples niveles, afectando la integridad del genoma, transcriptoma, epigenoma, proteoma y organelos celulares (López-Otín et al., 2023). Este daño acumulado compromete la homeostasis y función de los tejidos, llevando a las manifestaciones fenotípicas del envejecimiento.

### Los Pilares del Envejecimiento como marco conceptual

López-Otín y sus colegas (2013, 2023) presentaron un marco conceptual para estudiar el envejecimiento, identificando características clave llamadas pilares o "hallmarks". Estos pilares se dividen en tres grupos: (1) pilares primarios, que causan daño celular; (2) pilares antagónicos, que son respuestas compensatorias al daño, útiles al principio, pero dañinas si se mantienen durante mucho tiempo; y (3) pilares integrativos, que aparecen cuando el daño se acumula y las respuestas compensatorias fallan, mostrando efectos sistémicos del envejecimiento (Figura 1). Este marco reúne varios mecanismos moleculares y celulares que se relacionan entre sí durante el proceso de envejecimiento.

|  |
| --- |
| ![](data:image/png;base64...) |
| **Figura 1.** **Pilares (*hallmarks*) del envejecimiento.** Representación esquemática de los mecanismos determinantes del deterioro fisiológico categorizados en pilares primarios, antagónicos e integrativos. Adaptado de López-Otín et al. (2023). |

###

### Pilares primarios: Causas del daño celular

Los pilares primarios son las fuentes iniciales de daño que se acumulan a medida que envejecemos. Dos de estos pilares son especialmente importantes para entender cómo envejecen las células NK.

#### Pérdida de la proteostasis

La proteostasis (homeostasis de proteínas) se refiere a los mecanismos que mantienen la estabilidad del proteoma, incluyendo la síntesis, plegamiento, control de calidad y degradación de proteínas (López-Otín et al., 2013, 2023). Con el envejecimiento, la capacidad de mantener la proteostasis disminuye progresivamente debido al deterioro de sistemas como las chaperonas moleculares, el proteasoma y la autofagia, así como por la acumulación de proteínas mal plegadas y agregados proteicos (Hipp et al., 2019). Un aspecto crítico de la proteostasis es el balance entre proteasas y antiproteasas, que regula la degradación controlada de proteínas y la remodelación de la matriz extracelular. Durante el envejecimiento, este balance se altera significativamente: la actividad de proteasas aumenta debido al SASP y la inflamación crónica, mientras que la expresión de antiproteasas se modifica como respuesta compensatoria (López-Otín & Bond, 2008).

### Pilares antagónicos: Respuestas compensatorias al daño

#### Disfunción mitocondrial y estrés oxidativo

La disfunción mitocondrial representa otro importante marcador crítico, caracterizado por el deterioro progresivo de la función de la cadena de transporte de electrones, disminución en la producción del ATP y el aumento en la generación de especies reactivas de oxígeno (ROS) (López-Otín et al., 2023). Con el envejecimiento, las mitocondrias acumulan daño en su DNA (mtDNA), presentan alteraciones en su dinámica de fusión y fisión, y reducen su eficiencia en la fosforilación oxidativa.

El exceso de especies reactivas de oxígeno (ROS) generado por mitocondrias disfuncionales crea un estado de estrés oxidativo, definido como el desbalance entre la producción de ROS y la capacidad antioxidante celular (Finkel & Holbrook, 2000). Las ROS pueden oxidar componentes celulares críticos como lípidos, proteínas y ácidos nucleicos, perpetuando un ciclo de deterioro celular. Con el envejecimiento, tanto la producción de ROS aumenta como la eficiencia de los sistemas antioxidantes endógenos (superóxido dismutasa, catalasa, glutatión) disminuye, exacerbando el estado de estrés oxidativo crónico (Beckman & Ames, 1998).

#### Senescencia celular

La senescencia celular representa un pilar antagónico, siendo inicialmente una respuesta protectora frente al daño que puede volverse deletérea cuando se acumula con la edad. La senescencia se define como un estado de arresto proliferativo estable acompañado de cambios fenotípicos estereotípicos (Campisi & d'Adda di Fagagna, 2007). Inicialmente la senescencia celular representa una respuesta protectora frente al daño, suprimiendo la oncogénesis y facilitando la reparación tisular. Pero cuando las senescentes se acumulan en tejidos envejecidos y secretan un conjunto de factores inflamatorios, proteasas y otros mediadores, como el SASP (Coppé et al., 2010). La senescencia contribuye al envejecimiento tanto por la pérdida de capacidad regenerativa de los tejidos como por los efectos deletéreos del SASP.

### Pilares integrativos: Consecuencias sistémicas del envejecimiento

#### Inflammaging: inflamación crónica de bajo grado

El inflammaging se define como un estado de inflamación crónica sistémica de bajo grado, estéril (en ausencia de infección evidente) y persistente, que emerge como una alteración prominente en la comunicación intercelular durante el envejecimiento (Franceschi & Campisi, 2014; López-Otín et al., 2023). Este fenotipo proinflamatorio latente resulta de la acumulación multifactorial de daño celular y del fallo en las respuestas homeostáticas compensatorias. Molecularmente, se caracteriza por niveles elevados de citocinas circulantes como IL-6,TNF-α,IL-1β y proteína C reactiva (PCR), factores que contribuyen a la patogénesis de enfermedades cardiovasculares, neurodegenerativas y metabólicas en la segunda mitad de la vida (Franceschi et al., 2018).

Este estado mantiene al sistema inmunitario en una activación prolongada que deriva en un "círculo vicioso": la señalización basal elevada agota los recursos inmunológicos y provoca un agotamiento celular que disminuye la capacidad de respuesta de los leucocitos ante amenazas agudas (Furman et al., 2019). Para romper este ciclo, estrategias como el uso de senolíticos buscan eliminar células senescentes y reducir la carga inflamatoria asociada al Fenotipo Secretor Asociado a la Senescencia (SASP), mostrando resultados prometedores en la mejora de la función inmune y la salud general (Fuentealba et al., 2024).

## 6.3 El sistema inmune y su papel durante el envejecimiento

### Descripción general del sistema inmune y sus componentes clave

El sistema inmunológico es una red compleja de células, tejidos y órganos que trabajan conjuntamente para defender al organismo contra patógenos y sustancias dañinas (López-Otín et al., 2023). Este sistema puede dividirse en dos grandes componentes: el sistema inmune innato y el sistema inmune adaptativo, los cuales actúan de forma coordinada para proporcionar protección contra infecciones, eliminar células dañadas o transformadas, y mantener la homeostasis del organismo (Furman et al., 2019).

El sistema inmune innato constituye la primera línea de defensa y responde de manera rápida e inespecífica a los patógenos y señales de daño. Sus principales componentes incluyen barreras físicas (como la piel y las mucosas), proteínas antimicrobianas, el sistema del complemento, y células especializadas como neutrófilos, monocitos/macrófagos, células dendríticas, células NK y mastocitos. Este sistema reconoce patrones moleculares asociados a patógenos (PAMPs) y patrones moleculares asociados a daño (DAMPs) mediante receptores de reconocimiento de patrones (PRRs), como los receptores tipo Toll (TLRs) (Fuentealba et al., 2024).

El sistema inmune adaptativo responde de forma específica y tiene memoria inmunológica, lo que permite defender al cuerpo de manera más eficaz si se enfrenta varias veces al mismo patógeno. Sus principales componentes son los linfocitos T y B, que poseen receptores muy específicos (TCR y BCR, respectivamente) capaces de reconocer diversos tipos de antígenos (Luo et al., 2022). Las células T se dividen en subpoblaciones, como las células T CD4+ auxiliares (que incluyen Th1, Th2, Th17 y T reguladoras) y las células T CD8+ citotóxicas. Las células B se encargan de producir anticuerpos.

Ambos sistemas inmunes operan a través de una compleja red de comunicación mediada por citocinas, quimiocinas y otros mediadores solubles, que regulan la magnitud y duración de las respuestas inmunitarias. Los órganos linfoides primarios (médula ósea y timo) son responsables de la producción y maduración de células inmunes, mientras que los órganos linfoides secundarios (ganglios linfáticos, bazo y tejidos linfoides asociados a mucosas) facilitan la interacción entre células inmunes y antígenos, promoviendo respuestas inmunitarias efectivas (Furman et al., 2019).

Los cambios asociados al envejecimiento adulto en los sistemas inmunes innatos y adaptativos no ocurren de manera aislada, sino que representan un fenómeno interconectado donde la disfunción de un componente afecta directamente al otro. Por ejemplo, la desregulación en la producción de citoquinas por células de la inmunidad innata como los monocitos durante el envejecimiento influye directamente en la polarización de las células T, favoreciendo perfiles más inflamatorios. Simultáneamente, la acumulación de células T senescentes CD28- genera un ambiente proinflamatorio que altera las funciones de las células presentadoras de antígenos, creando un círculo vicioso que perpetúa la inmunosenescencia durante la transición del envejecimiento adulto (Fülöp et al., 2018).

### Cambios relacionados con la edad en el sistema inmune

A medida que las personas envejecen, su sistema inmunológico se debilita de forma progresiva, lo que se conoce como inmunosenescencia. Esto afecta tanto al sistema inmune innato como al adaptativo y reduce la capacidad del cuerpo para responder a nuevos antígenos y mantener la tolerancia inmunológica en las etapas avanzadas de la vida (Baechle et al., 2023).

Las células NK, componentes del sistema inmune innato, muestran alteraciones funcionales evidentes durante la transición del envejecimiento adulto, incluyendo una citotoxicidad reducida y alteraciones en la producción de citocinas. Aunque los cambios en el número absoluto de células NK varían entre individuos, se observan modificaciones consistentes en la distribución de sus subpoblaciones, con cambios en la proporción de células NK CD56 dim y CD56 bright (subpoblaciones especializadas en citotoxicidad y producción de citocinas, respectivamente) que se acentúan en edades avanzadas (Hazeldine J & Lord JM., 2013). Estudios recientes han documentado que las células NK de individuos en diferentes etapas del envejecimiento adulto pueden presentar fenotipos transcripcionales distintivos y trayectorias de senescencia específicas de subtipo (Luo et al., 2022).

Durante el envejecimiento adulto, los efectos acumulativos de la involución tímica se manifiestan como una disminución progresiva en la generación de células T naive, contrayendo el repertorio inmunológico y limitando la respuesta inmune a nuevos antígenos. Esta contracción del espacio inmunológico se ve reflejada en la reducción de la proporción de células T naive CD4+ y CD8+, mientras aumentan las células T de memoria y, de manera notable en adultos mayores, las células T senescentes CD28- y CD57+, caracterizadas por su proliferación reducida, mayor resistencia a la apoptosis y un fenotipo proinflamatorio (Luo et al., 2022).

Las células B también cambian de forma importante a medida que envejecemos. Se ha visto que la producción de células B naive disminuye, mientras que aumentan las células B de memoria, lo que lleva a un repertorio de anticuerpos más limitado y menos diverso (López-Otín et al., 2023). También se han encontrado células B asociadas a la edad (ABCs), que son un tipo de células B de memoria que expresan T-bet, un factor de transcripción clave en el sistema inmunológico, y están relacionadas con el aumento de enfermedades autoinmunes en personas mayores (Baechle et al., 2023).

La inmunosenescencia es un proceso multifacético que trasciende la mera disminución numérica celular; representa una reconfiguración profunda de la composición, el fenotipo y la función de los linajes innatos y adaptativos. Esta metamorfosis se caracterizada por la contracción del repertorio *naive* (T y B), la acumulación de células senescentes y la redistribución de subpoblaciones de células NK lo cuál genera un sistema cualitativamente distinto al de la juventud, comprometiendo la respuesta a patógenos y la vigilancia contra células transformadas. En consecuencia, el sistema inmune no es solo un reflejo del envejecimiento, sino un objetivo estratégico para intervenciones que busquen mitigar el *inflammaging*. Comprender estos mecanismos subyacentes permite desarrollar estrategias de modulación que, más allá de describir el deterioro, busquen prolongar la salud funcional en la vejez

### Alteraciones en las respuestas inmunes innatas y adaptativas

La inmunosenescencia en adultos mayores afecta la función del sistema inmunitario. En la inmunidad innata, células como los monocitos y los neutrófilos están más activas en reposo, pero responden menos ante nuevos estímulos. Los receptores de reconocimiento de patrones, como los TLRs, cambian su expresión y su señalización, lo que dificulta la detección temprana de patógenos y aumenta la susceptibilidad a infecciones en personas mayores (Baechle et al., 2023).

Durante el envejecimiento, las células dendríticas captan menos antígenos, migran a órganos linfoides y activan células T. Esto conduce a respuestas inmunitarias más bajas ante vacunas y nuevas infecciones en personas mayores (Furman et al., 2019). Las células NK, aunque pueden variar en número, presentan una disminución constante de su citotoxicidad y de la producción de citocinas como el IFN-γ, lo que puede afectar la vigilancia contra tumores y microbios (Luo et al., 2022).

En el sistema inmune adaptativo, el envejecimiento reduce el número de células T naive, lo que limita la respuesta ante nuevos antígenos. Las células T envejecidas presentan problemas en la señalización del TCR, producen menos IL-2, proliferan menos y son más propensas a la apoptosis (Mittelbrunn & Kroemer, 2021). También disminuyen la eficiencia y la afinidad de los anticuerpos, lo que reduce la eficacia de las vacunas en adultos mayores.

Uno de los aspectos más relevantes de la desregulación inmune asociada al envejecimiento adulto es la pérdida de la tolerancia inmunológica, que contribuye al desarrollo de autoinmunidad e inflamación crónica. Este fenómeno se relaciona con alteraciones en la función de células T y B reguladoras y en los mecanismos de tolerancia central y periférica (Fülöp et al., 2018). Aunque las manifestaciones celulares de la inmunosenescencia difieren entre los componentes innatos y adaptativos, sus consecuencias funcionales convergen en patrones similares: tanto la reducción en la diversidad del repertorio de células T como la disminución en la variedad de receptores de reconocimiento de patrones en células mieloides conducen al estrechamiento del rango de patógenos reconocibles, explicando una característica importante de la inmunosenescencia: mayor susceptibilidad a infecciones aunado a una mayor propensión a la inflamación crónica (Furman et al., 2019). Estas alteraciones funcionales en los sistemas inmunes innato y adaptativo no solo comprometen la capacidad defensiva del organismo, sino que también crean las condiciones para un estado inflamatorio sistémico persistente.

## 6.4 Células Natural Killer y su relación con la senescencia



Las células *Natural Killer* (NK) son linfocitos granulares grandes que forman parte del sistema inmune innato. Se consideran la primera línea de defensa contra células infectadas por virus y células tumorales (Cerwenka & Lanier, 2001). Las células NK se originan a partir de progenitores linfoides comunes en la médula ósea y maduran en tejidos linfoides secundarios. Su función principal es la citotoxicidad directa contra células diana sin necesidad de sensibilización previa, a diferencia de los linfocitos T citotóxicos del sistema inmune adaptativo (Paul & Lal, 2017).

Las células NK defienden al organismo mediante mecanismos de citotoxicidad directa, como la liberación de gránulos de perforina y granzimas, o la interacción con ligandos de muerte celular (Abel et al., 2018). También pueden eliminar células mediante procesos dependientes de anticuerpos. Además, participan en la respuesta inmune al secretar citocinas inmunomoduladoras como IFN-γ y TNF-α. Estas funciones citotóxicas y reguladoras son esenciales para la vigilancia celular. En la siguiente sección se explicará con más detalle cómo las células NK identifican y eliminan células senescentes.

### Papel de las células NK en la eliminación de células senescentes

Además de su función conocida en la defensa contra virus y tumores, estudios recientes muestran que las células NK participan en la vigilancia y eliminación de células senescentes (Antonangeli et al, 2019). Estas células se acumulan con la edad y contribuyen a las enfermedades asociadas al envejecimiento mediante la secreción de factores proinflamatorios (Childs et al., 2015).

La eliminación de células senescentes por las células NK depende del reconocimiento de señales de estrés y, una vez fijado un blanco por este medio, se destruyen las células objetivo y se activa la respuesta inmunitaria. El proceso comienza cuando las células NK reconocen ligandos de estrés en la superficie de las células senescentes. Estas células cambian su perfil y aumentan la presencia de moléculas como MICA/B, que son ligandos del receptor NKG2D, y CD155, que interactúa con el receptor DNAM-1 (Soriani et al., 2009). Esta combinación de señales indica que la célula debe ser eliminada, lo que la vuelve más vulnerable al ataque del sistema inmunitario. Cuando las señales activadoras superan a las inhibidoras, las células NK inician la destrucción directa de la célula senescente. Se ha demostrado que las células NK eliminan principalmente mediante la liberación de gránulos citotóxicos, como perforina y granzimas, lo que provoca la muerte celular por apoptosis (Ovadya et al., 2018). Además de eliminar células de forma directa, las células NK también producen citocinas y quimiocinas tras activarse. Estas sustancias, como IFN-γ y TNF-α, ayudan a atraer y activar otros tipos de células inmunitarias, como los macrófagos y los linfocitos T citotóxicos. Así, el sistema inmunitario no solo elimina las células dañadas, sino que también mantiene la vigilancia y el equilibrio en los tejidos (Peterson et al., 2021).

Varios estudios in vitro y en modelos animales han demostrado la capacidad de las células NK para eliminar activamente la senescencia celular (Sagiv et al., 2016). Por ejemplo, su depleción en ratones conduce a la acumulación de estas células en los tejidos, mientras que su activación o transferencia adoptiva reduce esta carga y atenúa los fenotipos asociados a la edad (Kale A. et al, 2020).

Las células NK funcionan como guardianes contra la senescencia, iniciando respuestas para su eliminación y mantenimiento de la homeostasis tisular (Krizhanovsky et al., 2008). Sin embargo, con el envejecimiento, sufren cambios fenotípicos y funcionales (inmunosenescencia de NK) que comprometen su capacidad para eliminar eficientemente estos objetivos celulares, contribuyendo a su acumulación y al desarrollo de patologías relacionadas con la edad (Camous X, et al., 2012).

En conjunto, las células NK desempeñan un gran papel en la vigilancia y eliminación de la senescencia celular mediante citotoxicidad directa y orquestación de respuestas inmunes. Su disfunción relacionada con la edad contribuye a la acumulación de estos elementos deletéreos y al desarrollo de enfermedades asociadas al envejecimiento. Estrategias para rejuvenecer o restaurar la función NK podrían ofrecer nuevas vías terapéuticas para estas condiciones.

### Poblaciones de células NK y sus roles específicos

Existen dos linajes principales cuando se habla de células NK, que pueden diferenciarse por la cantidad de los marcadores CD56 y CD16 (Peng & Tian, 2017). Esta diferencia no es solo de apariencia, sino que también implica funciones distintas. Por un lado, las células NK CD56 bright constituyen un subgrupo que representa solo el 10% de las células en sangre periférica, pero tienen una gran capacidad de producción de sustancias. Aunque son más inmaduras y su capacidad citotóxica es limitada, son importantes porque secretan muchas citocinas proinflamatorias, como IFN-γ y TNF-α. Además, hay evidencia de que estas células son precursoras de la subpoblación CD56 dim.

Por otro lado, la mayoría de las células NK circulantes, cerca del 90%, son del tipo CD56 dim CD16 bright. Estas células están en su etapa más madura y tienen una maquinaria citotóxica muy eficiente, además de expresar muchos receptores inhibidores KIR y el receptor CD16, que reconoce la región Fc de las IgG. Estas dos poblaciones no solo se diferencian en sus funciones y en cómo responden a ciertas citocinas, sino también en su movimiento y ubicación en el cuerpo. Las células NK CD56 bright se encuentran principalmente en los tejidos linfoides secundarios, mientras que las CD56 dim circulan principalmente en la sangre y se dirigen en gran número a los sitios de inflamación (Cerwenka & Lanier, 2001).

A medida que envejecemos, cambian las proporciones de las poblaciones de células NK. Diversos estudios han encontrado que en personas mayores hay menos células NK CD56 bright y más células NK CD56 dim que en adultos jóvenes (Almeida-Oliveira et al., 2011). Este cambio sugiere que, con la edad, puede disminuir la producción de citocinas y aumentar la citotoxicidad de las células NK.

### Cambios fenotípicos y funcionales

Las células NK en personas mayores presentan cambios claros en su aspecto. Se ha observado que expresan menos receptores activadores, como NKp30 y NKp46, lo que puede reducir su capacidad citotóxica (Almeida-Oliveira et al., 2011). También se ha encontrado que tienen más del receptor inhibidor NKG2A, lo que podría dificultar su activación (Lutz et al., 2005).

El envejecimiento se asocia con una disminución en la actividad citotóxica de las células NK. Esta reducción en la citotoxicidad puede atribuirse a la menor expresión de receptores activadores, la señalización intracelular alterada y la disminución en la liberación de gránulos citotóxicos (Hazeldine et al., 2012). Además, las células NK de individuos mayores muestran una producción alterada de citocinas. Se ha observado una disminución en la producción de IFN-γ y TNF-α por parte de las células NK en respuesta a estímulos, lo que puede afectar la regulación de otras células inmunes (Després-Brummer et al., 2020).

En conjunto, estos cambios fenotípicos y funcionales, no solo comprometen la función intrínseca de las células NK, sino que también modifican profundamente su capacidad para comunicarse e interactuar con otros componentes del sistema inmune. La producción reducida de IFN-γ y TNF-α, por ejemplo, limita la activación de células dendríticas y macrófagos, mientras que la menor citotoxicidad puede afectar la presentación cruzada de antígenos y la activación de células T. Así, el deterioro funcional de las células NK durante el envejecimiento no representa un evento aislado, sino que tiene ramificaciones sistémicas que alteran la dinámica de toda la red inmunológica, como se discutirá en la siguiente sección.

**Interacciones de las células NK con otros componentes del sistema inmune durante el envejecimiento**

La disfunción de las células NK asociada al envejecimiento puede tener implicaciones en la inmunovigilancia y la inflamación. La incapacidad de las células NK para eliminar células infectadas por virus y células tumorales puede aumentar la susceptibilidad a enfermedades infecciosas y cáncer en la población de edad avanzada (Hazeldine & Lord, 2013).

Las células NK no actúan de manera aislada, sino que interactúan con otros componentes del sistema inmune. Durante el envejecimiento, los cambios en las células NK pueden afectar estas interacciones y la función inmune general. Por ejemplo, las células NK senescentes pueden tener una disminución en la activación de células dendríticas y también en las respuestas de células T (Müller-Durovic et al., 2016).

El envejecimiento también provoca cambios en otros componentes del sistema inmune, como la disminución de la función de las células T y B. Esto afecta de forma indirecta a las células NK, ya que reduce las señales activadoras (IL-2, IL-15), altera la presentación de antígenos y disminuye la citotoxicidad celular dependiente de anticuerpos (Solana et al., 2012). Esta relación muestra que la inmunosenescencia es una desregulación sistémica que provoca un deterioro de distintos tipos celulares. Entender estas interacciones serviría para diseñar intervenciones que restauren la función inmune en personas mayores.

El envejecimiento produce cambios en la cantidad, el tipo y la función de las células NK. Estos cambios pueden hacer que las personas mayores sean más propensas a infecciones, cáncer y a un estado inflamatorio crónico. Comprender cómo y por qué las células NK funcionan peor con la edad, y cómo interactúan con otras partes del sistema inmune, ayuda a crear estrategias para mejorar la defensa del cuerpo y favorecer un envejecimiento saludable.

## 6.5. Secuenciación de RNA de célula única en células NK durante el envejecimiento

La transcriptómica es el estudio del conjunto completo de RNAs en una muestra y ha evolucionado desde la secuenciación *bulk* o en bulto (promediando la expresión génica y enmascara la heterogeneidad celular (Haque et al., 2017)), hasta la secuenciación de célula única (scRNA-seq). Esta tecnología permite capturar perfiles de expresión individuales mediante un flujo de trabajo que incluye la disociación tisular, el aislamiento de células (vía microfluídica o *sorting*), la lisis, la captura de RNA y la posterior amplificación de bibliotecas de cDNA para su secuenciación masiva (Svensson et al., 2018; Macosko et al., 2015). Al no promediar señales, la scRNA-seq permite identificar subpoblaciones poco frecuentes, estudiar trayectorias de diferenciación y detectar cambios sutiles que pasan desapercibidos en análisis poblacionales (Tanay & Regev, 2017).

En el contexto de la inmunosenescencia, esta resolución sin precedentes es fundamental para descubrir estados celulares asociados a la edad y mecanismos reguladores a nivel de célula única (Kimmel et al., 2019). Específicamente en las células NK, la scRNA-seq ha revelado una complejidad molecular y trayectorias de diferenciación que los enfoques clásicos no lograban capturar (Rebuffet et al., 2024). Sin embargo, existe un vacío en la comprensión de la trayectoria de la inmunosenescencia, ya que la mayoría de los mapas de referencia se centran en individuos sanos o en contextos oncológicos.

Estudios previos han intentado abordar este proceso; por ejemplo, Luo et al. (2022) identificaron un fenotipo exhausto (mayor expresión de MHC-II y genes de agotamiento) en células NK de adultos mayores de 65 años con fragilidad. No obstante, dicho estudio contó con una muestra limitada (n=17), lo que restringe la generalización de sus hallazgos debido a la alta variabilidad de cada individuo durante el envejecimiento. Para superar esta limitación, el presente estudio propone la integración de datos de múltiples donantes y cohortes publicadas. Al aumentar el tamaño de la muestra y captar una mayor diversidad biológica, se incrementa el poder estadístico para identificar biomarcadores robustos de la inmunosenescencia humana.

Esta integración masiva conlleva desafíos técnicos y computacionales críticos. Un control de calidad riguroso es indispensable para eliminar artefactos y células de baja calidad (Luecken & Theis, 2019). Particularmente, al combinar datos de distintos experimentos, surge el efecto de lote (variación técnica no biológica), cuya corrección es vital para asegurar que las diferencias observadas entre jóvenes y adultos mayores sean biológicas y no técnicas (Haghverdi et al., 2018). Finalmente, la asignación de identidades celulares precisas requiere herramientas especializadas y marcadores conocidos para una anotación meticulosa (Abdelaal et al., 2019). Solo mediante este rigor analítico es posible transformar la transcriptómica de célula única en una herramienta capaz de identificar objetivos terapéuticos que mitiguen la disfunción inmune relacionada con la edad.

# 7. Metodología

##

## 7.1 Recolección y preprocesamiento de datos

El análisis se realizó con datos de tipo scRNA-seq obtenidos del repositorio *CellxGene* Census (CZ CELLxGENE, 2023), restringiendo la búsqueda a muestras de tejido sanguíneo humano provenientes de donantes sanos. Para el procesamiento y análisis computacional se emplearon scripts personalizados desarrollados en Python (versión 3.9.7).

La selección de las muestras se rigió por criterios de inclusión y exclusión diseñados para garantizar la calidad y la relevancia biológica del estudio. Se incluyeron únicamente datos primarios de donantes sanos con edades iguales o superiores a 34 años, cuyas células estuvieran anotadas específicamente como células Natural Killer o sus subtipos, y que contaran con metadatos completos referentes a edad, sexo y etapa de desarrollo. Por contraparte, se excluyeron aquellos datos provenientes de tejidos distintos a la sangre periférica, de muestras de individuos sometidos a tratamientos farmacológicos, de donantes menores de 34 años, así como cualquier célula que careciera de una anotación clara o perteneciera a linajes celulares distintos.

### Estratificación por grupos de edad

Para caracterizar los cambios asociados al envejecimiento, la cohorte se dividió en dos grupos de edad definidos con base en evidencia proteómica y clínica previa. El primer grupo, denominado "Adultos" (34-60 años), se estableció con base en el punto de inflexión molecular identificado a los 34 años en el proteoma plasmático (Lehallier et al., 2019). El segundo grupo, "Adultos Mayores" (>60 años), se definió con base en la misma evidencia presentada por el mismo grupo de investigación y considerando las definiciones integrales utilizadas por la Organización Mundial de la Salud (Ranasinghe et al., 2025). Esta agrupación nos permitió observar el paso de una fase de mantenimiento homeostático en adultos hacia una fase de senescencia inmunológica esperada en adultos mayores.

### Identificación de las poblaciones de células NK

Las anotaciones de tipos celulares fueron estandarizadas y agrupadas utilizando un diccionario de ontología celular a través del CellGuide (Chan Zuckerberg Initiative, s.f.) y posteriormente adaptado de estudios recientes de perfilado de células mononucleares de sangre periférica (Kian Hong Hu Y., et al., 2024). Esta estandarización permitió una comparación consistente entre conjuntos de datos a nivel de tipo celular, mientras se mantenía la granularidad de las clasificaciones de subtipos celulares. Para asegurar la calidad de los datos y la compatibilidad entre estudios, implementamos un proceso de homogeneización del espacio de características, convirtiendo todos los identificadores de genes a símbolos HGNC estándar y eliminando características duplicadas o ambiguas.

## 7.2 Control de calidad

Implementamos un flujo de trabajo parcialmente inspirados por trabajos como los de Luecken M.D., *et al.*, 2022 o Sanbomics 2022 pero con modificaciones orientadas al control de calidad (Subramanian, A., *et al.*, 2022) y diseñado para análisis de células NK adultas, asegurando la confiabilidad de los datos mientras se conservaron las señales biológicas relevantes.

### Detección y eliminación de células dobletes

Empleamos SOLO, un método de detección de dobletes basado en aprendizaje profundo (Bernstein et al., 2020), implementado mediante el marco de trabajo scVI (scvi-tool, versión 1.1.5). Este enfoque fue seleccionado por su capacidad para manejar conjuntos de datos a gran escala y mantener la sensibilidad a las características de los tipos celulares. Las células fueron identificadas como dobletes si la puntuación de probabilidad diferencial entre predicciones de células dobletes y de célula única era >0.3 y las métricas de complejidad excedían el percentil 95.

### Métricas de calidad celular

Las métricas de control de calidad se calcularon utilizando un enfoque basado en datos fundamentado en el método de Desviación Absoluta de la Mediana (Subramanian, A., *et al.*, 2022), con parámetros optimizados para células NK adultas:

Complejidad genética (mínimo 100 genes por célula), Conteos UMI (mínimo 50 conteos por célula), Filtrado de células con contenido de genes mitocondriales y ribosomales variables, no mayor a 2.5 de Desviación Absoluta de la Mediana por clúster, con límite máximo de 20%

El pipeline de control de calidad fue implementado utilizando un enfoque basado en agrupamiento de Leiden (resolución = 1.5) con reducción de dimensionalidad a 30 componentes, asegurando una identificación del tipo celular durante el proceso de control de calidad.

## 7.3 Normalización y Escalado

La normalización de datos se llevó a cabo utilizando la librería Scanpy (versión 1.10.2; Wolf FA, *et al.*, 2018) mediante una estrategia de dos etapas. Inicialmente, se normalizó la profundidad de secuenciación de cada célula a un total de 10,000 UMIs empleando la función `normalize\_total`, seguido de una transformación logarítmica (log1p) para estabilizar la varianza. Para reducir la dimensionalidad del análisis y mitigar el ruido técnico, se seleccionaron los 7,000 genes altamente variables (HVGs), priorizando aquellos que mantenían una dispersión biológica consistente a través de los múltiples lotes experimentales procesados.

## 7.4 Comprobación de los marcadores canónicos para tipos celulares

Con el objetivo de corroborar la identidad celular y depurar posibles contaminaciones de otros linajes linfoides, se evaluó la expresión de genes marcadores canónicos derivados de las tablas ASCT+B del Atlas de Referencia Humana (Börner et al., 2021).

El análisis se realizó utilizando tres paneles de validación. El panel de identidad de células NK incluyó 80 genes característicos, entre ellos NKG7, GNLY, PRF1, GZMA, KLRD1, TYROBP y FCGR3A, para los cuales se verificaron tanto el porcentaje de positividad como la expresión media esperada. Además, la pureza del conjunto de datos se evaluó mediante un panel de 50 marcadores de células T, con especial énfasis en el complejo CD3 (CD3E, CD3D, CD3G), y un panel de 15 marcadores de células B, como CD79A, MS4A1 e IGHM.

Se creó una estrategia especial para detectar la presencia de células T, usando la expresión conjunta de los componentes del receptor CD3 (Thermo Fisher Scientific, 2025; DrugBank, 2025). Se hicieron filtros para CD3E, CD3D y CD3G, lo que permitió encontrar células que fueran positivas para los tres marcadores. De forma similar, se encontraron células con alta expresión de marcadores de células B.

## 7.5 Integración de Datos

El flujo de trabajo de análisis se basó en parte en el pipeline desarrollado por Sanbomics (2023), adaptando las estrategias de preprocesamiento y normalización al contexto de las células NK en el estudio de la inmunosenescencia. Se usó un enfoque de integración en dos etapas para corregir los efectos de lote y preservar la variación biológica relacionada con el envejecimiento.

### Arquitectura del modelo scVI

La primera etapa de integración se realizó mediante scVI (*single-cell Variational Inference*), un modelo de *autoencoder* variacional (VAE) que comprime los datos de expresión génica a un espacio latente de baja dimensión. scVI utiliza una arquitectura *encoder-decoder.* En el, la parte del codificador (*encoder)* transforma los conteos de expresión génica en una representación latente comprimida, después el decodificador (*decoder)* reconstruye los datos originales, asegurando la preservación de información biológica relevante. Finalmente, el modelo aprende de esta forma a corregir los efectos técnicos del lote mientras mantiene las señales biológicas. Esto nos permite generar una representación unificada de los datos de múltiples estudios, reduciendo la variabilidad técnica entre lotes experimentales.

Los parámetros fueron ajustados según los resultados obtenidos con el fin de obtener una buena integración de datos de acuerdo el *benchmark Single-cell integration benchmarking (scIB,* versión 1.1.5) con 2 capas ocultas de 128 nodos cada una y un espacio latente de 30 dimensiones. El modelo empleó una distribución binomial negativa para modelar los conteos, con una tasa de dropout de 0.1 y normalización tanto de capa como de lote. El entrenamiento se ejecutó con una tasa de aprendizaje de 1e-3 (con reducción programada por meseta, factor 0.6) y un calentamiento de la divergencia KL de 30 pasos.

### Integración Refinada con scANVI

Posteriormente, se refinó la integración mediante scANVI (Single-cell ANnotation using Variational Inference), una extensión con enfoque semisupervisado de scVI (Lopez et al., 2018). scANVI extiende la arquitectura VAE e incorpora información de etiquetas celulares conocidas para ayudar a separar la variación biológica de los artefactos técnicos. Esta etapa se adaptó con el fin de corregir los efectos de lote que pudieran provenir de la variable asociada al estudio de origen, ajustando, además, por covariables técnicas como el tipo de ensayo, la etnicidad y el sexo. El modelo fue entrenado durante 150 épocas con un muestreo de 100 células por etiqueta, logrando separar eficazmente la variación técnica de la biológica. La evaluación de calidad mediante el marco scIB confirmó la eliminación de los efectos de lote (Luecken M.D., et al., 2022), preservando las señales biológicas del envejecimiento.

## 7.6 Análisis de Expresión Diferencial

El análisis de expresión diferencial se diseñó para identificar cambios transcripcionales asociados a la transición del envejecimiento adulto, empleando un enfoque de pseudo-bulk para controlar la variación a nivel de donante y proporcionar una inferencia estadística robusta. Este enfoque presenta ventajas metodológicas críticas. En primer lugar, reconoce que las células de un mismo donante no son observaciones independientes, ya que comparten el mismo fondo genético, estado de salud y condiciones ambientales. En segundo lugar, proporciona robustez estadística, pues al agregar los conteos se promedian las fluctuaciones estocásticas a nivel celular (ruido técnico y biológico intraindividual), permitiendo que emerjan señales biológicas consistentes asociadas al envejecimiento a nivel poblacional. Finalmente, asegura la compatibilidad con métodos establecidos, ya que la agregación permite el uso de herramientas estadísticas bien validadas para RNA-seq bulk, cuyas propiedades están ampliamente aceptadas en la comunidad científica.

Para la ejecución del análisis utilizamos el paquete DESeq2 (Love et al., 2014), el cual emplea modelos lineales generalizados con distribución binomial negativa y estrategias de contracción (*shrinkage*) para una estimación robusta de la dispersión y los cambios de expresión (*fold changes*). El método normaliza los datos por profundidad de secuenciación, controla la tasa de falsos positivos mediante el procedimiento de Benjamini-Hochberg (FDR) y proporciona estimaciones confiables de los cambios transcripcionales asociados al envejecimiento.

### Diseño del Análisis

El análisis comparó dos grupos principales: adultos (34-60 años, 384 personas) y adultos mayores (más de 60 años, 118 personas). Para cada individuo, se sumaron los conteos de todas sus células NK y se utilizaron estos datos totales. De esta manera, el análisis estadístico muestra las diferencias entre personas según la edad y no las diferencias entre células de una misma persona.

### Parámetros del análisis

Nuestro modelo experimental se definió con la siguiente fórmula `~ grupo\_edad + sexo + [covariables técnicas]`. En el apartado de covariables técnicas se añadieron variables, como el lote de secuenciación, cuando fue necesario. Se utilizaron criterios de significancia adaptados a nuestro estudio para asegurar una significancia biológica. Se estableció un valor p ajustado (FDR) menor que 0.05 y un cambio absoluto mínimo en el log2 fold change mayor que 1.0 (lo que equivale a un cambio de expresión de al menos 2 veces). También se filtraron los genes con una expresión promedio inferior a 10 conteos para aumentar el poder estadístico del análisis.

## 7.7 Análisis de patrones temporales

El envejecimiento del sistema inmune no sigue necesariamente una dinámica lineal y uniforme. Múltiples estudios han documentado que los procesos celulares asociados al envejecimiento pueden presentar fases con distintas tasas de cambio, períodos de estabilidad relativa seguidos de deterioro acelerado, o puntos de transición críticos donde los sistemas compensatorios colapsan (Brauning et al., 2022). Para capturar esta complejidad en las células NK, se evaluó el ajuste de la expresión de cada gen frente a la edad cronológica mediante cinco modelos que representan diferentes hipótesis de cambio: (1) nulo o *null* (ausencia de cambio), (2) lineal (desgaste acumulativo y uniforme), (3) cuadrático (aceleración o desaceleración progresiva), (4) logarítmico (cambio rápido inicial seguido de estabilización) y (5) exponencial (aceleración extrema o colapso catastrófico) (Muthén, 2004).

La selección del modelo óptimo para cada unidad genética se realizó mediante el Criterio de Información Bayesiano (BIC), el cual permite balancear el ajuste con la parsimonia al penalizar la complejidad del modelo (Schwarz, 1978). Un gen se clasificó con una trayectoria no lineal si su modelo óptimo presentaba una mejora en el BIC ≥2 respecto al modelo lineal, lo que constituye evidencia positiva según la escala de Kass-Raftery.

Para asegurar que estos modelos posean capacidad de generalización y no sean producto de un sobreajuste, se implementó una validación cruzada (*cross-validation*) de 3 pliegues. En este proceso, los datos se dividieron en tres subgrupos estratificados, utilizando el ~67% para el entrenamiento y el ~33% restante para la evaluación, calculando el coeficiente de determinación (R2) promedio entre las iteraciones (Raschka, 2018). Finalmente, la robustez de las asociaciones se confirmó mediante la corrección por comparaciones múltiples utilizando la tasa de descubrimiento falso (FDR) mediante el método de Benjamini-Hochberg con α=0.05 (Benjamini & Hochberg, 1995). Es pertinente enfatizar que este análisis es de naturaleza transversal, reflejando diferencias entre individuos de distintas edades en un punto temporal fijo y no cambios longitudinales en los mismos donantes.

## 7.8 Análisis de Enriquecimiento Funcional

La interpretación biológica de los cambios transcripcionales se realizó mediante un análisis de enriquecimiento funcional diseñado para identificar vías biológicas y procesos celulares significativamente alterados durante la progresión de la inmunosenescencia.

Para este estudio, se utilizó la plataforma Enrichr (Chen et al., 2013; Kuleshov et al., 2016) como herramienta de análisis, lo que permitió explorar simultáneamente varias bibliotecas de conocimiento biológico. Esto facilitó el mapeo de rutas metabólicas y de señalización mediante bases de datos como Reactome (Gillespie et al., 2022; Milacic et al., 2024) y WikiPathways, que recopilan información sobre vías biológicas generada por la comunidad científica.

El análisis se extendió más allá de las vías canónicas para explorar redes de regulación transcripcional a partir de las bibliotecas ChEA y ENCODE TF ChIP-seq, lo que permitió identificar posibles factores de transcripción maestros responsables de los cambios observados. Se caracterizaron dominios proteicos funcionales a través de InterPro y se evaluó la relevancia de los hallazgos en el contexto del envejecimiento sistémico usando las firmas moleculares de GTEx Aging Signatures 2021. Este enfoque integral con Enrichr proporcionó una visión holística de las alteraciones funcionales asociadas al envejecimiento de las células NK.

Para asegurar la solidez biológica de los resultados, se realizó una validación utilizando g:Profiler (versión 2023) como herramienta de comparación (Raudvere et al., 2019; Kolberg et al., 2023). Esta plataforma sirvió para confirmar la consistencia de los términos enriquecidos, aplicando un umbral de significancia estadística muy estricto (padj < 1.905×10⁻⁶⁵) y así reducir el riesgo de falsos positivos en la identificación de ontologías. La coincidencia de resultados entre ambas plataformas demostró que las vías de inmunosenescencia identificadas son señales biológicas sólidas y reproducibles, superando los posibles sesgos de una sola base de datos o de un único algoritmo de enriquecimiento.

# 8. Resultados

## FASE A: Auditoría de Resultados Iniciales (Modelo Clásico)

> [!NOTE]
> En esta fase se reportan los resultados obtenidos mediante el análisis pseudo-bulk estándar previo a la corrección del sesgo técnico por lote de secuenciación. Se exponen los hallazgos que sugerían la pérdida del repertorio de receptores Ig.

## 8.1 Recolección de datos

De los 45 millones de células únicas disponibles en la plataforma de CellxGene al momento de realizar la selección de datos, 8.8 millones eran de tejido sanguíneo. Después de aplicar los criterios de inclusión y exclusión, se identificaron 14 estudios distintos con muestras provenientes de donantes adultos. La población de células NK incluía varios subtipos: células NK CD56 bright, células NK CD56 dim, células NK-T maduras, y otros subconjuntos de células NK, manteniendo proporciones consistentes con las frecuencias previamente reportadas en sangre periférica (Blum et al., 2007). Al realizar la estratificación de las células se recuperaron dos grupos: i) Adultos: 34-60 años (n = 384 donantes, 133,527 células) y ii) Adultos Mayores: >60 años (n = 118 donantes, 60,174 células). El conjunto de datos final con control de calidad retuvo 193,701 células y 7,000 genes, proporcionando una base para el análisis del envejecimiento en células NK adultas.

## 8.2 Análisis descriptivos

El análisis descriptivo de las muestras revela una distribución sesgada entre los grupos de edad, lo cual fue considerado en las comparaciones transcripcionales para el estudio de la inmunosenescencia. Como se observa en la Figura 2A, la población total de células NK analizadas (193,701 células) está distribuida en dos grupos: adultos (69%, 133,527 células) y adultos mayores (31%, 60,174 células).

|  |
| --- |
| ![](data:image/png;base64...)A. ![](data:image/png;base64...)B. ![](data:image/png;base64...)C![](data:image/png;base64...).D.  ![](data:image/png;base64...)E. |
| **Figura 2. Caracterización demográfica y validación de linaje.** (A) Distribución porcentual de la muestra en los grupos de estudio (adultos vs. adultos mayores). (B) Contribución celular total estratificada por estudio de origen, destacando la heterogeneidad de las fuentes integradas. (C) Análisis de frecuencia de los subtipos de células NK en función de la edad. (D) Histograma de la distribución etaria de los donantes incluidos. (E) Gráfico de puntos (dot plot) de validación de linaje mediante la expresión de marcadores canónicos de células NK, T y B para asegurar la pureza de la población analizada. |

El análisis de la distribución de los grupos de edad y por estudio de procedencia (Figura 2B) revela cierta heterogeneidad entre los grupos incluidos en el estudio. Destacando los datos del estudio de Travaglini, K. J., 2020, que aporta una mayor cantidad de células, especialmente del grupo adulto. Esta variabilidad en la contribución por muestra se consideró en los análisis subsecuentes mediante estrategias de reducción de la variabilidad técnica entre estudios y mediante el uso de dicha variable como covariable en los modelos para mitigar los efectos de lote que pudieran estar asociados a la muestra de origen.

En cuanto a la distribución por edades específicas ordenadas de manera cronológica (Figura 2C), se observó una representación que disminuye con las siguientes particularidades: Los grupos de Adultos mayores (especialmente a partir de los 80 años) muestran una disminución en cuanto a sus frecuencias absolutas. Se observó ausencia de muestras como a los 60 años y también a los 80 años, este fenómeno podría limitar la viabilidad de utilizar un enfoque pseudo longitudinal a no ser que se utilicen agrupaciones de edades un poco más amplias.

### Frecuencia y distribución de subtipos de células NK

La revisión de proporciones por subtipos celulares por grupo de edad (Figura 2D) muestra que la composición del reservorio de células NK varía con el envejecimiento. Las células NK CD56 dim (CD16-positivas) son más frecuentes en adultos, pero su proporción disminuye en los adultos mayores. Contrastando directamente, las células NK CD56 bright (CD16-negativas) son una población minoritaria (frecuencias <0.1) en todos los grupos de edad y muestran distribuciones similares entre grupos de edad. En cambio, las células NK-T maduras y las de tipo I tienen frecuencias bajas, pero tienden a estar más representadas en adultos mayores. Finalmente, las células NK generales presentan una distribución variable, en la que algunas muestras alcanzan frecuencias absolutas en el repertorio de células NK. La mediana de la frecuencia de las células NK generales es mayor en adultos mayores.

Estas diferencias en la distribución de subtipos facilitan la interpretación de los cambios transcripcionales observados, ya que la variación en la composición celular puede influir en los cambios funcionales. Además, la expansión o reducción de subtipos específicos puede indicar la presencia de poblaciones importantes en la inmunosenescencia. El conjunto de datos, que incluye casi todas las edades y subtipos celulares, es una base sólida para futuros análisis transcripcionales y para identificar genes relevantes en el envejecimiento de las células NK y sus subpoblaciones.

El conjunto de datos integrado, con representación de casi todas las edades y subtipos celulares, proporciona una base para los análisis transcripcionales subsecuentes y la identificación de genes importantes en el envejecimiento en células NK y sus subpoblaciones.

## 8.3 Validación de Tipos Celulares

El análisis sistemático de expresión de marcadores específicos de linaje confirmó la identidad de las células NK en nuestro conjunto de datos y permitió cuantificar el grado de contaminación por otros tipos celulares.

###

###

### Expresión de marcadores NK canónicos

El análisis de expresión de marcadores canónicos reveló un patrón de expresión consistente con el fenotipo esperado para células NK. Específicamente, se observó expresión de NKG7 en el 91.0% de las células (expresión media 22.06), GNLY en el 93.2% (media 31.17), GZMA en el 78.6% (media 4.47), KLRD1 en el 82.5% (media 3.01) y CCL5 en el 68.3% (media 8.97). En general, se encontró una firma consistente donde la totalidad de genes canónicos se encuentran presentes y expresados en un porcentaje considerable de células (Figura 2E).

### Evaluación de contaminación celular

Para descartar la presencia de células T no deseadas, se revisó la presencia de ciertos marcadores. Se encontró CD3E en el 33.5% de las células, CD3D en el 9.4% y CD3G en el 8.5%. Lo más importante es que solo el 3.7% (13,409 células) tenía los tres marcadores CD3 al mismo tiempo, lo que indicó una baja proporción de células T.

En cuanto a la posible presencia de células B, los marcadores típicos de estas células se encontraron en niveles muy bajos, y la mayoría de ellos estaban presentes en menos del 5% de las células. Las únicas excepciones fueron CD44 (41.03% en adultos mayores) y MYBL1 (35.13% en adultos mayores), pero estos marcadores no son exclusivos de las células B. Los marcadores más específicos, como CD79A, MS4A1 e IGHM, casi no se detectaron, lo que confirma que casi no hay células B. El análisis indicó que los datos provienen de poblaciones NK de alta pureza, proporcionando una base robusta para identificar biomarcadores de envejecimiento.

## 8.4 Integración de datos y reducción de efectos batch

La integración de 14 estudios independientes generó una heterogeneidad técnica sustancial que requirió una armonización robusta. Para validar este proceso, se utilizó el marco de referencia *Single-cell Integration Benchmarking* (scIB) de Luecken et al. (2022), el cual evalúa el desempeño mediante un puntaje agregado que equilibra la corrección de lote y la preservación de la señal biológica. El modelo scANVI demostró una superioridad técnica frente a las aproximaciones de PCA (basal) y scVI, obteniendo una puntuación total de 0.62 (Figura 3A).

Este rendimiento se explica por un desempeño excepcional en la corrección de lote (Batch Correction: 0.98). Esta puntuación se deriva de métricas de mezcla local como el Índice de Simpson Inverso de Integración (iLISI) y la prueba de efecto de lote k-nearest neighbor (kBET), las cuales confirmaron que el espacio latente de scANVI permite una coexistencia homogénea de células procedentes de distintos donantes, eliminando sesgos derivados del centro de secuenciación o la tecnología empleada.

Por otro lado, la conservación biológica (Bio-conservation) obtuvo una puntuación de 0.38. Aunque este valor es moderado, refleja el compromiso (*trade-off*) necesario para lograr una integración profunda de múltiples cohortes. Esta categoría se evaluó mediante tres ejes fundamentales:

* NMI (Información Mutua Normalizada) y ARI (Índice de Rand Ajustado): Estas métricas comparan la concordancia entre los agrupamientos (*clusters*) generados por el algoritmo y las identidades celulares conocidas. Puntuaciones altas indican que la integración no "fusionó" tipos celulares distintos por error.
* ASW de etiqueta (Silhouette Label): Mide la silueta o cohesión de cada tipo celular. Un valor positivo confirma que las células de un mismo subtipo (ej. NK-T) se encuentran más cerca entre sí que de otros linajes en el espacio UMAP.
* cLISI (Índice de Simpson Inverso de Tipo Celular): Evalúa la pureza de los vecindarios locales para asegurar que no haya una mezcla excesiva que borre las fronteras entre subpoblaciones funcionales.

|  |
| --- |
| ![](data:image/png;base64...)A.![](data:image/png;base64...)B.  ![](data:image/png;base64...) C.  ![](data:image/png;base64...)D. |
| **Figura 3. Evaluación de la integración de datos.** (A) Comparativa de métricas de desempeño mediante el marco de referencia scIB (Single-cell Integration Benchmarking). (B) Proyección UMAP de la población integrada coloreada por subtipo celular, demostrando la preservación de la estructura biológica. (C) Visualización UMAP coloreada por grupo de edad, que evidencia una mezcla homogénea de células procedentes de diversos estudios y la ausencia de agrupamientos técnicos dominantes tras la normalización. (D) Visualización UMAP coloreada por estudio de origen. |

La visualización UMAP (Figura 3B y 3C) respalda estos números: se observa una mezcla completa de los estudios de origen, mientras que la estructura biológica se mantiene intacta, con una separación clara entre las poblaciones CD56 *bright* y CD56 *dim*. Este equilibrio garantiza que los análisis de expresión diferencial posteriores identifiquen cambios biológicos reales asociados a la edad y no artefactos técnicos de los estudios integrados.

El hecho de que se mantenga la organización biológica por tipo de célula, mientras se reducen los efectos de los lotes, demostró que el método de integración logró un equilibrio óptimo entre eliminar las diferencias técnicas y mantener la información biológica importante. Esto sirve como base para los próximos análisis sobre los cambios en la expresión y en las funciones relacionadas con el envejecimiento.

## 8.5 Análisis de expresión diferencial

### Análisis de expresión diferencial entre células NK

El análisis de expresión diferencial entre donantes adultos y adultos mayores reveló una firma molecular de 83 genes con cambios significativos (valor p ajustado < 0.05 y con Log Fold Change >1). Se observa una activación coordinada de mediadores proinflamatorios, destacando el incremento de *CXCL8* y *IL1B* (Tabla 1). Esta transición hacia un fenotipo proinflamatorio se apoya en el enriquecimiento funcional de la vía de respuesta inflamatoria y la señalización mediada por IL-17. Paralelamente, se identificó una reducción en componentes de reconocimiento molecular, tales como *IGLV2-8* e *IGHV3-23* (Tabla 2), sugiriendo un compromiso en la diversidad del repertorio de receptores durante la inmunosenescencia.

El aumento de ciertas proteínas que causan inflamación está liderado por *CXCL8* (IL-8), que es importante para atraer neutrófilos, junto con *CXCL2* y CXCL3. Este patrón inflamatorio también incluye un aumento de *IL1B*, que es clave en la inflamación, y de genes relacionados con la activación del sistema inmune como el AIF1. El mapa de calor (Figura 4) muestra cómo se distribuyen estos perfiles de genes y destaca grupos de genes que se activan más en adultos mayores: respuesta inflamatoria (*CXCL8*, *IL1B*, *CXCL2*), respuesta al estrés celular (*SERPINA1*, *CST3*, G0S2) y cambios en la matriz que rodea las células (SULF2, TNFAIP6, PTX3). Estos cambios muestran una reorganización molecular que coincide con el estado de "inflammaging" (Li et al., 2023).

|  |
| --- |
| ![](data:image/png;base64...) |
| **Figura 4. Perfil transcripcional diferencial global.** Mapa de calor (heatmap) que representa la expresión normalizada (Z-score) de los 83 genes con cambios significativos identificados entre adultos y adultos mayores, ordenados cronológicamente por la edad numérica de los donantes. |

Los genes subexpresados en células NK envejecidas presentaron un patrón distinto, con una disminución en la expresión de genes de la familia de inmunoglobulinas, predominantemente segmentos variables de cadenas ligeras y pesadas como *IGLV2-8*, *IGHV3-23* e IGLV1-44. Esta disminución generalizada de genes relacionados con inmunoglobulinas sugiere alteraciones en mecanismos de reconocimiento molecular asociados a la edad, potencialmente vinculados a cambios en los perfiles de receptores de células NK (Watson C. T., 2012).

El análisis detallado de los perfiles de expresión de genes diferencialmente expresados a lo largo de la adultez, agrupados en intervalos de 5 años de edad, reveló patrones temporales específicos en los genes relacionados con las inmunoglobulinas (Figura 5). Los gráficos de expresión muestran un patrón de disminución progresiva de la expresión de múltiples segmentos variables de cadenas ligeras y pesadas de inmunoglobulinas desde la juventud hasta la vejez.

|  |
| --- |
| ![](data:image/png;base64...) |
| **Figura 5. Declive de componentes de reconocimiento molecular.** Trayectorias de expresión de genes sub-expresados, centradas en segmentos variables de inmunoglobulinas (*IGLV*, *IGHV*, *IGKV*), mostrando una disminución progresiva y escalonada a lo largo de la vida adulta. |

### Sub-expresión de genes: declive de la inmunovigilancia

El análisis de los niveles de expresión de genes regulados de forma diferente en los distintos grupos de edad mostró que los genes de inmunoglobulinas están menos expresados en las células NK envejecidas.

Los genes de esta familia presentan una disminución progresiva de su expresión a lo largo de la adultez. Este descenso se observa en genes como *IGLV2-8*, *IGHV3-23*, IGLV1-44 e IGLV3-19, donde la expresión disminuye con la edad. La reducción afecta sobre todo a dos tipos de genes de inmunoglobulinas: los segmentos variables de cadenas ligeras (IGL), como *IGLV2-8*, IGLV1-44, IGLV3-25 e IGLV7-57, y los segmentos variables de cadenas pesadas (IGH), como *IGHV3-23*, IGHV3-74 e IGHV5-51. Ambos tipos son importantes para la diversidad en el reconocimiento de antígenos y en la interacción con los receptores de la superficie celular (Pende, D., et al., 2019).

Esta disminución generalizada y progresiva de los transcritos de inmunoglobulinas en células NK sugiere alteraciones en los mecanismos de reconocimiento molecular y en las interacciones con dianas celulares a medida que avanzan los procesos de envejecimiento. Considerando que las células NK no producen anticuerpos pero expresan diversos receptores de superficie que reconocen patrones moleculares específicos (Mace E. M., 2023), estas alteraciones podrían reflejar cambios en la expresión de receptores tipo inmunoglobulina (*g-like receptors*) o en mecanismos de reconocimiento que comparten características estructurales con dominios de inmunoglobulinas, comprometiendo potencialmente la de vigilancia inmunológica y la respuesta a células senescentes, infectadas o transformadas.

Para confirmar que los patrones de expresión de genes de inmunoglobulinas observados son intrínsecos a las células NK y no el resultado de contaminación por células B, se implementó un protocolo de validación. Como se detalla en la sección de metodología, se realizó un análisis de marcadores canónicos de células B. La expresión de estos marcadores característicos del linaje B fue extremadamente baja en la población celular evaluada, con la mayoría de ellos expresados en menores al 4% de las células analizadas.

Además, el análisis de patrones de expresión de múltiples genes marcadores simultáneamente permitió descartar la presencia de un subconjunto celular con perfil de células B. Esto, combinado con la expresión de marcadores canónicos de células NK como NKG7, GNLY, GZMA y KLRD1 en la población celular evaluada (Figura 2B), proporciona evidencia de que los patrones de expresión de genes de inmunoglobulinas observados representan un fenómeno biológico genuino en células NK senescentes y no un artefacto debido a contaminación celular.

|  |
| --- |
| ![](data:image/png;base64...) |
| **Figura 6. Dinámicas de expresión de genes sobre-regulados.** Gráficos de líneas que muestran la expresión media por intervalos de 5 años de genes clave asociados a la respuesta inflamatoria y al estrés celular. |

### Sobre-expresión de genes: Inflamación sostenida

El análisis de los genes sobreexpresados en células NK de adultos mayores revela patrones temporales y biológicamente relevantes (Figura 6). A diferencia de la disminución progresiva observada en los genes de inmunoglobulinas, los genes sobreexpresados muestran mayoritariamente un patrón de incremento abrupto en el grupo de mayor edad, sugiriendo una reprogramación transcripcional durante las etapas avanzadas de la adultez.

Los genes relacionados con la respuesta inflamatoria tienen una expresión baja y estable en los primeros años de la adultez, pero aumentan notablemente en los adultos mayores. *CXCL8* (IL-8), además de ser una quimiocina proinflamatoria importante, es uno de los genes que más se incrementan en este grupo. Otros genes de la familia de quimiocinas, como *CXCL2* y CXCL3, y la citocina proinflamatoria *IL1B*, muestran un patrón similar, lo que indica que varios mediadores inflamatorios se activan en conjunto con el envejecimiento.

*SERPINA1*, que codifica la alfa-1-antitripsina, es el gen con mayor incremento en adultos mayores. Al ser un inhibidor de proteasas con función antiinflamatoria, este aumento podría formar parte de una respuesta para compensar el estado proinflamatorio del envejecimiento. *CST3* (cistatina C), otro inhibidor de proteasas, también aumenta en adultos mayores, aunque con mayor variabilidad entre donantes (Xiheng Wang & Jie Ji, 2025).

Los genes asociados con la remodelación tisular y la respuesta al estrés, como PTX3 (pentraxina 3), SPON1 (espondina 1) y ANGPT2 (angiopoyetina 2), también presentan un aumento de expresión en adultos mayores. Este hallazgo indica la existencia de cambios en la interacción de las células NK con su entorno durante el envejecimiento (Judge, S. J., et al., 2020).

Los genes asociados a la función fagocítica y a la inmunidad innata, como LST1 (leucocyte-specific transcript 1) y AIF1 (allograft inflammatory factor 1), aumentan gradualmente con la edad y alcanzan niveles elevados en adultos mayores. Este patrón podría reflejar una adaptación progresiva de las células NK hacia fenotipos vinculados con la inmunidad innata generalizada (Fabisik, M., et al., 2021 y De León-Oliva, et al., 2023).

Un grupo de genes sobreexpresados, como LYPD2, TNFAIP6 y SERPINB2, exhibe trayectorias de expresión no lineales entre los diferentes grupos etarios, con niveles elevados principalmente en adultos mayores y una marcada variabilidad entre donantes. Este patrón probablemente refleja la heterogeneidad asociada al envejecimiento dentro de la población de células NK o la influencia de factores individuales, como infecciones crónicas o comorbilidades (Sen, P., et al., 2020 y Lin, D., et al., 2022).

Estos patrones de sobreexpresión revelan una activación predominante de programas transcripcionales relacionados con inflamación, respuesta a estrés y remodelación tisular en células NK senescentes, consistente con el fenómeno de *inflammaging* descrito en la literatura. El incremento coordinado de estos genes en adultos mayores, contrastando con los niveles más estables en adultos, sugiere un punto de inflexión transcripcional durante la progresión de la inmunosenescencia que podría contribuir a la disfunción inmune asociada a la edad.

## 8.6 Patrones temporales de Expresión Génica Durante el Envejecimiento

De los 83 genes diferencialmente expresados, 25 (30.1%) mostraron asociaciones significativas con la edad. Como se detalla en la Tabla 4, se observaron dos tendencias principales: una correlación positiva en genes inflamatorios y metabólicos, y una negativa en componentes de inmunidad adaptativa.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Tabla 4. Análisis de patrones temporales y modelos de trayectoria** | | | | |
| **Gen** | **Correlación (r)** | **p-adj** | **Dinámica Temporal** | **Mecanismo Sugerido** |
| *FAM131B-AS2* | +0.866 | 8.27×10⁻³ | Incremento lineal | Regulación desconocida |
| *G0S2* | +0.791 | 2.97×10⁻² | Aceleración cuadrática (ΔBIC=15.6) | Switch lipolítico / Senescencia |
| *IL1B* | +0.765 | 3.66×10⁻² | Aceleración cuadrática (R²=0.782) | Inflamaging tardío |
| *CXCL2* | +0.764 | 3.66×10⁻² | Aceleración cuadrática | Reclutamiento mieloide |
| *SERPINA1* | +0.666 | 8.92×10⁻² | Aceleración cuadrática (R²=0.643) | Respuesta compensatoria |
| *PDK4* | -0.055 | 8.95×10⁻¹ | No lineal | Switch metabólico mitocondrial |
| *IGLV1-44* | -0.952 | 1.53×10⁻³ | Declive lineal | Contracción repertorio Ig |
| *IGLV3-25* | -0.943 | 1.53×10⁻³ | Declive lineal | Contracción repertorio Ig |
| *IGHV4-59* | -0.939 | 1.53×10⁻³ | Declive lineal | Contracción repertorio Ig |
| *IGHV5-51* | -0.795 | 2.92×10⁻² | Declive cuadrático (ΔBIC=5.0) | Pérdida acelerada de diversidad |
| *IGHV4-34* | -0.852 | 1.11×10⁻² | Declive cuadrático (ΔBIC=4.7) | Pérdida acelerada de diversidad |
| *TRBV5-1* | -0.429 | 3.42×10⁻¹ | Trayectoria no lineal (ΔBIC=4.4) | Contracción del repertorio TCR |
| *IGKV1-12* | -0.074 | 8.71×10⁻¹ | Trayectoria no lineal (ΔBIC=4.4) | Dinámica de escape / Agotamiento |
| *TRDJ1* | -0.629 | 1.18×10⁻¹ | Declive lineal gradual | Reducción de vigilancia TCR |
| *TRBJ2-3* | -0.462 | 3.11×10⁻¹ | Declive lineal gradual | Reducción de vigilancia TCR |

La comparación de modelos matemáticos reveló una heterogeneidad sustancial en las dinámicas de cambio asociadas a la edad (Figura 7). Del total de genes analizados, el 39.8% fueron mejor descritos por modelos cuadráticos, el 28.9% por modelos lineales, y el 4.8% por modelos logarítmicos. Aplicando el criterio de ΔBIC ≥ 2, se identificó que el 31.3% de los genes exhiben trayectorias significativamente no lineales. Entre ellos, el 69.2% corresponden a modelos cuadráticos, sugiriendo dinámicas de aceleración o desaceleración progresiva más que una acumulación constante.

|  |
| --- |
| ![](data:image/png;base64...) |
| **Figura 7. Distribución de modelos de cambio temporal.** Proporción de genes cuya expresión es mejor descrita por trayectorias cuadráticas (39.8%), lineales (28.9%), por modelos sin cambio detectable (26.5%) o logarítmicas (4.8%), según el Criterio de Información Bayesiano (BIC). |

### Genes Inflamatorios y de Proteostasis

El análisis de patrones mostró diferencias en la activación de las vías inflamatorias. Mientras que las citocinas como IL-6 y *CXCL8* presentaron trayectorias lineales, indicativas de una acumulación gradual, otros genes como IL-1β mostraron una trayectoria cuadrática significativa, lo que indica una activación más rápida en edades avanzadas. *SERPINA1*, el gen más sobreexpresado, también presentó una dinámica cuadrática que posiblemente refleje una compensación tardía. Adicionalmente, G0S2 mostró la trayectoria cuadrática más pronunciada. Además, PDK4 (kinasa 4 de la deshidrogenasa de piruvato), un regulador mitocondrial, presentó una trayectoria no lineal, consistente con la hipótesis de una transición metabólica en la tercera edad.

### Inmunoglobulinas y Declive de la Respuesta Adaptativa

La pérdida de inmunoglobulinas no es uniforme. Varios genes mostraron trayectorias no lineales, como IGHV5-51 (ΔBIC = 5.0) y TRBV5-1 (ΔBIC = 4.4), indicando que la contracción del repertorio inmunológico presenta fases de aceleración y no es meramente lineal. La validación cruzada demostró que los modelos seleccionados generalizan adecuadamente, confirmando la robustez de estas clasificaciones temporales.

### Validación y Robustez de Resultados

Para evaluar la capacidad de generalización de los modelos seleccionados, se realizó una validación cruzada de 3 pliegues. El coeficiente de determinación promedio obtenido fue de R2=−19.95±64.11. Si bien los valores negativos reflejan la alta variabilidad, podría ser debido a la propia naturaleza de los datos de célula única y a la sensibilidad de la métrica ante el número limitado de puntos temporales, la robustez del análisis se sustenta en la consistencia de la selección del modelo óptimo. A través de las iteraciones, la clasificación de las trayectorias (lineales vs. no lineales) permaneció estable, validando que las dinámicas observadas no son producto de un sobreajuste a un conjunto específico de datos.

## 8.7 Análisis de patrones de expresión génica en subtipos de células NK durante el envejecimiento

El análisis transcriptómico evidenció distintos grados de susceptibilidad al envejecimiento entre los subtipos de células NK, sugiriendo roles específicos durante la inmunosenescencia. Los subtipos analizados incluyen células NK generales, células NK CD56 dim (CD16-positivas), células NK CD56 bright (CD16-negativas), y células NK-T (maduras, tipo I y tipo II activadas) (Figura 8).

|  |
| --- |
| ![](data:image/png;base64...)A. ![](data:image/png;base64...)B.![](data:image/png;base64...)C.![](data:image/png;base64...)D.![](data:image/png;base64...)E.![](data:image/png;base64...)F.![](data:image/png;base64...)G.![](data:image/png;base64...)H.![](data:image/png;base64...)I. ![](data:image/png;base64...)J.  ![](data:image/png;base64...) |
| **Figura 8. Heterogeneidad de la inmunosenescencia por subtipos.** Comparativa de los patrones de expresión de genes críticos (ej. *CXCL8*, *IL1B*) entre los distintos subtipos celulares, identificando a las células NK CD56dim como las más sensibles al perfil proinflamatorio tardío. |

Las células NK CD56 dim emergieron como las principales contribuyentes al fenotipo proinflamatorio asociado al envejecimiento avanzado. Los cambios más pronunciados en este subtipo incluyen grandes incrementos en el grupo de adultos mayores (>80 años) para marcadores inflamatorios y de estrés, acompañados de una pérdida casi completa de la expresión de genes relacionados con las inmunoglobulinas, de manera consistente, al ser el grupo que presenta menor variabilidad y desviación. Este patrón sugiere una transición hacia un estado altamente inflamatorio durante la senescencia avanzada.

Por su parte, las células NK generales presentaron un perfil intermedio, lo que refleja un promedio de los cambios. Muestran tendencias similares a las células CD56 dim, pero con magnitudes más moderadas. El patrón ondulatorio observado en genes como AIF1 y LST1 sugiere una regulación dinámica durante la adultez antes del incremento final en la edad avanzada.

En contraste, las células NK CD56 bright mostraron una resistencia relativa a la inmunosenescencia. La menor magnitud de cambios transcriptómicos y la ausencia de incrementos abruptos en marcadores inflamatorios sugieren que este subtipo, posiblemente debido a su estado de maduración menos terminal, mantiene mayor estabilidad funcional durante el envejecimiento.

Finalmente, las células NK-T presentaron trayectorias divergentes, con patrones heterogéneos que sugieren mecanismos compensatorios distintos de los observados en el linaje NK clásico. En resumen, estos hallazgos indican que la inmunosenescencia no afecta de manera uniforme a todas las células NK, sino que está impulsada principalmente por la desregulación del subtipo citotóxico CD56 dim.



## FASE B: Auditoría Metodológica y Efecto de Lote (Ambient RNA)

> [!WARNING]
> Los hallazgos descritos en la Fase A, particularmente el declive generalizado de las inmunoglobulinas, desencadenaron una auditoría metodológica rigurosa para descartar que estos patrones fueran producto de contaminación técnica o sesgos de secuenciación.

La observación de transcritos propios del linaje B (tales como los segmentos variables de inmunoglobulinas *IGLV2-8* e *IGHV3-23*) dentro de la población de células NK motivó un escrutinio detallado de los datos de secuenciación. Aunque el análisis descriptivo descartó la presencia física de células B o T intactas, se procedió a investigar fuentes alternativas de ruido técnico, enfocando el análisis en el fenómeno conocido como *ambient RNA* (RNA ambiental o "sopa" de RNA). 

El *ambient RNA* consiste en transcritos extracelulares liberados durante el proceso de lisis y preparación celular, los cuales pueden ser encapsulados en las gotas de secuenciación de células individuales, creando firmas de expresión espurias. Se observó que los genes ribosomales (RPS y RPL), así como las inmunoglobulinas y marcadores de células T, representaban la mayor fracción de este ruido de fondo. 

Crucialmente, al estratificar estos genes hipervariables mediante covariables técnicas, se identificó que el efecto de lote más significativo no provenía del donante o la edad de manera primaria, sino de la variable `assay` (el protocolo y equipo de secuenciación específico utilizado por cada estudio independiente). El diseño del análisis de expresión diferencial original no contemplaba esta variable de forma robusta, lo que causaba que la caída de inmunoglobulinas se correlacionara erróneamente con la edad avanzada, cuando en realidad reflejaba diferencias técnicas entre las cohortes utilizadas.

Para solucionar este sesgo, se implementó una estrategia de corrección (denominada "V4-Clean"), incorporando el diseño multivariado `~ assay + age_group` mediante el paquete estadístico PyDESeq2 y aplicando la contracción Bayesiana `apeGLM`. Este ajuste metodológico neutralizó el sesgo de lote y purgó transcritos clasificados como falsos positivos (incluyendo las inmunoglobulinas y genes como FCER1G y CCL3), destilando una firma molecular pura asociada a la senescencia.

## 8.8 Perfil Transcripcional de Células NK Envejecidas

La integración de los datos nos muestra un patrón coherente que apunta hacia un estado de activación inflamatoria crónica acompañado de respuestas protectoras sobre activadas pero aparentemente insuficientes. Los genes sobreexpresados se agrupan en módulos funcionales relacionados con inflamación, estrés oxidativo, desbalances proteolíticos y reprogramación metabólica, mientras que los genes subexpresados sugieren pérdida de componentes de reconocimiento molecular. El análisis de enriquecimiento funcional, realizado mediante múltiples bases de datos complementarias (Enrichr, gProfiler), confirma y amplía esta interpretación, revelando la activación coordinada de vías regulatorias que establecen un ciclo auto-perpetuante de inflamación y estrés oxidativo.

A continuación, presentamos los resultados de manera organizada, integrando la evidencia de expresión diferencial con las vías enriquecidas y los reguladores transcripcionales identificados.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Tabla 1. Perfil de sobre-expresión génica diferencial en células NK envejecidas | | | | | |
| **Módulo funcional** | **Gen** | **Nombre completo** | **log2FC** | **p-adj** | **Función clave** |
| Inhibidores de proteasas | *SERPINA1* | Alpha-1 Antitrypsin | 2.94 | 1.37×10⁻31 | Inhibe elastasa neutrófilos; scavenger ROS; modula NF-κB |
|  | *CST3* | Cistatina C | 1.20 | 2.58×10⁻10 | Inhibe catepsinas (cisteína proteasas) |
|  | SERPINB2 | Serpin B2 | 2.32 | 6.39×10⁻3 | Inhibe serina proteasas |
|  | TNFAIP6 | TSG-6 | 1.97 | 9.29×10⁻4 | Inducida por TNF-α; compensatoria antiinflamatoria |
| Chemokines CXC | *CXCL8* | IL-8 | 2.03 | 2.24×10⁻12 | Reclutamiento neutrófilos (más potente) |
|  | *CXCL2* | MIP-2α | 1.96 | 1.84×10⁻7 | Reclutamiento mieloide |
|  | CXCL3 | MIP-2β | 2.17 | 1.77×10⁻5 | Reclutamiento mieloide |
| Marcadores de activación | LST1 | Leukocyte Specific Transcript 1 | 1.69 | 2.82×10⁻10 | Leucocito activado |
|  | AIF1 | Allograft Inflammatory Factor 1 | 1.69 | 5.53×10⁻9 | Leucocito activado |
|  | IFI27 | Interferon-Induced Protein 27 | 1.24 | 8.5×10⁻3 | Señalización IFN crónica; antiviral |
|  | PTX3 | Pentraxin 3 | 2.55 | 4.31×10⁻5 | Proteína fase aguda; daño tisular severo |
| Citoquinas inflamatorias | *IL1B* | Interleukin-1 Beta | 1.67 | 1.44×10⁻9 | Inflammasoma NLRP3; detección DAMPs |
|  | *IL6* | Interleukin-6 | 2.01 | 1.49×10⁻2 | Efectos sistémicos pleiotrópicos |
| Generación de ROS | *DUOX1* | Dual Oxidase 1 | 1.04 | 4.57×10⁻3 | Generación de H₂O₂ y estallido respiratorio. |
| Función proteolítica | CTSL | Cathepsin L | 2.07 | 2.7×10⁻5 | Proteasa lisosomal cisteína; autofagia |
| Metabolismo | PDK4 | Pyruvate Dehydrogenase Kinase 4 | 1.44 | 4.78×10⁻6 | Bloquea piruvato→Krebs; switch glicolítico |
|  | BST1 | Bone Marrow Stromal Cell Antigen 1 | 1.08 | 2.33×10⁻3 | Consume NAD⁺; marcador senescencia |
|  | G0S2 | G0/G1 Switch 2 | 1.97 | 2.31×10⁻8 | Regulador lipolisis |
|  | DEGS2 | Delta 4-Desaturase, Sphingolipid 2 | 1.17 | 4.66×10⁻9 | Síntesis ceramidas (pro-apoptóticas) |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  | | --- | --- | --- | --- | --- | | Tabla 2. Perfil de sub-expresión génica diferencial en células NK envejecidas | | | | | | **Categoría** | **Gen** | **Nombre completo** | **log2FC** | **p-adj** | | Cadenas ligeras variables (Lambda) | *IGLV2-8* | Immunoglobulin Lambda Variable 2-8 | -1.82 | 3.39×10⁻6 | |  | IGLV1-44 | Immunoglobulin Lambda Variable 1-44 | -1.24 | 1.69×10⁻5 | |  | IGLV3-25 | Immunoglobulin Lambda Variable 3-25 | -1.49 | 5.64×10⁻5 | |  | IGLV3-19 | Immunoglobulin Lambda Variable 3-19 | -1.51 | 1.28×10⁻4 | |  | IGLV6-57 | Immunoglobulin Lambda Variable 6-57 | -1.48 | 4.91×10⁻4 | |  | IGLV7-43 | Immunoglobulin Lambda Variable 7-43 | -1.73 | 6.08×10⁻3 | |  | IGLV7-46 | Immunoglobulin Lambda Variable 7-46 | -1.08 | 1.69×10⁻2 | | Cadenas pesadas variables | *IGHV3-23* | Immunoglobulin Heavy Variable 3-23 | -1.22 | 8.62×10⁻6 | |  | IGHV3-74 | Immunoglobulin Heavy Variable 3-74 | -1.49 | 2.47×10⁻5 | |  | IGHV3-15 | Immunoglobulin Heavy Variable 3-15 | -1.58 | 6.03×10⁻5 | |  | IGHV5-51 | Immunoglobulin Heavy Variable 5-51 | -1.41 | 6.76×10⁻5 | |  | IGHV1-46 | Immunoglobulin Heavy Variable 1-46 | -1.43 | 7.83×10⁻5 | |  | IGHV1-69D | Immunoglobulin Heavy Variable 1-69D | -1.39 | 1.57×10⁻4 | |  | IGHV4-59 | Immunoglobulin Heavy Variable 4-59 | -1.36 | 1.57×10⁻4 | | Cadenas Kappa variables | IGKV3-20 | Immunoglobulin Kappa Variable 3-20 | -1.08 | 8.48×10⁻5 | |  | IGKV1-39 | Immunoglobulin Kappa Variable 1-39 | -1.23 | 1.31×10⁻4 | |  | IGKV3-15 | Immunoglobulin Kappa Variable 3-15 | -1.16 | 3.13×10⁻4 | |  | IGKV1-12 | Immunoglobulin Kappa Variable 1-12 | -1.18 | 7.39×10⁻3 | |  | IGKV2D-29 | Immunoglobulin Kappa Variable 2D-29 | -1.86 | 1.21×10⁻2 | | Receptores de células T | TRDJ1 | T Cell Receptor Delta Joining 1 | -1.94 | 3.77×10⁻4 | |  | TRBJ2-3 | T Cell Receptor Beta Joining 2-3 | -1.21 | 1.52×10⁻3 | |  | TRBV5-1 | T Cell Receptor Beta Variable 5-1 | -1.01 | 6.83×10⁻3 | |  | TRBV24-1 | T Cell Receptor Beta Variable 24-1 | -1.34 | 2.94×10⁻2 | |  | TRDV1 | T Cell Receptor Delta Variable 1 | -1.12 | 8.23×10⁻3 | | Protección mitocondrial | MT-RNR2 | Mitochondrial 16S rRNA | -9.69 | 3.17×10⁻2 | | Factor de crecimiento | CSF2 | Colony Stimulating Factor 2 (GM-CSF) | -2.03 | 4.34×10⁻4 | |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Tabla 3. Enriquecimiento funcional y regulación transcripcional | | | | | |
| **Categoría Funcional** | **Factor/Vía** | **Base de Datos (g=gProfiler, e=EnrichR)** | **Estadístico (p-adj)** | **OR** | **Relevancia Biológica** |
| Vías inflamatorias | Señalización TNF-α vía NF-κB | MSigDB Hallmark (e) | 2.26×10⁻⁷ | 22.88 | Regulador maestro de la inflamación crónica |
|  | Señalización IL-17 | KEGG (e) | 3.44×10⁻⁵ | 28.62 | Inductor de citocinas proinflamatorias y autoinmunidad |
|  | Señalización NOD-like | KEGG (e) | 2.42×10⁻³ | 24.54 | Activación del inflamasoma |
|  | Respuesta Inflamatoria | MSigDB Hallmark (e) | 4.85×10⁻² | 14.67 | Confirmación del perfil inflamatorio sistémico |
| Quimiocinas | Dominio CXC Chemokine | InterPro (e) | 1.13×10⁻⁴ | 132.7 | Enriquecimiento estructural extremo de la familia CXC |
|  | Quimiotaxis de Leucocitos | GO:BP (g) | 6.20×10⁻⁶ | - | Reclutamiento activo de células mieloides (de Oliveira et al., 2013) |
|  | Actividad de Citocinas | GO:MF (e) | 1.84×10⁻² | 10.86 | Comunicación intercelular proinflamatoria |
| TFs Inflamación | RELB (Vía alternativa NF-κB) | ChEA 2022 (e) | 3.47×10⁻⁴ | 23.53 | Activación de la rama no canónica de NF-κB |
|  | NFKB1 (clásica NF-κB) | ARCHS4 (e) | 8.18×10⁻⁶ | 15.02 | Subunidad clásica de la respuesta inmune rápida |
|  | Deficiencia de PPARG | TF Perturbations (e) | 4.52×10⁻⁵ | 18.41 | Pérdida de protección antiinflamatoria (Ahmadian et al., 2013) |
| TFs Antioxidante | NFE2L2 (NRF2) | TRRUST 2019 (e) | 5.81×10⁻³ | 67.83 | Regulador maestro antioxidante (Tonelli et al., 2018) |
| TFs Estrés | ATF3 | ARCHS4 (e) | 8.00×10⁻⁷ | 17.44 | Respuesta integrada a estrés celular múltiple |
| Regulación del Zinc | MTF1 (Metal-Regulatory TF 1) | ARCHS4 (e) | 8.00×10⁻⁷ | 17.44 | Sensor de zinc; induce metalotioneínas |
|  | ZFP36 (Tristetraprolin) | TRRUST (e) | 2.59×10⁻⁵ | 291.9 | Destabilizador de mRNA inflamatorio (dependiente de Zn) |
|  | ZFY (Zinc Finger Protein Y) | Enrichr (e) | 4.18×10⁻¹⁰ | 25.70 | Factor de transcripción ZFP estructural |
|  | ZNF217 | TF Perturbations (e) | 1.47×10⁻⁴ | 13.10 | Factor de dedos de zinc |
| Proteasas/ROS | Dominio Serpina (Serpin) | InterPro (e) | 2.53×10⁻² | 26.35 | Control de proteólisis y daño tisular |
|  | Degranulación de Neutrófilos | Reactome (e) | 2.27×10⁻² | 6.52 | Liberación de gránulos citotóxicos (Ferrarotti et al., 2018) |
| Inmunidad (Sub) | Dominio Ig V-set | InterPro (e) | 3.91×10⁻⁵⁰ | 292.0 | Pérdida masiva de dominios de reconocimiento de antígenos |
|  | Unión a Antígenos | GO:MF (g) | 3.60×10⁻⁴⁴ | - | Compromiso del reconocimiento inmunitario (Pende et al., 2019) |
|  | Respuesta Inmune Adaptativa | GO:BP (g) | 2.06×10⁻⁴⁴ | - | Fallo en la memoria inmunológica y respuesta humoral |

El análisis diferencial muestra una sobrerregulación significativa de los mediadores inflamatorios (Tabla 1). Destaca la elevación de tres miembros de la familia de quimiocinas CXC: *CXCL8* (IL-8), *CXCL2* y CXCL3. El análisis de enriquecimiento funcional (Tabla 3) confirmó asociaciones con el "Dominio de Quimiocinas CXC" y la "Quimiotaxis de Leucocitos", vinculando estos genes con procesos de reclutamiento celular y una activación coordinada del módulo proinflamatorio. Adicionalmente, identificamos la sobreexpresión de citoquinas como *IL1B* e *IL6*. Este perfil se correlacionó significativamente con las vías de señalización "NOD-like Receptor" e "IL-17".

Se observó la elevación de genes asociados a la activación de leucocitos (LST1, AIF1) y a la señalización de interferón (IFI27). También detectamos un incremento significativo en PTX3 (Tabla 1). A nivel regulatorio, el análisis de factores de transcripción (Tabla 3) identificó un enriquecimiento predominante de la familia NF-κB, incluyendo RELB (el factor más enriquecido) y las subunidades clásicas (NFKB1, NFKB2) y que podrían interpretarse como marcadores de activación inmune y regulación transcripcional. Por último, se reportó una asociación con la firma de "Deficiencia de PPARG".

El gen con mayor magnitud de cambio fue el inhibidor de proteasas *SERPINA1* (Tabla 1). También se observó la elevación de otros inhibidores, como *CST3* (inhibidor de cisteína proteasa), SERPINB2 y TNFAIP6. El enriquecimiento funcional confirmó la sobrerrepresentación del "Dominio Serpina" y el factor de transcripción NFE2L2 (NRF2) mostró un enriquecimiento significativo en múltiples bases de datos, lo que se interpretó como respuesta al estrés proteolítico. Simultáneamente, detectamos la expresión elevada de *DUOX1* (Dual Oxidase 1), enzima generadora de H₂O₂ y evidencia de una generación de especies reactivas. En el eje proteolítico, identificamos la sobreexpresión de la catepsina CTSL. El análisis de vías mostró un enriquecimiento en "Degranulación de Neutrófilos" (Tabla 3).

El perfil metabólico se caracterizó por la sobreexpresión de PDK4 y BST1 (NAD⁺-glucohidrolasa). En contraste, el gen mitocondrial MT-RNR2 presentó una subexpresión significativa (Tabla 2), mostrando alteraciones metabólicas y mitocondriales. Los demás genes subexpresados estuvieron dominados por transcritos relacionados con inmunoglobulinas (IGLV, IGHV, IGKV) y receptores de células T (TRD, TRB), siendo *IGLV2-8* el gen más reprimido (Tabla 2), lo que implicaría una pérdida de componentes de reconocimiento molecular. El enriquecimiento funcional destacó términos como "Dominio Inmunoglobulina V-set" y "Unión a Antígeno" (Tabla 3), indicando una reducción en la expresión de receptores con dominios estructurales tipo Ig.

En conjunto, los análisis presentados nos muestran una reprogramación de las células NK asociada al envejecimiento y la inmunosenescencia que va más allá de la simple pérdida de función. Hemos identificado la emergencia de un fenotipo de hiperactivación disfuncional, definido por dos fuerzas contrapuestas que operan simultáneamente: una respuesta inflamatoria y de estrés exacerbada (caracterizada por la sobreexpresión de *SERPINA1*, la secreción activa de quimiocinas y la activación sostenida de vías proinflamatorias). Por otra parte, un compromiso severo de la identidad y vigilancia inmunológica, (evidenciado por la pérdida sistemática de transcritos relacionados con el reconocimiento de antígenos y el deterioro de la capacidad bioenergética y protectora mitocondrial).

Este perfil sugiere que las células NK envejecidas dejan de comportarse como centinelas eficientes para convertirse en promotores activos del inflammaging. La coexistencia de potentes mecanismos de defensa (como la respuesta antioxidante NRF2 y la inhibición de proteasas) junto con marcadores de daño oxidativo (*DUOX1*) también nos sugiere un estado de estrés crónico no resuelto. Los hallazgos mencionados sientan las bases para la discusión, donde integraremos estos ejes en un par de modelos tratando de unificar y reconciliar las discrepancias encontradas.



## FASE C: Verdad Biológica y Dicotomía Funcional NK (V4-Clean)

> [!TIP]
> Tras la eliminación rigurosa del sesgo técnico por lote de secuenciación (*ambient RNA*), se aislaron las señales biológicas genuinas de la inmunosenescencia en células NK, revelando una divergencia funcional entre subpoblaciones.

El re-análisis transcripcional, utilizando el diseño estadístico multivariado (V4-Clean), consolidó una firma génica purificada compuesta por marcadores que previamente habían sido enmascarados o tergiversados por el ruido técnico. Entre los hallazgos confirmados destaca la subexpresión de receptores inhibidores como *KIR3DL1* y *KIR3DL2*, sugiriendo alteraciones en la calibración y el umbral de activación de las células NK senescentes. Paralelamente, se observó la sobreexpresión de genes como *LYZ* (Lisozima) y mediadores de supervivencia, confirmando una reprogramación de la inmunidad innata sin los artefactos observados en la Fase A.

Al estratificar los resultados limpios por subpoblaciones, el análisis de enriquecimiento (GSEA) reveló una marcada dicotomía funcional en la progresión hacia la senescencia de las células NK:

### Células NK CD56dim (Hiper-reactividad y Ferroptosis)
Se observó que esta subpoblación, mayoritaria y citotóxica, no transita hacia un fenotipo de agotamiento clásico (*exhaustion*), sino que mantiene un estado de memoria efectora altamente hiper-reactiva. Esta activación sostenida culmina en un estrés tóxico y daño peroxidativo de lípidos, activando vías asociadas a la Ferroptosis (Reactome). Este subtipo es el principal responsable del Fenotipo Secretor Asociado a la Senescencia (SASP) y del *inflammaging* característico de las células NK maduras.

### Células NK CD56bright (Parálisis Bioenergética)
En contraste, la subpoblación CD56bright exhibió un apagón bioenergético caracterizado por la represión de la Fosforilación Oxidativa (OXPHOS) mitocondrial. Este fenotipo se asocia a un estado de inercia proliferativa y metabólica (Efecto Warburg), evidenciando que las células menos maduras sufren un bloqueo de desarrollo en lugar de una hiperactivación destructiva.

Ambas trayectorias, aunque funcionalmente divergentes, demostraron converger en marcadores universales de estrés transcripcional y desregulación epigenética. Estos ejes constituyen el reloj biológico central de la inmunosenescencia en el linaje NK, sentando las bases para una intervención terapéutica que considere la naturaleza asimétrica del envejecimiento celular.

# 9. Discusión

El presente estudio documenta una evolución metodológica y biológica fundamental en la caracterización de la inmunosenescencia de las células NK. Inicialmente, la Fase A reveló patrones de expresión diferencial que sugerían un declive generalizado en la expresión de genes de inmunoglobulinas. Sin embargo, la posterior auditoría técnica demostró que dicho efecto era producto de contaminación por *ambient RNA* y del sesgo introducido por los distintos lotes de secuenciación. 

La implementación de un diseño estadístico riguroso (V4-Clean) permitió corregir este artefacto, revelando la verdadera reprogramación transcripcional subyacente. Los hallazgos purificados demostraron que el envejecimiento de las células NK no se caracteriza por una pérdida pasiva de función, sino por una dicotomía funcional profunda entre las subpoblaciones CD56dim y CD56bright. Esta disfunción asimétrica, marcada por estrés transcripcional y desregulación epigenética, posiciona a las células NK como promotores activos del *inflammaging*.

## 9.1 Marcadores Moleculares del Envejecimiento de Células NK

### *SERPINA1*: Marcador más prominente

*SERPINA1* emerge como el biomarcador individual más robusto, combinando la mayor magnitud de cambio y con relevancia funcional multifacética. Como inhibidor de elastasa de neutrófilos con propiedades antioxidantes y antiinflamatorias documentadas (Meghadri *et al.*, 2022), su elevación extrema representa una respuesta de emergencia ante estrés crítico.

La magnitud de este cambio en este gen supera ampliamente los umbrales de ruido técnico. Su potencial como objetivo terapéutico y como marcador diagnóstico merece más investigación. Adicionalmente, *SERPINA1* mostró el patrón de asociación más amplio entre tejidos en el análisis de la base de datos GTEx (Genotype-Tissue Expression), correlaciona con cambios en el tejido adiposo (p=9.48×10⁻⁷), la próstata y la glándula adrenal, lo que sugiere que podría servir como indicador sistémico del envejecimiento más allá de las células NK (Hu et al., 2018).

###

### Mediadores inflamatorios como panel coordinado

*CXCL8*, *IL1B* e *IL6*, constituyen un módulo que afecta a las células NK pasando de vigilantes inmunológicos a productores activos de SASP. Los incrementos que observamos de *CXCL8* en nuestro análisis, superan los reportados en otros tipos celulares inmunes durante el envejecimiento. Lo que podría significar que las células NK contribuyen al ambiente inflamatorio en individuos mayores. Estos mediadores, junto con *CXCL2* y CXCL3, muestran incrementos que contrastan con los de los inhibidores de proteasas (*SERPINA1*, *CST3*), que aumentan gradualmente desde edades tempranas. Esta coordinación temporal diferencial sugiere una progresión del envejecimiento que no es uniforme, mostrando adaptaciones compensatorias iniciales, seguidas de una transición hacia estados patológicos.

### *CST3* un biomarcador local y sistémico convergente

El gen *CST3* (cistatina C) mostró un patrón de incremento progresivo con la edad. Tradicionalmente se ha estudiado como marcador sérico de la función renal y la fragilidad (Wang & Ji, 2025), pero su expresión específica en células NK sugiere funciones locales de protección frente a la degradación proteolítica. La capacidad de ser tanto biomarcador local (células NK) y también sistémico (suero), lo posicionan como un indicador con bastante potencial del estado de salud durante el envejecimiento, potencialmente reflejando la disfunción celular y deterioro orgánico.

### Validación como biomarcadores de envejecimiento

El campo de los biomarcadores del envejecimiento ha evolucionado desde predictores de edad cronológica (relojes epigenéticos de Horvath, 2013) hasta biomarcadores que predicen la edad biológica y los resultados de salud. El Biomarkers of Aging Consortium ha establecido un marco abarcador que incluye validación biológica, analítica, predictiva y clínica, junto con criterios prácticos de AFAR sobre accesibilidad técnica y aplicabilidad translacional (Moqri et al., 2024; Tao et al., 2024).

Nuestros hallazgos cumplen satisfactoriamente con la validación biológica al reflejar mecanismos conservados evolutivamente, como la activación de NF-κB y la inflamación, centrales en el envejecimiento de múltiples especies. A diferencia de biomarcadores en sangre total, nuestro estudio aporta una especificidad celular única, permitiendo identificar la susceptibilidad diferencial entre subpoblaciones (NK CD56 dim vs bright). Además, la magnitud robusta de los cambios en *SERPINA1* y la identificación de patrones temporales informativos (declive progresivo vs activación tardía) proporcionan una riqueza biológica superior a marcadores lineales simples, todo ello siendo medible mediante técnicas estándar accesibles.

Sin embargo, existen aspectos pendientes de desarrollo para lograr una validación completa. Es esencial realizar validaciones con grupos independientes, en particular en poblaciones con mayor diversidad étnica, para mitigar sesgos de diversidad. Nuestro diseño experimental fue transversal, lo que limitó la evaluación del efecto directo; por ello, resultan necesarios estudios longitudinales para confirmar las trayectorias de envejecimiento. Finalmente, se requiere una validación funcional directa para confirmar si los cambios transcripcionales se traducen en alteraciones fenotípicas, así como una integración multiómica y la estandarización analítica de los protocolos de medición.

## 9.3 Modelos Integrativos de Inmunosenescencia Asimétrica

La evidencia transcriptómica purificada sugiere que la progresión hacia la senescencia celular diverge drásticamente según el grado de maduración de la célula NK, convergiendo en fenotipos disfuncionales distintos pero sinérgicos en su contribución al deterioro sistémico.

### Hiper-reactividad y Ferroptosis en Células NK CD56dim
Se propone que las células CD56dim, en lugar de experimentar un agotamiento clásico mediado por receptores inhibidores como PD-1, sufren de un estado de "memoria efectora patológica". La estimulación crónica a lo largo de la vida adulta mantiene a estas células en un umbral de hiper-reactividad. A nivel molecular, este estado exacerba el estrés oxidativo lipídico, precipitando cascadas metabólicas que culminan en fenotipos similares a la ferroptosis. En lugar de una muerte celular silenciosa (apoptosis), la disfunción peroxidativa provoca la secreción explosiva de DAMPs y citocinas proinflamatorias, convirtiendo a la subpoblación CD56dim en el motor primario del *inflammaging* y del Fenotipo Secretor Asociado a la Senescencia (SASP).

### Parálisis Bioenergética en Células NK CD56bright
En contraposición, las células CD56bright, que exhiben un fenotipo menos maduro, responden al estrés del envejecimiento mediante la represión de la Fosforilación Oxidativa (OXPHOS) mitocondrial. Este cambio hacia la inercia metabólica mimetiza un Efecto Warburg truncado, donde la maquinaria celular entra en un estado de preservación ineficiente. En lugar de activar vías destructivas, estas células experimentan un bloqueo en su desarrollo funcional, perdiendo la capacidad plástica para transitar hacia el estado citotóxico maduro.

## 9.4 Convergencia en el Estrés Transcripcional y Epigenético

Independientemente de la divergencia metabólica entre los subtipos, se identificó un colapso en la capacidad de responder al estrés transcripcional (evidenciado por la caída en firmas de reparación de daño por luz UV). Adicionalmente, las alteraciones en reguladores de la cromatina indican que la desregulación epigenética actúa como el reloj maestro del envejecimiento en todo el linaje NK. Estos ejes compartidos sugieren que las intervenciones terapéuticas deben dirigirse a restaurar la estabilidad genómica y epigenética, en lugar de intentar revertir las consecuencias terminales de la ferroptosis o la parálisis metabólica.

## 9.5 Implicaciones Biomédicas y Direcciones Futuras

### Potencial terapéutico: múltiples niveles de intervención

Los hallazgos derivados de este análisis transcriptómico nos permiten teorizar sobre diversos objetivos con posible potencial terapéutico, orientados a diferentes puntos de intervención dentro del ciclo de la inmunosenescencia. Comenzando con, la vía NF-κB sugiere que la modulación de este nodo crítico mediante inhibidores selectivos podría, eventualmente, atenuar el fenotipo proinflamatorio característico de las células NK envejecidas. Al respecto, compuestos como los análogos de IκB han mostrado eficacia en modelos preclínicos (Mitchell et al., 2018), lo que amerita una evaluación específica en el contexto de la senescencia inmunológica; no obstante, cualquier estrategia futura debe abordar el desafío crítico de lograr una inhibición precisa que no comprometa las respuestas inmunes esenciales del organismo.

En un enfoque nutricional y personalizado, la dependencia de zinc identificada mediante la actividad de factores como MTF1, ZFP36 y ZFY representa una oportunidad de intervención dirigida. Si bien se ha reportado que la suplementación con zinc mejora la función de las células NK en adultos mayores (Wessels et al., 2017), nuestros datos proporcionan un posible mecanismo molecular subyacente que podría refinar este enfoque. En este sentido, un ensayo clínico que evalúe la suplementación guiada por los niveles de expresión de ZFP36 podría validar una aproximación de medicina de precisión. Es fundamental considerar, sin embargo, variables como la biodisponibilidad de las distintas formas de zinc y la posible necesidad de emplear ionóforos para superar el secuestro del metal por metalotioneínas, aspectos que requieren mayor investigación experimental. De manera complementaria, la modulación metabólica emerge como una estrategia viable para corregir el desbalance metabólico sugerido por los datos. El enfoque en PDK4 para intentar restaurar el metabolismo oxidativo, o la suplementación con precursores de NAD⁺ (como NR o NMN) para contrarrestar la depleción potencialmente mediada por BST1, constituyen vías de investigación prometedoras. Estudios recientes han indicado que la elevación de NAD⁺ puede mejorar la función mitocondrial y activar las sirtuinas en diversos modelos de envejecimiento, lo cual podría correlacionarse con las alteraciones observadas en nuestra cohorte (Yusri, K., et al., 2025).

Finalmente, a una escala sistémica y celular, la terapia adoptiva con células NK y el intercambio terapéutico de plasma se perfilan como direcciones futuras de gran relevancia. La infusión de células NK activadas ex vivo ha demostrado capacidad para eliminar células senescentes y reducir el perfil de secreción SASP (Deng & Terunuma, 2024); en este contexto, nuestros resultados sugieren que dicha terapia podría optimizarse mediante la selección de subpoblaciones NK CD56 bright —potencialmente más resistentes— o mediante la modificación genética para sobreexpresar los genes protectores aquí identificados. Por otro lado, enfoques sistémicos como el intercambio terapéutico de plasma, que en combinación con IVIG ha sugerido un rejuvenecimiento de la edad biológica de hasta 2.61 años con efectos notables en la composición inmune (Fuentealba et al., 2024), podrían proporcionar el ambiente sistémico favorable necesario para potenciar la eficacia de las terapias dirigidas a las células NK. En conjunto, estas propuestas teóricas establecen una hoja de ruta para futuras validaciones funcionales que trascienden el nivel del transcriptoma.

### Hacia la medicina personalizada del envejecimiento

Esta investigación pone sobre la mesa una veta terapéutica fascinante: la posibilidad de rehabilitar la vigilancia senolítica natural de las células NK en lugar de apostar exclusivamente por fármacos senolíticos, cuya selectividad suele ser cuestionable y cuyo perfil de toxicidad constituye un riesgo latente. Al potenciar las capacidades endógenas de estas células, estaríamos aprovechando un mecanismo evolutivo diseñado específicamente para purgar el organismo de células senescentes sin comprometer el tejido sano.

Es innegable que las células NK tienen ventaja en este tablero. Como bien han documentado Antonangeli et al. (2019, citado en Deng & Terunuma, 2024), su capacidad para identificar dianas senescentes mediante la detección de ligandos de estrés, tales como MICA/B y NKG2D, les confiere una precisión quirúrgica que los senolíticos farmacológicos convencionales simplemente no pueden emular debido a sus efectos sistémicos y potencialmente deletéreos. No obstante, nuestros análisis sugieren una realidad compleja: esta función senolítica se enfrenta a un doble sabotaje biológico durante la senescencia. Por un lado, observamos una alarmante pérdida de receptores de reconocimiento (evidenciada por la caída en la expresión de genes de Ig); por otro, las NK parecen sucumbir a un fenotipo proinflamatorio que mimetiza el SASP, lo que terminaría por asfixiar su propia potencia citotóxica.

Ante este panorama, surge la duda de si el uso de inhibidores de IL-1β, como el anakinra o el canakinumab, o de IL-6, como el tocilizumab, podría ser la clave para fracturar este bucle inflamatorio, aunque, como advierten Cavalli, G., & Dinarello, C. A. (2018), cualquier intervención de este tipo exige un equilibrio clínico para no aumentar el riesgo de infecciones. Si bien todavía carecemos de herramientas para manipular directamente la expresión de los genes Ig, es plausible que la preservación de un microambiente antiinflamatorio y antioxidante ralentice su deterioro. En última instancia, el debate científico no debería centrarse únicamente en la necesidad de senolíticos externos, sino en cómo recuperar la integridad funcional de nuestras propias NK. Los mecanismos y biomarcadores que hemos desglosado aquí no son solo datos; constituyen un roadmap estratégico para la medicina de precisión en el envejecimiento.

## 9.7 Fortalezas del estudio

La robustez de este trabajo radica en que posiblemente constituye uno de los mapeos más exhaustivos realizados hasta la fecha sobre el declive de las NK. No es una cuestión menor haber integrado 193,701 células de alta fidelidad procedentes de diversas cohortes, un volumen que nos otorga un músculo estadístico difícil de ignorar. Al abarcar un arco temporal que va desde la la adultez temprana hasta la novena década de vida, hemos capturado una panorámica del ciclo vital que suele escapar a los estudios con rangos etarios más estrechos, lo que nos ha permitido identificar patrones de envejecimiento que de otro modo habrían permanecido ocultos.

Finalmente, la columna vertebral de nuestra metodología es el análisis desglosado por subtipos celulares. Mientras que la tendencia histórica ha sido tratar a las NK como una masa homogénea, nuestra aproximación parte de la premisa de que no todas las poblaciones envejecen al mismo ritmo ni bajo las mismas presiones. Esta granularidad analítica es la que, a mi juicio, realmente allana el camino para intervenciones futuras que no solo sean dirigidas, sino también verdaderamente personalizadas.

## 9.8 Limitaciones

Sin embargo, es fundamental reconocer las limitaciones inherentes a este trabajo. El diseño transversal del estudio restringe nuestra capacidad para establecer causalidad definitiva, impidiendo determinar si los cambios observados son la causa del envejecimiento o una consecuencia del mismo. Adicionalmente, al incluir adultos mayores de 80 años sanos, existe un potencial sesgo de supervivencia, lo que implica que podríamos estar analizando a "supervivientes exitosos" y subestimando el deterioro presente en la población general enferma. Asimismo, la naturaleza puramente transcriptómica del análisis implica una falta de validación funcional directa, como ensayos de citotoxicidad o secreción proteica. Finalmente, aunque mecanísticamente plausible, el modelo del posible papel del Zinc es teórico y requiere validación bioquímica directa para confirmar los niveles intracelulares de zinc y la actividad funcional de ZFP36.

## 9.9 Conclusiones

Este estudio confirma que las células NK envejecidas sufren cambios transcripcionales que alteran sus dinámicas como parte del sistema inmune. No simplemente "fallan", sino que entran en un estado hiperactivo y disfuncional. Definimos un Ciclo Oxidativo-Inflamatorio autoperpetuante donde la producción de ROS (*DUOX1*), inflamación (NF-κB) y fallos metabólicos se refuerzan mutuamente. Identificamos a *SERPINA1* como un posible biomarcador prometedor de inmunosenescencia en células NK. Adicionalmente, ponemos sobre la mesa un posible papel del Zinc que trata de explicar la falla de los controles antiinflamatorios. Finalmente, concluimos que las NK envejecidas actúan como agentes dobles: pierden su capacidad de eliminar amenazas (cáncer, células senescentes) y simultáneamente se convierten en fuentes activas de inflamación sistémica.

## 9.10 Perspectivas

El avance de esta investigación requiere un enfoque integrado que comience con estudios longitudinales, siguiendo cohortes durante décadas para validar los patrones de expresión observados y determinar los factores que influyen en sus transiciones. Complementado con una validación funcional que correlacione los perfiles transcripcionales con la capacidad citotóxica, la producción de citocinas y la eliminación de células senescentes in vitro, utilizando modelos de cultivo que evalúen directamente cómo la reprogramación celular afecta la vigilancia inmunológica.

Dentro de este marco, la validación experimental de la hipótesis del zinc surge como una prioridad; mediante la cuantificación de zinc (total y libre), la expresión de metalotioneínas y la actividad de ZFPs, se podrán realizar ensayos de rescate con suplementación que confirmen o refuten este eje metabólico. Sin embargo, la comprensión del sistema no estará completa sin la integración con otros tipos celulares mediante proteómica y transcriptómica de célula única. Al capturar las interacciones entre las células NK envejecidas con el resto de componentes del sistema inmune, podríamos entender las redes que modulan a la senescencia inmune y que trascienden a la célula individual.

Finalmente, el desarrollo de intervenciones (como podrían ser; la terapia adoptiva con NK, la modulación de NF-κB y la suplementación dirigida de zinc) debe dirigirse en la identificación de nodos críticos en el ciclo oxidativo-inflamatorio (*DUOX1*-*SERPINA1*, PDK4-NADPH, MT-RNR2). Al romper el círculo vicioso en estos puntos estratégicos, dejamos de ver a las células NK como agentes activos del *inflammaging* y comenzar a entenderlas como unidades programables capaces de restablecer la función inmune. Esto abre la posibilidad no sólo de estimular el sistema inmune, sino de rejuvenecer sus mecanismos de control fundamental y restaurar el balance homeostático en el envejecimiento.

## Declaración de uso de la IA

En el desarrollo de este trabajo se han empleado herramientas de inteligencia artificial de forma complementaria y responsable. Se empleó Claude y Gemini (modelo Sonnet 4.5 y modelo 3 respectivamente) mediante solicitudes para llevar a cabo revisiones ortográficas, gramaticales, traducciones y de cohesión textual, sin que ello sustituyera la revisión académica humana. El uso de estas herramientas ha seguido criterios éticos y metodológicos según las normativas y lineamientos propuestos por la comisión europea de investigación e innovación (2025). Por último, el uso de estas herramientas se ha limitado a funciones auxiliares, sin intervenir en la generación de ideas, análisis crítico ni redacción argumentativa principal.

# 10. Bibliografía

10x Genomics. (2023, April 18). Single-cell RNA-seq Data Normalization. Analysis Guides. https://www.10xgenomics.com/analysis-guides/single-cell-rna-seq-data-normalization

Abdelaal, T., Michielsen, L., Cats, D., Hoogduin, D., Mei, H., Reinders, M. J., & Mahfouz, A. (2019). A comparison of automatic cell identification methods for single-cell RNA sequencing data. Genome Biology, 20(1), 1-19.

Abel, A. M., Yang, C., Thakar, M. S., & Malarkannan, S. (2018). Natural Killer Cells: Development, Maturation, and Clinical Utilization. Frontiers in Immunology, 9, 1869.

Aibar, S., González-Blas, C. B., Moerman, T., Imrichova, H., Hulselmans, G., Rambow, F., ... & Aerts, S. (2017). SCENIC: Single-cell regulatory network inference and clustering. Nature Methods, 14(11), 1083-1086.

Almeida-Oliveira, A., Smith-Carvalho, M., Porto, L. C., Cardoso-Oliveira, J., Ribeiro, A. S., Falcão, R. R., ... & Diamond, H. R. (2011). Age-related changes in natural killer cell receptors from childhood through old age. Human Immunology, 72(4), 319–329.

Altschuler, S. J., & Wu, L. F. (2010). Cellular heterogeneity: do differences make a difference?. Cell, 141(4), 559–563.

Antonangeli, F., Zingoni, A., Soriani, A., & Santoni, A. (2019). Senescent cells: living or dying is a matter of NK cells. Journal of Leukocyte Biology, 105(6), 1275-1283.

Arora, J. K., James, L. K., & Charoensawan, V. (2025). Understanding and mitigating the impact of ambient mRNA contamination in single-cell RNA-sequencing analysis. *PloS one*, *20*(9), e0332440. https://doi.org/10.1371/journal.pone.0332440

Baechle, J. J., Chen, N., Makhijani, P., Winer, S., Furman, D., & Winer, D. A. (2023). Chronic inflammation and the hallmarks of aging. Molecular Metabolism, 74, 101755.

Barbosa, M. X. S., da Costa Armstrong, A., de Souza, C. D. F., et al. (2024). Pentraxin-3 (PTX-3) as a potential biomarker for predicting death in hospitalized patients with COVID-19. Virology Journal, 21, 233.

Beckman, K. B., & Ames, B. N. (1998). The free radical theory of aging matures. Physiological Reviews, 78(2), 547–581.

Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: a practical and powerful approach to multiple testing. Journal of the Royal Statistical Society: Series B, 57(1), 289–300.

Bernstein, N. J., Fong, N. L., Lam, I., Roy, M. A., Hendrickson, D. G., & Kelley, D. R. (2020). Solo: Doublet Identification in Single-Cell RNA-Seq via Semi-Supervised Deep Learning. Cell Systems, 11(1), 95–101.e5.

Bi, J., & Tian, Z. (2017). NK Cell Exhaustion. Frontiers in Immunology, 8, 760.

Björklund, A. T., Carlsten, M., Sohlberg, E., Liu, L. L., Clancy, T., Karimi, M., ... & Ljungman, M. (2016). Complete Remission with Reduction of High-Risk Clones following Haploidentical NK-Cell Therapy against MDS and AML. Clinical Cancer Research, 24(8), 1834–1844.

Börner, K., Teichmann, S. A., Quardokus, E. M., Gee, J. C., Haendel, M. A., Mahadevan, R., ... & Snyder, M. P. (2021). Anatomical structures, cell types and biomarkers of the Human Reference Atlas. Nature Cell Biology, 23(11), 1117-1128.

Brauning, A., Rae, M., Zhu, G., Fulton, E., Admasu, T. D., Stolzing, A., & Sharma, A. (2022). Aging of the Immune System: Focus on Natural Killer Cells Phenotype and Functions. Cells, 11(6), 1017.

Camous, X., Pera, A., Solana, R., & Larbi, A. (2012). NK cells in healthy aging and age-associated diseases. Journal of Biomedicine and Biotechnology, 2012, 195956.

Campisi, J., & d'Adda di Fagagna, F. (2007). Cellular senescence: When bad things happen to good cells. Nature Reviews Molecular Cell Biology, 8(9), 729-740.

Cantoni, C., Bottino, C., Vitale, M., Pessino, A., Augugliaro, R., Malaspina, A., ... & Biassoni, R. (1999). NKp44, a triggering receptor involved in tumor cell lysis by activated human natural killer cells, is a novel member of the immunoglobulin superfamily. The Journal of Experimental Medicine, 189(5), 787–796.

Cavalli, G., & Dinarello, C. A. (2018). Anakinra therapy for non-cancer inflammatory diseases. Frontiers in Pharmacology, 9, 1157.

Cerwenka, A., & Lanier, L. L. (2001). Natural killer cells, viruses and cancer. Nature Reviews Immunology, 1(1), 41–49.

Chan Zuckerberg Initiative. (s.f.). CellGuide: Natural killer cell (CL\_0000623). CZ CELLxGENE. Recuperado el 26 de agosto de 2024.

Chelyapov, N., Nguyen, T. T., & Gonzalez, R. (2022). Autologous NK cells propagated and activated ex vivo decrease senescence markers in human PBMCs. Biochemistry and Biophysics Reports, 32, 101380.

Chen, E. Y., Tan, C. M., Kou, Y., Duan, Q., Wang, Z., Meirelles, G. V., ... & Ma'ayan, A. (2013). Enrichr: interactive and collaborative HTML5 gene list enrichment analysis tool. BMC Bioinformatics, 14, 128.

Cheng, M., Zhang, Z., Hu, Z., Lin, J., Feng, X., Wang, S., ... & Xu, Q. (2020). Reprogramming of Natural Killer Cells Into Adoptive Cellular Therapy Vehicles by Targeting Cellular Senescence. Frontiers in Immunology, 11, 619930.

Childs, B. G., Durik, M., Baker, D. J., & van Deursen, J. M. (2015). Cellular senescence in aging and age-related disease: from mechanisms to therapy. Nature Medicine, 21(12), 1424-1435.

Conboy, I. M., Conboy, M. J., Wagers, A. J., Girma, E. R., Weissman, I. L., & Rando, T. A. (2005). Rejuvenation of aged progenitor cells by exposure to a young systemic environment. Nature, 433, 760-764.

Coppé, J. P., Desprez, P. Y., Krtolica, A., & Campisi, J. (2010). The senescence-associated secretory phenotype: the dark side of tumor suppression. Annual Review of Pathology, 5, 99-118.

CZI Single-Cell Biology, et al. (2023). CZ CELLxGENE Discover: A single-cell data platform for scalable exploration, analysis and modeling of aggregated data. bioRxiv. https://doi.org/10.1101/2023.10.30.563174

Dann, E., Henderson, N. C., Teichmann, S. A., et al. (2022). Differential abundance testing on single-cell data using k-nearest neighbor graphs. Nature Biotechnology, 40, 245–253.

De Leon-Oliva, D., Garcia-Montero, C., Fraile-Martinez, O., Boaru, D. L., García-Puente, L., ... & Ortega, M. A. (2023). AIF1: Function and Connection with Inflammatory Diseases. Biology, 12(5), 694.

de Oliveira, S., Reyes-Aldasoro, C. C., Candel, S., Renshaw, S. A., Mulero, V., & Calado, A. (2013). Cxcl8 (IL-8) mediates neutrophil recruitment and behavior in the zebrafish inflammatory response. Journal of Immunology, 190(8), 4349–4359.

Del Bosque Plata, L. (2016). Envejecimiento y las enfermedades comunes en nuestra sociedad. En M. Konigsberg Fainstein (Ed.), ¿Por qué envejecemos? Y otras historias… (pp. 43-58). México: CONACYT.

Deng, X., & Terunuma, H. (2024). Adoptive NK cell therapy: a potential revolutionary approach in longevity therapeutics. Immunity & Ageing, 21(1), 43.

Després-Brummer, A., Rossi, S. L., & Elias, J. E. (2020). Impact of Aging on Innate Immunity and Microglial Function in Alzheimer's Disease. Frontiers in Immunology, 11, 577711.

DrugBank. (2025). T-cell surface glycoprotein CD3 delta chain. Recuperado en Marzo 27, 2025 de https://go.drugbank.com/

European Commission. (2025). Living guidelines on the responsible use of generative AI in research (2nd ed.). Directorate-General for Research and Innovation.

Fabisik, M., Tureckova, J., Pavliuchenko, N., Kralova, J., Balounova, J., ... & Brdicka, T. (2021). Regulation of Inflammatory Response by Transmembrane Adaptor Protein LST1. Frontiers in Immunology, 12, 618332.

Fali, T., Papagno, L., Bayard, C., Mouloud, Y., Boddaert, J., Sauce, D., & Appay, V. (2019). New Insights into Lymphocyte Differentiation and Aging from Telomere Length and Telomerase Activity Measurements. Journal of Immunology, 202, 1962–1969.

Ferrarotti, I., Ottaviani, S., De Silvestri, A., & Corsico, A. G. (2018). Update on α1-antitrypsin deficiency. Breathe, 14(2), e17–e24.

Finkel, T., & Holbrook, N. J. (2000). Oxidants, oxidative stress and the biology of ageing. Nature, 408(6809), 239–247.

Franceschi, C., & Campisi, J. (2014). Chronic inflammation (inflammaging) and its potential contribution to age-associated diseases. Journals of Gerontology Series A: Biomedical Sciences and Medical Sciences, 69(Suppl\_1), S4-S9.

Franceschi, C., Garagnani, P., Parini, P., Giuliani, C., & Santoro, A. (2018). Inflammaging: a new immune–metabolic viewpoint for age-related diseases. Nature Reviews Endocrinology, 14(10), 576-590.

Fuentealba, M., Kiprov, D., Schneider, K., Mu, W. C., ... & Furman, D. (2025). Multi-Omics Analysis Reveals Biomarkers That Contribute to Biological Age Rejuvenation in Response to Single-Blinded Randomized Placebo-Controlled Therapeutic Plasma Exchange. Aging Cell, e70103.

Furman, D., Campisi, J., Verdin, E., Carrera-Bastos, P., Targ, S., Franceschi, C., Ferrucci, L., Gilroy, D. W., Fasano, A., Miller, G. W., Miller, A. H., Mantovani, A., Weyand, C. M., Barzilai, N., Goronzy, J. J., Rando, T. A., Effros, R. B., Lucia, A., Kleinstreuer, N., & Slavich, G. M. (2019). Chronic inflammation in the etiology of disease across the life span. *Nature medicine*, *25*(12), 1822–1832. https://doi.org/10.1038/s41591-019-0675-0

Gallwitz, L., Bleibaum, F., Voss, M., Schweizer, M., Spengler, K., ... & Saftig, P. (2024). Cellular depletion of major cathepsin proteases reveals their concerted activities for lysosomal proteolysis. Cellular and Molecular Life Sciences, 81(1), 227.

GeneCards. (2021). The human gene database. Journal of Molecular Biology, 433(11), 166913.

Gideon Schwarz. "Estimating the Dimension of a Model." Ann. Statist. 6 (2) 461 - 464, March, 1978. https://doi.org/10.1214/aos/1176344136

Haghverdi, L., Lun, A. T., Morgan, M. D., & Marioni, J. C. (2018). Batch effects in single-cell RNA-sequencing data are corrected by matching mutual nearest neighbors. Nature Biotechnology, 36(5), 421-427.

Haque, A., Engel, J., Teichmann, S. A., et al. (2017). A practical guide to single-cell RNA-sequencing for biomedical research and clinical applications. Genome Medicine, 9, 75.

Hazeldine, J., & Lord, J. M. (2013). The impact of ageing on natural killer cell function and potential consequences for health in older adults. Ageing Research Reviews, 12(4), 1069–1078.

Hazeldine, J., Hampson, P., & Lord, J. M. (2012). Reduced release and binding of perforin at the immunological synapse underlies the age-related decline in natural killer cell cytotoxicity. Aging Cell, 11(5), 751–759.

Hipp, M. S., Kasturi, P., & Hartl, F. U. (2019). La red de proteostasis y su declive con el envejecimiento. Nature Reviews Molecular Cell Biology, 20, 421–435.

Horvath, S. (2013). DNA methylation age of human tissues and cell types. Genome Biology, 14(10), R115.

Hou, Y., & Huttenlocher, A. (2024). Advancing chemokine research: the molecular function of *CXCL8*. Journal of Clinical Investigation, 134(10), e180984.

Hu, Y., Xu, Y., Mao, L., Lei, W., Xiang, J., Gao, L., ... & Chen, G. (2022). Gene Expression Analysis Reveals Age and Ethnicity Signatures Between Young and Old Adults in Human PBMC. Frontiers in Aging, 2, 797040.

Judge, S. J., Murphy, W. J., & Canter, R. J. (2020). Characterizing the Dysfunctional NK Cell: Assessing the Clinical Relevance of Exhaustion, Anergy, and Senescence. Frontiers in Cellular and Infection Microbiology, 10, 49.

Kale, A., Sharma, A., Stolzing, A., Desprez, P. Y., & Campisi, J. (2020). Role of immune cells in the removal of deleterious senescent cells. Immunity & Ageing, 17, 16.

Keheler, D. S. (2021). Minimising multimorbidity clustering across the lifespan. The Lancet Regional Health - Europe, 3, 100064.

Kim, S., Joe, Y., Jeong, S. O., et al. (2013). Endoplasmic reticulum stress is sufficient for the induction of IL-1β production via activation of the NF-κB and inflammasome pathways. Innate Immunity, 20(8), 799-815.

Kimmel, J. C., Penland, L., Rubinstein, N. D., Hendrickson, D. G., Kelley, D. R., & Rosenthal, A. Z. (2019). Murine single-cell RNA-seq reveals cell-identity- and tissue-specific trajectories of aging. Genome Research, 29(12), 2088–2103.

Kirkwood, T. B. (2005). Understanding the odd science of aging. Cell, 120(4), 437–447.

Kolberg, L., Raudvere, U., Kuzmin, I., Adler, P., Vilo, J., & Peterson, H. (2023). g:Profiler—interoperable web service for functional enrichment analysis and gene identifier mapping (2023 update). Nucleic Acids Research, 51(W1), W207-W212.

Kontoh-Twumasi, R., Budkin, S., Edupuganti, N., Vashishtha, A., & Sharma, S. (2024). Role of Serine Protease Inhibitors A1 and A3 in Ocular Pathologies. Investigative Ophthalmology & Visual Science, 65(2), 16.

Krizhanovsky, V., Yon, M., Dickins, R. A., Hearn, S., Simon, J., ... & Lowe, S. W. (2008). Senescence of activated stellate cells limits liver fibrosis. Cell, 134(4), 657-667.

Kuleshov, M. V., Jones, M. R., Rouillard, A. D., Fernandez, N. F., Duan, Q., ... & Ma'ayan, A. (2016). Enrichr: a comprehensive gene set enrichment analysis web server 2016 update. Nucleic Acids Research, 44(W1), W90-W97.

Lai, W., Feng, Q., Lei, W., Xiao, C., Wang, J., ... & Luo, O. J. (2025). Deciphering immunosenescence from child to frailty: Transcriptional changes, inflammation dynamics, and adaptive immune alterations. Aging Cell, e70082.

Leivas, A., Perez-Martinez, A., Blanchard, M. J., Martín-Clavero, E., Fernández, L., ... & Martinez-Lopez, J. (2018). Novel treatment strategy with autologous activated and expanded natural killer cells plus anti-myeloma drugs for multiple myeloma. Oncoimmunology, 7(12), e1502751.

Li, X., Li, C., Zhang, W., Wang, Y., Qian, P., & Huang, H. (2023). Inflammation and aging: signaling pathways and intervention therapies. Signal Transduction and Targeted Therapy, 8, 239.

Lim, O., Lee, Y., Chung, H., Her, J. H., Kang, S. M., ... & Shin, E.-C. (2013). GMP-compliant, large-scale expanded allogeneic natural killer cells have potent cytolytic activity against cancer cells in vitro and in vivo. PLoS ONE, 8(1), e53611.

Lin, D., Li, W., Zhang, N., & Cai, M. (2022). Identification of TNFAIP6 as a hub gene associated with the progression of glioblastoma by weighted gene co-expression network analysis. IET Systems Biology, 16(5), 145–156.

Liu, X., Zhang, D., Hu, J., Xu, S., Xu, C., & Shen, Y. (2023). Allograft inflammatory factor 1 is a potential diagnostic, immunological, and prognostic biomarker in pan-cancer. Aging (Albany NY), 15, 2582-2609.

Lopez, R., Regier, J., Cole, M. B., Jordan, M. I., & Yosef, N. (2018). Deep generative modeling for single-cell transcriptomics. Nature Methods, 15(12), 1053–1058.

López-Otín, C., & Bond, J. S. (2008). Proteases: multifunctional enzymes in life and disease. The Journal of Biological Chemistry, 283(45), 30433–30437.

López-Otín, C., Blasco, M. A., Partridge, L., Serrano, M., & Kroemer, G. (2013). The hallmarks of aging. Cell, 153(6), 1194-1217.

López-Otín, C., Kroemer, G., Lahoz, A., López-Gallardo, E., Mandal, S., ... & Serrano, M. (2023). Hallmarks of aging: An expanding universe. Cell, 186(2), 243-278.

Love, M. I., Huber, W., & Anders, S. (2014). Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. Genome Biology, 15(12), 550.

Luecken, M. D., & Theis, F. J. (2019). Current best practices in single-cell RNA-seq analysis: A tutorial. Molecular Systems Biology, 15(6), e8746.

Luecken, M. D., Büttner, M., Chaichoompu, K., et al. (2022). Benchmarking atlas-level data integration in single-cell genomics. Nature Methods, 19, 41–50.

Luo, O. J., Lei, W., Zhu, G., Ren, Z., Xu, Y., ... & Chen, G. (2022). Multidimensional single-cell analysis of human peripheral blood reveals characteristic features of the immune system landscape in aging and frailty. Nature Aging, 2(4), 348–364.

Lutz, C. T., Moore, M. B., Bradley, S., Shelton, B. J., & Lutgendorf, S. K. (2005). Reciprocal age related change in natural killer cell receptors for MHC class I. Mechanisms of Ageing and Development, 126(6–7), 722–731.

Mace, E. M. (2023). Human natural killer cells: form, function, and development. Journal of Allergy and Clinical Immunology, 151(2), 371-385.

Macosko, E. Z., Basu, A., Satija, R., Nemesh, J., Shekhar, K., ... & McCarroll, S. A. (2015). Highly Parallel Genome-wide Expression Profiling of Individual Cells Using Nanoliter Droplets. Cell, 161(5), 1202–1214.

Mayack, S. R., Shadrach, J. L., Kim, F. S., & Wagers, A. J. (2010). Systemic signals regulate ageing and rejuvenation of blood stem cell niches. Nature, 463, 495-500.

Meghadri, S. H., Martinez-Delgado, B., Ostermann, L., Gomez-Mariano, G., Perez-Luz, S., ... & Janciauskiene, S. (2022). Loss of Serpina1 in Mice Leads to Altered Gene Expression in Inflammatory and Metabolic Pathways. International Journal of Molecular Sciences, 23(18), 10425.

Meyer, D. H., & Schumacher, B. (2024). Aging clocks based on accumulating stochastic variation. Nature Aging, 4, 871–885.

Miltenyi Biotec. (s.f.). NK cells (human). En *MACS Handbook*. Recuperado el 24 de enero de 2026, de<https://www.miltenyibiotec.com/ES-en/support/macs-handbook/human-cells-and-organs/human-cell-types/nk-cells-human.html>

Mittelbrunn, M., & Kroemer, G. (2021). Hallmarks of T cell aging. Nature Immunology, 22(6), 687–698.

Moqri, M., Herzog, C., Poganik, J. R., Ying, K., Justice, J. N., ... & Ferrucci, L. (2024). Validation of biomarkers of aging. Nature Medicine, 30(2), 360–372.

Muthén, B. (2004). Latent Variable Analysis: Growth Mixture Modeling and Related Techniques for Longitudinal Data. In D. Kaplan (Ed.), Handbook of Quantitative Methodology for the Social Sciences (pp. 345-368). Newbury Park, CA: Sage.

https://doi.org/10.4135/9781412986311.n19

Müller-Durovic, B., Lanna, A., Covre, L. P., Mills, R. S., Henson, S. M., & Akbar, A. N. (2016). Killer Cell Lectin-like Receptor G1 Inhibits NK Cell Function through Activation of Adenosine 5'-Monophosphate-Activated Protein Kinase. The Journal of Immunology, 197(7), 2891–2899.

Nabar, N. R., Heijjer, C. N., Shi, C. S., Hwang, I. Y., Ganesan, S., ... & Kehrl, J. H. (2022). LRRK2 is required for CD38-mediated NAADP-Ca2+ signaling and the downstream activation of TFEB (transcription factor EB) in immune cells. Autophagy, 18(1), 204–222.

Naeimi Kararoudi, M., Dolatshad, H., Trikha, P., Hussain, S.-R. A., Elmas, E., ... & Lee, D. A. (2020). Generation of Knock-out Primary and Expanded Human NK Cells Using Cas9 Ribonucleoproteins. Journal of Visualized Experiments, 158, e61058.

Niccoli, T., & Partridge, L. (2012). Ageing as a Risk Factor for Disease. Current Biology, 22, R741–R752.

Ovadya, Y., Landsberger, T., Leins, H., Vadai, E., Gal, H., ... & Krizhanovsky, V. (2018). Impaired immune surveillance accelerates accumulation of senescent cells and aging. Nature Communications, 9(1), 5435.

Paul, S., & Lal, G. (2017). The Molecular Mechanism of Natural Killer Cells Function and Its Importance in Cancer Immunotherapy. Frontiers in Immunology, 8, 1124.

Pende, D., Falco, M., Vitale, M., Cantoni, C., Vitale, C., ... & Moretta, L. (2019). Killer Ig-like receptors (KIRs): Their role in NK cell modulation and developments leading to their clinical exploitation. Frontiers in Immunology, 10, 1179.

Peterson, E. E., & Barry, K. C. (2021). The natural killer-dendritic cell immune axis in anti-cancer immunity and immunotherapy. Frontiers in Immunology, 11, 621254.

Raschka, S. (2018). Model evaluation, model selection, and algorithm selection in machine learning. *arXiv preprint arXiv:1811.12808*.

Ranasinghe, M. P., Andersen, H., Dempsey, R. K., Wexler, N., Davis, R., Francois, M., Gilbert, S., Okely, A. D., Sherrington, C., & Dempsey, P. C. (2025). Contemporary national and international guidelines on physical activity and sedentary behaviour for people living with chronic conditions, disability and advanced age: a scoping review. British Journal of Sports Medicine, 59(6). https://doi.org/10.1136/bjsports-2024-108247

Rebuffet, L., Melsen, J.E., Escalière, B. et al. High-dimensional single-cell analysis of human natural killer cell heterogeneity. Nat Immunol 25, 1474–1488 (2024). https://doi.org/10.1038/s41590-024-01883-0

Robinson, M. D., McCarthy, D. J., & Smyth, G. K. (2010). edgeR: a Bioconductor package for differential expression analysis of digital gene expression data. Bioinformatics, 26(1), 139–140.

Saelens, W., Cannoodt, R., Todorov, H., & Saeys, Y. (2019). A comparison of single-cell trajectory inference methods. Nature Biotechnology, 37(5), 547-554.

Sagiv, A., Burton, D. G., Moshayev, Z., Vadai, E., Wensveen, F., ... & Krizhanovsky, V. (2016). NKG2D ligands mediate immunosurveillance of senescent cells. Aging, 8(2), 328-344.

Salminen, A., Huuskonen, J., Ojala, J., Kauppinen, A., Kaarniranta, K., & Suuronen, T. (2008). Activation of innate immunity system during aging: NF-kB signaling is the molecular culprit of inflamm-aging. Ageing Research Reviews, 7(2), 83–105.

Sarr, D., Gingerich, A. D., Asthiwi, N. M., Almutairi, F., Sautto, G. A., ... & Rada, B. (2021). Dual oxidase 1 promotes antiviral innate immunity. Proceedings of the National Academy of Sciences U.S.A., 118(26), e2017130118.

Schulz, M. T., & Rink, L. (2025). Zinc deficiency as possible link between immunosenescence and age-related diseases. Immunity & Ageing, 22, 19.

Sen, P., Helmke, A., Liao, C. M., Sörensen-Zender, I., Rong, S., ... & Schmitt, R. (2020). SerpinB2 Regulates Immune Response in Kidney Injury and Aging. Journal of the American Society of Nephrology, 31(5), 983–995.

Smirnov, A., Panatta, E., Lena, A., Castiglia, D., Di Daniele, N., Melino, G., & Candi, E. (2016). FOXM1 regulates proliferation, senescence and oxidative stress in keratinocytes and cancer cells. Aging (Albany NY), 8, 1384-1397.

Solana, R., Tarazona, R., Gayoso, I., Lesur, O., Dupuis, G., & Fulop, T. (2012). Innate immunosenescence: Effect of aging on cells and receptors of the innate immune system in humans. Seminars in Immunology, 24(5), 331–341.

Soneson, C., & Robinson, M. D. (2018). Bias, robustness and scalability in single-cell differential expression analysis. Nature Methods, 15(4), 255-261.

Soriani, A., Zingoni, A., Cerboni, C., Iannitto, M. L., Ricciardi, M. R., ... & Santoni, A. (2009). ATM-ATR-dependent up-regulation of DNAM-1 and NKG2D ligands on multiple myeloma cells by therapeutic agents results in enhanced NK-cell susceptibility and is associated with a senescent phenotype. Blood, 113(15), 3503-3511.

Stuart, T., Butler, A., Hoffman, P., Hafemeister, C., Papalexi, E., ... & Satija, R. (2019). Comprehensive Integration of Single-Cell Data. Cell, 177(7), 1888–1902.e21.

Subramanian, A., Alperovich, M., Yang, Y., & Li, B. (2022). Biology-inspired data-driven quality control for scientific discovery in single-cell transcriptomics. Genome Biology, 23(1), 267.

Svensson, V., da Veiga Beltrame, E., & Pachter, L. (2020). A curated database reveals trends in single-cell transcriptomics. Database, 2020, baaa073.

Tang, F., Barbacioru, C., Wang, Y., Nordman, E., Lee, C., ... & Surani, M. A. (2009). mRNA-Seq whole-transcriptome analysis of a single cell. Nature Methods, 6(5), 377-82.

Tao, X., Zhu, Z., Wang, L., Li, C., Sun, L., Wang, W., & Gong, W. (2024). Biomarkers of Aging and Relevant Evaluation Techniques: A Comprehensive Review. Aging and Disease, 15(3), 977–1005.

Thermo Fisher Scientific. (2025). CD3 Antibodies. Recuperado en Marzo 27, 2025 de https://www.thermofisher.com/

Tilstra, J. S., Clauson, C. L., Niedernhofer, L. J., & Robbins, P. D. (2011). NF-κB in Aging and Disease. Aging and Disease, 2(6), 449–465.

Tonelli, C., Chio, I. I. C., & Tuveson, D. A. (2018). Transcriptional regulation by Nrf2. Antioxidants & Redox Signaling, 29(17), 1727–1745.

Trapnell, C., Cacchiarelli, D., Grimsby, J., Pokharel, P., Li, S., ... & Rinn, J. L. (2014). The dynamics and regulators of cell fate decisions are revealed by pseudotemporal ordering of single cells. Nature Biotechnology, 32(4), 381–386.

Villamayor, L., López-García, D., Rivero, V., Martínez-Sobrido, L., Nogales, A., & DeDiego, M. L. (2023). The IFN-stimulated gene IFI27 counteracts innate immune responses after viral infections by interfering with RIG-I signaling. Frontiers in Microbiology, 14, 1176177.

Wang, J., Qian, Y., & Gao, M. (2018). Overexpression of PDK4 is associated with cell proliferation, drug resistance and poor prognosis in ovarian cancer. Cancer Management and Research, 11, 251–262.

Wang, X., & Ji, J. (2025). Explainable machine learning framework for biomarker discovery by combining biological age and frailty prediction. Scientific Reports, 15, 13924.

Watson, C. T., & Breden, F. (2012). *The immunoglobulin heavy chain locus: Genetic variation, missing data, and implications for human disease*. *Genes & Immunity*, 13(5), 363-373.

Wessels, I., Maywald, M., & Rink, L. (2017). Zinc as a Gatekeeper of Immune Function. Nutrients, 9(12), 1286.

Wolf, F. A., Angerer, P., Theis, F. J., et al. (2018). SCANPY: large-scale single-cell gene expression data analysis. Genome Biology, 19, 15.

Xie, Z., Bailey, A., Kuleshov, M. V., Clarke, D. J. B., Evangelista, J. E., ... & Ma’ayan, A. (2021). Gene set knowledge discovery with Enrichr. Current Protocols, 1(3), e90.

Yaku, K., Palikhe, S., Izumi, H., et al. (2021). BST1 regulates nicotinamide riboside metabolism via its glycohydrolase and base-exchange activities. Nature Communications, 12, 6767.

Yusri, K., Jose, S., Vermeulen, K.S. et al. The role of NAD+ metabolism and its modulation of mitochondria in aging and disease. npj Metab Health Dis 3, 26 (2025). https://doi.org/10.1038/s44324-025-00067-0

# 12. Figuras Suplementarias

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Tabla S1. Genes con correlaciones significativas con edad (top 10 positivas y negativas) | | | | |
| **Gen** | **Pearson r** | **p-adj** | **Dirección** | **Función** |
| FAM131B-AS2 | +0.866 | 8.27×10⁻³ | ↑ | lncRNA |
| G0S2 | +0.791 | 2.97×10⁻² | ↑ | Ciclo celular/lipólisis |
| *IL1B* | +0.765 | 3.66×10⁻² | ↑ | Citokina pro-inflamatoria |
| *CXCL2* | +0.764 | 3.66×10⁻² | ↑ | Quimiokina |
| IGLV1-44 | -0.952 | 1.53×10⁻³ | ↓ | Inmunoglobulina |
| IGLV3-25 | -0.943 | 1.53×10⁻³ | ↓ | Inmunoglobulina |
| IGHV4-59 | -0.939 | 1.53×10⁻³ | ↓ | Inmunoglobulina |
| IGHV3-21 | -0.930 | 2.02×10⁻³ | ↓ | Inmunoglobulina |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Tabla S2. Genes inflamatorios y proteostasis: modelos y breakpoints | | | | |
| **Gen** | **Modelo óptimo** | **No lineal** | **R²** | **Función** |
| *SERPINA1* | Quadratic | ✓ | 0.643 | Inhibidor proteasas |
| *IL1B* | Quadratic | ✓ | 0.782 | Citokina |
| *IL6* | Linear | ✗ | 0.485 | Citokina |
| *CXCL8* | Linear | ✗ | 0.427 | Quimiokina |
| *CXCL2* | Quadratic | ✓ | 0.766 | Quimiokina |
| G0S2 | Quadratic | ✓ | 0.937 | Metabolismo/senescencia |
| *CST3* | Quadratic | ✗ | 0.385 | Cistatina C |
| CTSL | Quadratic | ✗ | 0.590 | Catepsina L |
| PDK4 | - | ✓ | - | Metabolismo mitocondrial |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Tabla S3. Comparación de cambios transcriptómicos entre subtipos de NK | | | | | | |
| **Subtipo celular** | **Mediadores inflamatorios (*CXCL8*, *IL1B*)** | **Inhibidores de proteasas (*SERPINA1*, *CST3*)** | **Factores de activación inmune (AIF1, LST1)** | **Genes de inmunoglobulinas** | **Magnitud de cambios** | **Patrón característico** |
| **NK CD56dim (CD16+)** | ↑↑↑ en 80-85 años | ↑↑↑ en >80 años | ↑↑ en edad avanzada | ↓↓↓ pérdida casi completa | **Muy pronunciados** | Incremento tardío abrupto |
| **NK generales** | ↑↑ en edad avanzada | ↑↑ en >75 años | Patrón ondulatorio | ↓↓ gradual durante adultez | **Moderados** | Perfil intermedio/ promedio |
| **NK CD56bright (CD16-)** | Sin incrementos abruptos | ↑ gradual en *CST3* | Estables o leves cambios | ↓ mantenimiento relativo | **Leves** | Resistencia relativa |
| **NK-T** | Patrón heterogéneo | Variables | Variables | ↓↓ progresiva | **Heterogéneos** | Divergente/ compensatorio |

|  |  |  |  |
| --- | --- | --- | --- |
| **Tabla S . Publicaciones de origen para los datos** | | | |
| **ID** | **Title of the Article** | **DOI** | **Mapping Reference (Figure Label)** |
| 2 | Asian Immune Diversity Atlas (AIDA) | 10.1101/2024.06.30.601119 | Kock (2025) |
| 3 | Single-cell Atlas of common variable immunodeficiency shows germinal center-associated epigenetic dysregulation in B-cell responses | 10.1038/s41467-022-29450-x | Rodríguez-Ubreva, J. (2022) |
| 4 | Single-cell proteo-genomic reference maps of the hematopoietic system enable the purification and massive profiling of precisely defined cell states | 10.1038/s41590-021-01059-0 | Triana, S. (2021) |
| 5 | Cross-tissue immune cell analysis reveals tissue-specific features in humans | 10.1126/science.abl5197 | Domínguez Conde, C. (2022) |
| 6 | Single-cell eQTL mapping identifies cell type specific genetic control of autoimmune disease | 10.1126/science.abf3041 | Yazar, S. (2022) |
| 7 | Local and systemic responses to SARS-CoV-2 infection in children and adults | 10.1038/s41586-021-04345-x | Yoshida, M. (2022) |
| 8 | A blood atlas of COVID-19 defines hallmarks of disease severity and specificity | 10.1016/j.cell.2022.01.012 | COMBAT Consortium. (2022) |
| 9 | Immunophenotyping of COVID-19 and influenza highlights the role of type I interferons in development of severe COVID-19 | 10.1126/sciimmunol.abd1554 | Lee, J. S. (2020) |
| 10 | Single-cell multi-omics analysis of the immune response in COVID-19 | 10.1038/s41591-021-01329-2 | Stephenson, E. (2021) |
| 11 | Single-cell RNA-seq reveals the cell-type-specific molecular and genetic associations to lupus | 10.1126/science.abf1970 | Perez, R. K. (2022) |
| 13 | COVID-19 immune features revealed by a large-scale single-cell transcriptome atlas | 10.1016/j.cell.2021.01.053 | Ren, X. (2021) |
| 15 | Single-cell atlas of peripheral immune response to SARS-CoV-2 infection | 10.1038/s41591-020-0944-y | Wilk, A. J. (2020) |
| 16 | Construction of a human cell landscape at single-cell level | 10.1038/s41586-020-2157-4 | Han, X. (2020) |
| 17 | A molecular cell atlas of the human lung from single cell RNA sequencing | 10.1038/s41586-020-2922-4 | Travaglini, K. J. (2020) |
# Pregunta de Investigación y Objetivos

## 5.1 Pregunta de Investigación

¿Es posible identificar patrones de alteración en el transcriptoma de subpoblaciones de células asesinas naturales en el contexto de la inmunosenescencia mediante la integración de datos de secuenciación de RNA de célula única?

## 5.2 Hipótesis Principal

La integración de datos de secuenciación de RNA de célula única permitirá la identificación de patrones de alteración en el transcriptoma de subpoblaciones de células asesinas naturales en el contexto de la inmunosenescencia.

## 5.3 Objetivo General

Realizar el análisis transcriptómico de células asesinas naturales en el contexto de la inmunosenescencia, mediante la integración de datos de secuenciación de RNA de célula única, para identificar patrones de alteración en el transcriptoma de subpoblaciones.

## 5.4 Objetivos Específicos

* **Procesar e integrar** datos de múltiples estudios para construir un atlas transcriptómico representativo.
* **Identificar** genes diferencialmente expresados en el contexto de la inmunosenescencia.
* **Determinar** la heterogeneidad de la reacción al envejecimiento entre los distintos subtipos celulares.
* **Dilucidar** las vías biológicas comprometidas por las alteraciones transcriptómicas.

