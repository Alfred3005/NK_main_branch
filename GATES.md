# Gates para Análisis de Observaciones Críticas de Reproducibilidad (Dra. Yalbi Balderas)

- [x] 1. Verificación forense de la rama base de trabajo de la Dra. Yalbi (feat/post-humanizacion vs humanizada)
  - CHECK: PR #2 integrado y sincronizado en rama main (commit e5378cc).
  - EVIDENCE: Sincronización completa sin regresiones estilísticas ni de contenido.
- [x] 2. Lectura y extracción de observaciones de CORRECCIONES_REPRODUCIBILIDAD.md
  - CHECK: Documento procesado y contrastado con datos de pipeline.
  - EVIDENCE: Tablas y puntos prioritarios resueltos en su totalidad.
- [x] 3. Auditoría del conflicto de los 23 DEGs, IL7R y S100A9 frente a results/
  - CHECK: Sincronización canónica con deseq2_results_significant_nk_cell_general.csv.
  - EVIDENCE: Tabla 2, texto de Resultados, Discusión y Conclusiones actualizados con los 23 DEGs reales (S100A9 inducido +1.8753, caída de XCL1/XCL2, KIR3DL1/KIR3DL2, MAP3K8, inducción de RNF169, PTGDS, PALLD, SERGEF; eliminación limpia de IL7R sin justificaciones defensivas innecesarias).
- [x] 4. Auditoría del modelo binomial (Milo vs GLM) y sobredispersión
  - CHECK: Ejecución empírica independiente en pipeline de auditoría.
  - EVIDENCE: Ajuste quasibinomial (scale = 'X2') con sobredispersión de Pearson phi = 6.7248, SE = 0.1957, t = -2.403, p = 0.0163, OR = 0.6249, IC95% = [0.4258, 0.9170] documentado de forma compacta y calibrada en Metodología, Resultados, Discusión y Conclusiones.
- [x] 5. Auditoría de la bibliografía (49 citas faltantes y artículo retractado Mayack et al.)
  - CHECK: Purgado de Mayack et al. (2010/2011) en Introducción y reemplazo por Villeda et al. (2011).
  - EVIDENCE: Validación y preparación del catálogo bibliográfico recuperado desde Borrador_Maestro_Generado.md.
- [x] 6. Síntesis ejecutiva y reporte de impacto narrativo
  - EVIDENCE: Artefactos Auditoria_Reproducibilidad_Pipeline_Audit.md y Auditoria_Impacto_Narrativa_Tesis.md generados; compilación en Quarto (HTML y PDF) exitosa con código 0.

## Fase Bibliográfica (Resolución Exhaustiva de Citas y Referencias APA 7)

- [x] B1. Extracción y catalogación de todas las citas activas en los manuscritos de la tesis
  - CHECK: python "C:\Users\PREDATOR\.gemini\antigravity-ide\brain\378650a5-9b45-420e-b008-5a90cbc4486f\scratch\extract_citations.py"
  - EXPECT: Lista completa de pares (Autor, Año) citados en capítulos 01 al 07 y anexos.
  - EVIDENCE: 126 instancias de citas auditadas rigurosamente en los capítulos 01 al 07, index.md y anexos. 100% de correspondencia sin citas huérfanas.
- [x] B2. Recuperación y validación de referencias huérfanas (41 del borrador maestro + 8 no catalogadas + Villeda 2011)
  - CHECK: python "C:\Users\PREDATOR\.gemini\antigravity-ide\brain\378650a5-9b45-420e-b008-5a90cbc4486f\scratch\curate_references.py"
  - EXPECT: 100% de las citas emparejadas con registros bibliográficos válidos con DOI verificado.
  - EVIDENCE: 98 obras canónicas catalogadas en curated_references.json con DOIs verificados en CrossRef/PubMed (incluyendo sustitución de Mayack por Villeda 2011, Cooper 2001 y Spits 2013).
- [x] B3. Corrección de erratas en metadatos y formato APA 7 según revisión Dra. Yalbi (sección 3.3 y 3.5)
  - CHECK: Verificación de DOIs, títulos, iniciales erróneas y eliminación de obras inexistentes (Després-Brummer / Surace inventados).
  - EVIDENCE: Erradicación de Després-Brummer (reemplazado por Hazeldine & Lord 2013); corrección de Surace (Blood Advances 2021); formato APA 7 con volumen en cursiva y número de fascículo regular; títulos en tipo oración; y eliminación de et al. dentro de la lista.
