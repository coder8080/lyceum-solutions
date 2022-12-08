import pygame


def draw(screen: pygame.Surface, w: int, n: int, width: int):
    screen.fill((0, 0, 0))
    colors = [pygame.Color((255, 0, 0)), pygame.Color(
        (0, 0, 255)), pygame.Color((0, 255, 0))]
    index = 0
    center = (width // 2, width // 2)
    for number in range(n):
        pygame.draw.circle(screen, colors[index], center, (n - number) * w, 0)
        index += 1
        if index == 3:
            index = 0


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Мишень')
    try:
        w, n = [int(el) for el in input().split()]
        width = w * n * 2
        size = width, width
        screen = pygame.display.set_mode(size)
        draw(screen, w, n, width)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
    except ValueError:
        print('Неправильный формат ввода')
    pygame.quit()
