# -*- coding: utf-8 -*-
# coding=utf-8
from selenium import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time, threading, unittest, datetime

now = datetime.datetime.now()
print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"))
