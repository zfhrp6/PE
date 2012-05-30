# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 91

点P(x1, y1)と点Q(x2, y2)はともに整数係数の点であり, 原点O(0,0)と合わせてΔOPQをなす.
各係数が0と2の間にあるとき, すなわち0 ≤ x1, y1, x2, y2 ≤ 2のとき, 直角三角形は14個できる
では, 0 ≤ x1, y1, x2, y2 ≤ 50のとき, 直角三角形は何個作れるか?
"""
import time
import itertools
t0=time.time()
answer=0
for x1,y1,x2,y2 in itertools.product(range(51), repeat=4):
    v1=(x1,y1)
    v2=(x2,y2)
    v3=(x2-x1,y2-y1)
    if v1==v2 or v1==(0,0) or v2==(0,0):
        continue
    if (v1[0]*v2[0]+v1[1]*v2[1]==0 or
        v2[0]*v3[0]+v2[1]*v3[1]==0 or
        v3[0]*v1[0]+v3[1]*v1[1]==0):
            answer+=1

print answer/2
print time.time()-t0, "seconds"
