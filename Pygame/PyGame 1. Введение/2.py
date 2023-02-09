import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Прямоугольник')
    try:
        size = width, height = [int(el) for el in input().split()]
        screen = pygame.display.set_mode(size)
        pygame.draw.rect(screen, pygame.Color('red'),
                         (1, 1, width - 2, height - 2))
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
    except ValueError:
        print('Неправильный формат ввода')
