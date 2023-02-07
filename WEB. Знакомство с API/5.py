import os
import sys
import pygame
import requests

pos_url = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=австралия&format=json'
data = requests.get(pos_url).json()
pos_str = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
pos = pos_str.split()

photo_url = f'http://static-maps.yandex.ru/1.x/?ll={",".join(pos)}&spn=20,20&l=sat'
response = requests.get(photo_url)

if not response:
    print('Ошибка')
    sys.exit(1)

photo_filename = "australia.png"
photo_file = open(photo_filename, 'wb')
photo_file.write(response.content)
photo_file.close()
del photo_file

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(photo_filename), (0, 0))
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(photo_filename)
