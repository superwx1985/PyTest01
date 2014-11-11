'''
Created on 2014年10月31日

@author: viwang
'''
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re
import HTMLTestRunner

br = webdriver.Chrome()
br.get('file:///C:/Users/viwang/Desktop/frame.html')
print(br.current_url)
iframs = br.find_elements_by_tag_name('iframe')#找出当前页面全部iframe，不包含iframe里面的iframe
print(range(len(iframs)))#遍历所有iframe的index
for i in range(len(iframs)):
    print(i)
    br.switch_to_frame(i)#转到index为i的iframe
    print(br.current_url)
    br.switch_to_default_content()#回到最顶层

iframe1=br.find_element_by_css_selector('iframe[rel="f1"]')#先找到某个iframe，定义为iframe1
br.switch_to_frame(iframe1)#转到之前找到的iframe1
print(br.current_url)
br.switch_to_frame('f3')#转到iframe1下面的id为“f3”的iframe里，switch_to_frame()的参数可以是iframe对象，或者iframe的id，name
print(br.current_url)

br.switch_to_default_content()#回到最顶层
print(br.current_url)
br.quit()