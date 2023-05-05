import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from datetime import date

TOKEN: str = TOKEN
GROUP_ID: int = GROUP_ID

days = ['понедельник', 'вторник', 'среда',
        'четверг', 'пятница', 'суббота', 'воскресенье']


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, GROUP_ID)

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            sender_id: int = int(event.obj.message['from_id'])
            text = event.obj.message['text']
            response = f"Привет"
            try:
                splitted = text.split('-')
                year = int(splitted[0])
                month = int(splitted[1])
                day = int(splitted[2])

                message_date = date(year, month, day)
                weekday = message_date.weekday()
                response = days[weekday]
            except Exception:
                response = 'Отправьте мне дату в формате YYYY-MM-DD, и я скажу, какой это день недели'
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=response,
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
