'''
Created on 2014年12月15日

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, unittest, datetime, threading, wait_element
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS import import_test_data, init
from KWS.my_test_case import MyTestCase
from selenium.webdriver.common.action_chains import ActionChains


    
class MyTest(MyTestCase):
    def setUp(self):
        # environment = 1  # 1=qa, 2=stg, 3=live
        # browser = 3  # 1=ie, 2=ff, 3=chrome, 4=remote_chrome, 5=remote_mac, 6=remote_ff
        self.driver = init.setUp_(self.environment, self.browser)
         
    def atest_01(self):
        'KWS - (Shopping Cart Page) - Verify "Continue Shopping" link functions correctly.'
        try:
            driver = self.driver
            br = driver.br
            KWS_module.add_product_paddle_fan_Brown(driver, 7)
            br.get('https://qa.weddingshop.theknot.com/cart/shoppingcart.aspx')
            wait_element.wait_for_element_visible(br, 'xpath', '//a[contains(text(),"CONTINUE SHOPPING") and @href="/"]', 10, True)
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

    def test_03(self):
        'KWS - (Shopping Cart Page) - Verify if a user is already logged in, we will recognize that user when they proceed to checkout.'
        try:
            driver = self.driver
            br = driver.br
            KWS_module.go_to_homepage(driver)
            KWS_module.login_in_header(driver, 1)
            KWS_module.add_product_paddle_fan_Brown(driver, 7)
            br.get('https://qa.weddingshop.theknot.com/cart/shoppingcart.aspx')
            wait_element.try_to_click(br, 'xpath', '//button[contains(text(),"PROCEED TO CHECKOUT")]', 10)
            wait_element.wait_for_element_visible(driver.br, 'id', 'mybillshipModalLabel', 30, True)
        except:
            raise
            
    def tearDown(self):
        init.tearDown(self.driver)
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')