# DUAL-AAV PRIME-DT

Co-transduction-aware digital twin of dual-AAV prime editing, applied as a **synthetic** computational hypothesis to LRRK2-associated Parkinson disease.

> **Interpretation boundary.** All LRRK2 outputs are synthetic model results. They are not human clinical efficacy estimates and not direct experimental evidence of LRRK2 editing. Published studies are used only as evidence constraints.

## What the model does
Each virtual cell carries AAV-A and AAV-B occupancy and propagates it through reconstitution, editing, molecular rescue and functional rescue:

`C = P(AB) x P(R|AB) x P(E|R) x P(M|E) x P(F|M)`, with `P(AB) = min[P(A)P(B)eta_AB, P(A), P(B)]` and Poisson occupancy `P(A) = 1 - exp(-lambda_A)`.

## Quick start
```bash
pip install -r requirements.txt      # or: conda env create -f environment.yml
python run_all.py                    # analyses  -> outputs/advanced_analysis/
python run_all.py --figures          # + all ten figures -> figures/
python -m pytest -q                  # checks the headline numbers quoted in the manuscripts
```

## Headline results (synthetic; seed 20261008; 10,000 virtual patients)
| Quantity | Value |
|---|---|
| Mean therapeutic coverage | 1.24% (median 0.79%; patient 5th-95th percentile 0.12-3.93%) |
| Bootstrap 95% interval of the mean | 1.21-1.26% (Monte Carlo only) |
| Patients above 0.5 / 1 / 2 / 5% coverage | 66.9 / 41.5 / 18.3 / 2.6% |
| A/B independence vs baseline | 1.17% (-5%) |
| Perfect co-transduction vs baseline | 2.16% (+74%; ratio of means 1.74; patient-level fold change median 2.08, mean 2.49) |
| +/-25% stress tests (x baseline) | delivery 0.70/1.28; co-transduction 0.78/1.18; reconstitution 0.75/1.25; editing 0.75/1.25; rescue (M+F) 0.56/1.56 |
| Value of information (nats) | editing 2.25 > co-transduction 1.42 > reconstitution 1.19 > phenotype 0.99 |

## Repository layout
```
src/                 analysis code (run_advanced_analysis.py, bayesian_calibration.py)
data/                virtual cohorts (10,000 patients; 90,000 cells), evidence ledger, calibration and sensitivity tables
outputs/             regenerated analysis outputs (created by run_all.py)
reference_outputs/   archived reference copies of the key output tables
figure_code/         matplotlib scripts for every figure (make_figures.py is the driver)
figures/             Fig. 1-10 as PNG (600 dpi, RGB), TIFF (600 dpi, LZW), PDF and SVG (vector); graphical_abstract/ (same four formats)
manuscript/          biotechnology_and_bioengineering/ (Wiley Biotechnology and Bioengineering: manuscript DOCX/PDF, APA 7 reference list, highlights, graphical-abstract caption)
source_data/         workbook of the numbers behind each figure panel
submission/          biotechnology_and_bioengineering/ (cover letter, submission checklist)
docs/                MODEL_SCOPE, REPRODUCIBILITY, FIGURE_MAP, CHANGELOG, reference_audit.csv
tests/               regression tests for the headline numbers
```

## Reproducibility scope
See [docs/REPRODUCIBILITY.md](docs/REPRODUCIBILITY.md). In brief: the cohorts, analyses, figures and headline numbers are reproducible from this repository; the scripts that generated the virtual cohort and the Sobol indices are **not** included (their outputs are provided as data).

## Known properties of the synthetic cohort
- `lambda_B = 0.92 * lambda_A` for every patient, so AAV-A and AAV-B exposure are collinear and their effects cannot be separated.
- The Frechet bound on `P(AB)` is active for 8.1% of patients.
- Sobol indices depend on unequal assumed parameter ranges.
- Performance metrics are evaluated on outcomes from the same model family (internal consistency, not external validation).

## Manuscript
- `manuscript/biotechnology_and_bioengineering/`: *Biotechnology and Bioengineering* Research Article (title page, abstract of at most 200 words with 3-6 keywords on page 2, body from page 3, APA 7 citations), with graphical abstract, 50-word caption and optional highlights. There is no supplementary material: all 10 figures and 11 tables are in the main text.
- `docs/reference_audit.csv`: every reference with its verification status. Author lists in the reference list are truncated to the first author plus et al. and must be completed to APA 7 before acceptance.

## License and citation
Code: MIT (see `LICENSE`). Please cite via `CITATION.cff`. Replace `OWNER` in `CITATION.cff` with the GitHub account once the repository is created, and consider adding a data/figure license (for example CC BY 4.0) if you want one different from MIT.
