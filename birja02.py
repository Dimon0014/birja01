import json
import requests

res = requests.get('https://yobit.net/api/3/info') # получаем данные
res_obj = json.loads(res.text) # переводим полученный текст в объект с данными
#print(res_obj)
print("Получено %d пар(ы)!" % len(res_obj['pairs']))
pairs = '-'.join(res_obj['pairs']) # Формируем строку в нужном формате


pairs2 = [pair for pair in res_obj['pairs']]
print(pairs2)


#print(pairs)