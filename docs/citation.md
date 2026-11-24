# Citation metadata

`CITATION.cff` identifies this software project and references the original
Tenaillon et al. (2016) study. It uses Haotian Tang's supplied name and email.
No ORCID is asserted because none was supplied. The template's
`date-released` is omitted until an actual release is made in lesson 12;
the existing project version remains 0.1.0.

From the project root, validate and generate citations with the same tool
version used in CI:

```bash
pixi exec --spec 'python=3.13.*' --spec 'cffconvert=2.0.0' -- cffconvert --validate -i CITATION.cff
pixi exec --spec 'python=3.13.*' --spec 'cffconvert=2.0.0' -- cffconvert -i CITATION.cff -f apalike
pixi exec --spec 'python=3.13.*' --spec 'cffconvert=2.0.0' -- cffconvert -i CITATION.cff -f bibtex
```

This is a separate Pixi tool environment; it does not update the analysis
manifest, lock or Conda exports. GitHub uses the valid root citation file
for its "Cite this repository" control. Cite the original paper and dataset
as well when discussing their data or biology (`reports/references.bib`).

## Finding the version behind a figure

Use `pixi.lock` for the exact package/build/checksum on the relevant platform,
and `docs/software-versions.txt` for the readable snapshot. The report also
prints its key versions. The pipeline's samtools version is 1.25; report tools
run in `default`, while bioinformatics tools run in `pipeline`. These two
environments can have different Quarto versions, as recorded in the snapshot.

To regenerate the version lists and rule graph after intentional workflow
or environment changes:

```bash
pixi list -e pipeline --explicit --color never
pixi list -e default --explicit --color never
pixi run -e pipeline snakemake --rulegraph > docs/rulegraph.dot
pixi run -e pipeline dot -Tsvg docs/rulegraph.dot -o docs/rulegraph.svg
```

The graph shows rule dependencies, not measured task execution or timing.
If Graphviz cannot find its SVG renderer after a new installation, run
`pixi run -e pipeline dot -c` once before rendering.
