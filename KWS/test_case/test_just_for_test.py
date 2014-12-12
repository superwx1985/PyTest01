'''
Created on 2014年11月11日

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, unittest, datetime, wait_element
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS import init
from KWS.my_test_case import MyTestCase
from selenium.webdriver.common.action_chains import ActionChains

    
class MyTest(MyTestCase):
    
    def setUp(self):
        self.environment = 1
        self.browser = 3
        self.driver = init.Driver(self.environment, self.browser)
        #self.err = []
        print('\nenvironment=%s, browser=%s' % (self.environment, self.browser))
         
    def atest_01(self):
        '01'
        try:
            driver = self.driver
            br = driver.br
            br.get("http://127.0.0.1/")
            currentwindow = br.current_window_handle
            br.find_element_by_id('b2').click()
            # time.sleep(5)
            i=0
            while (True):
                print (i)
                i += 1
                for window in br.window_handles:
                    if window != currentwindow:
                        br.switch_to.window(window)
                        i = -1
                if i == -1 or i > 10:
                    break
                time.sleep(1)

            br.find_element_by_id('a1').click()
            time.sleep(2)

        except:
            raise

    def test_02(self):
        '02'
        try:
            driver = self.driver
            br = driver.br
            br.get("https://weddingshop.theknot.com/")
        except:
            raise
            
    def tearDown(self):
        try:
            SSname = 'D:\\vic_test_data\\KWS_test\\result_' + datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.%f") + '_SS.png'
            self.driver.br.get_screenshot_as_file(SSname)
            print('SS was saved as %s\nThe final URL is %s\n' % (SSname, self.driver.br.current_url))
        except:
            print('cannot get the SS and final URL, because:\n')
            raise
        self.driver.br.quit()
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
    #suppresses a superfluous ResourceWarning which was being emitted at the time of writing.  It may have disappeared by the time you read this; feel free to try removing it!
