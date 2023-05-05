from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup
from translate import Translator
from config import BOT_TOKEN

user_to_lang = dict()

translation_options = [['На английский'],
                       ['На русский']]
options_keyboard = ReplyKeyboardMarkup(translation_options)


async def start(update, context):
    chat_id = update.message.chat_id
    user_to_lang[chat_id] = 'en'
    reply = 'Привет! Я Бот-Переводчик. Напиши мне фразу, и я её переведу.' +\
        ' По умолчанию я перевожу с русского на английский. Чтобы выбрать ' +\
        'другой вариант, нажми соответствующую конпку на клавиатуре'
    await update.message.reply_text(reply, reply_markup=options_keyboard)
    return 1


async def main_handler(update, context):
    text = update.message.text
    chat_id = update.message.chat_id
    if text == 'На английский':
        user_to_lang[chat_id] = 'en'
        await update.message.reply_text('Настройки сохранены')
        return 1
    elif text == 'На русский':
        user_to_lang[chat_id] = 'ru'
        await update.message.reply_text('Настройки сохранены')
        return 1
    else:
        return await translation_handler(update, context)


async def translation_handler(update, context):
    text = update.message.text
    chat_id = update.message.chat_id
    to_lang = user_to_lang[chat_id]
    from_lang = list(filter(lambda x: x != to_lang, ['ru', 'en']))[0]
    translator = Translator(to_lang=to_lang, from_lang=from_lang)
    translation = str(translator.translate(text))
    await update.message.reply_text(translation, reply_markup=options_keyboard)
    return 1


def main():
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, main_handler)]
        },
        fallbacks=[])
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
