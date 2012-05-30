#coding:utf-8
#!/usr/bin/env python
"""
Project Euler Problem 74

"""
import time
import math
import Euler

t0 = time.time()
answer = 0

def next(n):
    n = list(str(n))
    nn = 0
    for item in n:
        nn += math.factorial(int(item))
    return nn

def chain(n):
    elem = [n]
    count = 1
    n = next(n)
    while n not in elem:
        elem.append(n)
        count += 1
        n = next(n)
        if count > 60:
            break
    return count

for i in xrange(1000000):
    if i%1000 == 0:
        print i
    if chain(i) == 60:
        answer += 1

print answer
print time.time() - t0, "seconds"