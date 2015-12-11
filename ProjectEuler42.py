#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Project Euler Problem42
三角数のn項は tn = ½n(n+1)で与えられる. 最初の10項は

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

である.
単語中のアルファベットを数値に変換した後に和をとる.
この和を「単語の値」と呼ぶことにする.
例えば SKY は 19 + 11 + 25 = 55 = t_10である.
単語の値が三角数であるとき, その単語を三角語と呼ぶ.
16Kのテキストファイル words.txt 中に約2000語の英単語が記されている. 三角語はいくつあるか?
"""

import time
time1 = time.time()

tri = [n * (n + 1) / 2 for n in range(1, 100)]
f = open("ProjectEuler42words.txt", "r")
words = f.read().split(",")
dic = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
       "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26, "\"": 0}
count = 0
for i in range(len(words)):
    n = 0
    for j in range(len(words[i])):
        n += dic[words[i][j]]
    if n in tri:
        count += 1

print("answer = %d" % (count))
print("%f Seconds" % (time.time() - time1))
