# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 191

ある学校では出席率が高く遅刻率が低い生徒に褒賞金を出している.
3日連続で休む, または, 2回以上遅刻した生徒は褒賞金を得る権利を失う.

n日間の各生徒の出席状況を3進の文字列で表す.
文字はL (late, 遅刻), O (on time, 出席), A (absent, 欠席) である.

4日間の場合, 81通りの3進の文字列が考えられる. そのうち賞を貰えるのは以下の43個の文字列である.

OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
LAOO LAOA LAAO

30日間の場合, 賞を貰える文字列は何通りか?
"""
import time
import math
import Euler
t0=time.time()
def appending(lst):
    leng=len(lst)
    for i in range(len(lst)):
        txtO=lst[i]+"O"
        txtA=lst[i]+"A"
        txtL=lst[i]+"L"
        lst.append(txtO)
        if not "AAA" in txtA:
            lst.append(txtA)
        if txtL.count("L")<2:
            lst.append(txtL)
    del(lst[:leng])
    print len(lst)
lst=["O","A","L"]
for i in range(3):
    appending(lst)
answer=len(lst)


print answer
print time.time()-t0, "seconds"
