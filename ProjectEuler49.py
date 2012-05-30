# -*- coding: utf-8 -*-
#Project Euler Problem 49
"""
項差3330の等差数列1487, 4817, 8147は次の2つの変わった性質を持つ。

    * (i)3つの項はそれぞれ素数である。
    * (ii)各項は他の項の置換で表される。

1, 2, 3桁の素数にはこのような性質を持った数列は存在しないが、4桁の増加列にはもう1つ存在する。
それではこの数列の3つの項を連結した12桁の数を求めよ。
"""

import time
import Euler
import itertools
time1=time.time()

"""
s=[2]
i=3
while i<10000:
    for j in s:
        if i%j==0:
            break
        else:
            if j==s[-1]:
                s.append(i)
                break
    i=i+2

del(s[:168]) #1000より小さいリストの中の項を削除した
answer=[]
for k in range(len(s)-2):
    if len(answer)==2:
        break
    for l in range(2,4502,2):
        a=list(str(s[k]))
        a.sort()
        b=list(str(s[k]+l))
        b.sort()
        c=list(str(s[k]+2*l))
        c.sort()
        if (s[k]+l in s) and (s[k]+2*l in s):
            if a==b==c:
                answer.append((s[k],s[k]+l,s[k]+2*l))
                break
"""
answer=[]
primes=tuple(Euler.prime_make(10000))
for p1,p2 in itertools.combinations(primes,2):
    if p1<1000 or p2<1000:
        continue
    p3=2*p2-p1
    if p3 not in primes:
        continue
    p1str,p2str,p3str=map(list,map(str,[p1,p2,p3]))
    p1str.sort()
    p2str.sort()
    p3str.sort()
    if p1str==p2str and p2str==p3str:
        answer.append((p1,p2,p3))


print answer
print time.time()-time1,"Seconds"