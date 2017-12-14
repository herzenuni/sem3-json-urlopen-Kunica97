import pprint
import json
from urllib.request import urlopen

id = input()
request = "https://api.vk.com/method/users.get?user_ids={id}&v=5.8&fields=status".format(id = id)

try:
    request_obj = urlopen(request)
	obj = json.loads(request_obj.read())
except:
	print('Ошибка!')

print('Ответ сервера :')
pprint.pprint(obj)