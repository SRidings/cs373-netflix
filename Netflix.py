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

def getAnswerRating (movieID, customerID) :
    """
    read from cache of actual customer ratings
    """
    assert type(movieID) is str
    assert type(customerID) is str

    with open("/u/sridings/netflix-tests/netflix-tests/osl62-AnswerCache.json") as f:
        data=json.load(f)
        return data[movieID + "-" + customerID]

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

def netflix_predict(customerID, movieID) :
    """
        Currently experimenting with implementation #1
    """
    movieAverage = float(readAvgMovieRating(movieID))
    customerAverage = float(readAvgCustomerRating(customerID))
    movieOffset = glbl_mean - movieAverage
    customerOffset = customerAverage - glbl_mean

    return glbl_mean + movieOffset + customerOffset

def netflix_rate(r, w) :
    runningSqDiff=0
    count=0
    currentMovieID = ""

    while (True) :
        line = netflix_read(r)
        if not line :
            netflix_print(rmse(runningSqDiff,count),w)
            return
        elif line[-1] != ":" : #customer id
            prediction=netflix_predict(line, currentMovieID)
            actual=getAnswerRating(line,currentMovieID)
            runningSqDiff+=sqre_diff(actual,prediction)
            count+=1

            netflix_print(prediction, w)
            
        else : #movie id
            currentMovieID=line
            netflix_print(line, w)

def rmse (runningSqDiff, count) :
  
    return math.sqrt(runningSqDiff/count)


