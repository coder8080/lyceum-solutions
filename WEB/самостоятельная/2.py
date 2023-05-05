import json
import requests
from pprint import pprint

with open('back.json') as file:
    f = file.read()
    data = json.loads(f)

server = data['server']
port = data['port']
param = data['param']

url = f"http://{server}:{port}"

data = requests.get(url).json()
main_list = data[param]


average_list = list()

for numbers_list in main_list:
    s = sum(numbers_list)
    average_list.append(s)

ans = sum(average_list) / len(average_list)
ans = int(round(ans * 100)) / 100
print(ans)
