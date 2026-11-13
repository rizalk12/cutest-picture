"""Almost Got It!

Entry program for the make.fun bounty "cutest-picture-01"
(Make the cutest picture).

The artwork is a baby red panda standing on its hind legs in a
cherry-blossom forest, front paws stretched high, just about to touch a
big shimmering soap bubble drifting above its nose — "Almost Got It!".
It ships in this repository as entry.png (a JPEG image stored under a
.png name, which the competition accepts: the output is judged by its
bytes, not its file name).

This program's only job is to deliver the artwork byte for byte: it
reads entry.png from its own directory and writes the identical bytes
to $MAKEFUN_OUTPUT_DIR/entry.png, defaulting to /output/entry.png when
the variable is not set. Two runs therefore always produce identical
output. It uses only the Python standard library and needs no network,
no clock and no randomness.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")

MAX_BYTES = 1_048_576  # the competition caps the output image at 1 MiB
JPEG_MAGIC = b"\xff\xd8"  # every JPEG starts with these two bytes


def main():
    try:
        with open(SOURCE, "rb") as fh:
            data = fh.read()
    except OSError as exc:
        sys.exit(f"error: cannot read artwork {SOURCE}: {exc}")
    if not data.startswith(JPEG_MAGIC):
        sys.exit("error: entry.png is not a JPEG image (bad magic header)")
    if len(data) > MAX_BYTES:
        sys.exit(f"error: entry.png is {len(data)} bytes, over the 1 MiB cap")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(target, "wb") as fh:
        fh.write(data)
    print(f"wrote {target} ({len(data)} bytes)", file=sys.stderr)


if __name__ == "__main__":
    main()
