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

def calculateOverallMovieRating(ids) :
    runningSum = 0
    avgRating = 0
   
    temp = "/u/downing/cs/netflix/training_set/mv_"
    for i in ids :
        temp += (7-len(str(i)))*"0" + str(i) +".txt"
        with open(temp) as f:
            f.readline()
            for line in f :
                avgRating += float(line.split(",")[1])
                runningSum += 1
    if (runningSum!=0) :
        return avgRating/runningSum
        
    return 0        

   
def readAvgCustomerRating(customerID) :
    """
    read from cache of avg customer ratings
    """
    assert int(customerID) >= 0
    assert type(customerID) is str

    with open("/u/sridings/netflix-tests/netflix-tests/bryan-customer_cache.json") as f:
    #with open("/u/mukund/cs373-netflix-tests/bryan-customer_cache.json") as f:
        data=json.load(f)
        return data[customerID]

   
def readAvgMovieRating(movieID) :
    """
    read from cache of avg movie ratings
    """

    assert int(movieID) >= 0
    assert type(movieID) is str

    with open("/u/sridings/netflix-tests/netflix-tests/rbrooks-movie_average_rating.json") as f:
    #with open("/u/mukund/cs373-netflix-tests/rbrooks-movie_average_rating.json") as f:
        data=json.load(f)
        return data[movieID]

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
    ratingSum=0
    ratingCount=0
    while (True) :
        line = netflix_read(r)
        if not line :
            return
        elif line[-1] != ":" : #customer id
            netflix_print(netflix_predict(line), w)
        else : #movie id
            netflix_print(line, w)

def rmse (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    s = len(a)
    v = sum(map(sqre_diff, a, p))
    return math.sqrt(v / s)


