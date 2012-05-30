# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 94

一辺の長さが整数の正三角形は面積が整数にならないことを示すのは簡単である.
しかし, 5-5-6の辺を持つ殆ど正三角形に近い疑正三角形 (almost equilateral triangle) は面積が12で整数である.

以降, 二等辺三角形で, 3つめの辺の長さが他と1つしか違わないもの (5-5-6, 5-5-4等) を, 疑正三角形と呼ぶ.

さて, 周囲の長さが1,000,000,000以下の面積が整数になる疑正三角形を考え, その周囲の長さの総和を求めよ.
"""
import time
import math
t0=time.time()
answer=0
limit=10**9
i=1
while i<limit/3+6:
    if i%100000==0:
        print i
    i+=1
    b=i-1
    if i+2*b>limit:
        continue
    if i%2==0:
        if math.sqrt((3*i-1)*(i-1))-int(math.sqrt((3*i-1)*(i-1)))==0.0:
            answer+=i+2*b
    else:
        if (math.sqrt((6*i-1)*(2*i+1)))/4.0-int((math.sqrt((6*i-1)*(2*i+1)))/4.0)==0.0:
            answer+=i+2*b

    c=i+1
    if i%2==0:
        if math.sqrt((3*i+1)*(i+1))-int(math.sqrt((3*i+1)*(i+1)))==0.0:
            answer+=i+2*c
    else:
        if (math.sqrt((6*i+5)*(2*i+3)))/4.0-int((math.sqrt((6*i+5)*(2*i+3)))/4.0)==0.0:
            answer+=i+2*c



print answer
print time.time()-t0, "seconds"
