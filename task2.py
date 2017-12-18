import pprint
import json
from urllib.request import urlopen

def user_vk(id):
    request = "https://api.vk.com/method/users.get?user_ids={id}&v=5.8&fields=status".format(id = id)

    try:
        request_obj = urlopen(request)
        obj = json.loads(request_obj.read())
    except:
        print('Ошибка!')
    return obj


if __name__ == "__main__":
    id = input(' Введите id :')
    print('Ответ сервера :')
    pprint.pprint(user_vk(id))