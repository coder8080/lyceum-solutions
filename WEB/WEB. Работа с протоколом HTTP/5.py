from get_coords import get_coords
import requests
import sys

coords = get_coords(' '.join(sys.argv[1:]))
address = 'https://geocode-maps.yandex.ru/1.x'
params = {"geocode": ','.join(list(map(str, coords))),
          "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
          "kind": "district",
          "format": "json",
          "results": 1}
data = requests.get(address, params=params).json()
print(data['response']['GeoObjectCollection']
      ['featureMember'][0]['GeoObject']['name'])
