# Contributing

For a bug report, include the Git commit, operating system, exact command
and full error message. Open an issue to discuss larger changes first.

1. Fork the repository and create a branch for your change.
2. Run `pixi install --locked --all` and `pixi run reproduce`.
3. For workflow changes, also run `pixi run compare-workflows` and
   `pixi run compare-to-shell`; compare complete VCF records, not counts alone.
4. Validate `CITATION.cff` with the command in `docs/citation.md`, then open
   a pull request. The Reproduce and Container checks must pass before merging.

Keep raw data and generated results out of Git. Commit `pixi.toml` and
`pixi.lock` together, and regenerate the exports in `envs/` and the version
snapshot in `docs/software-versions.txt` after environment changes. Record
analysis decisions in `docs/decisions.md`; keep source credits and licenses.

Contributions are covered by the relevant terms in `docs/licenses.md`.
Everyone participating follows `CODE_OF_CONDUCT.md`.
