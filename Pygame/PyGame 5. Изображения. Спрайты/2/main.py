import pygame
from os import path
from sys import exit


def load_image(name):
    fullname = path.join('data', name)
    if not path.exists(fullname):
        print(f'Не удалось найти файл {fullname}')
        exit(1)
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Герой двигается!')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    is_running = True
    clock = pygame.time.Clock()
    player_x = 0
    player_y = 0
    speed = 10
    creature = load_image('creature.png')
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_y -= speed
                elif event.key == pygame.K_DOWN:
                    player_y += speed
                elif event.key == pygame.K_RIGHT:
                    player_x += speed
                elif event.key == pygame.K_LEFT:
                    player_x -= speed
        screen.fill('white')
        screen.blit(creature, (player_x, player_y))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
