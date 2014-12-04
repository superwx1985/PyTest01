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
from selenium.webdriver.common.action_chains import ActionChains

    
class MyTest(MyTestCase):
    
    def setUp(self):
        self.environment = 1
        self.browser = 7
        self.driver = KWS_module.Driver(self.environment, self.browser)
        self.err = []
        print('\nenvironment=%s, browser=%s' % (self.environment, self.browser))
         
    def test_01(self):
        '01'
        try:
            driver = self.driver
            br = driver.br
            br.get(driver.baseURL)
            e1 = br.find_element_by_css_selector('ul.nav.navbar-nav>li:nth-of-type(3)>a')
            # time.sleep(2000)
            e2 = br.find_element_by_css_selector('ul.nav.navbar-nav>li:nth-of-type(3)>ul>li>ul>li:nth-of-type(8)>a')
            ActionChains(br).move_to_element(e1).click(e2).perform()
            time.sleep(5)
        except:
            raise

    def atest_02(self):
        '02'
        try:
            assert(1 == 2),'failedaa'
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
