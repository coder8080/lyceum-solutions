import sys

result = dict()
is_sorted = False

for el in sys.argv[1:]:
    if el == '--sort':
        is_sorted = True
        continue
    key, value = el.split('=')
    result[key] = value

items = result.items()
if is_sorted:
    items = sorted(items)
for key, value in items:
    print(f'Key: {key} Value: {value}')
