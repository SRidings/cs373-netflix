#!/usr/bin/env python3

import math

def netflix_read(r):
    """
    reads in a line from probe.txt
    """
    s=r.readline()[:-1]
    return s
#       return netflix_predict(s)

def sqre_diff(a, p) :
    return (a - p) ** 2

def netflix_write (s, w) :
    w.write(str(s) + "\n")

def netflix_predict(cust) :
    return 0

def netflix_rate(r, w) :
    while (True) :
        line = netflix_read(r)
        if not line :
            return
        elif line[-1] != ":" :
            netflix_print(netflix_predict(line), w)
        else :
            netflix_print(line, w)

def rmse (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    s = len(a)
    v = sum(map(sqre_diff, a, p))
    return math.sqrt(v / s)

