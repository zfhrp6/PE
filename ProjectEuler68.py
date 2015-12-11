#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 68

問題は省略した。魔法陣の問題だったような気がする。あらかじめ求める順番を考えて最小になるように頑張っている。
なるかどうかは別問題。
"""
import time
import itertools
time1 = time.time()
anslist = []
for i in itertools.permutations(list(range(1, 11))):
    if i[0] + i[1] + i[2] == i[3] + i[2] + i[4] == i[5] + i[4] + i[6] == i[7] + i[6] + i[8] == i[9] + i[8] + i[0]:
        anslist.append(i)

anslist2 = []
for j in anslist:
    anslist2.append(str(j[0]) + str(j[1]) + str(j[2]) + str(j[3]) + str(j[2]) + str(j[4]) + str(j[5]) +
                    str(j[4]) + str(j[6]) + str(j[7]) + str(j[6]) + str(j[8]) + str(j[9]) + str(j[8]) + str(j[0]))

anslist3 = []
for k in anslist2:
    if len(k) == 16:
        anslist3.append(int(k))
anslist3.sort()

print(anslist3)
print(time.time() - time1, "seconds")
