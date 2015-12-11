#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 99

指数の形で表される2つの数, 例えば 2^11 と 3^7, の大小を調べることは難しくはない.
電卓を使えば, 2^11 = 2048 < 3^7 = 2187 であることが確かめられる.

しかし, 632382^518061 > 519432^525806 を確認することは非常に難しい (両者ともに300万桁以上になる).

各行に1組が書かれている1000個の組を含んだ22Kのテキストファイルbase_exp.txtから,
最大の数が書かれている行の番号を求めよ.

注: ファイル中の最初の二行は上の例である.
"""
import time
import math
t0 = time.time()
answer_val = 0
line = 0
for x in open("projecteuler99base_exp.txt", "r"):
    line += 1
    num = math.log(int(x.split(",")[0])) * int(x.split(",")[1])
    if num > answer_val:
        answer_val = num
        answer = line
    print(line)

print("answer=%d" % (answer))
print(time.time() - t0, "seconds")
