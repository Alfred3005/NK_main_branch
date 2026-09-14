import os
import base64
import pandas as pd

def get_image_base64(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

def run_compile_report():
    base_dir = "results/descriptive_analysis_v5"
    fig_dir = os.path.join(base_dir, "figures")
    tbl_dir = os.path.join(base_dir, "tables")
    out_html = os.path.join(base_dir, "Reporte_Descriptivo_Seccion_5_1_5_2.html")

    print(f"Compilando reporte descriptivo en {out_html}...")

    # Cargar imágenes
    img_1a = get_image_base64(os.path.join(fig_dir, "Figura_1A_Demografia_Cohorte.png"))
    img_1b = get_image_base64(os.path.join(fig_dir, "Figura_1B_QC_Purificacion_Metrics.png"))
    img_2a = get_image_base64(os.path.join(fig_dir, "Figura_2A_scVI_UMAP_Assay.png"))
    img_2b = get_image_base64(os.path.join(fig_dir, "Figura_2B_scVI_UMAP_AgeGroup.png"))
    img_3a = get_image_base64(os.path.join(fig_dir, "Figura_3A_UMAP_Subtipos_NK.png"))
    img_3b = get_image_base64(os.path.join(fig_dir, "Figura_3B_Dotplot_Marcadores_Canonicos.png"))
    img_3c = get_image_base64(os.path.join(fig_dir, "Figura_3C_Proporciones_CD56bright_Donante.png"))

    # Cargar Tabla 1
    csv_path = os.path.join(tbl_dir, "tabla1_demografia_cohorte.csv")
    tabla1_html = ""
    if os.path.exists(csv_path):
        df1 = pd.read_csv(csv_path)
        tabla1_html = df1.to_html(classes="data-table", index=False, border=0)

    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte Descriptivo y Control de Calidad - Secciones 5.1 y 5.2</title>
    <style>
        body {{
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
            margin: 0;
            padding: 30px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: #1e293b;
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        }}
        h1 {{
            color: #38bdf8;
            border-bottom: 2px solid #334155;
            padding-bottom: 15px;
            font-size: 2rem;
            text-align: center;
        }}
        h2 {{
            color: #f472b6;
            margin-top: 40px;
            border-left: 4px solid #f472b6;
            padding-left: 12px;
            font-size: 1.4rem;
        }}
        p, li {{
            color: #cbd5e1;
            line-height: 1.7;
            font-size: 1rem;
        }}
        .card {{
            background-color: #0f172a;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 20px;
            margin: 25px 0;
            text-align: center;
        }}
        .card img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
        }}
        .caption {{
            margin-top: 12px;
            font-size: 0.9rem;
            color: #94a3b8;
            font-style: italic;
        }}
        .grid-2 {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }}
        .data-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 0.95rem;
        }}
        .data-table th {{
            background-color: #334155;
            color: #38bdf8;
            padding: 12px;
            text-align: left;
        }}
        .data-table td {{
            padding: 12px;
            border-bottom: 1px solid #334155;
            color: #f1f5f9;
        }}
        .data-table tr:hover {{
            background-color: #1e293b;
        }}
        .badge {{
            background-color: #0284c7;
            color: white;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🧬 Reporte Descriptivo y Control de Calidad (Secciones 5.1 & 5.2)</h1>
        <p style="text-align: center;"><span class="badge">NK_pipeline_RNA_ambient_Main_Branch</span> <span class="badge">V5 Dedicated Output</span></p>
        
        <h2>5.1 Caracterización de la Cohorte y Purificación de Datos</h2>
        <p>A continuación se resume la estructura demográfica de la cohorte de 547 muestras purificadas (>200 células por donante), tras el protocolo de control de calidad adaptativo (DDQC), remoción de RNA ambiental (scAR) y filtrado de dobletes (SOLO).</p>
        
        <div class="card">
            <img src="{img_1a}" alt="Demografía de Cohorte">
            <div class="caption"><strong>Figura 1A: Demografía de Cohorte.</strong> Distribución de donantes por grupo de edad (Adultos vs. Adultos Mayores) estratificados por sexo (izquierda) y por ensayo/plataforma 10x Genomics (derecha).</div>
        </div>

        <div class="card">
            <img src="{img_1b}" alt="Métricas QC">
            <div class="caption"><strong>Figura 1B: Métricas de Calidad y Purificación Ambiental.</strong> Distribución de UMIs totales por célula, genes detectados y porcentaje de lecturas mitocondriales por grupo de edad y lote de secuenciación.</div>
        </div>

        <h3>Tabla 1: Resumen Demográfico y Transcriptómico de la Cohorte</h3>
        <div style="overflow-x: auto;">
            {tabla1_html}
        </div>

        <h2>5.2 Reducción de Dimensionalidad (scVI) y Definición de Subtipos</h2>
        <p>Evaluación de la eliminación del efecto de lote mediante el modelo variacional profundo (scVI) y validación de las identidades transcripcionales de las subpoblaciones NK.</p>

        <div class="grid-2">
            <div class="card">
                <img src="{img_2a}" alt="UMAP Assay">
                <div class="caption"><strong>Figura 2A: Integración scVI por Assay.</strong> Proyección UMAP latente coloreada por tecnología (10x 3' v2, 3' v3, 5') demostrando la mezcla homogénea y remoción de batch effect.</div>
            </div>
            <div class="card">
                <img src="{img_2b}" alt="UMAP Edad">
                <div class="caption"><strong>Figura 2B: Integración scVI por Edad.</strong> Proyección UMAP latente coloreada por grupo de edad (Adult vs Old).</div>
            </div>
        </div>

        <div class="grid-2">
            <div class="card">
                <img src="{img_3a}" alt="UMAP Subtipos">
                <div class="caption"><strong>Figura 3A: Subpoblaciones NK.</strong> Clusters latentes etiquetados según la identidad biológica (CD56dim vs CD56bright).</div>
            </div>
            <div class="card">
                <img src="{img_3c}" alt="Proporción CD56bright">
                <div class="caption"><strong>Figura 3C: Proporción de CD56bright por Donante.</strong> Distribución de la abundancia relativa de células CD56bright por donante en función de la edad.</div>
            </div>
        </div>

        <div class="card">
            <img src="{img_3b}" alt="Dotplot Marcadores">
            <div class="caption"><strong>Figura 3B: Dotplot de Marcadores Canónicos.</strong> Perfil de expresión relativa y fracción de células expresando los marcadores clave de identidad y función de linaje NK.</div>
        </div>

        <p style="text-align: center; margin-top: 40px; color: #64748b; font-size: 0.85rem;">Generado automáticamente por Antigravity IDE • Phoenix Protocol V5</p>
    </div>
</body>
</html>
"""

    with open(out_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"[OK] Reporte HTML descriptivo auto-contenido generado exitosamente en:\n   {out_html}")

if __name__ == "__main__":
    run_compile_report()
