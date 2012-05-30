# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 290

0 ≤ n < 10^18 であり n の桁の合計が 137n の桁の合計と等しいような整数 n はいくつあるか。
"""
import time
import math
import Euler
time1=time.time()
sums=0
i=0
while i<7490000:
    i+=1


print sums%1000000000
print time.time()-time1, "seconds"
