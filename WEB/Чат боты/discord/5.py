from config import BOT_TOKEN
import discord
from discord.ext import commands
import asyncio
import pymorphy2
from translate import Translator

HELP_TEXT = """
!!set_lang сменить язык (пример `!!set_lang ru-en`)
!!text выполнить перевод (пример `!!text привет`)
!!help_bot показать это сообщение
"""

to_lang = dict()
from_lang = dict()


def set_default(author: str):
    if author not in to_lang:
        to_lang[author] = 'en'
    if author not in from_lang:
        from_lang[author] = 'ru'


class MorphThings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='set_lang')
    async def numerals(self, ctx, option):
        author = ctx.author
        set_default(author)
        fr, to = option.split('-')
        from_lang[author] = fr
        to_lang[author] = to
        await ctx.send(f"Настройки успешно сохранены")

    @commands.command(name='text')
    async def text(self, ctx, *words):
        author = ctx.author
        set_default(author)
        text = ' '.join(words)
        translator = Translator(
            to_lang=to_lang[author], from_lang=from_lang[author])
        translation = str(translator.translate(text))
        await ctx.send(translation)

    @commands.command(name='help_bot')
    async def help(self, ctx):
        await ctx.send(HELP_TEXT)


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!!', intents=intents)


async def main():
    await bot.add_cog(MorphThings(bot))
    await bot.start(BOT_TOKEN)

asyncio.run(main())
