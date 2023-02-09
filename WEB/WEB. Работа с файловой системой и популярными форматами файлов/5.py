from zipfile import Path, ZipInfo
from os import path


def human_read_format(n: int) -> str:
    treshold = [2 ** 30, 2 ** 20, 2 ** 10, 0]
    names = ['ГБ', 'МБ', 'КБ', 'Б']
    for i in range(len(treshold)):
        if n >= treshold[i]:
            return f'{round(n / max(treshold[i], 1))}{names[i]}'


def recurse(level, zippath: Path):
    basename = path.basename(zippath.filename)
    nextLevel = level + 1
    if basename == "input.zip":
        nextLevel -= 1
    else:
        if zippath.is_dir():
            print(level * (' ' * 2) + path.basename(zippath.filename))
        else:
            size = len(zippath.read_bytes())
            print(level * (' ' * 2) +
                  path.basename(zippath.filename) + ' ' + human_read_format(size))
    if zippath.is_dir():
        for item in zippath.iterdir():
            recurse(nextLevel, item)


recurse(0, Path('input.zip'))
