# 🧬 Design Rationale & Biological Decisions

Este documento captura el contexto de diseño, los errores técnicos evitados y la justificación estadística de la metodología de la rama principal. Su objetivo es dotar de memoria a los agentes automatizados y a los investigadores humanos.

## 1. Filtrado de Masa Crítica y DDQC
La pérdida estocástica de genes en single-cell (*dropout*) genera ruido. Al establecer un umbral estricto de **>200 células por donante**, sacrificamos el volumen bruto de donantes (de 600+ a 547) pero ganamos una potencia estadística sin precedentes para el análisis pseudobulk.

## 2. La Inclusión de `assay` en PyDESeq2 (`~ assay + age_group`)
En ramas exploratorias fallidas, el análisis se realizó dividiendo por ensayo o sin control de ensayo. Eso produjo "hits" monumentales falsos como `LYZ`, `FCER1G` y `CCL3/4`. Estos genes eran marcadores mieloides que variaban drásticamente debido a las diferencias de captura entre químicas de 10x Genomics (3' vs 5'). Al incluir `assay` en el diseño aditivo y aplicar la contracción Bayesiana **apeGLM**, la señal técnica colapsó y emergió una firma pura de inmunosenescencia (KIRs, S100A8/9).

## 3. El Efecto Cancelación (Global NK)
Se detectó que analizar a las células NK como un solo grupo homogéneo generaba una falsa señal en cascada. La masiva abundancia de las CD56dim (95%) oculta fenotipos clave de las CD56bright (5%).
- Ejemplo clave: La vía `TNF-alpha via NF-kB` parecía fuertemente reprimida globalmente, pero al aislar a las CD56bright, la vía estaba significativamente activada (fenotipo SASP).

## 4. Modelos Mixtos y Abundancia (CD56bright)
La población CD56bright es extremadamente rara. 
- **Expresión:** El DEA clásico vía Pseudobulk colapsa por la falta de poder estadístico. Usamos *Modelos Mixtos Lineales (LMM)* gen-por-gen con el factor aleatorio `donante_id` para controlar el shot noise. Aunque arrojó 0 DEGs individuales tras FDR, validamos el enfoque al "rescatar" la señal funcional usando *GSEA Preranked* (31 vías detectadas).
- **Abundancia:** En lugar del test de Mann-Whitney U, que ignora el tamaño de la librería de cada donante y produce un falso negativo (p=0.16), utilizamos un **GLM Binomial**. Esto permitió ponderar la profundidad de lectura por donante y corregir por lote (`assay`), revelando una pérdida poblacional altamente significativa de CD56bright con la edad.
