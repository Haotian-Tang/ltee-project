# LTEE variant calling

[![Reproduce](https://github.com/Haotian-Tang/ltee-project/actions/workflows/reproduce.yml/badge.svg)](https://github.com/Haotian-Tang/ltee-project/actions/workflows/reproduce.yml)

Variant calling on three *E. coli* clones from population Ara-3 of Richard
Lenski's Long-Term Evolution Experiment, sampled at 5,000, 15,000 and 50,000
generations. Question: how many mutations accumulated, and how sensitive are
the counts to the minimum read depth used to filter variant calls?

Author: **Haotian Tang**. Built for CBIO7501, following the Data Carpentry
*Wrangling Genomics* workflow (CC BY 4.0).

## Publication

This is a course analysis of the data from Tenaillon et al. (2016), *Tempo
and mode of genome evolution in a 50,000-generation experiment*, Nature
536:165-170, [doi:10.1038/nature18959](https://doi.org/10.1038/nature18959).
It is not a reproduction of that study's complete dataset or analysis.

## Reproduce the results

Install [Pixi](https://pixi.prefix.dev/latest/installation/) and Git. The
complete pipeline supports Linux and macOS; use WSL2 on x86-64 Windows.
The default report/notebook environment also has native Windows packages.
Internet access is needed to conda-forge, Bioconda, figshare and NCBI on a
fresh installation.

```bash
git clone https://github.com/Haotian-Tang/ltee-project.git
cd ltee-project
pixi install --locked --all
pixi run reproduce
```

Open **`reports/ltee-report.html`**. The one-command workflow verifies the
seven raw-file checksums, runs Snakemake and renders the self-contained
Quarto report. Software comes from `pixi.lock`; settings are in
`config/config.yaml` and samples in `metadata/samples.tsv`. Raw data is
read-only, outputs are rebuilt and neither is stored in Git. Reproduce CI
checks the same workflow from a fresh Linux clone on each push and PR.

Other entry points:

- `pixi run run-nextflow`: the independent Nextflow implementation.
- `pixi run compare-workflows`: compare complete Nextflow/Snakemake VCF records.
- `pixi run compare-to-shell`: compare complete Snakemake/shell VCF records.
- `pixi task list`: list all tasks; see [project structure](docs/structure.md).

For [Conda/Mamba exports](envs/README.md) or the [lock-based container](containers/README.md),
follow those linked instructions. The pinned lesson-08 image predates the
workflow managers; rebuilding the Dockerfile uses the current lock.

## Hardware

No GPU is needed. A practical budget for the native workflows is **10 GB free
disk and 4 GB RAM**; additional space is needed for container images/archives.

Measured on 2026-11-24 on an Apple M5 Pro (24 GiB RAM), using four workflow
cores: a forced rebuild of all 49 Snakemake jobs took **35.70 seconds**;
`time -l` reported about **383 MiB maximum RSS**. This excludes installation,
initial download and Quarto rendering. Environments use about 3.7 GB, raw data
332 MB; the existing results tree is about 1.0 GB including earlier shell,
container and Nextflow copies. See [measurement details](docs/hardware.md).
Timing varies by machine and previously completed work can be reused.

## Outputs

| Path | Content |
| --- | --- |
| `reports/ltee-report.html` | Executed report: reads, quality, variants, depth sensitivity and software versions |
| `results/qc/multiqc/multiqc_report.html` | Combined read quality report |
| `results/vcf/` | Filtered variants per sample at the configured minimum depth |
| `results/sensitivity/` | Variant calls at minimum depths 2, 5, 10 and 15 |
| `results/bam/`, `results/stats/` | Indexed sorted alignments, flagstat and variant statistics |
| `results/nextflow/` | Independent Nextflow outputs and execution report |
| `results/shell-script/` | Independent shell baseline for cross-checking |

Expected filtered variants at **minimum depth 2**:

| Sample | Generation | Variants |
| --- | ---: | ---: |
| SRR2589044 | 5,000 | 10 |
| SRR2584863 | 15,000 | 25 |
| SRR2584866 | 50,000 | 775 |

Successful execution does not mean every FastQC module passed. Observed
WARN/FAIL flags and the limits of the depth comparison are explained in the
report and [project notes](docs/notes.md). An optional PDF can be rendered
with `pixi run quarto render reports/ltee-report.qmd --to typst`.

## Data and availability

Reads: 175,000 trimmed/subsampled read pairs per clone, prepared by Data
Carpentry, [figshare 7726454 v3](https://doi.org/10.6084/m9.figshare.7726454.v3),
file `sub.tar.gz` (14418248), **CC0**. Original SRA runs are in BioProject
**PRJNA295606**. Reference: *E. coli* B str. REL606, **GenBank CP000819.1**,
assembly **GCA_000017985.1**, downloaded from NCBI.

Exact URLs and provider MD5 checksums are in `metadata/sources.tsv`; retained
raw-file SHA256 values are in `metadata/checksums.sha256`. Sample metadata is
credited to Data Carpentry (CC BY 4.0). The [data dictionary and acquisition
record](metadata/README.md) describe the fields and source verification.
`pixi run download` recreates the input collection; `pixi run reproduce`
recreates the primary outputs. Code and the locked software specification
are available in this repository.

## Repository contents

See [docs/structure.md](docs/structure.md) for folder rules and all task
entry points, and [the workflow graph](docs/rulegraph.svg) for dependencies.
Each folder has a README. [Software versions](docs/software-versions.txt)
record both environments; `pixi.lock` records exact packages per platform.

## Cite

See [`CITATION.cff`](CITATION.cff), or GitHub's **Cite this repository** control.
[Citation instructions](docs/citation.md) include validation and APA/BibTeX
export. Cite the original paper and data when using their findings or data.

## License

Original code/configuration: **MIT** ([LICENSE](LICENSE)). Original report
text, figures and documentation: **CC BY 4.0**. Adapted Data Carpentry
workflow material retains **CC BY 4.0** and its source credits. The reads are
**CC0**; the NCBI reference retains its original terms. See
[licenses and credits](docs/licenses.md) for the complete material/source map.

## Contact

Open a [GitHub issue](https://github.com/Haotian-Tang/ltee-project/issues) for
questions or reproduction problems. Author: **haotian.tang@mbzuai.ac.ae**.
Contributions follow [CONTRIBUTING.md](CONTRIBUTING.md) and participation
follows [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
