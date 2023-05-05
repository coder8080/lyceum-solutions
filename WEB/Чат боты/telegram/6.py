from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import ReplyKeyboardMarkup
from config import BOT_TOKEN


DEFAULT_TEXT = ''
ROOM1 = 'Комната 1: Эпоха первобытной общины'
ROOM2 = 'Комната 2: Распад первобытной общины'
ROOM3 = 'Комната 3: Эпоха Великого переселения народов'
ROOM4 = 'Комната 4: Культура Древней Руси'
EXIT = 'Выход'


async def entrance(update, context):
    text = 'Добро пожаловать! Пожалуйста, сдайте верхнюю одежду в гардероб!'
    response_keyboard = [[ROOM1]]
    markup = ReplyKeyboardMarkup(response_keyboard)
    await update.message.reply_text(text, reply_markup=markup)


async def exit_handler(update, context):
    text = 'Всего доброго, не забудьте забрать верхнюю одежду в гардеробе!'
    response_keyboard = [['/start']]
    markup = ReplyKeyboardMarkup(response_keyboard)
    await update.message.reply_text(text, reply_markup=markup)


async def first_room(update, context):
    text = 'В данном зале представлена эпоха прообщины, ранный и средний палиолит.' +\
        ' Ископаемые останки первых людей, найденные в Восточной Африке, имеют' +\
        ' возраст 2.5-1.8 миллиона лет. Они уже могли изготавливать примитивные' +\
        ' каменные орудия, и были объединены в пока еще аморфные, неустойчивые' +\
        ' коллективы, называемые праобщиной.\nВыберите следующую комнату'
    response_keyboard = [[ROOM2, EXIT]]
    markup = ReplyKeyboardMarkup(response_keyboard)
    await update.message.reply_text(text, reply_markup=markup)


async def second_room(update, context):
    text = 'В энеолите и бронзовом веке происходит прогрессирующее развитие всех' +\
        ' отраслей хозяйственной деятельности человека, сопровождающиеся' +\
        ' изменениями в структуре общества и сложными этнокультурными процессами.'
    resonse_keyboard = [[ROOM3]]
    markup = ReplyKeyboardMarkup(resonse_keyboard)
    await update.message.reply_text(text, reply_markup=markup)


async def third_room(update, context):
    text = 'Экспозиция зала посвящена периоду перехода от древности к' +\
        ' средневековью, III-VIII вв. нашей эры. В это время появляются' +\
        ' группы племен, послужившие основой для сложения народов,' +\
        ' существующих до настоящего времени'
    response_keyboard = [[ROOM1, ROOM4]]
    markup = ReplyKeyboardMarkup(response_keyboard)
    await update.message.reply_text(text, reply_markup=markup)


async def fourth_room(update, context):
    text = 'Сложная и трудная история Руси сохранила ничтожную часть того' +\
        ' богатства памятников архитектуры, письменности и прикладного' +\
        ' искусства, которые были созданы умелыми руками наших предков в' +\
        ' IX – XIII веках.'
    response_keyboard = [[ROOM1]]
    markup = ReplyKeyboardMarkup(response_keyboard)
    await update.message.reply_text(text, reply_markup=markup)

NAMES = [ROOM1, ROOM2, ROOM3, ROOM4, EXIT]
HANDLERS = [first_room, second_room, third_room, fourth_room, exit_handler]


async def main_handler(update, context):
    text = update.message.text
    if text not in NAMES:
        await update.message.reply_text('Я не смог вас понять(')
        return
    idx = NAMES.index(text)
    handler = HANDLERS[idx]
    await handler(update, context)


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', entrance))
    application.add_handler(MessageHandler(filters.TEXT, main_handler))
    application.run_polling()


if __name__ == '__main__':
    main()
