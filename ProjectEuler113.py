#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 113

ある数の桁を左から右へと順に見たとき, 任意の桁の数が自身の左にある桁の数以上であるとき,
その数を増加数 (increasing number) と呼ぶ; 例えば134468は増加数である.
同様に, 任意の桁の数が自身の右にある桁の数以上であるとき,
その数を減少数 (decreasing number) と呼ぶ;例えば66420がそうである.
増加数でも減少数でもない数を "はずみ"数 ("bouncy" number) と呼ぶ; 155349がそうである.
nが大きくなるにつれ, n以下のはずみ数の割合は大きくなる.
例えば, 100万未満では, はずみ数でない数は12951個しかない. 同様に, 1010未満では277032個しかない.
googol数 (10^100) 未満ではずみ数でないものの数を答えよ.
"""
import time
time1 = time.time()
lst = [x for x in range(1, 101)]
i = 100
while i < 10 ** 100:
    i += 1
    if i % 100000 == 0:
        print(i)
    stri = str(i)
    listi = list(stri)
    listup = list(stri)
    listup.sort()
    listdown = list(stri)
    listdown.sort()
    listdown.reverse()
    if listi == listup or listi == listdown:
        lst.append(i)
    if time1 - time.time() > 300:
        break

print(len(lst))
print('{} seconds'.format(time.time() - time1))
