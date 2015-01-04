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
from urllib.parse import urlencode



url = 'http://retailerapi-qa-1048811846.us-east-1.elb.amazonaws.com/retailer/v1/registry'
headers={'access-key':'839d35cd515746b5167d494f856e4ef0','Content-Type':'application/json; charset=utf-8'}
#===============================================================================
# url_params = {'apikey':'ca7f6e91ee8134de9717707d86b29100'}
# url=url+'?'
# for key, value in url_params.items():
#     url = url+key+'='+value+'&'
#===============================================================================
data = '''{
    "RetailerRegistryCode": "vic14123106",
    "RegistrantFirstName": "Zacharey",
    "RegistrantLastName": "Hayes",  
    "RegistrantEmail": "111@gmail.com",
    "CoRegistrantFirstName": "Millie",
    "CoRegistrantLastName": "Lily",
    "CoRegistrantEmail": "aaa@gmail.com",
    "City": "TALLAHASSEE",
    "State": "FL",
    "Zip": "510000",
    "EventTypeId": 1,
    "EventDate": "2015-01-28",
    "EventDescription": "",
    "ReferralStatusCode": "",
    "RegistryClickId": "",
    "AltRetailerRegistryCode": "",
    "ModifiedDate": "2014-12-04"
}'''
if isinstance(data, dict):
    body = urlencode(data)
else:
    body = data
#body = str(data).replace('\'', '\"')

h = httplib2.Http()
response, content = h.request(url, 'PUT', headers=headers, body=body)

str_content = content.decode('utf-8')
print(response)
print(str_content)

