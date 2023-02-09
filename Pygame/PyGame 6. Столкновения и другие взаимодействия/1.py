x1, y1, r1 = [int(el) for el in input().split()]
x2, y2, r2 = [int(el) for el in input().split()]

max_hypot = (r1 + r2) ** 2
current_hypot = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2
print('YES' if current_hypot <= max_hypot else 'NO')
