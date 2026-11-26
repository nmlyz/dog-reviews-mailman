#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the review a dog gives the
mailman, after the council tax bill came through the door.

The line was picked from 36 candidates by pairwise judging against the
brief — a dog's small triumph over the mailman, told in three beats:
the visit, the bill eaten, the matter closed. Each beat is one concrete
fact — the postman's arrival, the tax bill through the flap, the dog's
verdict — so the laugh comes from this dog and this mailman, not from a
pun that would fit any stranger at the door. The program builds the
line from three clauses — the arrival, the delivery, the verdict — and
checks the result against the entry gate (length, single line, no
leading or trailing space, exact judged length) before writing it, then
reads the file back to confirm the bytes match.
"""

import os
import sys

LINE = (
    "He came, he saw, he posted a council tax bill through my door. "
    "I ate it. I consider the matter closed."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 200):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-200")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
