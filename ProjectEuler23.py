# -*- coding: utf-8 -*-
#Project Euler Problem 23
"""
完全数とは, その数の真の約数の和がそれ自身と一致する数のことである.
たとえば, 28の真の約数の和は, 1 + 2 + 4 + 7 + 14 = 28であるので, 28は完全数である.
真の約数の和がその数よりも少ないものを不足数といい, 真の約数の和がその数よりも大きいものを過剰数と呼ぶ.
12は, 1+2+3+4+6=16となるので, 最小の過剰数である.
よって2つの過剰数の和で書ける最少の数は24である.
数学的な解析により, 28123より大きい任意の整数は2つの過剰数の和で書けることが知られている.
    /* 実は20161より大きい任意の整数は2つの過剰数の和で書けるようだ。
2つの過剰数の和で表せない最大の数がこの上限よりも小さいことは分かっているのだが,
この上限を減らすことが出来ていない.
2つの過剰数の和で書き表せない正の整数の総和を求めよ.
"""
import time
import math
time1=time.time()
sum=276 #23までは2つの過剰数の和で表せないので、23までの和を含めておく。
lst=[]
for i in range(11,20163):
    s=0
    for j in range(1,int(math.sqrt(i)+1)):
        if i%j==0:
            s+=j+i/j
    s-=i
    if math.sqrt(i)%1==0:
            s-=math.sqrt(i)
    if s>i:
        lst.append(i) #ここまでで過剰数のリスト(lst)を生成


for k in range(25,20163):
    check=0
    l=0
    while lst[l]<=k/2:
        if k-lst[l] in lst:
            check+=1
            break
        l+=1
    if check==0:
        sum+=k


print "answer is %d"%(sum)
print "%f Seconds"%(time.time()-time1)