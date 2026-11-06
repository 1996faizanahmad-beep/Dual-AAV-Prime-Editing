"""Run the DUAL-AAV PRIME-DT analyses (and optionally regenerate all figures).

    python run_all.py              # advanced synthetic analyses -> outputs/advanced_analysis/
    python run_all.py --figures    # also rebuild main and Extended Data figures -> figures/
"""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
rc = subprocess.call([sys.executable, str(ROOT / "src" / "run_advanced_analysis.py")], cwd=ROOT)
if rc == 0 and "--figures" in sys.argv:
    rc = subprocess.call([sys.executable, str(ROOT / "figure_code" / "make_figures.py")], cwd=ROOT)
raise SystemExit(rc)
