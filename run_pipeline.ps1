# 🚀 Antigravity - Master Execution Script (Main Branch)
# This script automates the full pipeline execution for the immunosenescence project.

Write-Host "Iniciando Pipeline de Inmunosenescencia NK (Main Branch)..." -ForegroundColor Cyan

$scripts = @(
    "scripts\05-preprocessing-metadata.py",
    "scripts\00-run-pipeline.py",
    "scripts\03-consolidate-scar.py",
    "scripts\12_scar_ambient_validation.py",
    "scripts\04-adaptive-qc.py",
    "scripts\04-purify-qc-lineage.py",
    "scripts\05-doublets-solo.py",
    "scripts\13_solo_doublet_validation.py",
    "scripts\apply_mass_critical_filter.py",
    "scripts\10-pydeseq2-pseudobulk-clean.py",
    "scripts\17_differential_expression_figures.py",
    "scripts\17b_pydeseq2_visualizations.py",
    "scripts\20_functional_enrichment.py",
    "scripts\22_pseudobulk_subtypes_pydeseq2.py",
    "scripts\23_differential_abundance_milo.py",
    "scripts\24_subtypes_ranked_gsea.py",
    "scripts\25_extract_subset_cd56bright.py",
    "scripts\26_run_single_cell_scvi.py",
    "scripts\27_run_single_cell_mixedlm.py",
    "scripts\28_subtypes_mixed_gsea.py",
    "scripts\compile_integration_report.py"
)

foreach ($script in $scripts) {
    if (Test-Path $script) {
        Write-Host "=> Ejecutando $script..." -ForegroundColor Yellow
        # Nota: Un agente automatizado debe asegurar que su venv está activo antes de correr esto
        $env:PYTHONIOENCODING="utf-8"
        python $script
        if ($LASTEXITCODE -ne 0) {
            Write-Host "❌ Error detectado en $script. Pipeline detenido." -ForegroundColor Red
            exit $LASTEXITCODE
        }
    } else {
        Write-Host "⚠️ Advertencia: No se encontró $script" -ForegroundColor DarkYellow
    }
}

Write-Host "🎉 Pipeline completado con éxito." -ForegroundColor Green
