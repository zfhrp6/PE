# -*- coding: utf-8 -*-
# project euler problem 15
# 2 × 2 のマス目の左上からスタートした場合、引き返しなしで右下にいくルートは 6 つある。
# では、20 × 20 のマス目ではいくつのルートがあるか。

# n*n の時は(2*n)!/(n!*n!)通りのルートがある。

import math
import time
time1 = time.time()
n = 20
s = (math.factorial(2 * n)) / ((math.factorial(n)) ** 2)
print("answer is"), s
print(time.time() - time1, "seconds")
