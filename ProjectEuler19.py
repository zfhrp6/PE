# -*- coding: utf-8 -*-
#Project Euler Problem 19
"""
次の情報が与えられている。
    * 1900年1月1日は月曜日である。
    * 9月、4月、6月、11月は30日まであり、2月を除く他の月は31日まである。
    * 2月は28日まであるが、うるう年のときは29日である。
    * うるう年は西暦が4で割り切れる年に起こる。しかし、西暦が400で割り切れず100で割り切れる年はうるう年でない。
20世紀（1901年1月1日から2000年12月31日）で月の初めが日曜日になるのは何回あるか。
"""

import time
time1=time.time()
count=0
d=366
for year in range(1901,2001):
    for month in range(1,13):
        if month==1:
            if d%7==0:
                count+=1
            for i in range(31):
                d+=1
        if month==2:
            if d%7==0:
                count+=1
            if year%4==0:
                if year%400!=0 and year%100==0:
                    for i in range(28):
                        d+=1
                else:
                    for i in range(29):
                        d+=1
            else:
                for i in range(28):
                    d+=1
        if month==3:
            if d%7==0:
                count+=1
            for i in range(31):
                d+=1
        if month==4:
            if d%7==0:
                count+=1
            for i in range(30):
                d+=1
        if month==5:
            if d%7==0:
                count+=1
            for i in range(31):
                d+=1
        if month==6:
            if d%7==0:
                count+=1
            for i in range(30):
                d+=1
        if month==7:
            if d%7==0:
                count+=1
            for i in range(31):
                d+=1
        if month==8:
            if d%7==0:
                count+=1
            for i in range(31):
                d+=1
        if month==9:
            if d%7==0:
                count+=1
            for i in range(30):
                d+=1
        if month==10:
            if d%7==0:
                count+=1
            for i in range(31):
                d+=1
        if month==11:
            if d%7==0:
                count+=1
            for i in range(30):
                d+=1
        if month==12:
            if d%7==0:
                count+=1
            for i in range(31):
                d+=1



print "answer is %d"%(count)
print "%f Seconds"%(time.time()-time1)