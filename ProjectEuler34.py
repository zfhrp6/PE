# -*- coding: utf-8 -*-
#project euler problem 34
#各桁の数の階乗の和が自分自身と一致するような数の総和を求めよ.
#1と2は除く.
import time
import math
time1=time.time()
n=3
s=0
while n<2540160:
    sum=0
    st=str(n)
    for i in range(0,len(st)):
        sum+=math.factorial(int(st[i]))
    if sum==n:
        s+=n
    n=n+1
    i=1
print s
print time.time()-time1, "seconds"