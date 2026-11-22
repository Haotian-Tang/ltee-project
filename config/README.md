# Workflow settings

`config.yaml` selects the sample sheet and compressed reference, fixes BWA's
batch size with `-K 10000000`, and sets the final filter and sensitivity depths.
The default minimum depth is 2; sensitivity runs use 2, 5, 10 and 15.

Change settings here and inspect `pixi run -e pipeline snakemake -n` before
running. Sample IDs and FASTQ paths come from `metadata/samples.tsv`.

Nextflow uses the same file via `-params-file config/config.yaml`.
Launch both workflows from the project root so sample and reference paths resolve.
