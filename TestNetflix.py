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

    

    def test_predict_1 (self) :
        try :
            result = netflix_predict(0, 0, 0)
        except AssertionError :
            pass
        except Exception :
            print ("unknown exception raised.")

    def test_predict_2 (self) :
        try :
            result = netflix_predict(-1, -1, -1 )
        except AssertionError :
            pass
        except Exception :
            print ("unknown exception raised.")

    def test_predict_3 (self) :
        result = netflix_predict(1, 1, 1)
        self.assertEqual(result, 1)
    

        
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
        self.assertEqual(round(math.sqrt(10/3),4), result)
    
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
        self.assertEqual(w.getvalue(), "2043:\n3.9\n3.7\n3.9\n1.6442\n")
    
    def test_netflix_rate_2 (self) :
        r = StringIO("10:\n1952305\n1531863\n")
        w = StringIO()
        netflix_rate(r, w)
        self.assertEqual(w.getvalue(), "10:\n3.3\n3.2\n0.255\n")
    
    def test_netflix_rate_3 (self) :
        r = StringIO("10849:\n2494075\n335030\n1943479\n")
        w = StringIO()
        netflix_rate(r, w)
        self.assertEqual(w.getvalue(), "10849:\n3.2\n3.7\n3.6\n0.911\n")
    
main()
