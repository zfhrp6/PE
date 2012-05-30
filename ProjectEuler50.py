#coding:utf-8
#!/usr/bin/env python
"""
Project Euler Problem 50

素数41は6つの連続する素数の和として表せる:

41 = 2 + 3 + 5 + 7 + 11 + 13.

100未満の素数を連続する素数の和で表したときにこれが最長になる.
同様に, 連続する素数の和で1000未満の素数を表したときに最長になるのは953で21項を持つ.
100万未満の素数を連続する素数の和で表したときに最長になるのはどの素数か?
"""
import time
import math
import Euler
time1=time.time()
maxl=0

limit=1000000
answer=0

max_kosuu=550  #この個数を超えて和を求めても100万を超過する

primes=tuple(Euler.prime_make(limit))
primes_2=tuple(primes[1:])

for i in xrange(2,max_kosuu,2):
    sums=sum(primes[:i])
    length=len(primes[:i])
    if sums>limit:
        break
    if length>maxl and sums in primes:
        maxl=length
        answer=sums
        print maxl,"""primes[:i],""""sum is",sums

for i in xrange(3,max_kosuu,2):
    for j in xrange(len(primes_2)-i):
        sums=sum(primes_2[j:i])
        length=len(primes[j:i])
        if sums>limit:
            break
        if length>maxl and sums in primes:
            maxl=length
            answer=sums
            print maxl,"""primes_2[j:i],""""sum is",sums

"""
def inlistcheck(x,seq):
    seq=seq.sort()
    if seq[0]==x:
        return 1
    elif seq[0]>x:
        return 0
    else:
        if x>seq[len(seq)/2]:
            inlistcheck(x,seq[:len(seq)/2])
        else:
            inlistcheck(x,seq[len(seq)/2:])
"""
"""
number=0 #条件を満たす最後の素数を保持する
l=22
k=22
for l in range(22,len(s)-100):
    for i in range(len(s)-l):
        if sum(s[i:i+l]) in s:
            number=sum(s[i:i+l])
            k=l
"""

print answer
print time.time()-time1, "seconds"