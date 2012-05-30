# -*- coding: utf-8 -*-
"""
Problem 26

単位分数とは分子が1の分数である。分母が2から10の単位分数を10進数で表記すると次のようになる。

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

0.1(6)は 0.166666... という数字であり、1桁の循環節を持つ。1/7 の循環節は6桁ある。

d < 1000 なる 1/d の中で循環節が最も長くなるような d を求めよ。
"""
import time
time1=time.time()

num=0
for i in range(1,1000):
    k=i
    while i%5==0:
        i=i/5
    while i%2==0:
        i=i/2
    if i==1:
        continue

    j=1
    while True:
        if (10**j)%i==1:
            if j>num:
                num=k
            break
        j+=1


print num
print time.time()-time1, "seconds"