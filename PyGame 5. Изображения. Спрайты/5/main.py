import pygame
from sys import exit
from os import path


def load_image(name: str) -> pygame.Surface:
    fullname = path.join('data', name)
    if not path.exists(fullname):
        print(f'Не удалось найти файл {fullname}')
        exit(1)
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Game over')
    size = width, height = 600, 300
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    is_running = True
    gameover = load_image('gameover.png')
    current_position = -600
    speed = 8
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                current_position = -600
        if current_position < 0:
            current_position += speed
        screen.fill('blue')
        screen.blit(gameover, (current_position, 0))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
