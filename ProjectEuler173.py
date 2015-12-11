#!/usr/bin/env python
# coding:utf-8
"""
Project Euler Problem 173

輪郭が正方形で、正方形の穴を持ち、縦にも横にも対称性をもつようなものをlaminaeと定義する。
例えば、32個のタイルを使うと以下の二つの異なったlaminaeが作れる。

100個以下のタイルを使うと、41種類のlaminaeが作れる。

100万個以下のタイルを使うと何種類のlaminaeが作れるか?
"""
import time
t1 = time.time()

count = 0
for i in range(3, 500001):
    if i % 100 == 0:
        print(i)
    for j in range(i % 2, i - 1, 2):
        if j == 0:
            continue

        ij = (i + j) * (i - j)
        if ij < 1000001:
            count += 1

print(count)
print(time.time() - t1, "seconds")
