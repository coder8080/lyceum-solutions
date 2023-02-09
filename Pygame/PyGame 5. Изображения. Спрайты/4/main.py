import pygame
from sys import exit
from os import path
from random import randrange


def load_image(name):
    fullname = path.join('data', name)
    if not path.exists(fullname):
        print(f'Не найден файл {fullname}')
        exit(1)
    image = pygame.image.load(fullname)
    return image


class Bomb(pygame.sprite.Sprite):
    bomb_image = load_image('bomb.png')
    boom_image = load_image('boom.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bomb.bomb_image
        self.rect = self.image.get_rect()
        self.rect.x = randrange(0, 450)
        self.rect.y = randrange(0, 449)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = Bomb.boom_image


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Boom them all')
    sprites = pygame.sprite.Group()
    for i in range(20):
        Bomb(sprites)
    clock = pygame.time.Clock()
    is_running = True
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                sprites.update(event)
        screen.fill('black')
        sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
