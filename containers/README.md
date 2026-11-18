# Containers

Build the locked pipeline environment (Linux amd64, emulated on Apple silicon):

```bash
docker build --platform linux/amd64 -f containers/Dockerfile \
  --build-arg ENV_NAME=pipeline -t ltee-project:0.1.0 .
docker run --rm --platform linux/amd64 -v "$PWD":/work -w /work \
  ltee-project:0.1.0 bash scripts/run_variant_calling.sh
```

The two-stage image installs `pipeline` with `pixi install --locked`, then
copies its environment and activation script into Ubuntu. Both base images
are pinned by digest. Only the manifest and lock enter the build context;
the project and data are supplied through the bind mount.

From [CBIO7501 lesson 08](https://khanlab.bio/cbio7501-f26/pages/08-containers.html).

## Verified image and results

Pinned published image: `ghcr.io/haotian-tang/ltee-project@sha256:03103b20d4f2654546047e2f6eb5724349f6d3d31f51c32ad2a4b816d8207301`.
Local image ID, software versions, source commit and archive SHA-256 are in
`provenance.json`. The saved `ltee-project_0.1.0.tar.gz` passed gzip validation
and `docker load`; it is kept locally and excluded from Git.

On 2026-11-18, Docker reproduced 25, 775 and 10 variants for SRR2584863,
SRR2584866 and SRR2589044. Sorted CHROM/POS/REF/ALT identities match the
earlier native run. Run `pixi run python scripts/check_container_results.py`
to check them against `expected-variants.tsv`. Raw data remained read-only
and all seven checksums matched. Omitting the bind mount failed as expected.

`Container` CI builds and runs the image on push/PR. Successful pushes publish
commit tags to GHCR; `0.1.0` preserves the first tested release image. The CI
uses a single-platform export; source, lock, image and archive digests record provenance.

## Apptainer on Linux or HPC

```bash
apptainer build containers/ltee-project.sif containers/apptainer.def
apptainer exec containers/ltee-project.sif samtools --version
apptainer run containers/ltee-project.sif bash scripts/run_variant_calling.sh
```

The recipe uses the pinned registry image. Apptainer is optional and was not
run on this Mac; no cluster account was used.
