import pygame
from random import randint

all_sprites = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface(
            (radius * 2, radius * 2), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, 'red', (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = randint(-5, 5)
        self.vy = randint(-5, 5)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy *= -1
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx *= -1


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        if x1 == x2:
            # вертикальная стенка
            super().__init__(vertical_borders)
            self.image = pygame.Surface((1, y2 - y1))
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        elif y1 == y2:
            # горизонтальная стенка
            super().__init__(horizontal_borders)
            self.image = pygame.Surface((x2 - x1, 1))
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)
        else:
            raise ValueError(
                f'incorrect points for border: ({x1}, {y1}); ({x2}, {y2})')


if __name__ == '__main__':
    Border(5, 5, 495, 5)  # врехняя
    Border(495, 5, 495, 495)  # правая
    Border(5, 495, 495, 495)  # нижняя
    Border(5, 5, 5, 495)  # левая

    for i in range(20):
        Ball(20, randint(20, 480), randint(20, 480))

    pygame.init()
    pygame.display.set_caption('Balls')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    is_running = True
    clock = pygame.time.Clock()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
        screen.fill('white')
        all_sprites.update()
        vertical_borders.update()
        horizontal_borders.update()

        all_sprites.draw(screen)
        vertical_borders.draw(screen)
        horizontal_borders.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
