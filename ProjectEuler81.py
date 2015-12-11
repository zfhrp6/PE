#!/usr/bin/env python
# coding:utf-8
"""
Project Euler Problem 81


"""
import time
time1 = time.time()

rows = []
f = open("projecteuler81matrix.txt", "r")
for line in f:
    rows.append(list(map(int, line[:-1].split(","))))
f.close()

# problem 67 no youni triangle wo tsukutte toku. ue hanbun to shita hanbun.

sup_tri = []
sub_tri = []
for i in range(0, 80):
    ins = []
    for j in range(0, i + 1):
        ins.append(rows[i - j][j])
    sup_tri.append(ins)

for i in range(0, 79):
    ins = []
    for j in range(0, i + 1):
        ins.append(rows[79 - j][79 - i + j])
    sub_tri.append(ins)

sub_tri_r = sub_tri[::-1]
sup_tri_r = sup_tri[::-1]

for i in range(len(sup_tri) - 1):
    sup_tri[i + 1][0] += sup_tri[i][0]
    sup_tri[i + 1][-1] += sup_tri[i][-1]
    for j in range(len(sup_tri[i]) - 1):
        if sup_tri[i][j] < sup_tri[i][j + 1]:
            sup_tri[i + 1][j + 1] += sup_tri[i][j]
        else:
            sup_tri[i + 1][j + 1] += sup_tri[i][j + 1]

for i in range(len(sub_tri) - 1):
    sub_tri[i + 1][0] += sub_tri[i][0]
    sub_tri[i + 1][-1] += sub_tri[i][-1]
    for j in range(len(sub_tri[i]) - 1):
        if sub_tri[i][j] < sub_tri[i][j + 1]:
            sub_tri[i + 1][j + 1] += sub_tri[i][j]
        else:
            sub_tri[i + 1][j + 1] += sub_tri[i][j + 1]

"""
for i in xrange(len(sup_tri_r)-1):
    for j in xrange(0,len(sup_tri_r)-i-1):
        if sup_tri_r[i][j]<=sup_tri_r[i][j+1]:
            sup_tri_r[i+1][j]+=sup_tri_r[i][j]
        else:
            sup_tri_r[i+1][j]+=sup_tri_r[i][j+1]

for i in xrange(len(sub_tri_r)):
    for j in xrange(0,len(sub_tri_r)-i-1):
        if sub_tri_r[i][j]<=sub_tri_r[i][j+1]:
            sub_tri_r[i+1][j]+=sub_tri_r[i][j]
        else:
            sub_tri_r[i+1][j]+=sub_tri_r[i][j+1]
"""

answers_ = []
for i in range(len(sup_tri[-1]) - 1):
    if sup_tri[-1][i] < sup_tri[-1][i + 1]:
        answers_.append(sub_tri[-1][i] + sup_tri[-1][i])
    else:
        answers_.append(sub_tri[-1][i] + sup_tri[-1][i + 1])

print(min(answers_))
print(time.time() - time1, "seconds")
