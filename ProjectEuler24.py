# -*- coding: utf-8 -*-
"""
Problem 24

順列とはモノの順番付きの並びのことである
. たとえば, 3124は数1, 2, 3, 4の一つの順列である.
すべての順列を数の大小でまたは辞書式に並べたものを辞書順と呼ぶ.
0と1と2の順列を辞書順に並べると
012 021 102 120 201 210
になる.

0,1,2,3,4,5,6,7,8,9からなる順列を辞書式に並べたときの100万番目を答えよ
"""
import time
import itertools
time1=time.time()

l=list(itertools.permutations(range(10)))

print l[999999]
print time.time()-time1, "seconds"