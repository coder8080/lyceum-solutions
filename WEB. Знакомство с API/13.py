import requests
import math

HEIGHT = 525


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


address = input()
url = f'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}&format=json'
data = requests.get(url).json()
pos1 = map(float, data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(
    ' '))
url = f'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Останкинская Телебашня&format=json'
data = requests.get(url).json()
pos2 = map(float, data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(
    ' '))
l = lonlat_distance(pos1, pos2) / 1000
h = (l / 3.6 - math.sqrt(HEIGHT)) ** 2
print(str(round(h)) + 'м')
