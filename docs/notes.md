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

## 2026-11-04 — Conda and Pixi interchange

Completed [lesson 5b](https://khanlab.bio/cbio7501-f26/pages/05b-conda-comparison.html),
source revision `7126d008236e54f0add5da879f129ec59aec32d4`, in three parts:
importing an example, exporting the pipeline, and checking compatibility.

The separate `conda-comparison/from-conda` workspace imported the example
with Python 3.13 and samtools/bcftools 1.24. Channel order and the 1.24 version
constraints were retained, a lock was generated, and both tools ran at 1.24.
The project's existing pipeline was not downgraded.

The range-based `envs/pipeline.yml` was built with micromamba 2.10.0.
Samtools and FastQC ran successfully using `micromamba run`:

| Check | Observed result |
| --- | --- |
| Conda samtools | samtools 1.25 |
| Conda FastQC | FastQC v0.13.0 |
| Conda Python | Python 3.13.18 |
| Conda Quarto, solved from ranges | 1.11.9 |
| Existing Pixi Quarto, from the lock | 1.11.9 |

Both the Conda copy and the existing locked pipeline environment reported
Quarto 1.11.9. This match does not make the range-based YAML an exact spec;
a future solve may select other permitted versions or builds. The default
Pixi environment separately locks Quarto 1.9.38, which is the value recorded
in the lesson 5 default-tool check. The three explicit exports contain the
exact locked pipeline URLs and matching checksums: 321 packages for linux-64,
and 265 each for osx-arm64 and osx-64.

For the wrong-platform exercise, Linux packages installed into `wrong-env`
on this Apple-silicon Mac, but running samtools failed with `cannot execute
binary file`, as expected. The native Conda copy, the wrong-platform copy
and this lesson's dedicated micromamba cache were removed afterwards.
The imported Pixi practice workspace remains available separately.

The project manifest, lock and pipeline/download scripts were checked against
the lesson 5 baseline and are unchanged. No data analysis was added or rerun
locally for this comparison. Installed environments are not committed.
