# Anexo B: Versión Preliminar del Manuscrito de Tesis {#sec-anexo-b}

Como parte del compromiso con la reproducibilidad científica, la transparencia metodológica y la trazabilidad histórica del presente proyecto de investigación, este anexo consigna la referencia formal a la versión preliminar del manuscrito de tesis:

* **Título del documento original:** *Análisis transcriptómico de células asesinas naturales en el contexto de la inmunosenescencia* (Borrador con correcciones del comité tutorial y sínodo evaluador).
* **Extensión y características:** 79 páginas, estructurado bajo el flujo inicial de análisis.
* **Archivo de resguardo en el repositorio:** `Tesis_NK_05_correciones.pdf` (archivado en el repositorio de control de versiones Git del proyecto).

---

## Justificación y Trazabilidad de la Evolución Metodológica

En dicha versión preliminar se documentaron las primeras aproximaciones exploratorias de la cohorte transcriptómica, caracterizadas por:

1. **Ausencia de depuración probabilística de ARN ambiental:** En el flujo preliminar no se había implementado el algoritmo `scAR`, lo cual ocasionó que la señal proinflamatoria extracelular en muestras de adultos mayores (dominada por transcritos de origen mieloide como *CXCL8*, *IL1B*, *SERPINA1* y *CST3*) fuera preliminarmente interpretada como una activación celular directa de las células NK, fenómeno que posteriormente fue develado como contaminación del microambiente en solución.
2. **Ausencia de contracción de tasas de cambio (LFC *shrinkage*):** El análisis diferencial preliminar carecía de regularización bayesiana mediante apeGLM, lo que generaba estimaciones infladas en transcritos con conteos bajos o alta sobredispersión.
3. **Perspectiva de Flujo Único y madurez conceptual:** Con base en las recomendaciones de los revisores y sínodos evaluadores, la arquitectura de la tesis evolucionó hacia el modelo de *Flujo Único*, en el cual los artefactos técnicos y diagnósticos exploratorios se trasladaron a los anexos, reservando el cuerpo central exclusivamente para la delimitación biológica definitiva (anergia funcional, parálisis bioenergética y estrés genotóxico).

El documento íntegro en formato digital (`Tesis_NK_05_correciones.pdf`) se mantiene a disposición de los comités evaluadores y la comunidad científica en el repositorio institucional Git del proyecto.
