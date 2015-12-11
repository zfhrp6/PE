#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 39

辺の長さが{a,b,c}と整数の3つ組である直角三角形を考え, その周囲の長さをpとする.
p = 120のときには3つの解が存在する:

    {20,48,52}, {24,45,51}, {30,40,50}

p ≦ 1000 で解の数が最大になる p を求めよ.
-------------------------------------------------------------
"""
import time
import math
time1 = time.time()
ansdic = {}
for a in range(1, 1000):
    for b in range(a, 1000):
        c = math.sqrt(a ** 2 + b ** 2)
        if c == int(c):
            c = int(c)
            if c + a + b < 1001:
                if c < a + b and c > a and c > b:
                    try:
                        ansdic[a + b + c] += 1
                    except KeyError:
                        ansdic[a + b + c] = 1
p, amount = 0, 0
for i, j in ansdic.items():
    if j > amount:
        p, amount = i, j

print("answer is %d . %d has %d solutions." % (p, p, amount))
print(time.time() - time1, "seconds")
