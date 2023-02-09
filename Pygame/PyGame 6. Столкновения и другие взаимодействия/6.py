import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__(player_group)
        self.image = pygame.Surface((20, 20))
        pygame.draw.rect(self.image, 'blue', (0, 0, 20, 20))
        self.rect = self.image.get_rect()
        self.rect.y = -20
        self.speed = 5.0 / 6.0
        self.y = None

    def update(self, event=None):
        if not event:
            if self.y is None:
                return
            self.y += self.speed
            colliding_sprite = pygame.sprite.spritecollideany(self, platforms)
            if colliding_sprite:
                self.y = colliding_sprite.rect.y - 20
        elif event:
            if hasattr(event, 'pos'):
                x, y = event.pos
                self.rect.x = x - 10
                self.y = y - 10
            elif hasattr(event, 'key'):
                if event.key == pygame.K_RIGHT:
                    self.rect.x += 10
                elif event.key == pygame.K_LEFT:
                    self.rect.x -= 10
        if self.y is not None:
            self.rect.y = round(self.y)


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(platforms)
        self.image = pygame.Surface((50, 10))
        self.image.fill('gray')
        self.rect = self.image.get_rect()
        self.rect.x = x - 25
        self.rect.y = y - 5


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Платформы')

    platforms = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    Player()

    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    player_group.update(event)
                elif event.button == 1:
                    Platform(*event.pos)
            elif event.type == pygame.KEYDOWN:
                player_group.update(event)
        screen.fill('black')
        platforms.update()
        player_group.update()
        platforms.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
