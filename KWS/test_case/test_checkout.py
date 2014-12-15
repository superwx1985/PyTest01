# -*- coding: utf-8 -*-
import time, threading, unittest, datetime
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS import init
from KWS.my_test_case import MyTestCase


if False:
    br = webdriver.Firefox()


class MyTest(MyTestCase):
    def setUp(self):
        # environment = 1  # 1=qa, 2=stg, 3=live
        # browser = 3  # 1=ie, 2=ff, 3=chrome, 4=remote_chrome, 5=remote_mac, 6=remote_ff
        self.driver = init.setUp_(self.environment, self.browser)
                 
    def test_01(self):
        'KWS - (Checkout) - Checkout as guest via CC'
        try:
            driver = self.driver
            br = driver.br
            KWS_module.add_product_paddle_fan_Brown(driver, 7)
            br.get('https://qa.weddingshop.theknot.com/cart/shoppingcart.aspx')
            KWS_module.shopping_cart_checkout_as_guest(driver, 1)
            KWS_module.checkout_via_credit_card(driver, 1)
        except:
            raise
            
    def test_02(self):
        'KWS - (Checkout) - Checkout as user via CC'
        try:
            driver = self.driver
            br = driver.br
            KWS_module.add_product_paddle_fan_Brown(driver, 7)
            br.get('https://qa.weddingshop.theknot.com/cart/shoppingcart.aspx')
            KWS_module.shopping_cart_checkout_as_user(driver, 1, 1)
            KWS_module.checkout_via_credit_card(driver, 1)
        except:
            raise
 
    def test_03(self):
        'KWS - (Checkout) - Checkout as guest via Paypal'
        try:
            driver = self.driver
            br = driver.br
            KWS_module.add_product_paddle_fan_Brown(driver, 7)
            br.get('https://qa.weddingshop.theknot.com/cart/shoppingcart.aspx')
            KWS_module.shopping_cart_checkout_as_guest(driver)
            KWS_module.checkout_via_paypal(driver)
        except:
            raise
 
    def test_04(self):
        'KWS - (Checkout) - Checkout as user via Paypal'
        try:
            driver = self.driver
            br = driver.br
            KWS_module.add_product_paddle_fan_Brown(driver, 7)
            br.get('https://qa.weddingshop.theknot.com/cart/shoppingcart.aspx')
            KWS_module.shopping_cart_checkout_as_user(driver, 1)
            KWS_module.checkout_via_paypal(driver)
        except:
            raise
        
    def test_05(self):
        'KWS - (Checkout) - Checkout as guest via Amazon'
        try:
            driver = self.driver
            br = driver.br
            KWS_module.add_product_paddle_fan_Brown(driver, 7)
            br.get('https://qa.weddingshop.theknot.com/cart/shoppingcart.aspx')
            KWS_module.shopping_cart_checkout_as_guest(driver)
            KWS_module.checkout_via_amazon(driver)
        except:
            raise
         
    def test_06(self):
        'KWS - (Checkout) - Checkout as user via Amazon'
        try:
            driver = self.driver
            br = driver.br
            KWS_module.add_product_paddle_fan_Brown(driver, 7)
            br.get('https://qa.weddingshop.theknot.com/cart/shoppingcart.aspx')
            KWS_module.shopping_cart_checkout_as_user(driver, 1)
            KWS_module.checkout_via_amazon(driver)
        except:
            raise

    def tearDown(self):
        init.tearDown(self.driver)

def make_TC_suite():

    suite = unittest.TestSuite()
    # suite.addTest(MyTest('test_smoke_test_Amazon_logout',1,3))
    suite.addTest(MyTest('sample2', 1, 1))
    suite.addTest(MyTest('sample1'))
    return suite


if __name__ == '__main__':
    # unittest.main(warnings='ignore')
    
    suite = unittest.TestSuite()
    suite.addTest(MyTest('test_01', 1, 3))
    suite.addTest(MyTest('test_02', 1, 3))
    print(suite)
    runner = unittest.TextTestRunner()
    runner.run(suite)

    #===========================================================================
    # driver = KWS_module.Driver(1, 6)
    # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), threading.currentThread(), 'smoke_test_3 start')
    # KWS_module.KWS_add_product_beer(driver, 2)
    # KWS_module.KWS_go_to_shopping_cart_via_cart_flyout(driver)
    # KWS_module.KWS_shopping_cart_checkout_as_guest(driver)
    # KWS_module.KWS_checkout_via_paypal(driver)
    # driver.br.quit()
    #===========================================================================
