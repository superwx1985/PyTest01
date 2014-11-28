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



class Page(object):
    bd_url = 'http://www.baidu.com'
    def __init__(self, selenium_driver, base_url=bd_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent
        self.tabs = {}
        
    def open(self):
        self.driver.get(self.base_url)
    
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    
    def send_keys(self,loc,value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, '_%s' % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            print ('%s page does not have "%s" locator' %(self,loc))

#===============================================================================
# br = webdriver.Chrome()
# if False:
#     br.find_element('', '').send_keys()
# loc = ('id','kw')
# page1 = Page(br)
# page1.open()
# page1.find_element(*loc).send_keys('123')
#===============================================================================
assert(1==2)
