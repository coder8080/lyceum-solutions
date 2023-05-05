from telegram.ext import Application, MessageHandler, ConversationHandler, CommandHandler, filters
from config import BOT_TOKEN
import requests


async def start(update, context):
    response = 'Привет. Напиши мне название места, которое хочешь увидеть, и я отправлю тебе карту'
    await update.message.reply_text(response)
    return 1


async def main_handler(update, context):
    request_text = update.message.text
    geocoder_apikey = "40d1649f-0493-4b70-98ba-98533de7710b"
    url = f'https://geocode-maps.yandex.ru/1.x?geocode={request_text}&apikey={geocoder_apikey}&format=json'
    response = requests.get(url)
    if response.status_code != 200:
        await update.message.reply_text(f'Во время получения данных произошла ошибка с кодом {response.status_code}. Попробуй повторить запрос позже')
        return 1
    json = None
    try:
        json = response.json()
    except Exception as e:
        await update.message.reply_text(f'Во время обработки данных прозошла ошибка {type(e.__class__).__name__}. Попробуйте повторить запрос позже')
        return 1
    lon = None
    lat = None
    try:
        pos = json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        lon, lat = [float(el) for el in pos.split()]
    except Exception:
        await update.message.reply_text("По вашему запросу ничего не нашлось. Попробуйте сформулировать иначе")
        return 1
    map_url = f'http://static-maps.yandex.ru/1.x/?ll={lon},{lat}&spn=0.02,0.02&l=map&pt={lon},{lat},round'
    await context.bot.send_photo(update.message.chat_id, map_url, caption="Вот что я нашёл. Что ещё вы хотите увидеть?")
    return 1


def main():
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, main_handler)]},
        fallbacks=[]
    )
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
