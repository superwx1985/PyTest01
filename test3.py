'''
Created on 2014年10月31日

@author: viwang
'''
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re
import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#br1=webdriver.Remote(command_executor='http://127.0.0.1:5556/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
br2=webdriver.Remote(command_executor='http://172.25.20.19:5555/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
#br1.close()
br2.close()
