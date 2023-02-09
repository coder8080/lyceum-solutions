import pygame
from os import path
from random import randint

all_sprites = pygame.sprite.Group()


def load_image(name: str) -> pygame.Surface:
    fullname = path.join('data', name)
    if not path.exists(fullname):
        print(f'Файл с изображением {fullname} не найден')
        exit(1)
    image = pygame.image.load(fullname)
    return image


class Bomb(pygame.sprite.Sprite):
    bomb_image = load_image('bomb.png')
    boom_image = load_image('boom.png')

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Bomb.bomb_image
        self.rect = self.image.get_rect()
        width = self.rect.width
        height = self.rect.height

        self.rect.x = randint(0, 500 - width)
        self.rect.y = randint(0, 500 - height)
        while len(pygame.sprite.spritecollide(self, all_sprites, False)) > 1:
            self.rect.x = randint(0, 500 - width)
            self.rect.y = randint(0, 500 - height)

    def update(self, event: pygame.MOUSEBUTTONDOWN = None):
        if not event:
            return
        if self.rect.collidepoint(*event.pos):
            self.image = Bomb.boom_image


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Boom them all — 2')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    is_running = True

    for _ in range(10):
        Bomb()

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)
        screen.fill('black')
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
