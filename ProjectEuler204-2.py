# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 204

ハミング数とは, どの素因数も5以下であるような正整数のことである.
最初から順に並べると, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15となる.
10^8以下のハミング数は1105個ある.

素因数がn未満の正整数を, type nの一般化ハミング数と呼ぶことにする.
するとハミング数はtype 5の一般化ハミング数である.

10^9以下のtype 100の一般化ハミング数の個数を答えよ.
"""
import time
import math
import Euler
time1=time.time()
i=0
count=0
p=(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
p_len=[]
for i in xrange(len(p)):
    p_len.append(math.log(10**9,p[i])+1)
for i0 in xrange(p_len[0]):
    for i1 in xrange(p_len[1]):
        for i2 in xrange(p_len[2]):
            for i3 in xrange(p_len[3]):
                for i4 in xrange(p_len[4]):
                    for i5 in xrange(p_len[5]):
                        for i6 in xrange(p_len[6]):
                            for i7 in xrange(p_len[7]):
                                for i8 in xrange(p_len[8]):
                                    for i9 in xrange(p_len[9]):
                                        for i10 in xrange(p_len[10]):
                                            for i11 in xrange(p_len[11]):
                                                for i12 in xrange(p_len[12]):
                                                    for i13 in xrange(p_len[13]):
                                                        for i14 in xrange(p_len[14]):
                                                            for i15 in xrange(p_len[15]):
                                                                for i16 in xrange(p_len[16]):
                                                                    for i17 in xrange(p_len[17]):
                                                                        for i18 in xrange(p_len[18]):
                                                                            for i19 in xrange(p_len[19]):
                                                                                for i20 in xrange(p_len[20]):
                                                                                    for i21 in xrange(p_len[21]):
                                                                                        for i22 in xrange(p_len[22]):
                                                                                            for i23 in xrange(p_len[23]):
                                                                                                for i24 in xrange(p_len[24]):
                                                                                                    if (ps[0]**i0+ps[1]**i1+ps[2]**i2+ps[3]**i3+ps[4]**i4+
                                                                                                        ps[5]**i5+ps[6]**i6+ps[7]**i7+ps[8]**i8+ps[9]**i9+
                                                                                                        ps[10]**i10+ps[11]**i11+ps[12]**i12+ps[13]**i13+ps[14]**i14+
                                                                                                        ps[15]**i15+ps[16]**i16+ps[17]**i17+ps[18]**i18+ps[19]**i19+
                                                                                                        ps[20]**i20+ps[21]**i21+ps[22]**i22+ps[23]**i23+ps[24]**i24)<10**9:
                                                                                                            count+=1

print count
print time.time()-time1, "seconds"