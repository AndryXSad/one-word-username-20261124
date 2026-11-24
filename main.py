"""One Word, One Username, One Reward — entry program.

Writes the entrant's own make.fun username, and nothing else, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
The handle was verified against the make.fun account API before
this program was written: it is the account's own username.
"""

import os

USERNAME = "anzzz"


def main() -> None:
    word = USERNAME.strip()
    if not word or len(word) > 30 or any(ch.isspace() for ch in word):
        raise ValueError("username must be one word of 1-30 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)


if __name__ == "__main__":
    main()
