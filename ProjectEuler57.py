# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 57

2の平方根は無限に続く連分数で表すことができる.
√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
最初の4回の繰り返しを展開すると以下が得られる.
    1 + 1/2 = 3/2 = 1.5
    1 + 1/(2 + 1/2) = 7/5 = 1.4
    1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
    1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
次の3つの項は99/70, 239/169, 577/408である. 第8項は1393/985である.
これは分子の桁数が分母の桁数を超える最初の例である.
最初の1000項を考えたとき, 分子の桁数が分母の桁数を超える項はいくつか?
"""
import time
import math
import Euler
t0=time.time()
answer=0
bunshi=3
bunbo=2
i=0
while i<=1000:
    i+=1
    if int(math.log10(bunshi))>int(math.log10(bunbo)):
        answer+=1
    bunshi,bunbo=2*bunbo+bunshi,bunbo+bunshi

print answer
print time.time()-t0, "seconds"
