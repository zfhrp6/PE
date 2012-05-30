# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 43

数1406357289は0から9のPandigital数である (0から9が1度ずつ現れるので).
この数は部分語が面白い性質を持っている.
d_1を1桁目, d_2を2桁目の数とし, 以下順にd_nを定義する. この記法を用いると次のことが分かる.
    d_2 d_3 d_4=406は2で割り切れる
    d_3 d_4 d_5=063は3で割り切れる
    d_4 d_5 d_6=635は5で割り切れる
    d_5 d_6 d_7=357は7で割り切れる
    d_6 d_7 d_8=572は11で割り切れる
    d_7 d_8 d_9=728は13で割り切れる
    d_8 d_9 d_10=289は17で割り切れる
このような性質をもつ0から9のPandigital数の総和を求めよ.
"""
import time
import itertools
time1=time.time()
amount=0
for j in itertools.permutations([1,2,3,4,5,6,7,8,9,0]):
    i=0
    for k in j:
        i+=k
        i*=10
    i/=10
    if (int(str(i)[1:4])%2==0
        and int(str(i)[2:5])%3==0
        and int(str(i)[3:6])%5==0
        and int(str(i)[4:7])%7==0
        and int(str(i)[5:8])%11==0
        and int(str(i)[6:9])%13==0
        and int(str(i)[7:10])%17==0):
            amount+=i

print amount
print time.time()-time1, "seconds"