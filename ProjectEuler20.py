# -*- coding: utf-8 -*-
# project euler problem 20
# 100!の各桁の数字の総和を求めよ.
import math
import time

time1 = time.time()
s = 0
st = str(math.factorial(100))
for i in range(0, len(st)):
    s += int(st[i])
print(s)
print(time.time() - time1, 'seconds')
