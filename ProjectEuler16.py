# -*- coding: utf-8 -*-
# project euler problem 16
# 2**1000 の各桁の数字の合計を求めよ。
import time
time1 = time.time()

s = 0
num = 2 ** 1000
while num >= 10:
    s += num % 10
    num = (num - num % 10) / 10

s += num
print(s)
print(time.time() - time1, "seconds")
