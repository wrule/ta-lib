#!/opt/homebrew/bin/python3

import numpy
import talib

close = numpy.random.random(100)
output = talib.MA(close, 44)
print(output)
