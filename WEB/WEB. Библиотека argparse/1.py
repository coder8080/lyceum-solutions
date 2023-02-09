import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*')
args = parser.parse_args().arg
if len(args) == 0:
    print('no args')
for el in args:
    print(el)
