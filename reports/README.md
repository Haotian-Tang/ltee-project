# Reports

`ltee-report.qmd` computes sample and read tables, a quality profile,
inline summaries and software versions from the LTEE data.

```bash
pixi run quarto render reports/ltee-report.qmd
pixi run quarto render reports/ltee-report.qmd -P max_reads:2000
pixi run quarto render reports/ltee-report.qmd --to typst
```

The default is 10,000 reads per FASTQ for length, GC and quality summaries;
read counts use all reads. HTML embeds its resources; PDF hides source code.
Generated files are ignored by Git. The Variants section reads Snakemake outputs and the depth-sensitivity results.

Adapted from [CBIO7501 lesson 07](https://khanlab.bio/cbio7501-f26/pages/07-quarto.html).

`pixi run report` builds the HTML after verifying raw data, and is included
in `pixi run reproduce` and CI.

Checked 2026-11-15: HTML/PDF, the 2,000-read parameter override, Word practice,
notebook caption/alt text and output clearing. The hidden-state render failed
with the expected undefined `samples` error; temporary exercises were removed.

Lesson 09: `report` depends on `run-snakemake`. Tables and figures show mapped
reads, SNPs/indels and thresholds 2/5/10/15; the decision keeps depth 2 for
comparability and reports sensitivity. At 50,000 generations the counts are
775, 723, 415 and 123; the late clone has about 26–33 times the variants of
the 15,000-generation clone across these thresholds.
