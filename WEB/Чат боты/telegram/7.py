from telegram.ext import Application, ConversationHandler, filters, CommandHandler, MessageHandler
from config import BOT_TOKEN
from telegram import ReplyKeyboardMarkup

text = ['— Скажи-ка, дядя, ведь недаром',
        'Москва, спаленная пожаром,',
        'Французу отдана?',
        'Ведь были ж схватки боевые,',
        'Да, говорят, еще какие!',
        'Недаром помнит вся Россия',
        'Про день Бородина!']

user_stage = dict()


async def start(update, context):
    chat_id = update.effective_message.chat_id
    user_stage[chat_id] = 1  # индекс ожидаемой строчки
    response_keyboard = [['/stop']]
    markup = ReplyKeyboardMarkup(response_keyboard)
    await update.message.reply_text(text[0], reply_markup=markup)
    return 1


async def main_handler(update, context):
    chat_id = update.effective_message.chat_id
    expected_index = user_stage[chat_id]
    expected_string = text[expected_index]
    string = update.message.text
    if expected_string == string:
        response_text = text[expected_index + 1]
        user_stage[chat_id] = expected_index + 2
        response_keyboard = [[]]
        result = 1
        if user_stage[chat_id] >= len(text):
            response_text += '\nМне очень понравилось. Повторим?'
            response_keyboard[0].append('/start')
            result = ConversationHandler.END
        else:
            response_keyboard[0].append('/stop')
        markup = ReplyKeyboardMarkup(response_keyboard)
        await update.message.reply_text(response_text, reply_markup=markup)
        return result
    else:
        response_text = 'Нет, не так'
        response_keyboard = [['/suphler', '/stop']]
        markup = ReplyKeyboardMarkup(response_keyboard)
        await update.message.reply_text(response_text, reply_markup=markup)
        return 1


async def stop(update, context):
    response_text = 'Ладно. Может быть, начнём сначала?'
    response_keyboard = [['/start']]
    markup = ReplyKeyboardMarkup(response_keyboard)
    await update.message.reply_text(response_text, reply_markup=markup)
    return ConversationHandler.END


async def help(update, context):
    chat_id = update.effective_message.chat_id
    expected_string = text[user_stage[chat_id]]
    await update.message.reply_text(f'Должно быть вот так: "{expected_string}"')
    return 1


def main():
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, main_handler)]
        },
        fallbacks=[CommandHandler('stop', stop),
                   CommandHandler('suphler', help)
                   ]
    )
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(conversation_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
