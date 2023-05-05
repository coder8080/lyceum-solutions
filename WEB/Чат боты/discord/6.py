import asyncio
from discord.ext import commands
import discord
from config import BOT_TOKEN, WEATHER_KEY
import requests
from datetime import datetime


def get_lonlat(request_text: str):
    geocoder_apikey = "40d1649f-0493-4b70-98ba-98533de7710b"
    url = f'https://geocode-maps.yandex.ru/1.x?geocode={request_text}&apikey={geocoder_apikey}&format=json'
    response = requests.get(url)
    json = None
    json = response.json()
    pos = json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    lon, lat = [float(el) for el in pos.split()]
    return lon, lat


HELP_TEXT = """
#!place изменить место получения прогноза
#!current получить текущую погоду
#!forecast {days} получить прогноз на {days} дней вперёд (максимум 5)
#!help_bot показать это сообщение
"""

user_lon = dict()
user_lat = dict()
user_place = dict()


def parse_to_text(response, author):
    global user_place
    data = response["main"]
    current_temperature = round(data["temp"] - 273)
    current_pressure = data["pressure"]
    current_humidity = data["humidity"]
    a = response["weather"]
    weather_description = a[0]["description"]
    wind_data = response['wind']

    result = f"""
# Weather in {user_place[author]} {response['dt_txt']}
Desciprion: {weather_description}
Temperature: {current_temperature}
Pressure: {current_pressure}
Humidity: {current_humidity}
Wind speed: {wind_data['speed']}
Wind deg: {wind_data['deg']}
--
            """
    return result


class MorphThings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='place')
    async def place(self, ctx, *words):
        global user_lon
        global user_lat
        global user_place
        author = ctx.author
        text = ' '.join(words)
        lon, lat = get_lonlat(text)
        user_place[author] = text
        user_lon[author] = lon
        user_lat[author] = lat
        await ctx.send('Успешно сохранено')

    @commands.command(name='current')
    async def current(self, ctx, *words):
        global user_lon
        global user_lat
        global user_place
        author = ctx.author
        if author not in user_lon or author not in user_lat:
            await ctx.send('Сначала выберите место')
            return
        lon = user_lon[author]
        lat = user_lat[author]
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_KEY}'
        response = requests.get(url).json()
        now = str(datetime.now())
        response['dt_txt'] = now

        result = parse_to_text(response, author)

        await ctx.send(result)

    @commands.command(name='forecast')
    async def forecast(self, ctx, days):
        global user_lon
        global user_lat
        global user_place
        days = int(days)
        author = ctx.author
        if author not in user_lon or author not in user_lat:
            await ctx.send('Сначала выберите место')
            return
        lon = user_lon[author]
        lat = user_lat[author]
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={WEATHER_KEY}'
        response = requests.get(url).json()
        result = []
        for item in response['list']:
            dt_txt = item['dt_txt']
            _, time = dt_txt.split()
            if time != '15:00:00':
                continue
            text = parse_to_text(item, author)
            result.append(text)
        result = result[:days]
        for item in result:
            await ctx.send(item)

    @commands.command(name='help_bot')
    async def help(self, ctx):
        await ctx.send(HELP_TEXT)


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#!', intents=intents)


async def main():
    await bot.add_cog(MorphThings(bot))
    await bot.start(BOT_TOKEN)

asyncio.run(main())
