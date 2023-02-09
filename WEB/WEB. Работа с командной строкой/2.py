import sys

result = 0
try:
    assert len(sys.argv) == 3
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    result = n1 + n2
except Exception:
    pass
print(result)
