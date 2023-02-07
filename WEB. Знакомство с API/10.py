import requests

API_KEY = '73961a13-a537-4463-a34a-bff0205a48e8'

address = input()
url = f'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}&format=json'
data = requests.get(url).json()
pos_str = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].replace(
    ' ', ',')
url = f'https://search-maps.yandex.ru/v1/?apikey={API_KEY}&text=метро&lang=ru_RU&ll={pos_str}&type=biz&results=1'
data = requests.get(url).json()

result = data['features'][0]['properties']['CompanyMetaData']['name']
print(result)
