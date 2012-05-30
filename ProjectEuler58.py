# -*- coding: utf-8 -*-
#Project Euler Problem 28
"""
1から初めて, 以下のように反時計回りに数字を並べていくと, 辺の長さが7の渦巻きが形成される.
37* 36	35	34	33	32	31*
38	17*	16	15	14	13*	30
39	18	5*	4	3*	12	29
40	19	6	1	2	11	28
41	20	7*	8	9	10	27
42	21	22	23	24	25	26
43*	44	45	46	47	48	49

面白いことに, 奇平方数が右下の対角線上に出現する.
もっと面白いことには, 対角線上の13個の数字のうち, 8個が素数である.
ここで割合は8/13 ≈ 62%である.

渦巻きに新しい層を付け加えよう.
すると辺の長さが9の渦巻きが出来る.
以下, この操作を繰り返していく.
対角線上の素数の割合が10%未満に落ちる最初の辺の長さを求めよ.
"""
import time
import math
import Euler
time1=time.time()

amount=0
p_amount=0
c=0
add_count=0
add_num=2
i=1
while True:
    if amount!=0 and math.sqrt(i)%1==0 and int(math.sqrt(i))%2==1:
        if p_amount*10<=amount:
            break
    if add_count==4:
        add_count=0
        add_num+=2
    i+=add_num
    add_count+=1
    amount+=1
    if Euler.primecheck(i):
        p_amount+=1
print math.sqrt(i),i
print time.time()-time1,"Seconds"