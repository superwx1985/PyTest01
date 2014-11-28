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

br = webdriver.Chrome()
br.get('http://www.baidu.com')
br.find_element_by_id('kw').send_keys('搜索一下')
time.sleep(2)
br.find_element_by_id('su').click()
a=br.find_elements_by_css_selector('div.result.c-container a')

for a1 in a:
    print(a1.text)
br.close()
