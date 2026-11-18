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
