'''
Created on 2014年11月11日

@author: viwang
'''
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS import Verification
from KWS.MyTestCase import MyTestCase

    
class MyTest(MyTestCase):
    
    def setUp(self):
        # environment = 1  # 1=qa, 2=stg, 3=live
        # browser = 3  # 1=ie, 2=ff, 3=chrome, 4=remote_chrome, 5=remote_mac, 6=remote_ff
        self.driver = KWS_module.Driver(self.environment, self.browser)
        self.err = []
        print('\nenvironment=%s, browser=%s' %(self.environment,self.browser))
        
    def test_VerifyTheSearchResultReturnedIsRelatedToSearchCondition(self):
        try:
            driver = self.driver
            driver.br.get(driver.baseURL)
            KWS_module.KWS_search(driver, 'Paper Fan')
            Verification.verification_text_persent(driver, 'Paper Fan')
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