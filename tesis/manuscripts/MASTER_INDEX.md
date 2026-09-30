# MASTER INDEX: TESIS NK 2

## Estructura Lógica Consolidada (Flujo Único)

1. Resumen / Summary
2. Introducción
3. Marco Teórico
4. Pregunta de Investigación, Hipótesis y Objetivos
    * *Nota: La sección de Objetivos se mantiene sin cambios según instrucción directa.*
5. Metodología
    * *Nota: Describe directamente el pipeline avanzado (V4-Clean, scAR, PyDESeq2, Milo). Incluirá el diagrama de flujo Mermaid general.*
6. Resultados
    * Abundancia Diferencial (Milo)
    * Expresión Diferencial (PyDESeq2)
    * Análisis de Enriquecimiento (GSEA/ORA)
7. Discusión
    * Enfocada en hallazgos biológicos (inflammaging, senescencia asimétrica, estrés transcripcional).
    * Breves referencias al Anexo A para justificar el rigor técnico.
8. Conclusiones
9. Bibliografía
10. Anexos
    * **Anexo A:** Análisis Exploratorio Inicial y Diagnóstico de Sesgos Técnicos (Historia de la evolución del pipeline, bimodalidad y contaminación por RNA ambiental).

## Arquitectura Narrativa ("El Enfoque Directo")
El objetivo de la tesis es presentar la investigación de forma clara, concisa y con la mayor robustez metodológica posible. Se abandona la estructura cronológica en favor de un formato científico tradicional. El trabajo inicial de diagnóstico de sesgos se mueve al Anexo A, dejando el cuerpo principal exclusivamente para la "Verdad Biológica".

**Estado Actual:**
* **Etapa de Transición Completada:** Se ajustó el paradigma estructural de la tesis al modelo de Flujo Único.
* **Capítulo 0: Resumen / Abstract (Completado):** Redactado en español e inglés, respetando la estructura asimétrica de senescencia y la metodología de depuración (scAR/apeGLM).
* **Capítulos 1-4 (Borradores Base):** Unificados y reformulados respetando la nomenclatura y la voz académica (estilo UNAM, pasiva refleja).
* **Capítulo 5: Resultados (Completado y Auditado Canónicamente):** Redactado bajo la "Opción A" (descriptivo empírico riguroso, sin redundancias metodológicas ni especulaciones prematuras). Integró con exactitud:
  - Cohorte global ($N=423$ donantes, 143,991 células) y cohorte balanceada libre de colinealidad ($N=187$ donantes, 62,553 células).
  - Abundancia diferencial del nicho *CD56bright* por GLM Binomial ($p < 0.0001$, $\beta = -0.4702$, $\text{RP} = 0.6249$, reducción relativa del 37.51%).
  - Firma limpia de 23 DEGs de alta confianza ($FDR < 0.05$) mediante PyDESeq2 y contracción apeGLM (colapso de *IL7R*, silenciamiento de *XCL1*/*XCL2*, represión genuina de *S100A9*, activación lítica efectora *GZMA*/*GZMH*/*NKG7*/*KLRG1*).
  - GSEA Tricéfalo: Parálisis bioenergética mitocondrial en *CD56bright*, estrés genotóxico crónico y fallas de *splicing* en *CD56dim*, y ausencia de agotamiento inmune clásico.
* **Capítulo 6: Discusión (Completado y Consolidado Definitivamente):** Estructurado en estricta prosa académica pasiva refleja (UNAM) y optimizado en un bloque narrativo continuo:
  - **Dinámica y Bioenergética (Cuerpo Introductorio):** Contracción poblacional del 37.51% (GLM Binomial) validada por represión global de *IL7R*, acoplada al colapso de la fosforilación oxidativa mitocondrial (asfixia bioenergética) y anergia transcripcional pura (TNF-$\alpha$/NF-$\kappa$B).
  - **6.1 Delimitación Fenotípica e Impacto Sistémico:** Ausencia de SASP y agotamiento clásico (PD-1/TIM-3). Acumulación de estrés genotóxico (UV Response Dn). La célula NK queda "armada pero bloqueada", lo que impide la senólisis periférica y consolida un bucle sistémico de inflammaging, reflejado indirectamente en el ARN ambiental (CXCL8, IL1B).
  - **6.2 Perspectivas y limitaciones:** Ceguera quimiotáctica por caída de *XCL1*/*XCL2* hacia cDC1, ineficacia de inmunoterapias tradicionales (anti-PD-1) y la necesidad de priorizar superagonistas de IL-15.
* **Capítulo 7: Conclusiones (Completado y Auditado Canónicamente):** Estructurado bajo el formato jerárquico formal de maestría (UNAM). Contiene la validación y confirmación directa de la Hipótesis Principal y del Objetivo General, articulada con cuatro conclusiones específicas numeradas que dan respuesta biunívoca a cada objetivo específico (control de sesgo técnico con scAR/PyDESeq2, firma de 23 genes, contracción poblacional del 37.51% en *CD56bright*, y delimitación fenotípica de anergia/asimetría metabólica sin SASP ni agotamiento clásico).
* **Capítulo 1 e Introducción (Revisión y Ajuste Fino):** Pulido estilístico y conceptual, reforzando la perspectiva senolítica de las células NK y la justificación de la resolución unicelular.
* **Capítulo 2: Marco Teórico (Depuración Temática y Sincronización Canónica):** Se eliminó el pilar huérfano de proteostasis consolidando los dos pilares primarios rectores (inestabilidad genómica y acortamiento telomérico). Se integró formalmente la definición de envejecimiento de la Organización Mundial de la Salud (OMS, 2015; Varela Pinedo, 2016) y se adoptó formalmente la denominación en español *envejecimiento inflamatorio* (*inflammaging*).
* **Referencias Bibliográficas:** Sincronizadas canónicamente en formato APA en `08_Bibliografia.md` (41 entradas completas numeradas de forma continua del 1 al 41).
* **Atención y Respuesta al Sínodo Evaluador (Completada):** Se estructuraron y blindaron las cartas/correos de respuesta para el comité tutorial y sínodo completo:
  - **Dra. Mariel Maldonado:** Justificación de la exclusión de *IFI27* (Torres-Machorro et al., 2024) por remoción de ARN ambiental (`scAR`), depuración de firmas de hiperinflación (*CXCL8*, *SERPINA1*) y consolidación de la firma de 23 genes.
  - **Dra. Juana Rosado Pérez:** Compactación integral de Resultados (eliminando tablas saturadas hacia Anexos) alineada directamente a objetivos e hipótesis.
  - **Dra. Leda Torres:** Resolución de 27 observaciones (estricta distinción entre ARNm y proteínas, cursivas para genes, reordenamiento lógico con Marco Teórico antes de Hipótesis, criterios independientes de inclusión/exclusión y modelos en español).
  - **Dr. Humberto Gutiérrez González y Dr. Víctor Manuel Mendoza Núñez:** Comunicaciones ejecutivas de entrega del manuscrito definitivo consolidado previo al examen de grado.
* **Próximo Paso Inmediato:** Redactar el **Anexo A** (Historia de la evolución del pipeline, bimodalidad y contaminación por RNA ambiental) y proceder a la compilación final en **Quarto/LaTeX** para la entrega formal y programación del examen.
