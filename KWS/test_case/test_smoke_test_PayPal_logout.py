# -*- coding: utf-8 -*-
import time, threading, unittest
from selenium import webdriver
from KWS.test_case.public import KWS_module


if False:
    br = webdriver.Firefox()
    br.get(KWS_module.baseURL)


class Mytest(unittest.TestCase):
    
    def setUp(self):
        #environment = 1  # 1=qa, 2=stg, 3=live
        #browser = 3  # 1=ie, 2=ff, 3=chrome, 4=remote_chrome, 5=remote_mac, 6=remote_ff
        self.driver = KWS_module.Driver(1, 4)
        self.err=[]
        
    def sample2(self):
        'test case name'
        try:
            driver = self.driver
            print('this is a sample test case')
            driver.br.get('http://www.baidu.com/')
            self.assertEqual("http://www.baidu.com/d", driver.br.current_url)
        except:
            raise
        finally:
            SSname='D:\\vic_test_data\\KWS_test\\result_' + time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + '_SS.png'
            self.driver.br.get_screenshot_as_file(SSname)
            print('SS was saved as %s' %SSname)
            
    def test_smoke_test_1(self):
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
        finally:
            SSname='D:\\vic_test_data\\KWS_test\\result_' + time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + '_SS.png'
            self.driver.br.get_screenshot_as_file(SSname)
            print('SS was saved as %s' %SSname)

    def tearDown(self):
        # input(time.strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(threading.currentThread()) + ' ' + 'case 1 has finished, press any key to continue\n')
        self.driver.br.quit()  

def make_suite():
    suite = unittest.TestSuite()
    #suite.addTest(Mytest('test_smoke_test_2'))
    suite.addTest(Mytest('sample1'))
    return suite


if __name__ == '__main__':
    suite = make_suite()
    runner = unittest.TextTestRunner()

