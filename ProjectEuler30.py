# -*- coding: utf-8 -*-
# project euler problem 30
# 各桁を5乗した和が元の数と一致するような数の総和を求めよ.
# 1は除く.
import time
time1 = time.time()
n = 2
s = 0
while n < 295346:
    sum = 0
    st = str(n)
    for i in range(0, len(st)):
        sum += (int(st[i])) ** 5
        i = i + 1
    if sum == n:
        s += n
    n = n + 1
    i = 1
print(s)
print(time.time() - time1, "seconds")
