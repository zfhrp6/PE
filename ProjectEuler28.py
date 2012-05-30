# -*- coding: utf-8 -*-
#Project Euler Problem 28
"""
1から初めて右方向に進み時計回りに数字を増やしていき, 5×5の螺旋が以下のように生成される:
21	22	23	24	25
20	7	8	9	10
19	6	1	2	11
18	5	4	3	12
17	16	15	14	13

両対角線上の数字の合計は101であることが確かめられる.

1001×1001の螺旋を同じ方法で生成したとき, 対角線上の数字の合計はいくつだろうか?
"""
import time
time1=time.time()

sum=1
c=0
j=1
jj=2
for i in range(2,1002002):
    if j==jj:
        sum+=i
        c+=1
        j=0
        if c==4:
            c=0
            jj+=2
    j+=1
print sum
print time.time()-time1,"Seconds"