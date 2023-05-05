import vk_api
from datetime import datetime


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    response = vk.wall.get(count=5)
    if response['items']:
        for item in response['items']:
            print(item['text'])
            num_date = item['date']
            post_datetime = datetime.utcfromtimestamp(num_date)
            string_data = f"date: {post_datetime.date()}, time: {post_datetime.time()}"
            print(string_data)


if __name__ == '__main__':
    main()
