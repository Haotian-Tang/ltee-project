# Project notes

## 2026-11-03 — Pixi environments and pipeline

The work is grouped into environment configuration, pipeline tasks, and
reproduction documentation. It follows
[lesson 05](https://khanlab.bio/cbio7501-f26/pages/05-pixi.html), source
revision `b0f36d9713bd53f9e9675e2bbda238a5b512b595`.

The default environment retains four platforms. The pipeline feature is
limited to Linux/macOS because the tested default-environment solve could
not find BWA for Windows. Both local environments were installed from the
lock with `pixi install --locked --all`.

| Tool | Verified local version |
| --- | --- |
| python | Python 3.13.18 |
| quarto | 1.9.38 |
| fastqc | FastQC v0.13.0 |
| multiqc | multiqc, version 1.35 |
| bwa | Version: 0.7.19-r1273 |
| samtools | samtools 1.25 |
| bcftools | bcftools 1.25 |

The current solve uses samtools and bcftools 1.25 rather than the lesson's
1.24 example. Exact builds for every supported platform are in `pixi.lock`.

### Local reproduction

`pixi run reproduce` completed successfully. It generated six FastQC reports,
a MultiQC report, three indexed sorted BAMs, filtered VCFs and statistics.
Samtools quickcheck passed for all three BAMs. The retained raw files still
match all seven recorded SHA-256 checksums and remain read-only.

| Sample | Generation | Filtered variants, minimum depth 2 |
| --- | ---: | ---: |
| SRR2589044 | 5,000 | 10 |
| SRR2584863 | 15,000 | 25 |
| SRR2584866 | 50,000 | 775 |

These counts match the lesson 05 example. No alternative depth comparison
was run. FastQC reported per-base sequence content FAIL for three files and
WARN for three; all six had WARN for per-sequence GC content and sequence
length distribution. These are recorded report flags, not pipeline execution
errors. No additional trimming or filtering of the raw reads was performed.

### Environment practice

- FastQC 0.12.1 help includes `-o`; 0.13.0 uses `--outdir`.
- The separate `~/cbio7501/pixi-practice` environment was cleaned and rebuilt
  with `pixi install --locked`; its lock and samtools version were unchanged.
- Samtools was changed to 1.21, then an old lock against the changed manifest
  was correctly rejected by `--locked`. The workspace was restored to 1.25.
- Cookiecutter 2.7.1 was installed with `pixi global` and its user bin directory
  made available to new zsh sessions.

The optional HPC exercise and neighbor swap were not performed. The GitHub
Reproduce workflow is the fresh-Linux-clone check for this project. Downloaded
data, installed environments and generated results stay outside Git.
