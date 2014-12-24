'''
Created on 2014年10月31日

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, unittest, datetime, threading
import import_test_data, wait_element
from KWS import init
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS.my_test_case import MyTestCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions 
import os

bace_dir = os.path.dirname(__file__)
print(bace_dir)
print('\u4e2d')