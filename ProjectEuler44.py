#!/usr/bin/env python
# coding:utf-8
"""
Project Euler Problem 44

五角数は P_n = n(3n-1)/2で生成される. 最初の10項は

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

である.

P_4 + P_7 = 22 + 70 = 92 = P_8である. しかし差 70 - 22 = 48は五角数ではない.
五角数のペア P_jとP_kについて, 差と和が五角数になるものを考える.
差を D = |P_k - P_j| と書く. 差 D の最小値を求めよ.
"""
import itertools
import time
import math
time1 = time.time()
pentalst = []


def is_penta(x):
    if ((1 + math.sqrt(1 + 24 * x)) / 6) % 1 == 0:
        return True
    else:
        return False
for i in range(1, 3001):
    pentalst.append(i * (3 * i - 1) / 2)
pentalst = tuple(pentalst)
diff_min = 100000000000000000000000000000000000000
for j, k in itertools.combinations(list(range(len(pentalst))), 2):
    sa = int(math.fabs(pentalst[j] - pentalst[k]))
    wa = int(pentalst[j] + pentalst[k])
    if is_penta(sa) and is_penta(wa) and (sa < diff_min):
        diff_min = sa
        break

print(diff_min)
print(time.time() - time1, "seconds")
