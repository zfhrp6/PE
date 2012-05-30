# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 206

二乗すると「1_2_3_4_5_6_7_8_9_0」の形となるような唯一の正整数を求めよ。ただし、「_」は1桁の数である。
"""
import time
import math
time1=time.time()
i=1010101010
while i<1390000000:
    i+=10
    s=str(i**2)
    if s[0]=="1":
        if s[2]=="2":
            if s[4]=="3":
                if s[6]=="4":
                    if s[8]=="5":
                        if s[10]=="6":
                            if s[12]=="7":
                                if s[14]=="8":
                                    if s[16]=="9":
                                        if s[18]=="0":
                                            answer=i
                                            break

print answer
print time.time()-time1, "seconds"