#!/usr/bin/env python3
"""
 Tests for Netflix.py
 Mark Sandan, Stephen Ridings
"""

from io       import StringIO
from unittest import main, TestCase
from Netflix import netflix_read, netflix_predict
#from Netflix import netflix_write, netflix_rsme

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
        
main()

