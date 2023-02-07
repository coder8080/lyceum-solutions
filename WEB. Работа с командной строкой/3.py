import sys

try:
    if len(sys.argv) == 1:
        print('NO PARAMS')
    else:
        result = 0
        for i, el in enumerate(sys.argv[1:]):
            if i % 2 == 0:
                result += int(el)
            else:
                result -= int(el)
        print(result)
except Exception as e:
    print(e.__class__.__name__)
