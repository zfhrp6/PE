# -*- coding: utf-8 -*-
#project euler problem 5
#1 から 20 までの整数全てで割り切れる数字の中で最小の値はいくらになるか。
import time
time1=time.time()
i=1
n=0
while i==1:
    n+=1
    if (n%1==0 and
        n%2==0 and
        n%3==0 and
        n%4==0 and
        n%5==0 and
        n%6==0 and
        n%7==0 and
        n%8==0 and
        n%9==0 and
        n%10==0 and
        n%11==0 and
        n%12==0 and
        n%13==0 and
        n%14==0 and
        n%15==0 and
        n%16==0 and
        n%17==0 and
        n%18==0 and
        n%19==0 and
        n%20==0):
            i=0
print n
print time.time()-time1,"seconds"