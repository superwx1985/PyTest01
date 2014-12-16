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

x=12116
map_ = {0: 'err', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
s=''
while(True):
    if x<27:
        s=s+map_[x]
        break
    y = int(x/26)
    if y > 26:
        if x%26 == 0:
            s=s+map_[26]
            x = y-1
            continue
        s=s+map_[x%26]
        x = y
        continue
    if x%26 == 0:
        s=s+map_[26]+map_[y-1]
    else:
        s=s+map_[x%26]+map_[y]
    x = y
    if y<=26:
        break
s=s[::-1]
print(s)