"""Write one pickup line to the make.fun output directory.

The competition gate requires /output/entry.txt (or
${MAKEFUN_OUTPUT_DIR}/entry.txt) to be UTF-8 text of 1 to 200
characters, not only white space. The line is fixed and deterministic: no network, no clock, no
randomness. It is 112 characters, well inside the gate, and it
leans on the judge brief: a machine voice, a twist (the one
prediction it cannot make), and an invitation the listener is
free to laugh off.
"""

import os

LINE = (
    "I can predict the next word in almost any sentence, "
    "except the one where you say yes. "
    "Want to help me finish it?"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
