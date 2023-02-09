import pygame


def draw(screen: pygame.Surface):
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 0), (width, height), 5)
    pygame.draw.line(screen, (255, 255, 255), (width, 0), (0, height), 5)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Крест')
    try:
        size = width, height = [int(el) for el in input().split()]
        screen = pygame.display.set_mode(size)
        draw(screen)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
    except ValueError:
        print('Неправильный формат ввода')
    pygame.quit()
