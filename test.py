# -*- coding: utf-8 -*-
import time, unittest, datetime, threading
import import_test_data, wait_element
from KWS import init
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS.my_test_case import MyTestCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions 
import httplib2



url = 'http://qa.services.theknot.com/registry/v1/retailers/86132002'
url_params = {'apikey':'ca7f6e91ee8134de9717707d86b29100','a':'1'}
url=url+'?'
for key, value in url_params.items():
    url = url+key+'='+value+'&'

h = httplib2.Http('.cache')
response, content = h.request(url, 'GET')


print(content)
print(isinstance(content, str))
str_content = content.decode('utf-8')

print(str_content)
print(isinstance(str_content, str))