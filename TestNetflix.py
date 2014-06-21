#!/usr/bin/env python3
"""
 Tests for Netflix.py
 Mark Sandan, Stephen Ridings
"""

from io       import StringIO
from unittest import main, TestCase
from Netflix import netflix_read, netflix_predict, netflix_write, sqre_diff, rmse
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
        a = [1, 2, 3]
        b = [0, 0, 0]
        result = rmse(a,b)
        self.assertEqual(math.sqrt(14/3), result)
    
    def test_rmse2 (self) :
        a = [0, 0, 0]
        b = [0, 0, 0]
        result = rmse(a,b)
        self.assertEqual(0, result)
    
    def test_rmse3 (self) :
        a = [1, 2, 3]
        b = [1, 2, 3]
        result = rmse(a,b)
        self.assertEqual(0, result)
    
main()
