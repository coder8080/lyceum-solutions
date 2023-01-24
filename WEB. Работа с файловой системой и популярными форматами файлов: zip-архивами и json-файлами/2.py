import os


def human_read_format(n: int) -> str:
    treshold = [2 ** 30, 2 ** 20, 2 ** 10, 0]
    names = ['ГБ', 'МБ', 'КБ', 'Б']
    for i in range(len(treshold)):
        if n >= treshold[i]:
            return f'{round(n / max(treshold[i], 1))}{names[i]}'


def get_files_sizes() -> str:
    files = list(os.walk('.'))[0][2]
    result = ''
    for file in files:
        result += f'{file} {human_read_format(os.path.getsize(file))}\n'
    return result.strip()


print(get_files_sizes())
