import requests

cities = ['Хабаровск', 'Уфа', 'Нижний Новгород', 'Калининград']

for city in cities:
    data = requests.get(
        f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={city}&format=json").json()
    print(city + ': ' + data['response']['GeoObjectCollection']
          ['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components'][1]['name'])
