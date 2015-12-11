# -*- coding: utf-8 -*-
# project euler problem 2
# フィボナッチ数列の400万までの項のうち偶数の項の総和を求めよ。
import time
time1 = time.time()
i = 1
j = 2
s = 2
while i <= 4000000:
    k = i + j
    i = j
    j = k
    if k % 2 == 0:
        s += k
print("answer is"), s
print(time.time() - time1, "seconds")
