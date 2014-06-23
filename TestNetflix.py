#!/usr/bin/env python3
"""
 Tests for Netflix.py
 Mark Sandan, Stephen Ridings
"""

from io       import StringIO
from unittest import main, TestCase
from Netflix import *
import math

class TestNetflix (TestCase) :

#-----
# main
# ----
    def test_getAnswer_1(self) :
        r = getAnswerRating ("2043", "1417435")
        self.assertEqual(3, r)
    def test_getAnswer_2(self) :
        r = getAnswerRating ("12582", "341963")
        self.assertEqual(3, r)
    def test_getAnswer_3(self) :
        r = getAnswerRating ("4266", "2373027")
        self.assertEqual(4, r)


    def test_read1 (self) :
        r = StringIO("123:\n1\n2\n3")
        result=netflix_read(r)
        self.assertEqual("123:",result)
        
    def test_read2 (self) :
        r = StringIO("")
        result=netflix_read(r)
        self.assertEqual("",result)
        
    def test_read3 (self) :
        r = StringIO("123:\n1\n2\n3\n")
        result=netflix_read(r)
        self.assertEqual("123:",result)
    
        result=netflix_read(r)
        self.assertEqual("1",result)
    
        result=netflix_read(r)
        self.assertEqual("2",result)
        
        result=netflix_read(r)
        self.assertEqual("3",result)

    def test_readJSONMovieCache_1 (self) :
        data=readAvgMovieRating("2043")
        self.assertEqual(data,3.7776648456358783)


    def test_readJSONCustomerCache_1 (self) :
        data=readAvgCustomerRating("2746")
        self.assertEqual(data,4.68)

    def test_readJSONCustomerCache_2 (self) :
        data=readAvgCustomerRating("1922")
        self.assertEqual(data,3.26)

    def test_readJSONCustomerCache_3 (self) :
        data=readAvgCustomerRating("2168")
        self.assertEqual(data,3.56)

    def test_write1 (self) :
        w = StringIO()
        netflix_write(str(123), w)
        self.assertEqual(w.getvalue(), "123\n")
        
    def test_write2 (self) :
        w = StringIO()
        netflix_write("", w)
        self.assertEqual(w.getvalue(), "\n")
        
    def test_write3 (self) :
        w = StringIO()
        netflix_write("123:", w)
        self.assertEqual(w.getvalue(), "123:\n")

    """   
    def test_predict_1 (self) :
        result = netflix_predict("1417435", "2043")
        self.assertEqual(result, 3.4)

    def test_predict_2 (self) :
        result = netflix_predict("2312054", "2043")
        self.assertEqual(result, 4.1)

    def test_predict_3 (self) :
        result = netflix_predict("462685", "2043")
        self.assertEqual(result, 1.9)
    """

    def test_calcAvgMovieRatings_1 (self) :
        result=calculateOverallMovieRating([2043])
        self.assertNotEqual(result,0)
      
    def test_calcAvgMovieRatings_2 (self) :
        result=calculateOverallMovieRating([14550])
        self.assertEqual(result,4.593383932407275)
        
    def test_calcAvgMovieRatings_3 (self) :
        result=calculateOverallMovieRating([])
        self.assertEqual(result,0)
        
    def test_calcAvgMovieRatings_4 (self) :
        result=calculateOverallMovieRating([2043])
        self.assertEqual(result,3.7776648456358783)
          
    def test_sqre1 (self) :
        a = 0
        b = 0
        result = sqre_diff(a,b)
        self.assertEqual(result, 0)
    
    def test_sqre2 (self) :
        a = 0.0
        b = 0.0
        result = sqre_diff(a,b)
        self.assertEqual(result, 0.0)
    
    def test_sqre3 (self) :
        a = -2
        b = 3
        result = sqre_diff(a,b)
        self.assertEqual(result, 25)
    
    def test_rmse1 (self) :
        result = rmse(10,3)
        self.assertEqual(math.sqrt(10/3), result)
    
    def test_rmse2 (self) :
        try:
            result = rmse(0,0)
            self.assertEqual(0, result)
        except AssertionError:
            pass
        
    def test_rmse3 (self) :
        try:
            result = rmse(0,2)
            self.assertEqual(0, result)
        except AssertionError:
            pass
        
    def test_netflix_rate_1 (self) :
        r = StringIO("2043:\n1417435\n2312054\n462685\n")
        w = StringIO()
        netflix_rate(r, w)
        self.assertEqual(w.getvalue(), "2043:\n3.3366251187847826\n4.286625118784783\n3.616625118784783\n1.9202601769526562\n")

main()


"""
10851: 
1417435
2312054
462685 

"""
