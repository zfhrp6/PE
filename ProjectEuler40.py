# -*- coding: utf-8 -*-
#project euler problem 40
#正の整数を順に連結して得られる以下の10進の無理数を考える:
#0.123456789101112131415161718192021...
#小数第12位は1である.
#d_nで小数第n位の数を表す. d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000 を求めよ.
import time

time1=time.time()
st=""
for i in range(1,300000):
    st=st+str(i)
print int(st[0])*int(st[9])*int(st[99])*int(st[999])*int(st[9999])*int(st[99999])*int(st[999999])
print time.time()-time1, "Seconds"