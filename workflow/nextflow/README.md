# Nextflow workflow

Run from the project root with the same config as Snakemake:

```bash
pixi run -e pipeline nextflow lint workflow/nextflow/
pixi run -e pipeline nextflow run workflow/nextflow/main.nf -params-file config/config.yaml
pixi run python scripts/compare_vcfs.py results/vcf results/nextflow/vcf
```

Processes cover QC, reference preparation, alignment, calling, filtering and
depth sensitivity. Outputs are copied into `results/nextflow/`; task inputs,
commands and cache live in `work/` and `.nextflow/`, outside Git.
`-resume` reuses tasks; `--min_depth 10 -resume -output-dir results/nextflow-d10`
changes the filter without changing the shared config file.

Checked 2026-11-22 with Nextflow 26.10.6: 32 full-pipeline tasks, exact VCF
records matching Snakemake (25, 775, 10 variants), and matching sensitivity
VCFs at all four depths. QC-only → full reused 4 tasks and ran 28; changing
depth ran only 3 filters and 3 statistics tasks, with 26 cached. Default
results were restored with all 32 cached. Wrong-directory launch failed as
expected; only that directory's temporary files were removed. Syntax lint,
execution report and cleanup of old runs passed; published outputs remained.

From [CBIO7501 lesson 10](https://khanlab.bio/cbio7501-f26/pages/10-nextflow.html).
Data Carpentry attribution is retained in `main.nf`.

`pixi run run-nextflow` verifies data and also writes
`results/nextflow/execution-report.html`. `pixi run compare-workflows` runs
both workflows and compares full variant records; CI runs this cross-check.
The task starts a new run; use the explicit Nextflow command with `-resume`
when you want to reuse existing tasks.

The separate `~/cbio7501/nextflow-practice` toy passed its two-task resume
check. The pinned `nf-core/demo` 1.2.0 test also completed successfully with
Docker's official `test,docker,emulate_amd64` profiles. Its results are in
`~/cbio7501/nf-core-demo-results`, outside this project. For real analyses,
check nf-core for an existing pipeline and pin its release; keep this
small LTEE comparison as the course workflow.

Native macOS omits CPU/memory task metrics without per-process containers;
the local execution report still provides task status and timing.
