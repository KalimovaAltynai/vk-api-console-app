import requests
import json

# Замените значение access_token на ваш токенннн
access_token = 'VK_ACCESS_TOKEN'
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