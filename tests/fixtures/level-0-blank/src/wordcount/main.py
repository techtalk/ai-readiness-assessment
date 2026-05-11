import sys
from pathlib import Path


def count_words(text):
    return len(text.split())


if __name__ == "__main__":
    path = Path(sys.argv[1])
    print(count_words(path.read_text()))
