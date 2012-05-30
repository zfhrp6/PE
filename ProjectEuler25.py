# -*- coding: utf-8 -*-
#project euler problem 25
#フィボナッチ数列において1000桁になる最初の項の番号を答えよ.
import time
time1=time.time()

i=1
j=2
n=2
k=0
while k<10**999:
    k=i+j
    n=n+1
    i=j
    j=k
print n+1
print time.time()-time1,"seconds"