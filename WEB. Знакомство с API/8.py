import sys
import requests

ans_name = ''
ans_pos = -1

for line in sys.stdin:
    city = line.strip().strip('\n')
    url = f'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={city}&format=json'
    data = requests.get(url).json()
    pos_str = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    pos = list(map(float, pos_str.split(' ')))
    lat = pos[1]
    if ans_pos == -1 or lat < ans_pos:
        ans_pos = lat
        ans_name = city

print(ans_name)
