#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 100

箱の中に15個の青い円盤と6個の赤い円盤からなる21個の色のついた円盤が入っていて、
無作為に2つ取り出すとき、青い円盤2つを取り出す確率P(BB)は
    P(BB) = (15/21) × (14/20) = 1/2
であることがわかる。

無作為に2つ取り出すとき、青い円盤2つを取り出す確率がちょうど1/2となるような次の組み合わせは、
箱が85個の青い円盤と35個の赤い円盤からなるときである。

箱の中の円盤の合計が10^12 = 1,000,000,000,000を超えるような最初の組み合わせを考える。
箱の中の青い円盤の数を求めよ。

※だいたい0.707107のところになる。
"""
import time
t0 = time.time()
amount = 100
blue = 0
flag = True

ans_l = []

while flag:
    amount += 1
    if amount % 1000 == 0:
        print(amount)
    for i in range(amount * 7065 / 10000, amount * 707108 / 1000000):
        if i * (i - 1) * 1.0 / (amount * (amount - 1)) == 0.5:
            blue = i
            ans_l.append((blue, amount, blue * 1.0 / amount))
            if len(ans_l) > 0:
                flag = False
                break

print('{}, {}, {}'.format(blue, amount, blue * 1.0 / amount))
print(ans_l)
print('{} seconds'.format(time.time() - t0))
