#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 95

ある数の真の約数とは, それ自身を除く約数すべてである.
例えば, 28 の真の約数は 1, 2, 4, 7, 14 である。これらの約数の和は 28 に等しいため, これを完全数と呼ぶ.
面白いことに, 220 の真の約数の和は 284 で, 284 の真の約数の和は 220 となっており,
二つの数が鎖をなしている. このため, 220 と 284 は友愛数と呼ばれる.
さらに長い鎖はあまり知られていないだろう. 例えば, 12496 から始めると, 5 つの数の鎖をなす.

 12496 , 14288 , 15472 , 14536 , 14264 (, 12496 , ...)

この鎖は出発点に戻っているため, 友愛鎖と呼ばれる.
いずれの要素も 1,000,000 を超えない最長の友愛鎖の最小のメンバーを求めよ.
"""
import time
import Euler
time1 = time.time()
templist = []
anslist = []
for i in range(11, 1000000):
    templist = []
    min_menber = i
    if Euler.sum_divisors(i) < i:
        continue
    while i >= min_menber:
        i = Euler.sum_divisors(i)
        if i == min_menber or i > 1000000:
            break
        templist.append(i)
    if i == min_menber and len(templist) > len(anslist):
        anslist = templist


print(min(anslist))
print(time.time() - time1, "seconds")
