from config import BOT_TOKEN
import discord
from discord.ext import commands
import asyncio
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

HELP_TEXT = """
#!numerals для согласования с числительными
#!alive чтобы определить одушевленность существительног
#!noun чтобы поставить существительное в нужную форму (nomn, gent, datv, accs, ablt, loct) и изменить форму числительного (single, plural)
#!inf для постановки в начальную форму
#!morph для морфологического анализа
#!help показать это сообщение
"""


class MorphThings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='numerals')
    async def numerals(self, ctx, word, number):
        word = str(word)
        number = int(number)
        comment = morph.parse(word)[0]
        result = comment.make_agree_with_number(number).word
        await ctx.send(f"{number} {result}")

    @commands.command(name='alive')
    async def alive(self, ctx, word):
        word = str(word)
        p = morph.parse(word)[0]
        if 'anim' in p.tag:
            await ctx.send('Одушевлённое существительное')
        else:
            await ctx.send('Неодушевлённое существительное')

    @commands.command(name='noun')
    async def noun(self, ctx, word, *tags):
        try:
            word = str(word)
            parsed = morph.parse(word)[0]
            tags_set = {*tags}
            word = parsed.inflect(tags_set)[0]
            await ctx.send(word)
        except Exception as e:
            await ctx.send(str(e))

    @commands.command(name='inf')
    async def inf(self, ctx, word):
        word = str(word)
        result = morph.parse(word)[0].normal_form
        await ctx.send(result)

    @commands.command(name='morph')
    async def morph(self, ctx, word):
        word = str(word)
        parsed = morph.parse(word)[0]
        result = parsed.tag
        await ctx.send(result)


class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.blurple(), description='')
        e.description += HELP_TEXT
        await destination.send(embed=e)


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#!', intents=intents,
                   help_command=MyHelpCommand())


async def main():
    await bot.add_cog(MorphThings(bot))
    await bot.start(BOT_TOKEN)

asyncio.run(main())
