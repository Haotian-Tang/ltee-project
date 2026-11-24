# Project structure

| Folder | Contents | Rule |
| --- | --- | --- |
| `data/raw/` | FASTQ files and compressed REL606 reference | Downloaded, checked, read-only; not committed |
| `data/processed/` | Decompressed reference and indexes | Rebuilt; not committed |
| `metadata/` | Sample sheet, sources, checksums and data dictionary | Small text files, committed |
| `scripts/` | Download, comparison and helper code | Committed, with source credits |
| `config/` | `config.yaml`, shared by both workflow engines | Committed |
| `workflow/` | Snakemake `Snakefile` and `nextflow/` implementation | Committed |
| `notebooks/` | Read exploration notebook | Source committed, outputs cleared |
| `reports/` | Quarto source and bibliography | Source committed, rendered HTML/PDF ignored |
| `results/` | QC, alignments, calls, sensitivity, statistics and logs | Rebuilt; not committed |
| `docs/` | Methods decisions, versions, rule graph and lesson notes | Committed |
| `envs/` | Conda exports generated from the Pixi environment | Export files committed; installed environments ignored |
| `containers/` | Lock-based Docker/Apptainer recipes and provenance | Recipes committed; image archives ignored |
| `.github/workflows/` | Citation, reproduction and container checks | Committed |

`pixi.toml` and `pixi.lock` define the software and tasks. Installed `.pixi/`
environments, `.snakemake/`, `.nextflow/`, `work/` and Quarto caches are ignored.

## Entry points

| Command | Purpose |
| --- | --- |
| `pixi run check` | Check Python and Quarto |
| `pixi run download` | Download or verify the seven raw files |
| `pixi run qc` | FastQC for the six FASTQ files and a MultiQC summary |
| `pixi run variant-calling` | Run the independent shell baseline |
| `pixi run run-snakemake` | Incremental QC, alignment, variants and depth sensitivity |
| `pixi run run-nextflow` | Run the Nextflow implementation and execution report |
| `pixi run compare-workflows` | Compare complete Nextflow and Snakemake VCF records |
| `pixi run compare-to-shell` | Compare complete Snakemake and shell VCF records |
| `pixi run notebook` | Execute read exploration on a fresh kernel |
| `pixi run report` | Run Snakemake, then render the standalone Quarto HTML report |
| `pixi run reproduce` | Verify inputs, run Snakemake and render the report |

Tasks select their environment automatically. For a direct pipeline tool,
use `pixi run -e pipeline TOOL`. The default environment contains the report
tools; the pipeline environment additionally contains the bioinformatics
and workflow tools. `docs/software-versions.txt` distinguishes the two.

## Template provenance

Layout generated from the [CBIO7501 project template](https://github.com/khan-lab/cbio7501-f26/tree/main/templates/cookiecutter-repro-project),
source commit `8c900ab14210187c27cdc8b82adeaf81c9ba45de` (MIT).
The original lesson-02 layout checks remain in `docs/lesson02-checks.txt`.
Earlier verification records are preserved in `docs/notes.md` and
`docs/lesson03-checks.txt` / `docs/lesson04-checks.txt`.
