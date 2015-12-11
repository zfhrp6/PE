#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 104

フィボナッチ数列は再帰的な関係によって定義される:
F_n = F_n−1 + F_n−2

F_541 (113桁)は, 下9桁に1から9までの数字をすべて含む初めてのフィボナッチ数である.
そして, F_2749 (575桁)は, 頭から9桁に1から9までの数字をすべて含む初めてのフィボナッチ数である.

F_kが, 頭から9桁と下9桁のどちらも1から9までの数字をすべて含む初めてのフィボナッチ数とするとき, kを求めよ.
"""
import time
time1 = time.time()
i = 1
j = 2
s = 2
count = 3
answer = 0
while i < (10 ** 10000):
    k = i + j
    i = j
    j = k
    count += 1
    if k < 10 ** 9:
        continue
    st1 = str(k)[:9]
    st2 = str(k)[-9:]
    if ("0" in st1) or ("0" in st2):
        continue
    else:
        if len(list(set(list(st1)))) == 9:
            if len(list(set(list(st2)))) == 9:
                answer = count
                break

print(k, answer)
print('{} seconds'.format(time.time() - time1))
input()
