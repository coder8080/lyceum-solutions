import vk_api


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
    response = vk.friends.get(fields="bdate, first_name, last_name")
    result = []
    if response['items']:
        for i in response['items']:
            friend_str = f"{i['last_name']} {i['first_name']}: {i['bdate']}"
            result.append(friend_str)
    result.sort()
    print(*result)


if __name__ == '__main__':
    main()
