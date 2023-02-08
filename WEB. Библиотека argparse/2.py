import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--barbie', help="отношение пользователя к куклам", type=int, nargs='?', default=50)
parser.add_argument('--cars', help='отношение пользователя к машинам',
                    type=int, nargs='?', default=50)
parser.add_argument(
    '--movie', help='любимая телевизионная программа пользователя из списка' +
    ' [melodrama, football, other]', type=str, nargs='?', default='other')
args = parser.parse_args()
barbie, cars, movie = args.barbie, args.cars, args.movie
movie_value = 50
if movie == 'melodrama':
    movie_value = 0
elif movie == 'football':
    movie_value = 100
if cars < 0 or cars > 100:
    cars = 50
if barbie < 0 or barbie > 100:
    barbie = 50
boy = int((100 - barbie + cars + movie_value) / 3)
girl = 100 - boy
print(f'boy: {boy}')
print(f'girl: {girl}')
