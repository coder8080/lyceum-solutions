import requests

data = requests.get(
    "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Петровка, 38&format=json").json()
print(data['response']['GeoObjectCollection']
      ['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['postal_code'])
