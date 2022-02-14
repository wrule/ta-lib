#!/opt/homebrew/bin/python3

import numpy
import talib
import json
import datetime

data = json.load(open('btcusd.json', 'r'))

# a = dict.items(data.__dict__)

list = []
for key, value in data['data']['points'].items():
  list.append({
    'time': int(key),
    'price': value['v'][0],
  })
list.sort(key = lambda x: x['time'], reverse = False)

prices = map(lambda x: x['price'], list)

print(len(prices))

# print(len(data['data']['points']))

# close = numpy.random.random(100)
# output = talib.MA(close, 44)
# print(output)
