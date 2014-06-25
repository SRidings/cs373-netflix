#!/usr/bin/env python3

import math,json
from pprint import pprint

#Average of every movie rated
"""
Paths to the following cache files

glbl_path_to_answer_cache
glbl_path_to_customer_cache
glbl_path_to_average_rating

"""
glbl_mean=3.604289964420661
glbl_mean2 = 3.6054151647682318
glbl_cust_mean = 3.6736284920068587
user ="sridings/netflix-tests/"
glbl_path_to_answer_cache = "/u/"+user+"netflix-tests/osl62-AnswerCache.json"
glbl_path_to_customer_cache = "/u/"+user+"netflix-tests/osl62-CustomerCache.json"
glbl_path_to_average_rating = "/u/"+user+"netflix-tests/rbrooks-movie_average_rating.json"
glbl_path_to_norm_average_rating = "sridings-mov-normed-avg.json"
glbl_path_to_cust_avg = "/u/"+user+"netflix-tests/bryan-customer_cache.json"

def netflix_read(r):
    """
    Input r is a reader. r reads from sys. in
    reads in a line from probe.txt
    """
    s=r.readline().split("\n")[0]
    return s    
   
def sqre_diff(a, p) :
    """
    returns ( a - p ) squared
    """
    return (a - p) ** 2

def netflix_write (s, w) :
    """
    writes the object s to the writer w.
    It appends a new line also.
    """
    
    w.write(str(s) + "\n")

def netflix_predict(customerAverage, normMovAvg, movAvg, custAvg) :
    """
        Currently experimenting with implementation #1
        Trying different combinations of numerators and
        denominators.

    """
      
    if (customerAverage[2] == 0) :
        
       return (((movAvg)*(9/10)) + (customerAverage[1]*(14/10)))/2

    else :
       return (movAvg + customerAverage[1])/2
   
    
    
    #return (customerAverage* (525/1000) + movAvg * (475/1000))
    #return (customerAverage[0]) + (customerAverage[2])*normMovAvg
    #return ((overallMean + movieAverage + customerAverage) / 3)
    #return customerAverage*(num1/d) + movieAverage*(num2/d)

#TODO: switch 

#def netflix_rate(r, w, num1,num2,d) :
def netflix_rate(r, w) :
    """
    r is the reader
    w is the writer
    Generates predictions of ratings based on the 
    given input from sys in (Probe.txt). The predictions
    are given by netflix_predict.

    The rmse is also calculated by keeping track of the
    running sum of the square differences instead of keeping
    the actual and corresponding predicted values in separate
    lists. 
    """
    runningSqDiff=0
    count=0
    currentMovieID = ""

    answerCache = open(glbl_path_to_answer_cache, "r") 
    customerCache = open(glbl_path_to_customer_cache, "r")
    averageRating = open(glbl_path_to_average_rating, "r")
    normAvgRating = open(glbl_path_to_norm_average_rating, "r")
    customerAvg = open(glbl_path_to_cust_avg, "r")

    #TODO: remove and point to proper probe.txt path
   # data = open("/u/sridings/cs373-netflix/probe.txt", "r")
    
    answerDict = json.loads(answerCache.read())
    customerDict = json.loads(customerCache.read())
    averageDict = json.loads(averageRating.read())
    normAvgDict = json.loads(normAvgRating.read())
    customerAvgDict = json.loads(customerAvg.read())

    while (True) :
        #TODO: switch 
        line = netflix_read(r)
       # line= data.readline().split("\n")[0]

        if not line :
            print (rmse(runningSqDiff,count))
            break

        elif line[-1] != ":" : #customer id
#TODO: switch
#            prediction=netflix_predict(customerDict[line], averageDict[currentMovieID])

            prediction=netflix_predict(customerDict[line],normAvgDict[currentMovieID],averageDict[currentMovieID], customerAvgDict[line])
            actual=answerDict[currentMovieID + "-" + line]
            runningSqDiff+=sqre_diff(actual,prediction)
            count += 1

            #netflix_write(prediction, w)
      
        else : #movie id
            #TODO: write the predictions out?
            currentMovieID=line[:-1]
        
            #netflix_write(line, w)

def rmse (runningSqDiff, count) :
    """
    rmse calculates the root mean square error.
    It is given the running sum of square differences
    and the count to divide by. The square root is then 
    returned.
    """
    assert count > 0 
    return math.sqrt(runningSqDiff/count)


