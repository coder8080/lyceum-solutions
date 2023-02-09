import pygame


def draw(screen: pygame.Surface, a: int, n: int):
    screen.fill((255, 255, 255))
    square_size = a // n
    start = 0 if n % 2 != 0 else 1
    for row in range(n):
        for cell in range((row + start) % 2, n + 1, 2):
            pygame.draw.rect(screen, (0, 0, 0), (cell * square_size,
                             row * square_size, square_size, square_size), 0)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Шахматная клетка')
    try:
        a, n = [int(el) for el in input().split()]
        size = a, a
        screen = pygame.display.set_mode(size)
        draw(screen, a, n)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    except ValueError:
        print('Неправильный формат ввода')
