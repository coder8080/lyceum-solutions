import os
import shutil
import requests
from get_coords import get_coords
from random import choice, randrange
from render_coords import render_coords
import pygame

ADDRESS = "http://static-maps.yandex.ru/1.x/"

cities = ['Челлябинск', 'Чехов', 'Владивосток', 'Тюмень']
if os.path.exists('images'):
    shutil.rmtree('images')
os.mkdir('images')
images = []
for i, city in enumerate(cities):
    coords = list(get_coords(city))
    lon_delta = randrange(20, 30) / 1000.0
    lat_delta = randrange(20, 30) / 1000.0
    if choice([True, False]):
        lon_delta *= -1
    if choice([True, False]):
        lat_delta *= -1
    spn = randrange(5, 30) / 1000.0
    coords[0] += lon_delta
    coords[1] += lat_delta
    lonlat = render_coords(coords)
    params = {"ll": lonlat, "l": choice(['map', 'sat']), "spn": f'{spn},{spn}'}
    response = requests.get(ADDRESS, params=params)
    filename = os.path.join('images', f'{i}.png')
    file = open(filename, 'wb')
    file.write(response.content)
    file.close()
    images.append(pygame.image.load(filename))
    del file


pygame.init()
pygame.display.set_caption('Угадай-ка город')
screen = pygame.display.set_mode((600, 450))
is_running = True
image = choice(images)
clock = pygame.time.Clock()
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            break
        elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
            prev_image = image
            while prev_image == image:
                image = choice(images)
    screen.fill('black')
    screen.blit(image, (0, 0))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


shutil.rmtree('images')
