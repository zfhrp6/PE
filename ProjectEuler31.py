#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 31

イギリスでは硬貨はポンド£とペンスpがあり，一般的に流通している硬貨は以下の8種類である.
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
以下の方法で£2を作ることが可能である.
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
これらの硬貨を使って£2を作る方法は何通りあるか?
"""
import time
time1 = time.time()
# all search
count = 0
for i200 in range(2):
    for i100 in range(3 - i200):
        for i50 in range(5 - i200 * 4 - i100 * 1):
            for i20 in range(11 - i200 * 10 - i100 * 5 - i50 * 2):
                for i10 in range(21 - i200 * 20 - i100 * 10 - i50 * 5 - i20 * 2):
                    for i5 in range(41 - i200 * 40 - i100 * 20 - i50 * 10 - i20 * 4 - i10 * 2):
                        for i2 in range(101 - i200 * 100 - i100 * 50 - i50 * 25 - i20 * 10 - i5 * 2):
                            for i1 in range(201 - i200 * 200 - i100 * 100 - i50 * 50 - i20 * 20 - i10 * 10 - i5 * 5 - i2 * 2):
                                if i200 * 200 + i100 * 100 + i50 * 50 + i20 * 20 + i10 * 10 + i5 * 5 + i2 * 2 + i1 * 1 == 200:
                                    count += 1

print(count)
print(time.time() - time1, "seconds")
