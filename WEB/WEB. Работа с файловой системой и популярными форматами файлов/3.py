from zipfile import Path
from os import path


def recurse(level, zippath: Path):
    basename = path.basename(zippath.filename)
    nextLevel = level + 1
    if basename == "input.zip":
        nextLevel -= 1
    else:
        print(level * (' ' * 2) + path.basename(zippath.filename))
    if zippath.is_dir():
        for item in zippath.iterdir():
            recurse(nextLevel, item)


recurse(0, Path('input.zip'))
