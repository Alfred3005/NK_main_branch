# Conclusiones

A partir de los resultados del análisis transcriptómico a nivel de célula única obtenidos en esta investigación, se establecen las siguientes conclusiones respecto a la inmunosenescencia en el linaje periférico de las células NK:

## Conclusión General

Se confirma la hipótesis planteada en este trabajo. La integración de datos de secuenciación de ARN de célula única permitió identificar patrones definidos y disociados de alteración transcriptómica y dinámica poblacional entre los subtipos de células NK durante el envejecimiento. Los hallazgos demuestran que la inmunosenescencia en este linaje no obedece a un colapso funcional homogéneo ni a un estado de agotamiento clásico generalizado, sino a una reconfiguración celular diferenciada entre subtipos celulares que puede ser caracterizada por la atrofia homeostática cuantitativa del compartimento inmaduro y la instauración de una senescencia efectora armada pero anérgica en el compartimento maduro.

## Conclusiones Específicas

1. **Construcción y estandarización del atlas transcriptómico unicelular:**
   Se construyó y validó un atlas transcriptómico unicelular de alta resolución a partir de cohortes de células mononucleares de sangre periférica ($N=187$ donantes y 62,553 células). La implementación del modelo de remoción de ARN ambiental y el modelado aditivo del efecto de lote en pseudobulk mostraron reducir significativamente los sesgos técnicos sistemáticos y el ruido proinflamatorio extracelular, garantizando que las señales obtenidas correspondan exclusivamente a variaciones biológicas asociadas a la edad.

2. **Identificación de la firma de expresión génica diferencial:**
   Se determinó una firma depurada de 23 genes diferencialmente expresados ($FDR < 0.05$) asociada a la inmunosenescencia en el linaje NK. Dicha firma se distingue por la represión coordinada del receptor trófico *IL7R* y de las quimiocinas de reclutamiento intercelular *XCL1* y *XCL2*, una disminución significativa de *S100A9*, y la sobreexpresión de componentes de la maquinaria lítica citotóxica (*GZMA*, *GZMH*, *NKG7*) junto con el marcador de diferenciación terminal y senescencia replicativa *KLRG1*.

3. **Heterogeneidad y dinámica poblacional de las subpoblaciones celulares:**
   Se demostró una respuesta asimétrica al envejecimiento entre los compartimentos NK. El subconjunto inmaduro e inmunorregulador $CD56^{bright}$ experimenta una contracción poblacional cuantitativa estadísticamente significativa del 37.51% en su probabilidad de captura ($\text{RP} = 0.6249$, $p < 0.0001$), congruente con la pérdida transcripcional composicional de *IL7R*. En contraste, el subconjunto maduro $CD56^{dim}$ preserva su representación numérica relativa en sangre periférica, pero adopta un estado de diferenciación terminal.

4. **Caracterización de vías biológicas y delimitación fenotípica:**
   El análisis funcional mediante enriquecimiento de conjuntos de genes (GSEA) evidenció que el envejecimiento compromete vías biológicas divergentes según el subtipo celular:
   * **Firma de estrés genotóxico universal:** Se comprobó la acumulación de un estrés celular crónico, evidenciado por la activación de la firma de daño genotóxico (`UV Response Dn`) de manera ubicua y unificadora para todo el linaje (tanto en células $CD56^{bright}$ como en $CD56^{dim}$).
   * **Atenuación bioenergética en $CD56^{bright}$:** De forma específica, el subconjunto inmaduro sufre un colapso transcripcional de componentes de la fosforilación oxidativa mitocondrial y del ensamblaje del Complejo I.
   * **Anergia inflamatoria y falla de splicing en $CD56^{dim}$:** El subconjunto maduro presenta una represión de la maquinaria de corte y empalme (*splicing*) del ARN y un estado de anergia funcional, determinado por la represión significativa de la cascada proinflamatoria TNF-$\alpha$/NF-$\kappa$B.
   * **Delimitación del fenotipo senescente:** Se verificó que las células NK no adquieren un fenotipo secretor asociado a senescencia (SASP) autónomo ni un perfil de agotamiento inmunológico clásico (*exhaustion* de linfocitos T con sobreexpresión de *PDCD1*, *HAVCR2* o *LAG3*). En su lugar, la anergia de la vía TNF-$\alpha$/NF-$\kappa$B en el compartimento maduro configura a la célula NK como un efector armado, pero transcripcionalmente refractario ante los estímulos inflamatorios sistémicos.

En conjunto, estos hallazgos establecen un nuevo marco conceptual para el estudio de la inmunosenescencia en el linaje periférico NK. Al abandonar la extrapolación de los modelos clásicos de agotamiento linfoide, esta investigación subraya la necesidad de redirigir el enfoque traslacional: en lugar de buscar la reactivación mediante el bloqueo de puntos de control inmunitario, el rescate funcional de las células NK en la vejez dependerá del desarrollo de intervenciones enfocadas en la revitalización metabólica, la mitigación del estrés genotóxico y la restauración de su sensibilidad transcripcional.

## Declaración de uso de la IA

En el desarrollo de este trabajo se han empleado herramientas de inteligencia artificial de forma complementaria y responsable. Se empleó Claude y Gemini (modelo Sonnet 4.5 y modelo 3.1 pro respectivamente) mediante solicitudes para llevar a cabo revisiones ortográficas, gramaticales, traducciones y de cohesión textual, sin que ello sustituyera la revisión académica humana. El uso de estas herramientas ha seguido criterios éticos y metodológicos según las normativas y lineamientos propuestos por la comisión europea de investigación e innovación (2025). Por último, el uso de estas herramientas se ha limitado a funciones auxiliares, sin intervenir en la generación de ideas, análisis crítico ni redacción argumentativa principal.
