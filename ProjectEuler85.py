#!/usr/bin/env python
# coding:utf-8
"""
Project Euler Problem 85

注意深く数えると, 横が3, 縦が2の長方形の格子には, 18個の長方形が含まれている.

ぴったり2,000,000個の長方形を含むような長方形の格子は存在しない.
一番近い解を持つような格子の面積を求めよ.


n*mの長方形に含まれる長方形の数は、1/4 * (m^2*n^2 +m^2*n +m*n^2 +m*n)　である.
"""
import time
import math
t1 = time.time()


def countf(tate, yoko):
    r_ct = 0
    for i in range(1, tate + 1):
        for j in range(1, yoko + 1):
            r_ct += (tate + 1 - i) * (yoko + 1 - j)
    return r_ct


def countf_2(m, n):
    return (m ** 2 * n ** 2 + m ** 2 * n + m * n ** 2 + m * n) / 4


def main():
    answer_dif = 9999999999999
    answer_s = 0
    target = 2 * 10 ** 6
    h = k = 0
    for h in range(1, 10 ** 3):
        for k in range(h, 10 ** 3):
            if math.fabs(countf_2(h, k) - target) < answer_dif:
                answer_dif = math.fabs(countf_2(h, k) - target)
                answer_s = h * k
                print(h, k)
    return answer_s


if __name__ == '__main__':
    answer = main()

print(answer)
print(time.time() - t1, "seconds")
