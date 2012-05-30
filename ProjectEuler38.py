# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 38

192を1, 2, 3で掛けてみよう.

   192 × 1 = 192
   192 × 2 = 384
   192 × 3 = 576

積を連結することで1から9のPandigital数 192384576 が得られる.
192384576を 192と(1,2,3)の連結積と呼ぶ.
同じようにして, 9を1,2,3,4,5と掛け連結することでPandigital数918273645が得られる.
これは9と(1,2,3,4,5)との連結積である.
整数と(1,2,...,n) (n > 1) との連結積として得られる9桁のPandigital数の中で最大のものを答えよ.
"""
import time
import math
import Euler
time1=time.time()
lst=[]
for i in range(1,10**4):
    sttr=""
    for j in range(1,10):
        sttr+=str(i*j)
        if len(sttr)<9:
            continue
        elif len(sttr)==9 and Euler.pandigital_check(int(sttr)):
            lst.append(sttr)
        else:
            break


print max(lst)
print time.time()-time1, "seconds"
