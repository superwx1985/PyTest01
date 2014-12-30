# -*- coding: utf-8 -*-
# coding=utf-8
import time, unittest, datetime, threading, wait_element
from selenium import webdriver
from KWS.test_case.public import KWS_module

from KWS.my_test_case import MyTestCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions 


data = dict(Id=86132002,Name='861320edit02',IsDeleted=False,CreatedBy='QA1',ModifiedBy='QA1')
print (data)