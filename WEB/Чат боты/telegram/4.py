from telegram.ext import Application, filters, CommandHandler, ConversationHandler, MessageHandler
from telegram import ReplyKeyboardMarkup
from config import BOT_TOKEN
from datetime import datetime
from random import randrange


def get_dice_keyboard():
    reply_keyboard = [['кинуть один шестигранный кубик',
                       'кинуть 2 шестигранных кубика одновременно'],
                      ['кинуть 20-гранный кубик', 'вернуться назад']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    return markup


def get_timer_keyboard():
    reply_keyboard = [['30 секунд', '1 минута'],
                      ['5 минут', 'вернуться назад']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    return markup


async def start(update, context):
    reply_keyboard = [['/dice', '/timer']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text('Выбери команду на клавиатуре', reply_markup=markup)


async def dice(update, context):
    await update.message.reply_text('Выбери команду на клавиатуре', reply_markup=get_dice_keyboard())


async def timer(update, context):
    markup = get_timer_keyboard()
    await update.message.reply_text('Выбери продолжительность таймера', reply_markup=markup)


def remove_job_if_exists(chat_id, context):
    current_jobs = context.job_queue.get_jobs_by_name(str(chat_id))
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


async def task(context):
    markup = get_timer_keyboard()
    await context.bot.send_message(context.job.chat_id, text="Время вышло", reply_markup=markup)


async def set_timer(update, context, time):
    chat_id = update.effective_message.chat_id
    job_removed = remove_job_if_exists(chat_id, context)
    context.job_queue.run_once(task, time, chat_id=chat_id, name=str(chat_id))
    text = 'Таймер установлен'
    if job_removed:
        text += ', при этом старый таймер уделён.'
    reply_keyboard = [['Остановить таймер']]
    markup = ReplyKeyboardMarkup(reply_keyboard)
    await update.message.reply_text(text, reply_markup=markup)


async def stop_timer(update, context):
    chat_id = update.effective_message.chat_id
    job_removed = remove_job_if_exists(chat_id, context)
    text = ''
    if job_removed:
        text = 'Таймер остановлен'
    else:
        text = 'У тебя нет запущенных таймеров'
    markup = get_timer_keyboard()
    await update.message.reply_text(text, reply_markup=markup)


async def handle_message(update, context):
    text = update.message.text
    if text == 'вернуться назад':
        await start(update, context)
    elif text == 'кинуть один шестигранный кубик':
        await update.message.reply_text(f"Выпало {randrange(1, 6)}", reply_markup=get_dice_keyboard())
    elif text == 'кинуть 2 шестигранных кубика одновременно':
        await update.message.reply_text(f"Выпало {randrange(1, 6)} и {randrange(1, 6)}", reply_markup=get_dice_keyboard())
    elif text == 'кинуть 20-гранный кубик':
        await update.message.reply_text(f"Выпало {randrange(1, 20)}",  reply_markup=get_dice_keyboard())
    elif text == '30 секунд':
        await set_timer(update, context, 30)
    elif text == '1 минута':
        await set_timer(update, context, 60)
    elif text == '5 минут':
        await set_timer(update, context, 60 * 5)
    elif text == 'Остановить таймер':
        await stop_timer(update, context)
    else:
        await update.message.reply_text('Я тебя не понимаю')


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('dice', dice))
    application.add_handler(CommandHandler('timer', timer))
    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    application.run_polling()


if __name__ == '__main__':
    main()
