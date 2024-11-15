import requests
import json

# Замените значение access_token на ваш токен
access_token = 'vk1.a.fMod3-bJFgnhiuS9TPLYKdux7CaxGDHLDslumO1UnP4_VMyrAd0Ww2_CinUgQbN1O0Q7CoMglq7cPLLNp0vHmcHNwtNoyJKyNXPgH5DLopfOUltP2W-7maxxARklyCGr0VgtvBBawLfF7Bt5gTIuy00wcK4cdp-gmcvAYipnl38b0ARXxJy9UXWYXPQ0XeBk2a1IjvMHgkUpA75KCY5DqQ'
user_id = '169188359'  # Укажите здесь свой ID ВКонтакте

def get_user_info(user_id, access_token):
    """Получение информации о пользователе"""
    url = 'https://api.vk.com/method/users.get'
    params = {
        'user_ids': user_id,
        'access_token': access_token,
        'v': '5.131'
    }
    response = requests.get(url, params=params)
    return response.json()

def get_friends(user_id, access_token):
    """Получение списка друзей пользователя"""
    url = 'https://api.vk.com/method/friends.get'
    params = {
        'user_id': user_id,
        'access_token': access_token,
        'v': '5.131',
        'fields': 'nickname'
    }
    response = requests.get(url, params=params)
    return response.json()

def get_groups(user_id, access_token):
    """Получение списка групп пользователя"""
    url = 'https://api.vk.com/method/groups.get'
    params = {
        'user_id': user_id,
        'access_token': access_token,
        'v': '5.131',
        'extended': 1  # Позволяет получить больше информации о группах
    }
    response = requests.get(url, params=params)
    return response.json()

def save_to_json(data, filename='result.json'):
    """Сохранение данных в JSON файл"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    # Получение информации о пользователе
    user_info = get_user_info(user_id, access_token)
    print("Информация о пользователе:", user_info)

    # Получение друзей пользователя
    friends = get_friends(user_id, access_token)
    print("Список друзей:", friends)

    # Получение групп пользователя
    groups = get_groups(user_id, access_token)
    print("Список групп:", groups)

    # Сохранение всех данных в один JSON файл
    data = {
        'user_info': user_info,
        'friends': friends,
        'groups': groups
    }
    save_to_json(data)
    print("Данные сохранены в файл result.json")

if __name__ == '__main__':
    main()