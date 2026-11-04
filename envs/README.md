# Environment interchange

`pixi.toml` and `pixi.lock` are the project's source of truth. Files in this
folder support collaborators who use Conda or Mamba.

## Importing a Conda environment into Pixi

`examples/variant-calling.yml` is the lesson 5b example. It requests Python
3.13 and samtools/bcftools 1.24 from conda-forge and bioconda. This is a
separate conversion exercise; it does not downgrade the LTEE pipeline.

From the project folder, create a separate workspace:

```bash
pixi init --import envs/examples/variant-calling.yml ../conda-comparison/from-conda
cd ../conda-comparison/from-conda
pixi run bcftools --version
```

The import preserves channel order and translates `samtools=1.24` into
`samtools = "1.24.*"`. It creates a Pixi manifest and lock file. The imported
workspace was built locally and both samtools and bcftools reported 1.24.
