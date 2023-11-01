# art.py

import sys
import random

chars = r"\|/"


def draw(rows, columns) -> None:
    for _ in range(rows):
        print("".join(random.choice(chars) for _ in range(columns)))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: art.py rows columns")
    draw(int(sys.argv[1]), int(sys.argv[2]))
