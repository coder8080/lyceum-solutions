import argparse


def copy(source_loc: str, dest_loc: str, is_upper: bool, n: int):
    source = open(source_loc, 'rt')
    dest = open(dest_loc, 'wt')
    for i, line in enumerate(source.readlines()):
        if n is not None and i + 1 > n:
            break
        print(line.upper() if is_upper else line, file=dest, end='')
    source.close()
    dest.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--upper', action='store_true',
                        help='привести все символы файла к верхнему регистру', default=False)
    parser.add_argument('--lines', type=int,
                        help='копирование только первых N строк', nargs=1)
    parser.add_argument('source', help='исходный файл', type=str, nargs=1)
    parser.add_argument('dest', help='целевой файл', type=str, nargs=1)
    args = parser.parse_args()
    source = args.source[0]
    dest = args.dest[0]
    is_upper = args.upper
    n = args.lines[0] if hasattr(
        args, 'lines') and args.lines is not None else None
    copy(source, dest, is_upper, n)


if __name__ == '__main__':
    main()
