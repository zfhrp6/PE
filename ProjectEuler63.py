#!/usr/bin/env python
# coding:utf-8
"""
Project Euler Problem 63


5桁の数 16807 = 7^5は自然数を5乗した数である.
同様に9桁の数 134217728 = 8^9も自然数を9乗した数である.
自然数をn乗して得られるn桁の正整数は何個あるか?
"""
import time
import math
c = 0
ls = []
time1 = time.time()
for i in range(1, 10):  # 10以上は無駄
    for j in range(1, 101):  # 9^100乗が96桁しかないので。
        if math.log10(i ** j) + 1 >= j:
            c += 1
            ls.append(i ** j)

print(c)
print(time.time() - time1, "seconds")
del(c, i, j)