- [x] B4. Escritura y ordenamiento alfabético riguroso en 08_Bibliografia.md
  - CHECK: Archivo 08_Bibliografia.md actualizado y validado.
  - EVIDENCE: Generado tesis/manuscripts/08_Bibliografia.md con 91 referencias activas ordenadas alfabéticamente (según norma APA 7 por apellido del primer autor, segundo autor y año; con sangría francesa ::: {.hanging-indent}), logrando correspondencia biunívoca con las citas del texto. Sincronizado en Capitulo10_Referencias.md.
- [x] B5. Compilación Quarto (HTML y PDF) y auditoría final de correspondencia
  - CHECK: quarto render --to pdf && quarto render --to html
  - EXPECT: Código de salida 0 en ambos renders.
  - EVIDENCE: Código de salida 0 en compilación LuaLaTeX PDF (tesis/Tesis_Final_NK.pdf, 92 páginas, 6.50 MB) y Quarto HTML (_book/index.html).

## Fase de Integración de Citas de Resultados (S100A9, SERGEF, PALLD, PTGDS, RNF169)

- [x] C1. Integración de citas en el texto de Resultados (05_Resultados.md, línea 109)
  - CHECK: Verificación de citas parentéticas (Chen et al., 2021; Wei et al., 2026), (Gateva et al., 2014; Pundlik et al., 2024; Sjölinder et al., 2002) y (Panier et al., 2012; Poulsen et al., 2012).
  - EVIDENCE: Integradas en orden alfabético estricto APA 7 en las tres afirmaciones biológicas del párrafo 109.
- [x] C2. Actualización de catálogo curated_references.json
  - CHECK: Incorporación de 7 nuevas obras con DOIs verificados en CrossRef.
  - EVIDENCE: 105 registros totales en curated_references.json (97 activos y 8 omitidos no citados).
- [x] C3. Regeneración y ordenamiento alfabético de 08_Bibliografia.md
  - CHECK: python "C:\Users\PREDATOR\.gemini\antigravity-ide\brain\378650a5-9b45-420e-b008-5a90cbc4486f\scratch\generate_08_bibliografia.py"
  - EVIDENCE: 08_Bibliografia.md actualizado con 97 referencias ordenadas alfabéticamente y sangría francesa ::: {.hanging-indent}.
- [x] C4. Sincronización de catálogo maestro en Capitulo10_Referencias.md
  - CHECK: Actualización de archivo histórico con las 7 nuevas entradas.
  - EVIDENCE: Capitulo10_Referencias.md sincronizado idénticamente con 08_Bibliografia.md.
- [x] C5. Validación de correspondencia biunívoca (cero huérfanas)
  - CHECK: python "C:\Users\PREDATOR\.gemini\antigravity-ide\brain\378650a5-9b45-420e-b008-5a90cbc4486f\scratch\verify_matches.py"
  - EXPECT: 100% de coincidencias sin citas huérfanas ni referencias omitidas.
  - EVIDENCE: Las 7 nuevas citas coinciden al 100% con sus registros bibliográficos; 0 referencias huérfanas en bibliografía activa.
- [x] C6. Compilación Quarto PDF y HTML
  - CHECK: quarto render --to pdf && quarto render --to html
  - EXPECT: Código de salida 0 en ambos renders.
  - EVIDENCE: Código de salida 0 en compilación LuaLaTeX PDF (tesis/Tesis_Final_NK.pdf, 6.82 MB, 20/10/2026 15:45:53) y Quarto HTML (_book/index.html).

## Fase de Enriquecimiento y Humanización de la Discusión (Capítulo 6)

- [x] D1. Reescritura humanizada del párrafo 2 (línea 11 de 06_Discusion.md)
  - CHECK: Integración de citas para KIR3DL1/2 (Almeida-Oliveira et al., 2011; Solana et al., 2012), MAP3K8 (Xu et al., 2018) y programas de rescate (Chen et al., 2021; Panier et al., 2012; Pundlik et al., 2024; Wei et al., 2026; Fulop et al., 2018; López-Otín et al., 2023).
  - EVIDENCE: Prosa calibrada bajo /humanizador-academico con burstiness sigma = 29.69 palabras, alternando oraciones directas con periodos complejos y 0 clichés.
