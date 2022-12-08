import pygame


def draw(screen: pygame.Surface, w: int, h: int):
    screen.fill((0, 0, 0))
    color = pygame.Color(0, 0, 0)
    color.hsva = (h, 100, 100)
    half = w // 2

    n = 130

    d1 = (n - half, n)
    d2 = (n, n - half)
    d3 = (n + w, n - half)
    d4 = (n + half, n)
    pygame.draw.polygon(screen, color, (d1, d2, d3, d4))

    color.hsva = (h, 100, 75)
    d1 = (n - half, n)
    d2 = (n + half, n)
    d3 = (n + half, n + w)
    d4 = (n - half, n + w)
    pygame.draw.polygon(screen, color, (d1, d2, d3, d4))

    color.hsva = (h, 100, 50)
    d1 = (n + half, n)
    d2 = (n + w, n - half)
    d3 = (n + w, n + half)
    d4 = (n + half, n + w)
    pygame.draw.polygon(screen, color, (d1, d2, d3, d4))


if __name__ == "__main__":
    try:
        w, h = [int(el) for el in input().split()]
        if w < 1 or w > 100 or w % 4 != 0 or h < 0 or h > 360:
            raise ValueError()
        pygame.init()
        pygame.display.set_caption('Куб')
        size = width, height = 300, 300
        screen = pygame.display.set_mode(size)
        draw(screen, w, h)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    except ValueError:
        print('Неправильный формат ввода')
