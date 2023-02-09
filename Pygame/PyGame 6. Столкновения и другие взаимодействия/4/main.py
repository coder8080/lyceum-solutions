from os import path
import pygame

all_sprites = pygame.sprite.Group()


def load_image(name: str) -> pygame.Surface:
    fullname = path.join('data', name)
    if not path.exists(fullname):
        print(f'Файл с изображением {fullname} не найден')
        exit(1)
    image = pygame.image.load(fullname)
    return image


class Mountain(pygame.sprite.Sprite):
    image = load_image('mountain.png')

    def __init__(self) -> None:
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = height


class Landing(pygame.sprite.Sprite):
    image = load_image('pt.png')

    def __init__(self, x, y) -> None:
        super().__init__(all_sprites)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y - self.rect.height // 2
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 3

    def update(self):
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect.y += self.speed


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Высадка десанта')
    size = width, height = 789, 300
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    is_running = True

    mountain = Mountain()

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Landing(*event.pos)
        screen.fill('white')
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)
