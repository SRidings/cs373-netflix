#!/usr/bin/env python3

import math,json
from pprint import pprint

#Average of every movie rated
glbl_mean=3.604289964420661

def netflix_read(r):
    """
    reads in a line from probe.txt
    """
    s=r.readline()[:-1]
    return s

def readAvgMovieRating(movieID) :
    """
    read from cache of avg movie ratings
    """
    #with open("/u/mukund/cs373-netflix-tests/") as f:
    with open("/u/sridings/cs373-netflix/json_ex.json") as f:
        data=json.load(f)
        pprint(data)
        
      
    return 0

def sqre_diff(a, p) :
    return (a - p) ** 2

def netflix_write (s, w) :
    w.write(str(s) + "\n")

def netflix_predict(movieID) :
    """
        Currently experimenting with implementation #1
    """
    readAvgeMovieRating(movieID)
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

def main() : 
     readAvgMovieRating(0)

main()
