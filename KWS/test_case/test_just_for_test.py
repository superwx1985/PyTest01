'''
Created on 2014年11月11日

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, unittest, datetime, threading, wait_element
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS import import_test_data, init
from KWS.my_test_case import MyTestCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MyTest(MyTestCase):
    def setUp(self):
        # environment = 1  # 1=qa, 2=stg, 3=live
        browser = 2  # 1=ie, 2=ff, 3=chrome, 4=remote_chrome, 5=remote_mac, 6=remote_ff
        self.driver = init.setUp_(self.environment, self.browser)
        
    def test_01(self):
        '01'
        try:
            br = self.driver.br
            br.get('http://localhost/')
            f = EC.element_to_be_clickable((By.ID,'b3'))
            print(f(br))

        except:
            raise

    def atest_02(self):
        '02'
        try:
            pass
        except:
            raise
            
    def tearDown(self):
        init.tearDown(self.driver)
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
    #suppresses a superfluous ResourceWarning which was being emitted at the time of writing.  It may have disappeared by the time you read this; feel free to try removing it!
