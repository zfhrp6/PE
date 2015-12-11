# -*- coding: utf-8 -*-
# project euler problem 36
# 100万未満で10進でも2進でも回文数になるような数の総和を求めよ.

sum = 0
n = 1
st2 = ""
while n < 1000000:
    st10 = str(n)
    if st10 == st10[::-1]:
        if str(format(n, "b")) == str(format(n, "b"))[::-1]:
            sum = sum + n
    n = n + 1
print(sum)
