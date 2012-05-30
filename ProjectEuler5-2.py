# coding:utf-8
#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hi
#
# Created:     15/03/2011
# Copyright:   (c) hi 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time
time1=time.time()
i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            if (i*j) % k == 0:
                i *= j
                break
print i
print time.time()-time1,"seconds"