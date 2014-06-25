#!/usr/bin/env python3
import sys
from Netflix import netflix_rate
#from gen_cache import netflix_rate
from time import clock
"""
 Expects Probe.txt and cache file
"""

#-----
# main
#-----
"""
for m in [1000] :
    for i in range(1,m+1) :
        a=clock()
        print("result: " + str( netflix_rate(None,None,i, m-i,m) ) +" ("+str(i)+","+str(m-i) + ")", end = " ")
        b=clock()
        print ("%5.3f" % ((b-a) * 1000), "ms")
"""
netflix_rate(sys.stdin,sys.stdout)


