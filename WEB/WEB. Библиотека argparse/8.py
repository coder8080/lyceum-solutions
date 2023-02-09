import argparse


def print_error(message: str) -> None:
    print(f'ERROR: {message}!!')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('message', type=str, nargs='*')
    args = parser.parse_args()
    message = ' '.join(args.message)
    print('Welcome to my program')
    print_error(message)


if __name__ == '__main__':
    main()
