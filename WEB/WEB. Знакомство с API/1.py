import requests

data = requests.get(
    "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Красная пл-дь, 1&format=json").json()
print(data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
      ['metaDataProperty']['GeocoderMetaData']['AddressDetails']['Country']['AddressLine'])
print(data['response']['GeoObjectCollection']
      ['featureMember'][0]['GeoObject']['Point']['pos'])
