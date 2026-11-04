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

## Exporting the LTEE pipeline

Generate the files from the project configuration rather than editing them:

```bash
pixi workspace export conda-environment -e pipeline envs/pipeline.yml
pixi workspace export conda-explicit-spec -e pipeline envs/explicit
```

`pipeline.yml` contains dependency ranges from `pixi.toml`. A Conda user
builds a new environment with:

```bash
conda env create -p ./conda-env -f envs/pipeline.yml
conda run -p ./conda-env samtools --version
conda run -p ./conda-env fastqc --version
```

The lesson uses `pixi exec micromamba create -y -p ./conda-env -f
envs/pipeline.yml` instead. Activate the environment or use `conda run` /
`micromamba run` so runtime dependencies, including Java for FastQC, are set up.
Pixi task definitions are not included in the Conda export.

## Exact packages for one platform

`explicit/` contains package URLs and checksums from `pixi.lock`:

- `pipeline_linux-64_conda_spec.txt`
- `pipeline_osx-arm64_conda_spec.txt`
- `pipeline_osx-64_conda_spec.txt`

Choose the file matching both the operating system and CPU architecture:

```bash
conda create -p ./conda-env --file envs/explicit/pipeline_linux-64_conda_spec.txt
```

The command above is for Linux x86-64. The pipeline has no native Windows
specification; Windows users run it in WSL2. Do not use the Linux file on macOS.

| File | What it records | Rebuild behavior |
| --- | --- | --- |
| `pipeline.yml` | Requested version ranges and channels | Solves again; versions/builds may differ |
| `explicit/*_conda_spec.txt` | Exact package URLs and checksums | One operating system/architecture per file |
| `pixi.lock` | Exact packages for every configured environment/platform | Pixi selects the current platform automatically |

These files do not capture the raw data, hardware, system libraries or future
availability of package channels. Regenerate the exports after changing the
project manifest or lock file. Installed `conda-env/` and `wrong-env/` copies
are temporary and excluded from Git.
