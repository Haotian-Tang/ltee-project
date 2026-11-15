# scripts

Code you write: Python scripts, shell scripts, small helpers.

- Run scripts from the project folder (`pixi run python scripts/x.py`), and use
  paths relative to the project folder, never absolute paths like `/Users/me/...`.
- Turn repeated commands into Pixi tasks in `pixi.toml`.

`fastq_stats.py` provides read counts and sampled length, GC and Phred+33
quality summaries for the Quarto report. Adapted from
[CBIO7501 lesson 07](https://khanlab.bio/cbio7501-f26/pages/07-quarto.html).
