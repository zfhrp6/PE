# -*- coding: utf-8 -*-
#Project Euler Problem 17
"""
1 から 5 までの数字を英単語で書けば one, two, three, four, five であり、
全部で 3 + 3 + 5 + 4 + 4 = 19 の文字が使われている。
では 1 から 1000 (one thousand) までの数字をすべて英単語で書けば、全部で何文字になるか。
注: 空白文字やハイフンを数えないこと。例えば、342 (three hundred and forty-two) は 23 文字、
115 (one hundred and fifteen) は20文字と数える。なお、"and" を使用するのは英国の慣習。
"""

import time
time1=time.time()

sum=11
for i in range(1,1000):
    if i>=900:
        sum+=14 #nine hundred and
        j=i%900
    elif i>=800:
        sum+=15 #eight hundred and
        j=i%800
    elif i>=700:
        sum+=15 #seven hundred and
        j=i%700
    elif i>=600:
        sum+=13 #six hundred and
        j=i%600
    elif i>=500:
        sum+=14 #five hundred and
        j=i%500
    elif i>=400:
        sum+=14 #four hundred and
        j=i%400
    elif i>=300:
        sum+=15 #three hundred and
        j=i%300
    elif i>=200:
        sum+=13 #two hundred and
        j=i%200
    elif i>=100:
        sum+=13 #one hundred and
        j=i%100
    else:
        j=i

    if j==0:
        sum-=3 # and不要
        continue
    elif j>=90:
        sum+=6 #ninety
        j=j%90
    elif j>=80:
        sum+=6 #eighty
        j=j%80
    elif j>=70:
        sum+=7 #seventy
        j=j%70
    elif j>=60:
        sum+=5 #sixty
        j=j%60
    elif j>=50:
        sum+=5 #fifty
        j=j%50
    elif j>=40:
        sum+=5 #forty
        j=j%40
    elif j>=30:
        sum+=6 #thirty
        j=j%30
    elif j>=20:
        sum+=6 #twenty
        j=j%20
    elif j>=10:
        if j==17:
           sum+=9
        elif j==15 or j==16:
            sum+=7
        elif j==13 or j==14 or j==18 or j==19:
            sum+=8
        elif j==11 or j==12:
            sum+=6
        elif j==10:
            sum+=3
        continue

    if j==0:
        j=j
    elif j==1 or j==2 or j==6: # one two six ten
        sum+=3
    elif j==3 or j==7 or j==8: #three seven eight
        sum+=5
    elif j==4 or j==5 or j==9: #four five nine
        sum+=4
    j=0

print "answer is %d"%(sum)
print "%f Seconds"%(time.time()-time1)