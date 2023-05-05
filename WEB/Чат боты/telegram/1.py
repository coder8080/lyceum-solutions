from telegram.ext import Application, MessageHandler, filters, Updater, CommandHandler
from config import BOT_TOKEN
from datetime import datetime


async def echo(update, context):
    await update.message.reply_text(f'Я получил сообщение «{update.message.text}»')


async def time(update, context):
    now = datetime.now().time()
    string_now = f"{now.hour}:{now.minute}"
    await update.message.reply_text(string_now)


async def date(update, context):
    now = datetime.now().date()
    string_now = str(now)
    await update.message.reply_text(string_now)


async def task(context):
    await context.bot.send_message(context.job.chat_id, text=f"{context.job.data['timer']} с прошли")


def remove_job_if_exists(name, context):
    current_jobs = context.job_queue.get_jobs_by_name(str(name))
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


async def set_time(update, context):
    """ Добавляем задачу в очередь """
    timer = 5
    try:
        timer = int(context.args[0])
    except Exception:
        pass
    chat_id = update.effective_message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    context.job_queue.run_once(
        task, timer, chat_id=chat_id, name=str(chat_id), data={'timer': timer})
    text = f'вернусь через {timer} с'
    if job_removed:
        text += '\nстарая задачу удалена'
    await update.effective_message.reply_text(text)


async def unset(update, context):
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(chat_id, context)
    text = 'Таймер остановлен' if job_removed else 'У вас нет активных таймеров'
    await update.message.reply_text(text)


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(CommandHandler('time', time))
    application.add_handler(CommandHandler('date', date))
    application.add_handler(CommandHandler('set_timer', set_time))
    application.add_handler(CommandHandler('unset', unset))
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
