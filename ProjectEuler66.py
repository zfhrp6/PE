#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
project euler problem 66

次の形式の, 2次のディオファントス方程式を考えなさい:
    x^2 - D y^2 = 1
たとえばD=13のとき, xを最小にする解は649^2 - 13×180^2 = 1である.
Dが平方数(square)のとき, 正整数のなかに解は存在しないと考えられる.
D = {2, 3, 5, 6, 7}に対してxを最小にする解は次のようになる:
    3^2 - 2×2^2 = 1
    2^2 - 3×1^2 = 1
    9^2 - 5×4^2 = 1
    5^2 - 6×2^2 = 1
    8^2 - 7×3^2 = 1
したがって, D ≤ 7に対してxを最小にする解を考えると, D=5のときxは最大である.
D ≤ 1000に対するxを最小にする解で, xが最大になるようなDの値を見つけよ.
"""
import time
import math
t0 = time.time()
answer = 0
xDdic = {}
for D in range(1, 1000):
    if math.sqrt(D) % 1 == 0.0:
        continue
    print(D)
    flag = False
    x = 1
    while True:
        for y in range(x, 1, -1):
            if (x ** 2 - 1) * 1.0 / y ** 2 == float(D):
                xDdic[x] = D
                flag = True
                break
        if flag:
            break
        x += 1

print(xDdic[max(xDdic.keys())])
print(time.time() - t0, "seconds")
