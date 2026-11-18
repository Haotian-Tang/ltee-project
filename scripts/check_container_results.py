"""Check container VCF identities against the verified lesson-05 baseline."""

import argparse
import csv
import hashlib
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vcf_dir", nargs="?", type=Path, default=Path("results/vcf"))
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    with (root / "containers/expected-variants.tsv").open() as handle:
        expected = list(csv.DictReader(handle, delimiter="\t"))
    wanted = {f"{row['sample']}_final_variants.vcf" for row in expected}
    found = {path.name for path in args.vcf_dir.glob("*_final_variants.vcf")}
    if found != wanted:
        raise SystemExit(f"VCF files differ: expected {sorted(wanted)}, found {sorted(found)}")
    for row in expected:
        path = args.vcf_dir / f"{row['sample']}_final_variants.vcf"
        records = []
        with path.open() as handle:
            for line in handle:
                if not line.startswith("#"):
                    fields = line.rstrip("\n").split("\t")
                    records.append("\t".join(fields[i] for i in (0, 1, 3, 4)))
        canonical = "\n".join(sorted(records)) + "\n"
        digest = hashlib.sha256(canonical.encode()).hexdigest()
        if len(records) != int(row["variants"]) or digest != row["sha256"]:
            raise SystemExit(f"{row['sample']}: variant count or CHROM/POS/REF/ALT identities differ")
        print(f"{row['sample']}: {len(records)} variants; identities match")


if __name__ == "__main__":
    main()
