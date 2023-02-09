def solution():
    ax1, ay1, aw, ah = [int(el) for el in input().split()]
    bx1, by1, bw, bh = [int(el) for el in input().split()]

    ax2 = ax1 + aw
    ay2 = ay1 + ah

    bx2 = bx1 + bw
    by2 = by1 + bh

    # проверяю каждую вершину b
    # bx1, by1
    if ax1 <= bx1 <= ax2 and ay1 <= by1 <= ay2:
        return True

    # bx2, by1
    if ax1 <= bx2 <= ax2 and ay1 <= by1 <= ay2:
        return True

    # bx2, by2
    if ax1 <= bx2 <= ax2 and ay1 <= by2 <= ay2:
        return True

    # bx1, by2
    if ax1 <= bx1 <= ax2 and ay1 <= by2 <= ay2:
        return True

    # Верхняя сторона
    if ay1 <= by1 <= ay2 and bx1 <= ax1 and bx2 >= ax2:
        return True

    # Правая сторона
    if ax1 <= bx2 <= ax2 and by1 <= ay1 and by2 >= ay2:
        return True

    # Нижняя сторона
    if ay1 <= by2 <= ay2 and bx1 <= ax1 and bx2 >= ax2:
        return True

    # Левая сторона
    if ax1 <= bx1 <= ax2 and by1 <= ay1 and by2 >= ay2:
        return True

    return False


print('YES' if solution() else 'NO')
