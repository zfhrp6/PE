#!/usr/bin/env python
# coding:utf-8
"""
Project Euler Problem 71

nとdを正の整数として, 分数 n/d を考えよう. n<dかつHCF(n,d)=1のとき, 真既約分数と呼ぶ.

d ≤ 8について既約分数を大きさ順に並べると, 以下を得る:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

3/7のすぐ左の分数は2/5である.

d ≤ 1,000,000について真既約分数を大きさ順に並べたとき, 3/7のすぐ左の分数の分子を求めよ.
"""
import time
time1 = time.time()

values = []
lists = []
for d in range(1000001, 16, -1):
    if d % 1000 == 0:
        print(d)
    for n in range(int(d * 29999999999999.0 / 70000000000001), int(d * 3.00000001 / 7)):
        a = 1.0 * n / d
        if a > 3.0 / 7:
            break
        if a not in values:
            lists.append((a, n, d))

lists.sort()
lists = tuple(lists)

"""for i in xrange(len(lists)):
    if lists[i][1]==3 and lists[i][2]==7:
        answer=lists[i-1]
        break"""

print(lists[-1])
print(time.time() - time1, "seconds")
