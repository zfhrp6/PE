# -*- coding: utf-8 -*-
# project euler problem 9
# a + b + c = 1000(a<b<c)となるピタゴラスの三つ組が一つだけ存在する. このa,b,cの積を計算しなさい.
import math
import time
time1 = time.time()

a = 0
b = 1
check = 0
while a < 333:
    a = a + 1
    while b < 665:
        b = b + 1
        if a + b + math.sqrt(a ** 2 + b ** 2) == 1000:
            print(("(a,b,c) is ("), a, b, int(math.sqrt(a ** 2 + b ** 2)), (")"))
            print(("a*b*c is"), int(a * b * math.sqrt(a ** 2 + b ** 2)))
            check = 1
            break
    b = 1
    if check == 1:
        break
print(time.time() - time1, "seconds")
