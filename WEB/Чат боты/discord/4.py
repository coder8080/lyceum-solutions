from config import BOT_TOKEN
import discord
import random

left_for_user = dict()
user_score = dict()
bot_score = dict()
DEFAULT_SMILES = list('🧐💀🐍🥐🎮🚗')


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} подключился')

    async def on_message(self, message: str):
        global left_for_user
        global user_score
        global bot_score
        author = message.author
        if author == self.user:
            return
        if author not in left_for_user:
            left_for_user[author] = DEFAULT_SMILES
        if author not in user_score:
            user_score[author] = 0
        if author not in bot_score:
            bot_score[author] = 0
        left = left_for_user[author]
        text = message.content.lower()
        if not text.isdigit():
            if message == '/stop':
                del left_for_user[author]
                del user_score[author]
                del bot_score[author]
                await message.channel.send('Reset successful')
                return
            await message.channel.send('Ожидаю число')
        user_num = int(text) % len(left)
        bot_num = random.randrange(1, 100) % len(left)
        user_emoji = left[user_num]
        bot_emoji = left[bot_num]
        current_user_score = ord(user_emoji)
        current_bot_score = ord(bot_emoji)
        user_score[author] += current_user_score
        bot_score[author] += current_bot_score
        left_for_user[author] = list(filter(
            lambda x: x != bot_emoji and x != user_emoji, left_for_user[author]))
        if len(left_for_user[author]) > 0:
            result = f"""
            Your emoji: {user_emoji}
Bot emoji: {bot_emoji}
Score: You {user_score[author]} - Bot {bot_score[author]}
            """
        else:
            win_text = ''
            if user_score[author] > bot_score[author]:
                win_text = 'You win!'
            elif user_score[author] < bot_score[author]:
                win_text = 'Bot win!'
            else:
                win_text = 'Draw!'
            result = f"""
            Emotions are over
Your emoji: {user_emoji}
Bot emoji: {bot_emoji}
Score: You {user_score[author]} - Bot {bot_score[author]}
{win_text}
            """
        await message.channel.send(result)


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = YLBotClient(intents=intents)
client.run(BOT_TOKEN)
