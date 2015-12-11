# -*- coding: utf-8 -*-
# project euler problem 48
# 1**1 + 2**2 + 3**3 + ... + 1000**1000 の最後の10桁を求めよ。
# つまり1~1000までの数の、その数乗、の総和の下10桁をもとめる。

s = 0
i = 1
while i <= 1000:
    if i ** i > 9999999999:
        l = int(str(i ** i)[-10:])
        s = int(str(s + l)[-10:])
    else:
        s = s + i ** i
        if s > 9999999999:
            s = int(str(s))
    i = i + 1
print(s)
