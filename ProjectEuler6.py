# coding:utf-8
#!/usr/bin/env python
"""
Problem 6

最初の10個の自然数について、その和の二乗と、二乗数の和は以下の通り。
1² + 2² + ... + 10² = 385
(1 + 2 + ... + 10)² = 3025

これらの数の差は 3025 - 385 = 2640 となる。

同様にして、最初の100個の自然数について和の二乗と二乗の和の差を求めよ。

"""
import time
time1=time.time()
s1=0
s2=0
n1=0
n2=0
for number in range(1,101):
    n1+=1
    s1+=n1**2
print s1
for number in range(1,101):
    n2+=1
    s2+=n2
print s2**2
print ("answer is"), s2**2-s1
print time.time()-time1,"seconds"
raw_input()