#!/usr/bin/env python3

def netflix_read(r):
    """
    reads in a line from probe.txt
    """
    s=r.readline()
    return s
#       return netflix_predict(s)

def netflix_print (s, w) :
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

