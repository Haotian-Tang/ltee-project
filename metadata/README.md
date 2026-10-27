# metadata

Files that describe the raw data. They are small, written by hand and committed.

## sources.tsv

Where each raw file comes from. Columns: `name`; `url` (download link);
`md5` (checksum published by the provider: figshare record 7726454 and
NCBI's md5checksums.txt, copied 2026-10-24); `unpack` (`tar` = unpack the
archive, `none` = keep the file as is); `dest` (where it goes in the project).

## checksums.sha256

SHA-256 checksum of every raw file we keep. Check with
`sha256sum -c metadata/checksums.sha256`.

## samples.tsv

One row per sample.

| Column | Meaning |
|--------|---------|
| sample | SRA run accession, also used in all file names |
| strain | LTEE clone name (REL…) |
| generation | generation at which the clone was frozen |
| population | LTEE population (all Ara-3 here) |
| mutator | hypermutability status (`None` or `plus`) |
| cit | can use citrate (`plus`) or not known (`unknown`) |
| fastq_1, fastq_2 | read 1 and read 2 FASTQ files, relative to the project folder |

Source of the sample information: Data Carpentry, *Wrangling Genomics*,
`Ecoli_metadata_composite.csv` (CC BY 4.0), from Tenaillon et al. 2016,
*Nature* 536:165, <https://doi.org/10.1038/nature18959>. Runs are in NCBI
BioProject PRJNA295606.

## Acquisition record

- Downloaded and verified on 2026-10-27.
- figshare record: <https://doi.org/10.6084/m9.figshare.7726454.v3> (version 3,
  CC0); file 14418248, `sub.tar.gz`, 115,114,554 bytes. The provider MD5 was
  checked against the figshare API on the download date.
- Reference: GenBank CP000819.1, assembly GCA_000017985.1. The provider MD5 was
  checked against NCBI's assembly `md5checksums.txt` on the download date.
- The two provider MD5 values match those in the course's `sources.tsv`.
  All seven retained raw files match the course's SHA-256 values.
- The verified FASTQ archive was unpacked and removed; the reference remains
  compressed as supplied by NCBI. All seven raw files are read-only.
- Source tables, data dictionary and standard-library download script follow
  [lesson 03](https://khanlab.bio/cbio7501-f26/pages/03-data-management.html),
  source revision `2de12cc195a8c5c46238f339d063a915c55f8686`.
- Verification and the checksum corruption/repair exercise are recorded in
  `docs/lesson03-checks.txt`. No derived data or analysis results were created.
