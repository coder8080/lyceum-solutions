import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random
from requests import get

TOKEN: str = TOKEN
GROUP_ID: int = GROUP_ID

days = ['понедельник', 'вторник', 'среда',
        'четверг', 'пятница', 'суббота', 'воскресенье']

user_stage = dict()
user_text = dict()

text_to_map_type = {'спутник': 'sat', 'схема': 'map', 'гибрид': 'sat,skl'}


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, GROUP_ID)
    upload = vk_api.VkUpload(vk_session)

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:

            sender_id: int = int(event.obj.message['from_id'])
            text = event.obj.message['text']

            response = ''

            if sender_id not in user_stage:
                user_stage[sender_id] = 1

            if user_stage[sender_id] == 1:
                # Нужно попросить пользователя отправить место
                response = 'Введи название места, которое хочешь увидеть'
                user_stage[sender_id] = 2
                vk = vk_session.get_api()

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=response,
                                 random_id=random.randint(0, 2 ** 64))

            elif user_stage[sender_id] == 2:
                # Пользователь отправил название места
                user_text[sender_id] = text
                user_stage[sender_id] = 3

                vk = vk_session.get_api()

                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button('Схема', color=VkKeyboardColor.POSITIVE)
                keyboard.add_button(
                    'Спутник', color=VkKeyboardColor.POSITIVE)
                keyboard.add_button(
                    'Гибрид', color=VkKeyboardColor.POSITIVE)

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f'Выбери тип карты',
                                 random_id=random.randint(0, 2 ** 64),
                                 keyboard=keyboard.get_keyboard())
            elif user_stage[sender_id] == 3:
                text_map_type = text.lower()
                map_type = text_to_map_type.get(text_map_type, 'map')
                request_text = user_text[sender_id]
                geocoder_apikey = "40d1649f-0493-4b70-98ba-98533de7710b"
                url = f'https://geocode-maps.yandex.ru/1.x?geocode={request_text}&apikey={geocoder_apikey}&format=json'
                response = get(url).json()['response']
                pos = response['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']

                lon, lat = [float(el) for el in pos.split()]

                map_url = f'http://static-maps.yandex.ru/1.x/?ll={lon},{lat}&spn=0.02,0.02&l={map_type}'
                response = get(map_url)
                map_filename = 'map.png'
                with open(map_filename, 'wb') as file:
                    file.write(response.content)
                photo = upload.photo_messages(
                    [map_filename])
                vk_photo_id = f'photo{photo[0]["owner_id"]}_{photo[0]["id"]}'

                vk = vk_session.get_api()

                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f'Это {request_text}. Что Вы еще хотите увидеть?',
                                 attachment=vk_photo_id,
                                 random_id=random.randint(0, 2 ** 64),)
                user_stage[sender_id] = 2


if __name__ == '__main__':
    main()
