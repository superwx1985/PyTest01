# -*- coding: utf-8 -*-
import time, threading, unittest
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS.MyTestCase import MyTestCase


if False:
    br = webdriver.Firefox()
    br.get(KWS_module.baseURL)


class MyTest(MyTestCase):

    def setUp(self):
        # environment = 1  # 1=qa, 2=stg, 3=live
        # browser = 3  # 1=ie, 2=ff, 3=chrome, 4=remote_chrome, 5=remote_mac, 6=remote_ff
        self.driver = KWS_module.Driver(self.environment, self.browser)
        self.err = []
        print('\nenvironment=%s, browser=%s' %(self.environment,self.browser))
        
    def sample1(self):
        'test case name'
        try:
            driver = self.driver
            print('this is a sample test case')
            driver.br.get('http://www.baidu.com/baidu?wd=ip')
            #===================================================================
            # driver.br.get('http://www.baidu.com/baidu?wd=ip')
            # for i in range(5):
            #     driver.br.execute_script('scroll(0,100)')
            #     time.sleep(0.5)
            #     driver.br.execute_script('scroll(0,0)')
            #     time.sleep(0.5)
            #===================================================================
            time.sleep(5)
            # self.assertEqual("http://www.baidu.com/s", driver.br.current_url)
        except Exception as err:
            print(err)
        #=======================================================================
        # finally:
        #     SSname = 'D:\\vic_test_data\\KWS_test\\result_' + time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + '_SS.png'
        #     self.driver.br.get_screenshot_as_file(SSname)
        #     print('SS was saved as %s, the final URL is %s' % (SSname, driver.br.current_url))
        #=======================================================================
            
    def sample2(self):
        'test case name'
        try:
            driver = self.driver
            print('this is a sample test case')
            driver.br.get('http://www.baidu.com/')
            self.assertEqual("http://www.baidu.com/d", driver.br.current_url)
        except:
            raise
        #=======================================================================
        # finally:
        #     SSname = 'D:\\vic_test_data\\KWS_test\\result_' + time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + '_SS.png'
        #     self.driver.br.get_screenshot_as_file(SSname)
        #     print('SS was saved as %s, the final URL is %s' % (SSname, driver.br.current_url))
        #=======================================================================
            
    def test_smoke_test_CC_logout(self):
        'checkout as guest via CC'
        try:
            driver = self.driver
            print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_1 start')        
            KWS_module.KWS_add_product_beer(driver, 2)
            KWS_module.KWS_go_to_shopping_cart_via_cart_flyout(driver)
            KWS_module.KWS_shopping_cart_checkout_as_guest(driver)
            KWS_module.KWS_checkout_via_credit_card(driver)
            print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_1 end')
        except:
            raise
        #=======================================================================
        # finally:
        #     SSname = 'D:\\vic_test_data\\KWS_test\\result_' + time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + '_SS.png'
        #     self.driver.br.get_screenshot_as_file(SSname)
        #     print('SS was saved as %s' % SSname)
        #=======================================================================
            
    def test_smoke_test_CC_login(self):
        'checkout as user via CC'
        try:
            driver = self.driver
            print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_2 start')
            KWS_module.KWS_add_product_paddle_fan(driver, 7)
            KWS_module.KWS_go_to_shopping_cart_via_cart_flyout(driver)
            KWS_module.KWS_shopping_cart_checkout_as_user(driver)
            KWS_module.KWS_checkout_via_credit_card(driver)
            print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_2 end')
        except:
            raise
        #=======================================================================
        # finally:
        #     SSname = 'D:\\vic_test_data\\KWS_test\\result_' + time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + '_SS.png'
        #     self.driver.br.get_screenshot_as_file(SSname)
        #     print('SS was saved as %s' % SSname)
        #=======================================================================
 
    def test_smoke_test_Paypal_logout(self):
        'checkout as guest via Paypal'
        try:
            driver = self.driver
            print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_3 start')
            KWS_module.KWS_add_product_beer(driver, 2)
            KWS_module.KWS_go_to_shopping_cart_via_cart_flyout(driver)
            KWS_module.KWS_shopping_cart_checkout_as_guest(driver)
            KWS_module.KWS_checkout_via_paypal(driver)
        except:
            raise
        #=======================================================================
        # finally:
        #     print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_3 end')
        #     SSname = 'D:\\vic_test_data\\KWS_test\\result_' + time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + '_SS.png'
        #     self.driver.br.get_screenshot_as_file(SSname)
        #     print('SS was saved as %s' % SSname)
        #=======================================================================
 
    def test_smoke_test_Paypal_login(self):
        'checkout as user via Paypal'
        try:
            driver = self.driver
            print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_4 start')
            KWS_module.KWS_add_product_paddle_fan(driver)
            KWS_module.KWS_go_to_shopping_cart_via_cart_flyout(driver)
            KWS_module.KWS_shopping_cart_checkout_as_user(driver)
            KWS_module.KWS_checkout_via_paypal(driver)
        except:
            raise
        #=======================================================================
        # finally:
        #     print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_4 end')
        #     SSname = 'D:\\vic_test_data\\KWS_test\\result_' + time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + '_SS.png'
        #     self.driver.br.get_screenshot_as_file(SSname)
        #     print('SS was saved as %s' % SSname)
        #   
        #=======================================================================
    def test_smoke_test_Amazon_logout(self):
        'checkout as guest via Amazon'
        try:
            driver = self.driver
            print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_5 start')
            KWS_module.KWS_add_product_beer(driver, 2)
            KWS_module.KWS_go_to_shopping_cart_via_cart_flyout(driver)
            KWS_module.KWS_shopping_cart_checkout_as_guest(driver)
            KWS_module.KWS_checkout_via_amazon(driver)
        except:
            raise
        #=======================================================================
        # finally:
        #     print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_5 end')
        #     SSname = 'D:\\vic_test_data\\KWS_test\\result_' + time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + '_SS.png'
        #     self.driver.br.get_screenshot_as_file(SSname)
        #     print('SS was saved as %s' %SSname)
        #=======================================================================
         
    def test_smoke_test_Amazon_login(self):
        'checkout as user via Amazon'
        try:
            driver = self.driver
            print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_6 start')
            KWS_module.KWS_add_product_paddle_fan(driver, 7)
            KWS_module.KWS_go_to_shopping_cart_via_cart_flyout(driver)
            KWS_module.KWS_shopping_cart_checkout_as_user(driver)
            KWS_module.KWS_checkout_via_amazon(driver)
        except:
            raise
        #=======================================================================
        # finally:
        #     print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_6 end')
        #     SSname = 'D:\\vic_test_data\\KWS_test\\result_' + time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + '_SS.png'
        #     self.driver.br.get_screenshot_as_file(SSname)
        #     print('SS was saved as %s' %SSname)
        #=======================================================================

    def tearDown(self):
        try:
            SSname = 'D:\\vic_test_data\\KWS_test\\result_' + time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + '_SS.png'
            self.driver.br.get_screenshot_as_file(SSname)
            print('SS was saved as %s\nThe final URL is %s\n' % (SSname, self.driver.br.current_url))
        except:
            print('cannot get the SS and final URL, because:\n')
            raise
            
        # input(time.strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(threading.currentThread()) + ' ' + 'case 1 has finished, press any key to continue\n')
        self.driver.br.quit()

def make_TC_suite():

    suite = unittest.TestSuite()
    #suite.addTest(MyTest('test_smoke_test_Amazon_logout',1,3))
    suite.addTest(MyTest('sample2',1,1))
    suite.addTest(MyTest('sample1'))
    return suite


if __name__ == '__main__':
    #unittest.main()
    #suite = make_TC_suite()
    

    suite = unittest.TestSuite()
    #print(suite)
    suite.addTest(make_TC_suite())
    print(suite)
    runner = unittest.TextTestRunner()
    runner.run(suite)


    #===========================================================================
    # driver = KWS_module.Driver(1, 6)
    # print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_3 start')
    # KWS_module.KWS_add_product_beer(driver, 2)
    # KWS_module.KWS_go_to_shopping_cart_via_cart_flyout(driver)
    # KWS_module.KWS_shopping_cart_checkout_as_guest(driver)
    # KWS_module.KWS_checkout_via_paypal(driver)
    # driver.br.quit()
    #===========================================================================
