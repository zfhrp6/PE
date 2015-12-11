# -*- coding: utf-8 -*-
"""
Problem 21

d(n)をnの真の約数の和と定義する。（真の約数とはn以外の約数のことである。）
もし、d(a)=b かつ d(b)=a （a≠b）を満たすとき、aとbは友愛数（親和数）であるという。

例えば、220の約数は1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110なのでd(220)=284である。
また、284の約数は1, 2, 4, 71, 142なのでd(284)=220である。

それでは10000未満の友愛数の合計を求めよ。
"""
import time
from math import sqrt
time1 = time.time()

SUM = 0
for i in range(5, 10000):
    sum_a = 0
    sum_b = 0
    for j in range(2, int(sqrt(i))):
        if i % j == 0:
            sum_a += j + i / j
    if int(sqrt(i)) ** 2 == i:
        sum_a += int(sqrt(i))
    sum_a += 1

    if sum_a <= i:
        continue

    for k in range(2, int(sqrt(sum_a))):
        if sum_a % k == 0:
            sum_b += k + sum_a / k
    if int(sqrt(sum_a)) ** 2 == sum_a:
        sum_b += int(sqrt(sum_a))
    sum_b += 1

    if sum_a > 10000 or sum_b > 10000:
        continue

    if sum_b == i:
        SUM += sum_a + i

print(SUM)
print(time.time() - time1, "seconds")
