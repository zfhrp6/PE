# -*- coding: utf-8 -*-
#project euler problem 4
#3桁の数の積で表される回文数のうち最大のものはいくらになるか。
import time
time1=time.time()
i=1000
k=1000
nu=0
s=0
for j in range(100,1000):
    for l in range(100,j+1):
        n=j*l
        st=str(n)
        if st==st[::-1]:
            if n>s:
                s=n
print ("answer is"), s
print time.time()-time1,"seconds"
raw_input()