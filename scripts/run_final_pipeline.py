import subprocess
import os
import sys
import time

def run_script(script_path):
    print(f"\n{'='*60}")
    print(f"EXECUTING: {script_path}")
    print(f"{'='*60}")
    
    start_time = time.time()
    
    cmd = [sys.executable, script_path]
    
    # Force UTF-8 encoding for standard streams to handle emojis on Windows
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True,
            env=env
        )
        
        for line in process.stdout:
            print(line, end="")
            
        process.wait()
        duration = time.time() - start_time
        
        if process.returncode == 0:
            print(f"\nSUCCESS: {script_path} (Took {duration:.2f}s)")
            return True
        else:
            print(f"\nFAILED: {script_path} with exit code {process.returncode}")
            return False
            
    except Exception as e:
        print(f"\nERROR launching {script_path}: {e}")
        return False

def main():
    print("\n" + "#"*60)
    print("INICIANDO AUTOMATIZACION TOTAL: PIPELINE FINAL INMACULADO")
    print("#"*60 + "\n")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)  # Ensure we are in the scripts directory for relative paths (e.g., ../data/)
    
    scripts_to_run = [
        "22_pseudobulk_subtypes_pydeseq2.py",
        "23_differential_abundance_milo.py",
        "24_subtypes_ranked_gsea.py",
        "14_run_specialized_gsea.py",
        "25_subtypes_ora.py",
        "compile_gsea_table.py",
        "compile_integration_report.py"
    ]
    
    total_start_time = time.time()
    
    for script in scripts_to_run:
        script_full_path = os.path.join(base_dir, script)
        if not os.path.exists(script_full_path):
            print(f"CRITICAL ERROR: Script not found: {script_full_path}")
            sys.exit(1)
            
        success = run_script(script_full_path)
        if not success:
            print(f"\nPipeline abortado por error en {script}")
            sys.exit(1)
            
    total_duration = time.time() - total_start_time
    print("\n" + "#"*60)
    print(f"PIPELINE FINALIZADO EXITOSAMENTE (Tiempo Total: {total_duration/60:.2f} min)")
    print("#"*60)

if __name__ == "__main__":
    main()
