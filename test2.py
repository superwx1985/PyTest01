# -*- coding: utf-8 -*-
# coding=utf-8
import time, unittest, datetime, threading, wait_element
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS import import_test_data, init
from KWS.my_test_case import MyTestCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

br=webdriver.Chrome()
data = import_test_data.get_excle_data('D:/vic/workspace/PyTest01/vic_test/test.xlsx', 'Sheet1', True)


for i in range(2,data['rows']+1):
    print (i,data['C'+str(i)])
    if data['C'+str(i)] == 'go to url':
        assert(data['D'+str(i)] != ''), 'missing locator'
        br.get(data['D'+str(i)])
    elif data['C'+str(i)] == 'enter':
        assert(data['D'+str(i)] != ''), 'missing locator'
        assert(data['E'+str(i)] != ''), 'missing data'
        locator = data['D'+str(i)].split('|')
        if isinstance(data['F'+str(i)], (int,float)):
            ot=round(data['F'+str(i)])
        elif data['F'+str(i)].isdigit():
            ot=int(data['F'+str(i)])
        else:
            ot=10
        wait_element.try_to_enter(br, locator[0], locator[1], ot, data['E'+str(i)])
    elif data['C'+str(i)] == 'click':
        assert(data['D'+str(i)] != ''), 'missing locator'
        locator = data['D'+str(i)].split('|')
        if isinstance(data['F'+str(i)], (int,float)):
            ot=round(data['F'+str(i)])
        elif data['F'+str(i)].isdigit():
            ot=int(data['F'+str(i)])
        else:
            ot=10
        wait_element.try_to_click(br, locator[0], locator[1], ot)
    elif data['C'+str(i)] == 'verify test':
        assert(data['E'+str(i)] != ''), 'missing data'
        if isinstance(data['F'+str(i)], (int,float)):
            ot=round(data['F'+str(i)])
        elif data['F'+str(i)].isdigit():
            ot=int(data['F'+str(i)])
        else:
            ot=10
        wait_element.wait_for_text_present(br, data['E'+str(i)], ot, True)
    else:
        print('WTF')
print('end')
br.quit()