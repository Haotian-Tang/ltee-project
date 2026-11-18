# Decision log

- Keep raw files unchanged and verify them with the recorded SHA-256 checksums.
- Put pipeline tools in a Linux/macOS feature; retain Windows support for the
  default Python, Quarto and notebook environment.
- Use the lesson's BWA/samtools/bcftools workflow with haploid variant calling
  and the default minimum depth of 2. The local counts are recorded in notes.
- Lesson 04 reserved depth 10 for a later comparison; no threshold
  comparison had been performed at that stage.
- Record tool versions in pixi.lock and regenerate QC, alignments and variants
  through tasks rather than committing the generated outputs.

- 2026-11-18: report minimum depth 2 for comparison with Data Carpentry and
  retain sensitivity at 2, 5, 10 and 15. The late clone has about 26–33 times
  the variants of the 15,000-generation clone at all tested depths. Fix BWA
  batch size with `-K 10000000` to keep full variant records independent of
  the thread count.
