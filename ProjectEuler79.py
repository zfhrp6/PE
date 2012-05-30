#coding:utf-8
#!/usr/bin/env python
"""
Project Euler Problem 79


"""
import time
import math
import Euler
t1=time.time()

ans_list=[]
all_list=[]
all_list=["0", "1", "2", "3", "6", "7", "8", "9"]
f=open("projecteuler79keylog.txt","r")
in_list=f.read().split("\n")
for i in xrange(len(all_list)):
    temp=all_list[:]
    for item in in_list:
        temp.sort()
        if item[0] in ans_list:
            item=item[1:]
        if item[0] in ans_list:
            item=item[1]
        if len(item)>2 and item[2] in temp:
            temp.remove(item[2])
        elif len(item)>1 and item[1] in temp:
            temp.remove(item[1])

    if temp!=[]:
        temp=list(set(temp)-set(ans_list))
        if temp==[]:
            break
        ans_list.append(temp[0])

f.close()

answer="".join(ans_list)
print answer
print time.time()-t1, "seconds"