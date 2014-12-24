'''
Created on 2014年12月16日

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, unittest, datetime, threading
import import_test_data, wait_element
from KWS import init
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS.my_test_case import MyTestCase
from selenium.webdriver.common.action_chains import ActionChains
    
class MyTest(MyTestCase):
    def setUp(self):
        # environment = 1  # 1=qa, 2=stg, 3=live
        # browser = 3  # 1=ie, 2=ff, 3=chrome, 4=remote_chrome, 5=remote_mac, 6=remote_ff
        self.driver = init.setUp_(self.environment, self.browser)
         
    def test_01(self):
        'KWS - (Checkout Page) - Verify a valid promotional code can be applied and remove'
        try:
            driver = self.driver
            br = driver.br
            KWS_module.add_product_paddle_fan_Brown(driver, 7)
            KWS_module.mini_cart_checkout_as_guest(driver, 1)
            wait_element.wait_for_element_visible(driver.br, 'xpath', '//p[text()="Total:"]', 30)
            wait_element.wait_for_element_disappear(driver.br, 'id', 'data_loading', 30)
            data = import_test_data.get_excle_data('D:/viwang/workspace/PyTest01/KWS/test_data/Item List.xlsx','promotion code')
            wait_element.try_to_enter(driver.br, 'id', 'CouponCode1', 5, data['A3'])
            wait_element.try_to_click(driver.br, 'css selector', 'a.btn.btn-primary.btn-sm', 5)
            wait_element.wait_for_element_visible(driver.br, 'xpath', '//p[contains(text(),"\'SAVETENNOW\'")]', 30, True)
        except:
            raise

    def atest_02(self):
        'KWS - (Shopping Cart Page) - Verify products removed from the cart result in correctly updated subtotal.'
        try:
            driver = self.driver
            br = driver.br
            pass
        except:
            raise
            
    def tearDown(self):
        init.tearDown(self.driver)
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')