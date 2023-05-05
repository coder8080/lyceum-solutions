from config import BOT_TOKEN
import discord
import requests


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} подключился')

    async def on_message(self, message):
        pass


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = YLBotClient(intents=intents)
client.run(BOT_TOKEN)
