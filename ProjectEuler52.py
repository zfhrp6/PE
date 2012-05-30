# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 52

125874を2倍すると251748となる. これは元の数125874と同じ数を含む.

2x, 3x, 4x, 5x, 6xがxと同じ数を含むような最小の正整数xを求めよ.
"""
import time
time1=time.time()
x=0
while True:
    x+=1
    lst=list(str(x))
    lst2=list(str(2*x))
    lst3=list(str(3*x))
    lst4=list(str(4*x))
    lst5=list(str(5*x))
    lst6=list(str(6*x))
    lst.sort()
    lst2.sort()
    lst3.sort()
    lst4.sort()
    lst5.sort()
    lst6.sort()
    if lst==lst2==lst3==lst4==lst5==lst6:
        print x
        break
print time.time()-time1,"seconds"