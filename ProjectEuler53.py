# -*- coding: utf-8 -*-
# project euler problem 53
# 1 ≤ n ≤ 100について, 100万を超えるnCrは何通りか?
import math
import time

time1 = time.time()
s = 0
for n in range(5, 101):
    r = 1
    while r <= n:
        if math.factorial(n) / (math.factorial(r) * math.factorial(n - r)) > 1000000:
            s = s + 1
        r += 1
print(s)
print(time.time() - time1)
