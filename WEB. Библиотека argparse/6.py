import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--count', action='store_true',
                    default=False, help='вывести кол-во строк в конце сообщения')
parser.add_argument('--num', action='store_true',
                    default=False, help='вывод порядкового номера в начале каждой строки')
parser.add_argument('--sort', action='store_true',
                    default=False, help='сортировка строк в алфавитном порядке перед выводом')
parser.add_argument('filename', type=str, help='имя файла', nargs=1)

try:
    args = parser.parse_args()
    file = open(args.filename[0])
    lines = file.readlines()
    file.close()
    del file
    if args.sort:
        lines = sorted(lines)
    for i, line in enumerate(lines):
        if args.num:
            print(f'{i} ', end='')
        print(line.strip('\n'))
    if args.count:
        print(f'rows count: {len(lines)}')
except Exception:
    print('ERROR')
