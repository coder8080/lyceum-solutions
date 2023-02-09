import requests

server, port, a, b = [input() for _ in range(4)]
url = f'{server}:{port}?a={a}&b={b}'
data = requests.get(url).json()
print(sorted(data['result']))
print(data['check'])
