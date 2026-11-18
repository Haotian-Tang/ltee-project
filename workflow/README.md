# Snakemake workflow

Run from the project root:

```bash
pixi run -e pipeline snakemake -n
pixi run -e pipeline snakemake --cores 4
pixi run python scripts/compare_vcfs.py results/shell-script/vcf results/vcf
```

`Snakefile` reads `config/config.yaml` and `metadata/samples.tsv`. Rules cover
QC, reference preparation, alignment, calling, filtering and depth sensitivity.
Large SAM, unsorted BAM and raw BCF intermediates are temporary; logs are in
`results/logs/`. DAG and rule graphs are generated under `results/`.

Checked 2026-11-18: full VCF records match the shell (25, 775, 10 variants).
Changing minimum depth to 10 plans only three filters, three statistics jobs
and the target rule. Removing fixed BWA batch size changes four records in
SRR2584866; restoring it restores exact agreement. Toy target/wildcard/rerun
exercises passed separately. Formatting passed; lint advises more logs and
per-rule environments, while the whole workflow is pinned by `pixi.lock`.
The optional Slurm exercise was not run; no cluster account was configured.

From [CBIO7501 lesson 09](https://khanlab.bio/cbio7501-f26/pages/09-snakemake.html);
Data Carpentry attribution is retained in the Snakefile.
