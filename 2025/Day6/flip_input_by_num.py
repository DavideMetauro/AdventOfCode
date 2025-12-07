import sys
from pathlib import Path

#!/usr/bin/env python3
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
        # Try whitespace-separated tokens
        token_rows = [line.split() for line in lines]
        token_counts = [len(r) for r in token_rows]
        if all(c == token_counts[0] for c in token_counts) and token_counts[0] > 1:
                return token_rows, "tokens"
        # Otherwise treat as fixed-width characters
        char_lengths = [len(line) for line in lines]
        if all(l == char_lengths[0] for l in char_lengths):
                return [list(line) for line in lines], "chars"
        # Fallback: if single-token-per-line (one column), return tokens
        if all(len(r) == 1 for r in token_rows):
                return token_rows, "tokens"
        raise SystemExit("Input is not a well-formed rectangle (inconsistent row lengths).")

def transpose(rows):
        if not rows:
                return []
        return [list(col) for col in zip(*rows)]

def format_output(rows, mode):
        if mode == "tokens":
                return [" ".join(row) for row in rows]
        return ["".join(row) for row in rows]

def main():
        infile = "input_day6.txt"
        outfile = "input_day6_transposed.txt"
        lines = read_lines(infile)
        parsed, mode = detect_and_parse(lines)
        transposed = transpose(parsed)
        out_lines = format_output(transposed, mode)
        write_lines(out_lines, outfile)

if __name__ == "__main__":
        main()