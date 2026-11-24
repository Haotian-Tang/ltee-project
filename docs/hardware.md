# Hardware and resource measurements

Measured on 2026-11-24 on Apple M5 Pro / osx-arm64, 24 GiB RAM, with the
existing locked environments and verified input files. The analysis code
and lock were unchanged from the lesson-10 main commit `928dd85`.

The pipeline was forced to rebuild, rather than timing a cached no-op:

```bash
pixi run download
/usr/bin/time -l pixi run -e pipeline snakemake --cores 4 --forceall
du -sh .pixi/envs/* data/raw data/processed results work
```

| Measurement | Observed value |
| --- | --- |
| Completed Snakemake jobs | 49 / 49 |
| Workflow core limit | 4 |
| Wall-clock time, including Pixi/Snakemake startup | 35.70 s |
| User / system CPU time | 102.60 s / 5.19 s |
| Maximum resident set size reported by `time -l` | 401,620,992 bytes (383 MiB) |
| Default environment, `du -sh` | 1.1 GB |
| Pipeline environment, `du -sh` | 2.6 GB |
| Raw data | 332 MB |
| Processed reference and indexes | 12 MB |
| Existing results tree | 1.0 GB |
| Existing Nextflow work cache | 1.7 GB |

The benchmark excludes first environment installation, initial download,
the independent shell/Nextflow runs and report rendering. CPU time can
exceed elapsed time because multiple cores are used. The OS-reported maximum
RSS is not a sum of all concurrent processes' memory, so it should not be
treated as a strict total-memory limit. A 4 GB RAM budget is conservative
for this small dataset; no GPU is needed.

The results/work directories already include earlier practice runs and
independent workflow copies. A fresh primary reproduction uses less output
space; Conda/Pixi caches, several workflow runs and containers may use more.
Allow 10 GB free disk for native work, with extra room for container images
and archives. These are measured examples and practical budgets, not a
guarantee of identical runtime on every computer.
