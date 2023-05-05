from config import BOT_TOKEN
import discord
import requests


def download_cat_image(name: str):
    json = requests.get('https://api.thecatapi.com/v1/images/search').json()
    url = json[0]['url']
    response = requests.get(url)
    filename = f'{name}.jpg'
    with open(filename, 'wb') as file:
        file.write(response.content)
    return filename


def download_dog_image(name: str):
    json = requests.get('https://dog.ceo/api/breeds/image/random').json()
    url = json['message']
    response = requests.get(url)
    filename = f'{name}.jpg'
    with open(filename, 'wb') as file:
        file.write(response.content)
    return filename


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} подключился и готов показывать животных')

    async def on_message(self, message):
        if message.author == self.user:
            return
        text = message.content.lower()
        filename = None
        if 'котик' in text:
            filename = download_cat_image(message.author)
        elif 'собачка' in text:
            filename = download_dog_image(message.author)
        if filename is not None:
            with open(filename, 'rb') as file:
                picture = discord.File(file)
                await message.channel.send(file=picture)
        else:
            await message.channel.send('no cats or dogs found')


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = YLBotClient(intents=intents)
client.run(BOT_TOKEN)
