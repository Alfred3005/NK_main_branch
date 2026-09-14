# 🚀 Antigravity - Master Execution Script (Main Branch)
# This script automates the full canonical pipeline execution for the immunosenescence project.

Write-Host "Iniciando Pipeline de Inmunosenescencia NK (Main Branch Canónico)..." -ForegroundColor Cyan

$env:PYTHONIOENCODING="utf-8"
python scripts\run_final_pipeline.py

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error detectado en la ejecución del pipeline." -ForegroundColor Red
    exit $LASTEXITCODE
} else {
    Write-Host "🎉 Pipeline completado con éxito. Reporte generado en results/Reporte_Integrativo_Subtipos_Abundancia_V2.html" -ForegroundColor Green
}
