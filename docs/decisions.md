# Decision log

- Keep raw files unchanged and verify them with the recorded SHA-256 checksums.
- Put pipeline tools in a Linux/macOS feature; retain Windows support for the
  default Python, Quarto and notebook environment.
- Use the lesson's BWA/samtools/bcftools workflow with haploid variant calling
  and the default minimum depth of 2. The local counts are recorded in notes.
- Keep depth 10 as a candidate for a later comparison. No comparison or
  selection between thresholds has been performed.
- Record tool versions in pixi.lock and regenerate QC, alignments and variants
  through tasks rather than committing the generated outputs.
