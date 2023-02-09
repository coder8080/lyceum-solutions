import pygame
from os import path
from sys import exit


def load_image(name):
    fullname = path.join('data', name)
    if not path.exists(fullname):
        print(f'Файл с изображением {fullname} не найден')
        exit(1)
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Свой курсор мыши')
    pygame.mouse.set_visible(False)
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    is_running = True
    clock = pygame.time.Clock()
    arrow = load_image('arrow.png')
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
        screen.fill('black')
        if pygame.mouse.get_focused():
            screen.blit(arrow, pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
