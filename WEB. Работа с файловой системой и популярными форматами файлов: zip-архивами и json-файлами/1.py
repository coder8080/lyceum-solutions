def human_read_format(n: int) -> str:
    treshold = [2 ** 30, 2 ** 20, 2 ** 10, 0]
    names = ['ГБ', 'МБ', 'КБ', 'Б']
    for i in range(len(treshold)):
        if n >= treshold[i]:
            return f'{round(n / max(treshold[i], 1))}{names[i]}'
