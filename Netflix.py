#!/usr/bin/env python3

import math,json
from pprint import pprint

#Average of every movie rated
glbl_mean=3.604289964420661
glbl_mean2 = 3.6054151647682318
glbl_path_to_answer_cache = "/u/sridings/netflix-tests/netflix-tests/osl62-AnswerCache.json"
glbl_path_to_customer_cache = "/u/sridings/netflix-tests/netflix-tests/bryan-customer_cache.json"
glbl_path_to_average_rating = "/u/sridings/netflix-tests/netflix-tests/rbrooks-movie_average_rating.json"

def netflix_read(r):
    """
    reads in a line from probe.txt
    """
    s=r.readline().split("\n")[0]
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

        temp = "/u/downing/cs/netflix/training_set/mv_"

    if (runningSum!=0) :
        return avgRating/runningSum
        
    return 0        
"""
def getAnswerRating (movieID, customerID) :
    assert type(movieID) is str
    assert int(movieID) >= 0
    assert type(customerID) is str

    with open("/u/sridings/netflix-tests/netflix-tests/osl62-AnswerCache.json") as f:
        data=json.load(f)
        return data[movieID + "-" + customerID]

def readAvgCustomerRating(customerID) :
    assert int(customerID) >= 0
    assert type(customerID) is str

    with open("/u/sridings/netflix-tests/netflix-tests/bryan-customer_cache.json") as f:
    #with open("/u/mukund/cs373-netflix-tests/bryan-customer_cache.json") as f:
        data=json.load(f)
        return data[customerID]

   
def readAvgMovieRating(movieID) :
    

    assert int(movieID) >= 0
    assert type(movieID) is str

    with open("/u/sridings/netflix-tests/netflix-tests/rbrooks-movie_average_rating.json") as f:
    #with open("/u/mukund/cs373-netflix-tests/rbrooks-movie_average_rating.json") as f:
        data=json.load(f)
        return data[movieID]
"""

def sqre_diff(a, p) :
    return (a - p) ** 2

def netflix_write (s, w) :
    w.write(str(s) + "\n")

def netflix_predict(customerAverage, movieAverage) :
    """
        Currently experimenting with implementation #1
    """
    movieOffset = glbl_mean - movieAverage
    customerOffset = customerAverage - glbl_mean

    return glbl_mean + movieOffset + customerOffset

def netflix_rate(r, w) :
    runningSqDiff=0
    count=0
    currentMovieID = ""

    answerCache = open(glbl_path_to_answer_cache, "r") 
    customerCache = open(glbl_path_to_customer_cache, "r")
    averageRating = open(glbl_path_to_average_rating, "r")
    
    answerDict = json.loads(answerCache.read())
    customerDict = json.loads(customerCache.read())
    averageDict = json.loads(averageRating.read())

    while (True) :
        line = netflix_read(r)
        if not line :
            print(rmse(runningSqDiff,count))
            break
        elif line[-1] != ":" : #customer id
            prediction=netflix_predict(customerDict[line], averageDict[currentMovieID])
            actual=answerDict[currentMovieID + "-" + line]
            runningSqDiff+=sqre_diff(actual,prediction)
            count += 1

            #netflix_write(prediction, w)
      
        else : #movie id
            currentMovieID=line[:-1]
        
            #netflix_write(line, w)


def rmse (runningSqDiff, count) :
    assert count > 0 
    return math.sqrt(runningSqDiff/count)


