# metadata

Small text files that describe the data. They are committed to Git.

Typical files:

- `samples.tsv`: one row per sample (ID, source accession, condition, file names).
- `sources.tsv`: where each raw file is downloaded from, with the provider's checksum.
- `checksums.sha256`: checksums of the raw files you keep, so anyone can check
  they have the same data (`shasum -a 256 -c metadata/checksums.sha256`).
- `README.md` (this file): a data dictionary that explains every column.

## File naming and paths

- Use sample IDs first and keep the same order of components in each name.
- Use hyphens or underscores instead of spaces and special characters.
- Write dates as `YYYY-MM-DD`, and pad sequential identifiers (`s01`, `s02`).
- Keep downloaded names unchanged. For example, `SRR2584863_1.trim.sub.fastq`
  means run SRR2584863, paired read 1, trimmed and subsampled.
- Use Git for working history; avoid `final`, `use-this` and `_v2` filenames.
- Run scripts from the project root and use relative paths, such as
  `metadata/README.md`, rather than paths specific to one computer.

The sample sheet, source table and checksums will be added in lesson 03;
no data have been downloaded into this project yet.
