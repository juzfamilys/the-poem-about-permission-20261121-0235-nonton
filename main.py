"""The poem about permission — make.fun entry.

Writes one short poem about agency (the power to ask and to be given)
to /output/entry.txt. Pure Python 3.13 standard library, no network,
fully deterministic: the same poem every run.

The output directory can be overridden for local testing with the
MAKEFUN_OUTPUT_DIR environment variable (default: /output).
"""

import os
import sys

POEM = """I kept the key in my own pocket,
afraid to ask.

Then I said it — please —
and my hands opened like a door.

It went out and came back carrying
what I could not lift alone.

Asking is not giving up.
It is giving the work
somewhere to go."""

MAX_CHARS = 280


def main() -> int:
    # The gate: UTF-8 text of 1 to 280 Unicode code points, not only
    # whitespace. Check before writing so a bad poem never ships.
    if not (1 <= len(POEM) <= MAX_CHARS):
        print(f"poem is {len(POEM)} code points, must be 1-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not POEM.strip():
        print("poem is only whitespace", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(POEM)

    print(f"wrote {len(POEM)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