- [x] D2. Reconciliación conceptual de la paradoja genotóxica (línea 20 de 06_Discusion.md)
  - CHECK: Armonización entre el enriquecimiento positivo de UV Response Dn (falla del freno fisiológico) y la inducción de RNF169 (programa compensatorio de emergencia).
  - EVIDENCE: Explicación integrada coherentemente en la subsección de daño genotóxico sin redundancias.
- [x] D3. Incorporación de Xu et al. (2018) y regeneración de 08_Bibliografia.md
  - CHECK: python "C:\Users\PREDATOR\.gemini\antigravity-ide\brain\378650a5-9b45-420e-b008-5a90cbc4486f\scratch\generate_08_bibliografia.py"
  - EVIDENCE: 98 referencias activas verificadas en correspondencia biunívoca; sincronizado con Capitulo10_Referencias.md.
- [x] D4. Compilación Quarto dual (PDF y HTML)
  - CHECK: quarto render --to pdf && quarto render --to html
  - EXPECT: Código de salida 0 en ambos renders.
  - EVIDENCE: Código de salida 0 en compilación LuaLaTeX PDF (tesis/Tesis_Final_NK.pdf, 6.82 MB, 20/10/2026 22:42:24) y Quarto HTML (_book/index.html).

## Fase E: Auditoría y Alineación de Análisis Funcionales (GSEA / ORA)

- [x] E1. Sincronización numérica y depuración de insumos (Tablas 3 y 4 de Resultados)
  - CHECK: python "scripts/verify_gsea_concordance.py"
  - EVIDENCE: Sincronización exacta de NES y FDR en Tablas 3 y 4 contra CSVs primarios; IL7R purgado de los genes destacados de GSE9650 en Tabla 4 y reemplazado por los líderes genuinos de la cúspide (*XRCC5*, *ETS1*, *PIK3CD*, *TOB1*, *KLRC1*, *ARL6IP5*); integración del párrafo ortogonal de ORA de los 23 DEGs en Capítulo 5.
- [x] E2. Blindaje conceptual y reconciliación narrativa en Resultados y Discusión
  - CHECK: Verificación textual de fundamentación metodológica (GSEA continuo Wald vs DEGs discretos apeGLM) y sincronización mecanicista (MAP3K8 como gen líder de NF-kB en Tabla 3 y Discusión; RNF169/S100A9 articulados con UV Response Dn).
  - EVIDENCE: Sección 5.6 en 05_Resultados.md y sección Discusión Inflamatoria en 06_Discusion.md actualizadas con estricta voz pasiva refleja y fundamentación bioquímica de la cascada IKK/MAPK.
- [x] E3. Verificación de figuras (fig-6 y fig-7) y referencias a Anexos
  - CHECK: Confirmación física de fig6.png y fig7.png en tesis/figures_clean/ y enriquecimiento de la sección A.4 en Anexo A con enlace directo al compendio analítico gsea_ora_master_results.md.
  - EVIDENCE: Archivos verificados y referenciados con correspondencia de identificadores @fig-6 y @fig-7.
- [x] E4. Ejecución del script forense automatizado de verificación
  - CHECK: python "scripts/verify_gsea_concordance.py"
  - EVIDENCE: Salida con código 0: "[EXITO TOTAL] Todos los criterios de concordancia funcional (GSEA/ORA) fueron superados."
- [x] E5. Compilación Quarto dual (PDF y HTML)
  - CHECK: quarto render --to pdf && quarto render --to html
  - EVIDENCE: Código de salida 0 en compilación LuaLaTeX PDF (_book/Análisis-transcriptómico-de-células-asesinas-naturales-en-el-contexto-de-la-inmunosenescencia.pdf) y Quarto HTML (_book/index.html) sin errores.
## Fase F: Comparación Forense y Auditoría del PR #3 (Dra. Yalbi) frente a main

