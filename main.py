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
    'value': value,
  })
list.sort(key = lambda x: x['time'], reverse = True)
for item in list:
  print(datetime.datetime.fromtimestamp(item['time']))

# print(len(data['data']['points']))

# close = numpy.random.random(100)
# output = talib.MA(close, 44)
# print(output)
