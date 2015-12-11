# -*- coding: utf-8 -*-
# project euler problem 56
# a, b < 100について自然数a**bを考える. 桁の和の最大を答えよ.
import time
t0 = time.time()
a = 0
b = 1
m = 1
while a < 100:
    b = 1
    while b < 100:
        st = str(a ** b)
        i = 0
        sum = 0
        for i in range(0, len(st)):
            sum = sum + (int(st[i]))
            i = i + 1
        if m < sum:
            m = sum
        b = b + 1
    a = a + 1
print(m)
print(time.time() - t0, "seconds")
