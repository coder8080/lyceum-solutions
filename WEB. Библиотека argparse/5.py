import argparse
from sys import exit

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('numbers', nargs='*')
    args = parser.parse_args()
    numbers = args.numbers
    if len(numbers) == 0:
        print('NO PARAMS')
        exit(1)
    elif len(numbers) < 2:
        print('TOO FEW PARAMS')
        exit(1)
    elif len(numbers) > 2:
        print('TOO MANY PARAMS')
        exit(1)
    result = int(numbers[0]) + int(numbers[1])
    print(result)
except Exception as e:
    print(e.__class__.__name__)
