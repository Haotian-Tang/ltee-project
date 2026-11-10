# Notebooks

`explore-reads.ipynb` explores length and GC content for the first 5,000
read-1 sequences from each LTEE sample (15,000 reads total).

Start JupyterLab from the project root with `pixi run jupyter lab`.
Restart the kernel and run all cells before sharing; clear outputs before
committing. Reusable code belongs in `scripts/`, reported results in `reports/`.

Adapted from [CBIO7501 lesson 06](https://khanlab.bio/cbio7501-f26/pages/06-jupyter.html),
which credits [NBIS, Working with Jupyter](https://nbisweden.github.io/workshop-reproducible-research/pages/jupyter.html)
(John Sundh, Erik Fasterius and contributors), CC BY 4.0.

Run `pixi run notebook` from the project root for a fresh-kernel HTML export
at `results/notebooks/explore-reads.html`. It also runs in `pixi run reproduce`
and CI; the source notebook stays output-free.

Checked 2026-11-10: HTML export and in-place execution passed; clearing
outputs reduced the notebook from 27,580 to 4,555 bytes. Reads shorter than
100 bases: SRR2584863 21.0%, SRR2584866 21.8%, SRR2589044 21.4%.
The temporary out-of-order exercise failed with `NameError: min_length`
on a fresh kernel, then passed after moving the definition above its use.
The exercise files were deleted as instructed.
