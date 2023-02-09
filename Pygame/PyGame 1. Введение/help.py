import pygame


def draw(screen: pygame.Surface):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render('Hello, PyGame!', True, (100, 255, 100))
    text_w = text.get_width()
    text_h = text.get_height()
    text_x = width // 2 - text_w // 2
    text_y = height // 2 - text_h // 2
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10,
                     text_y - 10, text_w + 20, text_h + 20), 1)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Крест')
    try:
        size = width, height = [int(el) for el in input.split()]
        screen = pygame.display.set_mode(size)
        draw(screen)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
    except ValueError:
        print('')
    pygame.quit()
