from os import path, stat, walk
from itertools import chain

result = dict()


def human_read_format(n: int) -> str:
    treshold = [2 ** 30, 2 ** 20, 2 ** 10, 0]
    names = ['ГБ', 'МБ', 'КБ', 'Б']
    for i in range(len(treshold)):
        if n >= treshold[i]:
            return f'{round(n / max(treshold[i], 1))}{names[i]}'


def recurse(p: str) -> int:
    global result
    size = 0
    if path.isfile(p):
        size = stat(p).st_size
    else:
        for (_, dirnames, filenames) in walk(p):
            for item in chain(dirnames, filenames):
                size += recurse(item)
    result[path.basename(p)] = size
    return size


recurse('./')
del result['']
items = sorted(result.items(), key=lambda x: x[1], reverse=True)
mlw = 0
mrw = 0
for i in range(0, min(10, len(items))):
    name, size = items[i]
    mlw = max(mlw, len(name) + 10)
    mrw = max(mrw, len(f' {human_read_format(size)}'))
for i in range(0, min(10, len(items))):
    name, size = items[i]
    size = human_read_format(size)
    print(f'{name}{" " * (mlw - len(name))}-{" " * (mrw - len(size)) + size}')
