import sys
from os import path

is_counted = False
is_numbered = False
is_sorted = False
filename = ""

for el in sys.argv[1:]:
    if el == '--count':
        is_counted = True
    elif el == '--num':
        is_numbered = True
    elif el == '--sort':
        is_sorted = True
    else:
        filename = el

if not path.exists(filename):
    print('ERROR')
    sys.exit(1)

file = open(filename, 'rt')
lines = file.readlines()
file.close()
del file

if is_sorted:
    lines = sorted(lines)

for i, line in enumerate(lines):
    if is_numbered:
        print(str(i) + ' ', end='')
    print(line.strip('\n'))

if is_counted:
    print(f'rows count: {len(lines)}')
