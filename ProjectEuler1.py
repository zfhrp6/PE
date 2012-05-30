# -*- coding: utf-8 -*-
#Project Euler Problem 1
#1000までの数のうち3または5で割り切れる数の総和を求めよ
import time
time1=time.time()
i=0
s=0
for number in range(1,1000):
    i+=1
    if i%3==0:
        s+=i
    elif i%5==0:
        s+=i
    else:
        continue
print ("answer is"), s
print time.time()-time1, "seconds"
del(i,s,number,time1)
raw_input()