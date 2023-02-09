import requests
import os
import shutil
import pygame

if os.path.exists('slides'):
    shutil.rmtree('slides')
os.makedirs('slides')

coords = [['37.617698,55.755864', 0.25], [
    '21.301831,45.70333', 0.0002], ['-123.008118,45.408166', 0.0002], ['62.18605,52.479761', 0.005], ['-111.487119,32.664162', 0.005], ['113.99354,62.529423', 0.01]]
pygame_images = []

for (i, [pos, size]) in enumerate(coords):
    url = f'http://static-maps.yandex.ru/1.x/?ll={pos}&spn={size},{size}&l=sat'
    response = requests.get(url)
    filename = os.path.join('slides', f'{i}.png')
    file = open(filename, 'wb')
    file.write(response.content)
    file.close()
    del file
    pygame_images.append(pygame.image.load(filename))


pygame.init()
i = 0
screen = pygame.display.set_mode((600, 450))
is_running = True
clock = pygame.time.Clock()
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            break
        elif event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
            i += 1
            i %= len(pygame_images)
    screen.fill((0, 0, 0))
    screen.blit(pygame_images[i], (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
shutil.rmtree('slides')
