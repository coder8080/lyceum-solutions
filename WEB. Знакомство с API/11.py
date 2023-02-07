import pygame
import requests
import os
import math


def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000
    a_lon, a_lat = a
    b_lon, b_lat = b
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor
    distance = math.sqrt(dx * dx + dy * dy)
    return distance


coords = ['37.629331,55.816546', '37.635107,55.803646',
          '37.587093,55.733974', '37.617734,55.752004']

tdistance = 0
llon, llat = list(map(float, coords[0].split(',')))
for str_c in coords[1:]:
    lon, lat = list(map(float, str_c.split(',')))
    distance = lonlat_distance((lon, lat), (llon, llat))
    tdistance += distance
    llon, llat = lon, lat
tdistance = round(tdistance) / 1000
center = '37.617698,55.755864'
pl = ",".join(coords)
image_url = f'http://static-maps.yandex.ru/1.x/?ll={center}&spn=0.10,0.10&l=map&pl={pl}'

response = requests.get(image_url)
filename = 'image.png'
file = open(filename, 'wb')
file.write(response.content)
file.close()
del file
image = pygame.image.load(filename)
pygame.init()
font = pygame.font.Font(None, 50)
text = font.render("Длина пути: " + str(tdistance) + " км", True, 'red')
pygame.display.set_caption('Длина пути')
screen = pygame.display.set_mode((600, 450))
screen.blit(image, (0, 0))
screen.blit(text, ((600 - text.get_width()) / 2, 10))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(filename)
