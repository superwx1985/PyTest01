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

line = 3
data = import_test_data.get_csv_data('D:/viwang/workspace/PyTest01/KWS/test_data/address.csv')
print('%s/%s/%s/%s/%s/%s/%s/%s/%s/%s' % (data[line][0], data[line][1], data[line][2], data[line][3], data[line][4], data[line][5], data[line][6], data[line][7], data[line][8], data[line][9]))