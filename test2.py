# -*- coding: utf-8 -*-
# coding=utf-8
from selenium import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time, threading, unittest, datetime

x=702
done=0
y=0
z=0
map_ = {0: 'Z', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
list=[]
while(True):
    if x<27:
        list.append(x)
        break
    y=x/26
    if y<26:
        list.append(x%26)
        list.append(int(y))
        break
    else:
        list.append(x%26)
        x=int(y)

print(702/26,702%26)
list.sort(reverse=True)
print(list)
s=''
for i in list:
    #print(i)
    s=s+map_[i]
print('s is "%s"' %s)
