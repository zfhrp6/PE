#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 112

左から右までどの桁もその左の桁を上回らない数を増加数と呼ぶ。例えば、134468。
同様に、どの桁もその右の桁を上回らない数を減少数と呼ぶ。例えば、66420。
増加数でも減少数でもない正の整数を「活発な」数と呼ぶことにする。例えば、155349。
100以下の数に活発な数が無いのは明らかだが、1000より下の数では半数を少し上回る数(525)が活発である。
実際、活発な数の割合が50%に達する最少の数は538である。
驚くべきことに、活発な数はますます一般的になり、21780では活発な数の割合は90%に達する。
活発な数が数の割合が99%ちょうどになる最小の数を求めよ。
"""
import time
time1 = time.time()
lst = [x for x in range(1, 101)]
i = 100
while True:
    i += 1
    stri = str(i)
    listi = list(stri)
    listup = list(stri)
    listup.sort()
    listdown = list(stri)
    listdown.sort()
    listdown.reverse()
    if listi == listup or listi == listdown:
        lst.append(i)
    if len(lst) * 1.0 / i == 1.0 / 100:
        break
    if time1 - time.time() > 300:
        break

print(i)
print('{} seconds'.format(time.time() - time1))
