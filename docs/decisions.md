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

- 2026-11-24: keep the main README focused on the seven reader questions;
  move layout, license detail and measured hardware to linked documentation.
  Preserve the existing MIT code license and separate Data Carpentry, text
  and source-data terms. Validate the CFF in CI with a separate, pinned tool
  environment so the analysis lock and Conda exports do not change. Record
  both Pixi environments because the report and pipeline Quarto versions
  differ. Use a forced full workflow for timing, not an incremental no-op.
