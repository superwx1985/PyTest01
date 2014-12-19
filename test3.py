'''
Created on 2014年10月31日

@author: viwang
'''
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re, random
import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from KWS.test_case.public import KWS_module
from KWS import import_test_data


def test1():
    print (test1.__name__)
    test1.__name__ = 'aaaa'
    print (test1.__name__)
test1()