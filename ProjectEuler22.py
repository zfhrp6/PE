#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""project euler problem 22
5000個以上の名前が書かれている46Kのテキストファイルnames.txt を用いる.
まずアルファベット順にソートせよ.
のち, 各名前についてアルファベットに値を割り振り, リスト中の出現順の数と掛け合わせることで,
名前のスコアを計算する.
たとえば, リストがアルファベット順にソートされているとすると, COLINはリストの938番目にある.
またCOLINは3 + 15 + 12 + 9 + 14 = 53という値を持つ. よってCOLINは938 × 53 = 49714というスコアを持つ.
ファイル中の全名前のスコアの合計を求めよ."""

import time
time1 = time.time()

f = open("ProjectEuler22names.txt", "r")
names = f.read().split(",")
dic = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
       "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26, "\"": 0}
names.sort()
sum = 0
for i in range(len(names)):
    n = 0
    for j in range(len(names[i])):
        n += dic[names[i][j]]
    sum += (i + 1) * n

print("answer = %d" % (sum))
print("%f Seconds" % (time.time() - time1))
