import argparse


def count_lines(filepath: str) -> int:
    try:
        file = open(filepath, 'rt')
        result = len(file.readlines())
        file.close()
        return result
    except Exception:
        return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, nargs=1)
    args = parser.parse_args()
    filename = args.file
    print(count_lines(filename[0]))


if __name__ == '__main__':
    main()
