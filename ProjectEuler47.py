# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 47

連続する2つの数がそれぞれ2つの異なる素因数を持つのは
    * 14 = 2 × 7
    * 15 = 3 × 5 の場合である.
同様に連続する3つの数がそれぞれ3つの異なる素因数を持つのは
    * 644 = 22 × 7 × 23
    * 645 = 3 × 5 × 43
    * 646 = 2 × 17 × 19 の場合である.
連続する4つの数がそれぞれ4つの異なる素因数を持つ場合を考え, 連続する数の中で最小のものを答えよ.
"""
import time
import Euler
time1=time.time()

def func(x):
    ans=list(set(Euler.factoring(x)))
    ans.sort()
    return ans

x=0
while time.time()-time1<3000:
    x+=1
    if len(func(x+3))!=4:
        x+=3
        continue
    elif len(func(x+2))!=4:
        x+=2
        continue
    elif len(func(x+1))!=4:
        x+1
        continue
    elif len(func(x))!=4:
        continue
    else:
        print "ok"
        break
print "answer is %d"%(x)
print time.time()-time1,"seconds"
