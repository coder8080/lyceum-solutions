import pygame
from sys import exit
from os import path


def load_image(name):
    fullname = path.join('data', name)
    if not path.exists(fullname):
        print(f'Не удалось найти файл {fullname}')
        exit(1)
    image = pygame.image.load(fullname)
    return image


class Car(pygame.sprite.Sprite):
    image_right = load_image('car.png')
    image_left = pygame.transform.flip(image_right, True, False)
    speed = 2

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Car.image_right
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.direction = 'right'

    def update(self):
        if self.direction == 'right':
            self.rect.x = self.rect.x + Car.speed
            if self.rect.x > 450:
                self.direction = 'left'
                self.image = Car.image_left
        else:
            self.rect.x = self.rect.x - Car.speed
            if self.rect.x < 0:
                self.direction = 'right'
                self.image = Car.image_right


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Машинка')
    size = width, height = 600, 95
    screen = pygame.display.set_mode(size)
    is_running = True
    clock = pygame.time.Clock()
    sprites = pygame.sprite.Group()
    Car(sprites)
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
        screen.fill('white')
        sprites.draw(screen)
        sprites.update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
