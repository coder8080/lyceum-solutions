from config import BOT_TOKEN
import discord
from asyncio import sleep
import random

has_timers = dict()


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} подключился')

    async def on_message(self, message):
        if message.author == self.user:
            return
        text = message.content.lower().split()
        try:
            if text[0] != 'set_timer':
                return
            author = message.author
            if author not in has_timers:
                has_timers[author] = False
            if has_timers[author]:
                await message.channel.send('У вас уже запущен таймер')
                return
            _, _, hours, _, minutes, _ = text
            hours = int(hours)
            minutes = int(minutes)
            time = minutes * 60 + hours * 3600
            has_timers[author] = True
            await message.channel.send('Таймер запущен')
            while time > 0:
                await sleep(1)
                time -= 1
            await message.channel.send('⏰ Время X пришло!')
            has_timers[author] = False
        except Exception:
            await message.channel.send('Ваша команда не распознана. Напишите так: "set_timer in <a> hours <b> minutes"')


intents = discord.Intents.default()
intents.message_content = True
client = YLBotClient(intents=intents)
client.run(BOT_TOKEN)
