import sys
from io import BytesIO
import requests
from PIL import Image


def is_fullday(availabilities: list[map]):
    for entry in availabilities:
        if "TwentyFourHours" in entry and entry['TwentyFourHours'] == True:
            return True
    return False


def generate_point(str_coords: str, color: str):
    return f'{str_coords},pm2{color}l'


toponym_to_find = " ".join(sys.argv[1:])
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"].split(" ")
toponym_longitude, toponym_lattitude = toponym_coodrinates

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": ','.join([toponym_longitude, toponym_lattitude]),
    "type": "biz",
    "results": 10
}

data = requests.get(search_api_server, params=search_params).json()

roundclock = []
nonroundclock = []
unknown = []

for organizaiton in data["features"]:
    organization_coordinates = organizaiton['geometry']['coordinates']
    organization_metadata = organizaiton['properties']['CompanyMetaData']
    isroundclock = False
    isknown = False
    if 'Hours' in organization_metadata and 'Availabilities' in organization_metadata['Hours']:
        isroundclock = is_fullday(
            organization_metadata['Hours']['Availabilities'])
    if 'Hours' in organization_metadata:
        isknown = True
    str_coords = ','.join(map(str, organization_coordinates))
    if str_coords != '':
        if isroundclock:
            roundclock.append(str_coords)
        elif isknown:
            nonroundclock.append(str_coords)
        else:
            unknown.append(str_coords)
roundclock_str = '~'.join([generate_point(el, 'gn') for el in roundclock])
nonroundclock_str = '~'.join([generate_point(el, 'bl')
                             for el in nonroundclock])
unknown_str = '~'.join([generate_point(el, 'gr') for el in unknown])
to_join = []
if roundclock_str != '':
    to_join.append(roundclock_str)
if nonroundclock_str != '':
    to_join.append(nonroundclock_str)
if unknown_str != '':
    to_join.append(unknown_str)
pt = '~'.join(to_join)

map_params = {
    "l": "map",
    "pt": pt
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
Image.open(BytesIO(
    response.content)).show()
