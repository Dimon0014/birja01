import json
import math
import requests

res = requests.get('https://yobit.net/api/3/info') # получаем данные info
res_obj = json.loads(res.text) # переводим полученный текст в объект с данными

pairs = [pair for pair in res_obj['pairs']] # создадим массив названий пар
cnt = 1
# Проходим в цикле, отбирая каждый раз по 100 пар (или меньше, в хвосте)
for i in range(0, int(math.ceil(len(pairs)/50))):
    pairs_str = '-'.join(pairs[i*50:(i+1)*50]) # формируем строку для передачи тикеру

    ticker_res = requests.get('https://yobit.net/api/3/ticker/'+pairs_str) # получаем данные info
    ticker_res_obj = json.loads(ticker_res.text) # переводим полученный текст в объект с данными

    for pair in ticker_res_obj:
        print(
            cnt,
            pair,
            '%0.8f' % ticker_res_obj[pair]['buy'],
            '%0.8f' % ticker_res_obj[pair]['sell']
        )
        cnt += 1
        