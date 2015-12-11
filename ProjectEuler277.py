#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 277

整数の修正コラッツ列は値 a_1 から始めて次のようにして得られる:
a_n が 3 で割り切れるならば a_(n+1) = a_n/3. これを大きな下ステップ "D" と表す.
a_n を 3 で割った余りが 1 ならば a_(n+1) = (4a_n + 2)/3. これを大きな上ステップ "U" と表す.
a_n を 3 で割った余りが 2 ならば a_(n+1) = (2a_n - 1)/3. これを小さな下ステップ "d" と表す.

数列は a_n = 1 となれば終了する.

任意の整数が与えられたとき, ステップの列を書き出すことができる.
例えば a_1=231 なら, 数列 {a_n}={231,77,51,17,11,7,10,14,9,3,1} はステップ "DdDddUUdDD" に対応する.

もちろん, 同じ列 "DdDddUUdDD...." から始まる列は他にもある.
例えば, a_1=1004064 なら, ステップの列は DdDddUUdDDDdUDUUUdDdUUDDDUdDD である.
実際, 1004064 は, 列 DdDddUUdDD から始まる最小の可能な a_1 > 10^6 である.

列 "UDDDUdddDDUDDddDdDddDDUDDdUUDd" から始まる最小の a_1 > 10^15 は何か？
"""
import time
t0 = time.time()
answer = 0
# 条件の始めのUDDDUdddDDUDDdを考察して初期値が824080(mod 4782969)、以降4782969ずつ増やす
a = 10 ** 15 + 208182
flag = False
while True:
    text = ""
    a += 4782969
    an = a
    answer = an
    if an % 100000 == 0:
        print(an)
    while an != 1:
        if len(text) == 30:
            if text == "UDDDUdddDDUDDddDdDddDDUDDdUUDd":
                flag = True
                break
            break
        if an % 3 == 0:
            an = an / 3
            text += "D"
        elif an % 3 == 1:
            an = (4 * an + 2) / 3
            text += "U"
        else:
            an = (2 * an - 1) / 3
            text += "d"
    if flag:
        break

print(answer)
print(time.time() - t0, "seconds")
