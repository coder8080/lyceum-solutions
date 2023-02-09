import requests
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


school = input()
home = input()

scu = f'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={school}&format=json'
hcu = f'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={home}&format=json'
sdata = requests.get(scu).json()
hdata = requests.get(hcu).json()
spos = sdata['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
hpos = hdata['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
slon, slat = list(map(float, spos.split()))
hlon, hlat = list(map(float, hpos.split()))
distance = lonlat_distance((slon, slat), (hlon, hlat))
print(str(round(distance) / 1000) + " км")
