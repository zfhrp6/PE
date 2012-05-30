# -*- coding: utf-8 -*-
#project euler problem 3
#600851475143の素因数のうち最大のものを求めよ。

t=600851475143
while t!=1:
    n=3
    while t%n!=0:
        n=n+2
    t=t/n
    print n
print("answer is"), n
raw_input()