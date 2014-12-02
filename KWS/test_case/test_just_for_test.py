'''
Created on 2014年11月11日

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, unittest
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS import verification
from KWS.my_test_case import MyTestCase

    
class MyTest(MyTestCase):
    
    def setUp(self):
        self.driver = KWS_module.Driver(self.environment, self.browser)
        self.err = []
        print('\nenvironment=%s, browser=%s' % (self.environment, self.browser))
         
    def test_01(self):
        '01'
        try:
            self.driver.br.get('http://www.baidu.com/')
            verification.verification_element_present(self.driver, xpath='//img[@src="//www.baidu.com/img/bd_logo1.png"]')
        except:
            raise

    def atest_02(self):
        '02'
        try:
            assert(1 == 2)
        except:
            raise
            
    def tearDown(self):
        try:
            SSname = 'D:\\vic_test_data\\KWS_test\\result_' + time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + '_SS.png'
            self.driver.br.get_screenshot_as_file(SSname)
            print('SS was saved as %s\nThe final URL is %s\n' % (SSname, self.driver.br.current_url))
        except:
            print('cannot get the SS and final URL, because:\n')
            raise
        self.driver.br.quit()
        
if __name__ == '__main__':
    unittest.main()
