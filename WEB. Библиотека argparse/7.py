import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--sort', action='store_true',
                    help='упорядочить выводимые значения по ключу')
parser.add_argument('values', type=str, nargs='*', help='данные')
args = parser.parse_args()
result = dict()
for el in args.values:
    key, value = el.split('=')
    result[key] = value
items = result.items()
if args.sort:
    items = sorted(items)
for key, value in items:
    print(f'Key: {key}\tValue: {value}')
