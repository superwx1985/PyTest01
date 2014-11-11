# -*- coding: utf-8 -*-
import unittest, time, re, random, HTMLTestRunner
class Mytest2(unittest.TestCase):
    def step(self):
        pass
    
    def test1(self):
        print("test1")
        
    def tearDown(self):
        print('teardown')
        unittest.TestCase.tearDown(self)
        
if __name__ == '__main__':
    unittest.main()