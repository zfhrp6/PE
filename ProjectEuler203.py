# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 203

二項係数nCkは三角形の形に並べることができる. すなわちパスカルの三角形である. 以下を見よ.

              1
            1   1
          1   2   1
        1   3    3   1
      1  4    6    4   1
    1   5  10   10   5   1
  1  6  15   20   15   6   1
1  7   21  35   35  21   7   1
....

上から8行見るとパスカルの三角形は12個の異なる数を含む.
1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21, 35である.
任意の素数の二乗がnを割り切らないとき, 正整数nが平方因子を持たないと言う.
先ほどの12個の数字を見ると, 4, 20以外は平方因子を持たない.
従って, 最初の8行の平方因子を持たない異なる数の和は105になる.
パスカルの三角形の最初の51行に含まれる平方因子を持たない異なる数の和を答えよ.
"""
import time
import math
import Euler
time1=time.time()
sosu=Euler.prime_make(50000)
trilist=[x for x in range(1,50)]
answerlist=[]
for i in range(2,51):
    for j in range(int(i)):
        trilist.append((math.factorial(i)/(math.factorial(j)*math.factorial(i-j))))
trilist=list(set(trilist))
for k in trilist:
    check=1
    for l in sosu:
        if k%(l**2)==0:
            check=0
            break
    if check==1:
        answerlist.append(k)
answerlist=list(set(answerlist))

print sum(answerlist)
print time.time()-time1, "seconds"
