import pygame
from random import randint


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жёлтый круг')
    size = width, height = randint(300, 500), randint(300, 500)
    screen = pygame.display.set_mode(size)
    finished = False
    x, y = 0, 0
    is_drawn = False
    current_size = 0.0
    blue = pygame.Color('blue')
    clock = pygame.time.Clock()
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                current_size = 0.0
                is_drawn = True
        screen.fill(blue)
        if is_drawn:
            pygame.draw.circle(screen, 'yellow', (x, y), int(current_size), 0)
            current_size += (1 / 6)
        clock.tick(60)
        pygame.display.flip()
    pygame.quit()
