# -*- coding: utf-8 -*-
# project euler problem 80
"""
よく知られているように, 自然数の平方根が整数ではないならば, それは無理数である.
そのような平方根の10進数表示(decimal expansion)は繰り返しを持たない無限小数になる.
2の平方根は, 1.41421356237309504880...,であり, その頭から100桁の数字を合計すると475になる.
初めの100個の自然数の平方根のうち, 無理数について, それぞれの頭から100桁の数字を足した数の総和を求めよ.
"""
import time
import math
time1 = time.time()

s = 0
for i in range(1, 101):
    if math.sqrt(i) % 1 != 0:
        # if len
        for n in range(1, 101):
            s += int(str(i)[n])
print(s)
print(time.time() - time1, "Seconds")
