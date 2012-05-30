# -*- coding: utf-8 -*-
#project euler problem 14
#コラッツ予想に関する問題。
#100万未満の数字の中でどの数字からはじめれば一番長い数列を生成するか。
import time
time1=time.time()
i=2
k=1
n=1
max=1
while i<1000000:
    k=i
    n=0
    while k!=1:
        if k%2==0:
            k=k/2
        else:
            k=3*k+1
        n=n+1
    if n>max:
        max=n
        s=i
        print s
    i=i+1
print ("answer is"), s
print time.time()-time1, "seconds"
raw_input()