#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 35

197は巡回素数と呼ばれる.
桁を回転させたときに得られる数 197, 971, 719 が全て素数だからである.
100未満には巡回素数が13個ある: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, および97である.
100万未満の巡回素数は何個か?
"""
import time
import math
time1 = time.time()


def primecheck(n):
    check = 1
    if not isinstance(n, int) or n <= 1:
        check = 0
    elif n == 2:
        check = 1
    elif n % 2 == 0:
        check = 0
    else:
        for i in range(3, int(math.sqrt(n) + 1), 2):
            if n % i == 0:
                check = 0
                break
    if check == 1:
        return 1
    else:
        return 0


def even_in_check(n):
    if "2" in str(n):
        return 1
    elif "4" in str(n):
        return 1
    elif "5" in str(n):
        return 1
    elif "6" in str(n):
        return 1
    elif "8" in str(n):
        return 1
    elif "0" in str(n):
        return 1
    else:
        return 0

anslist = [2, 3, 5, 7]
for i in range(11, 1000000, 2):
    if even_in_check(i):
        notprime = 1
        continue
    else:
        notprime = 0
        for j in range(len(str(i)) + 2):
            k = i
            i = int(str(i)[1:] + str(i)[:1])
            if primecheck(i) != 1:
                notprime = 1
        if notprime == 0:
            anslist.append(k)


print(len(list(set(anslist))))
print(time.time() - time1, "seconds")
