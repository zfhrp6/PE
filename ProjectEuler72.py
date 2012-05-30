#coding:utf-8
#!/usr/bin/env python
"""
Project Euler Problem 72

nとdを正の整数として, 分数 n/d を考えよう. n<dかつHCF(n,d)=1のとき, 真既約分数と呼ぶ.
d ≤ 8について既約分数を大きさ順に並べると, 以下を得る:
    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
この集合は21個の要素をもつことが分かる.
d ≤ 1,000,000について, 真既約分数の集合は何個の要素を持つか?
"""
import time
import math
import Euler
t1=time.time()

ans_list=[]

def tagainiso(n,m):
    re=list(set(Euler.factoring(n))&set(Euler.factoring(m)))
    if re==[1]:
        re=[]
    return re

for d in xrange(1,1000000):
    print d
    for n in xrange(1,d):
        if tagainiso(n,d)==[]:
            ans_list.append(1.0*n/d)

ans_list=list(set(ans_list))
answer=len(ans_list)
print answer
print time.time()-t1, "seconds"