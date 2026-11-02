# Analysis decisions

- Preserve downloaded raw data and verify it against the recorded checksums.
  Write derived files separately instead of editing raw inputs.
- Keep the sample sheet, download sources, code and software lock under Git.
  Downloaded data and generated results remain outside version control.
- Keep minimum read depths 2 and 10 as candidate settings for a later
  comparison. No threshold has been selected from analysis results yet.

The depth alternatives came from the lesson 04 merge-conflict exercise.
No variant calling or threshold comparison has been run.
