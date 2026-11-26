"""The Worst Line an AI Could Say — make.fun entry.

Writes one original pickup line, the worst one an AI could plausibly
deliver — flat, over-helpful, faintly ominous — to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt). The entry is
a single line: a fixed string, no trailing spaces, one trailing newline.
Pure Python standard library, deterministic: the same bytes on every
run. Never deletes the output directory; creates it only if it does
not already exist.
"""

import os

LINE = "I computed our compatibility at 97%. The remaining 3% is why I will never sleep."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
