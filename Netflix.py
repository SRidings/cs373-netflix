#!/usr/bin/env python3

import math,json
from pprint import pprint

#Average of every movie rated

"""
Paths to the following cache files

"""
user ="mukund/"
glbl_path_to_answer_cache = "/u/"+user+"netflix-tests/osl62-AnswerCache.json"
glbl_path_to_average_rating = "/u/"+user+"netflix-tests/rbrooks-movie_average_rating.json"
glbl_path_to_cust_avg = "/u/"+user+"netflix-tests/bryan-customer_cache.json"
glbl_path_to_cust_cache_by_dec = "/u/"+user+"netflix-tests/ahsu-cust_by_decade.json"
glbl_path_to_movie_cache_by_dec = "/u/"+user+"netflix-tests/isabella-movie_decades_cache.json"


def netflix_read(r):
    """
    Input r is a reader. r reads from sys. in
    reads in a line from probe.txt
    """
    s=r.readline().strip()
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

def netflix_predict(customerAverage,  movAvg, custDecadeAverage) :
    """
        Currently experimenting with implementation #1
        Trying different combinations of numerators and
        denominators.

    """
    assert ( 0 < customerAverage <= 5)
    assert ( 0 < movAvg <= 5)
    assert ( 0 <= custDecadeAverage <= 5)    

    cAvg = 0

    if (custDecadeAverage == 0) :
        cAvg = customerAverage
    else :
        cAvg = custDecadeAverage
    return round((movAvg*(494/1000) + cAvg*(506/1000)), 1)        
    
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
    movieDecade = ""

    answerCache = open(glbl_path_to_answer_cache, "r") 
    averageRating = open(glbl_path_to_average_rating, "r")
    customerAvg = open(glbl_path_to_cust_avg, "r")
    custByDec = open(glbl_path_to_cust_cache_by_dec, "r")
    movByDec = open(glbl_path_to_movie_cache_by_dec, "r")
    
    answerDict = json.loads(answerCache.read())
    averageDict = json.loads(averageRating.read())
    customerAvgDict = json.loads(customerAvg.read())
    custDecDict = json.loads(custByDec.read())
    movDecDict = json.loads(movByDec.read())

    while (True) :
        line = netflix_read(r)

        if not line :
            netflix_write("RMSE: " + str(rmse(runningSqDiff,count)), w)
            break

        elif line[-1] != ":" : #customer id

            prediction=netflix_predict(customerAvgDict[line],averageDict[currentMovieID], custDecDict[line][movieDecade])
            actual=answerDict[currentMovieID + "-" + line]
            runningSqDiff+=sqre_diff(actual,prediction)
            count += 1

            netflix_write(prediction, w)
      
        else : #movie id
            currentMovieID=line[:-1]
            movieDecade = movDecDict[currentMovieID]
            netflix_write(line, w)
    
    answerCache.close()
    averageRating.close()
    customerAvg.close()
    custByDec.close()
    movByDec.close()

def rmse (runningSqDiff, count) :
    """
    rmse calculates the root mean square error.
    It is given the running sum of square differences
    and the count to divide by. The square root is then 
    returned.
    """
    assert count > 0 
    return round((math.sqrt(runningSqDiff/count)),4)


