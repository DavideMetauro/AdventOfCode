#!/usr/bin/env python3
import sys
from pathlib import Path

"""
flip_input.py
Read a rectangular input (y rows x columns) and transpose it (x rows y columns).
Usage:
    python flip_input.py [infile] [outfile]
If infile/outfile are omitted, stdin/stdout are used.
"""


def read_lines(path):
    if path is None:
        return [line.rstrip("\n") for line in sys.stdin]
    return Path(path).read_text().splitlines()


def write_lines(lines, path):
    out = "\n".join(lines)
    if path is None:
        sys.stdout.write(out)
    else:
        Path(path).write_text(out)


def detect_and_parse(lines):
    if not lines:
        return [], "chars"
    # Always treat each line as a sequence of characters (preserve spaces)
    char_lengths = [len(line) for line in lines]
    if not all(l == char_lengths[0] for l in char_lengths):
        raise SystemExit("Input is not a well-formed rectangle (inconsistent row lengths).")
    return [list(line) for line in lines], "chars"


def transpose(rows):
    if not rows:
        return []
    return [list(col) for col in zip(*rows)]


def format_output(rows, mode):
    if mode == "tokens":
        return [" ".join(row) for row in rows]
    return ["".join(row) for row in rows]


def main():
    infile = "input_day6_wo_op.txt"
    outfile = "input_day6_transposed.txt"
    lines = read_lines(infile)
    parsed, mode = detect_and_parse(lines)
    transposed = transpose(parsed)
    out_lines = format_output(transposed, mode)
    write_lines(out_lines, outfile)


if __name__ == "__main__":
    main()
