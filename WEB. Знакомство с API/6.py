import os
import sys
import requests
import pygame

positions = []
places = ['Спартак', 'Динамо', 'Лужники']

moscow_data = requests.get(
    'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=москва&format=json').json()
moscow_pos = moscow_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()

for place in places:
    url = f'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={place} москва&format=json'
    data = requests.get(url).json()
    pos_str = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    pos = pos_str.split()
    positions.append(pos)

pt_value = '~'.join(map(lambda x: f'{x[0]},{x[1]},round', positions[:3]))
photo_url = f'http://static-maps.yandex.ru/1.x/?ll={",".join(moscow_pos)}&spn=0.2,0.2&pt={pt_value}&l=map'
response = requests.get(photo_url)

if not response:
    print('Ошибка')
    sys.exit(1)

photo_filename = 'moscow.png'
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
