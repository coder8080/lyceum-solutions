import json
from telegram.ext import Application, MessageHandler, CommandHandler, ConversationHandler, filters
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
from config import BOT_TOKEN
from random import shuffle

available_for_user = dict()
correct_answer_count = dict()


print('Введите имя файла с вопросами')
filename = input()
with open(filename) as file:
    f = file.read()
    data = json.loads(f)['test']
print('Данные из файла получены. Запускаю бота')


async def start(update, context):
    chat_id = update.effective_message.chat_id
    available_for_user[chat_id] = data.copy()
    correct_answer_count[chat_id] = 0
    shuffle(available_for_user[chat_id])
    await update.message.reply_text(f'Пройдите тест\nДля досрочного завершения отправьте /stop\n\n# {available_for_user[chat_id][0]["question"]}', reply_markup=ReplyKeyboardRemove())
    return 1


async def main_handler(update, context):
    chat_id = update.effective_message.chat_id
    text = update.message.text
    correct_ans = available_for_user[chat_id][0]['response']
    available_for_user[chat_id].pop(0)
    if text == correct_ans:
        correct_answer_count[chat_id] += 1
    if len(available_for_user[chat_id]) == 0:
        cor_count = correct_answer_count[chat_id]
        all_count = len(data)
        percent = round(cor_count / all_count * 100)
        response_text = f'Вопросы закончились. Ваш результат {cor_count}/{all_count} : {percent}%'
        response_keyboard = [['/start']]
        markup = ReplyKeyboardMarkup(response_keyboard)
        await update.message.reply_text(response_text, reply_markup=markup)
        return ConversationHandler.END
    else:
        question = available_for_user[chat_id][0]['question']
        await update.message.reply_text('# ' + question)
        return 1


async def stop(update, context):
    chat_id = update.effective_message.chat_id
    del correct_answer_count[chat_id]
    del available_for_user[chat_id]
    response_text = 'Ладно. Чтобы начать сначала, напишите /start'
    response_keyboard = [['/start']]
    markup = ReplyKeyboardMarkup(response_keyboard)
    await update.message.reply_text(response_text, reply_markup=markup)
    return ConversationHandler.END


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        1: [MessageHandler(filters.TEXT & ~filters.COMMAND, main_handler)]
    },
    fallbacks=[CommandHandler('stop', stop)]
)

application = Application.builder().token(BOT_TOKEN).build()
application.add_handler(conv_handler)
application.run_polling()
