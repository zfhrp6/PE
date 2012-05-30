# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
project euler problem 102

3つの異なる点が -1000 ≤ x, y ≤ 1000 かつ三角形となるように, デカルト平面上にランダムに与えられる.
以下の2つの三角形を考える.

    * A(-340,495), B(-153,-910), C(835,-947)
    * X(-175,41), Y(-421,-714), Z(574,-645)

三角形ABCが原点を内部に含み, XYZは原点を内部に含まないことが確かめられる.
27Kのテキストファイルtriangles.txt にランダムな1000個の三角形が適当なフォーマットのもと含まれている.
内部に原点を含む三角形の数を答えよ.

注: ファイル中の最初の二つは三角形ABC, XYZである.
"""
import time
from math import fabs
time1=time.time()
file=open("ProjectEuler102triangles.txt","r")
sets=file.read().split("\n")
answer=0
for i in range(1000):
    t=sets[i].split(",")
    func=lambda a,b,c,d,e,f : fabs((a-e)*(d-f)-(b-f)*(c-e))/2
    func2=lambda a,b,c,d,e,f : (fabs(a*d-b*c)+fabs(c*f-d*e)+fabs(e*b-f*a))/2
    a,b,c,d,e,f=int(t[0]),int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5])
    if func(a,b,c,d,e,f)==func2(a,b,c,d,e,f):
            answer+=1



file.close()
print answer
print time.time()-time1, "seconds"