# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""Problem 251
3 個の正整数の組 (a,b,c) が次の式を満たすときこれをカルダノトリプレット(Cardano Triplet) と呼ぶ:

(a+b*√c)^1/3 + (a-b*√c)^1/3 = 1

例えば、(2,1,5) はカルダノトリプレットである。
a+b+c ≤ 1000 を満たすカルダノトリプレットは 149 ある。
a+b+c ≤ 110,000,000 を満たすカルダノトリプレットはいくつあるか。
注意: この問題は最近変更があった、正しいパラメータを使用しているか確認してほしい."""

import time
import itertools
import math

time1=time.time()
count=0
a=1;b=1;c=1;c2=1
t=math.exp(1/3*math.log(a+b*c2))+math.exp(1/3*math.log(a-b*c2))
for a,b,c in itertools.permutations(range(1,999),3):
    c2=math.sqrt(c)
    if b>a:
        continue
    elif a+b+c>1000:
        continue
    elif t==1:
        count+=1
    else:
        pass

print "answer is %d"%(count)
print "%f Seconds"%(time.time()-time1)