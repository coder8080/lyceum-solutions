from os import path
from sys import exit
import pygame

FPS = 60
WIDTH = 800
HEIGHT = 450
CELL_WIDTH = 50
CELL_HEIGHT = 50


def load_image(name: str) -> pygame.Surface:
    fullname = path.join('data', name)
    if not path.exists(fullname):
        print(f'Файл с изображением {fullname} не найден')
        exit(1)
    image = pygame.image.load(fullname)
    return image


def terminate():
    pygame.quit()
    exit()


def start_screen():
    intro_text = ['ЗАСТАВКА', '', 'Герой перемещается с помощью стрелок',
                  'на клавиатуре', 'Нажмите любую клавшину чтобы продолжить']
    background = pygame.transform.scale(
        load_image('background.jpg'), (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        text = font.render(line, 1, pygame.Color('black'))
        text_rect = text.get_rect()
        text_rect.top = text_coord
        text_rect.left = 10
        text_coord += 10
        text_coord += text_rect.height
        screen.blit(text, text_rect)
    is_running = True
    clock = pygame.time.Clock()
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
                is_running = False
                break
        pygame.display.flip()
        clock.tick(FPS)


class Player(pygame.sprite.Sprite):
    image = load_image('player.png')

    def __init__(self, x, y):
        super().__init__(player_group)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.x = x * CELL_WIDTH + 13
        self.rect.y = y * CELL_HEIGHT + 5

    def update(self, event=None):
        if not event:
            return
        if hasattr(event, 'key'):
            last_position = self.rect.x, self.rect.y
            if event.key == pygame.K_UP:
                self.rect.y -= CELL_HEIGHT
            elif event.key == pygame.K_DOWN:
                self.rect.y += CELL_HEIGHT
            elif event.key == pygame.K_LEFT:
                self.rect.x -= CELL_WIDTH
            elif event.key == pygame.K_RIGHT:
                self.rect.x += CELL_WIDTH
            else:
                return
            if self.rect.y < 0 or self.rect.x < 0 or self.rect.y >= HEIGHT\
                    or self.rect.x >= WIDTH or pygame.sprite.spritecollideany(self, boxes):
                self.rect.x, self.rect. y = last_position


class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y, image, group):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * CELL_WIDTH
        self.rect.y = y * CELL_HEIGHT


class Grass(Cell):
    image = load_image('grass.png')

    def __init__(self, x, y):
        super().__init__(x, y, Grass.image, grass)


class Box(Cell):
    image = load_image('box.png')

    def __init__(self, x, y):
        super().__init__(x, y, Box.image, boxes)


def load_level(number: int):
    fullname = path.join('levels', f'{number}.txt')
    if not path.exists(fullname):
        print('ERROR: Такого уровня не существует')
        terminate()
    file = open(fullname, 'rt', encoding='utf-8')
    level = file.readlines()
    for i in range(len(level)):
        level[i] = level[i].strip()
    file.close()
    player_group.empty()
    boxes.empty()
    grass.empty()
    for i in range(len(level)):
        for j in range(len(level[0])):
            sym = level[i][j]
            if sym == '*':
                Box(j, i)
            elif sym == '.':
                Grass(j, i)
            elif sym == '@':
                Player(j, i)
                Grass(j, i)


if __name__ == '__main__':
    print('Введите номер уровня (1, 2, ...)')
    number = int(input())
    pygame.init()
    pygame.display.set_caption('Перемещение героя')
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    grass = pygame.sprite.Group()
    boxes = pygame.sprite.Group()
    player_group = pygame.sprite.GroupSingle()
    is_running = True
    clock = pygame.time.Clock()
    start_screen()
    load_level(number)
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.KEYDOWN:
                player_group.update(event)
        screen.fill('black')
        grass.update()
        boxes.update()
        player_group.update()
        grass.draw(screen)
        boxes.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    terminate()