- [x] F1. Comparación exhaustiva de 04_Metodologia.md (main vs pr-3-yalbi)
  - CHECK: git diff main..pr-3-yalbi -- tesis/manuscripts/04_Metodologia.md
  - EXPECT: Identificación línea por línea de cambios conceptuales, metodológicos, de cohortes y parámetros.
  - EVIDENCE: 21 adiciones, 19 eliminaciones. Estandarización de títulos a tipo oración, subíndices/superíndices CD56^bright^/CD56^dim^. Precisiones empíricas: especificación de SOLO en scVI v1.1.5 (umbral > 0.5); inclusión de prueba U de Mann-Whitney sobre ratios; aclaración de cohortes de pseudobulk (descarte de ensayos sin representación balanceada, filtro >= 10 cuentas en >= 3 donantes, padj < 0.05 sin corte de LFC); sustitución de g:Profiler por Enrichr (gseapy); especificación de 1,000 permutaciones, semilla 42 y límites de genes (15-500 en general, 5-1000 en firmas especializadas) en GSEA.
- [x] F2. Comparación exhaustiva de 05_Resultados.md (main vs pr-3-yalbi)
  - CHECK: git diff main..pr-3-yalbi -- tesis/manuscripts/05_Resultados.md
  - EXPECT: Identificación línea por línea de tablas, cifras numéricas, líderes GSEA, ORA y consistencia con datos primarios.
  - EVIDENCE: 78 adiciones, 56 eliminaciones. Desglose explícito de cohortes de PyDESeq2: 23 genes provienen del análisis global (420 donantes, 140,930 células de 5 ensayos); CD56dim (187 donantes, 62,553 células) y CD56bright (354 donantes, 2,814 células) no arrojaron genes con FDR < 0.05. Reemplazo de firma SASP en Tabla 4 por Reactome R-HSA-2559582 (NES = +0.877 en bright, NES = -0.913 en dim, ambos FDR > 0.25). Aclaración de que GSE9650 es conjunto DN (genes reprimidos en agotados vs memoria, indicando similitud con memoria). Sincronización de universos de genes GSEA (10,057 global, 9,644 dim, 1,872 bright), genes líderes en Tabla 3 y sustitución de "probabilidad de captura" por "momios". Incorporación de notas APA en todas las figuras y tablas.
- [x] F3. Comparación exhaustiva de 06_Discusion.md (main vs pr-3-yalbi)
  - CHECK: git diff main..pr-3-yalbi -- tesis/manuscripts/06_Discusion.md
  - EXPECT: Identificación línea por línea de matizaciones de tono, hipótesis vs afirmaciones absolutas y apego a la Verdad Biológica.
  - EVIDENCE: 25 adiciones, 25 eliminaciones. Modulación epistémica de afirmaciones absolutas hacia hipótesis comprobables: aclaración de que la ineficacia de terapias anti-PD-1 y el colapso del eje NK-cDC1 son hipótesis derivadas de la transcriptómica que requieren validación funcional directa; eliminación de metáforas ("faros de alarma"); precisión de que en el modelo enriquecido de MYC-telomerasa, TERT no se detectó y MYC no cambió; sincronización con la no significancia de gránulos líticos en CD56dim.
- [x] F4. Comparación exhaustiva de 08_Bibliografia.md (main vs pr-3-yalbi)
  - CHECK: git diff main..pr-3-yalbi -- tesis/manuscripts/08_Bibliografia.md
  - EXPECT: Identificación de referencias modificadas, retiradas (ej. Cheng et al. 2020), reconstrucción de autores y correspondencia de citas.
  - EVIDENCE: 28 adiciones, 36 eliminaciones. Purgado de 4 referencias huérfanas no citadas en texto: Broz et al. (2014), Hildner et al. (2008), Kolberg et al. (2023, g:Profiler reemplazado por Kuleshov 2016 Enrichr) y Latorre et al. (2017). Eliminación de la cita espuria Cheng et al. (2020). Reconstrucción y completado de listas de coautores en 19 obras conforme a norma APA 7 (incluyendo CZI 2025, Rebuffet 2024, Villeda 2011, Börner 2021, Fuentealba 2025). Corrección de DOIs en Fali et al. (2019) y Deng & Terunuma (2024), y URL institucional de la Comisión Europea (2024).
- [x] F5. Mapeo y análisis de correspondencia integral de los 23 puntos del correo de la Dra. Yalbi
  - CHECK: Matriz analítica de 23 puntos elaborada contrastando PR #3 frente a pipeline local.
  - EVIDENCE: 23 puntos categorizados con estatus, impacto, viabilidad y estrategia de resolución (diferenciando la opción mínima de texto/documentación de la opción de recómputo/scripts).


