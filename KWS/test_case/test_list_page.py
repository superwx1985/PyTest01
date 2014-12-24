'''
Created on 2014年11月11日

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
        'KWS - (List Page) - Verify the search result returned is related to search condition.'
        try:
            driver = self.driver
            br = driver.br
            br.get(driver.baseURL)
            KWS_module.search(driver, 'Paper Fan')
            wait_element.wait_for_text_present(br, 'Paper Fan', 10, True)
        except:
            raise

    def test_02(self):
        'KWS - (List Page) - Verify facets (left nav) appear on subsubcategory pages and work well'
        try:
            driver = self.driver
            br = driver.br
            br.get(driver.baseURL + '/catalog/searchresults.aspx?search=wedding')
            wait_element.wait_for_element_visible(br, 'id', 'chkFilter_top_category_0', 10, True)
            br.find_element_by_xpath('//span[contains(text(),"reception")]').click()
            time.sleep(2)
            self.assertEqual(driver.br.current_url, driver.baseURL + '/catalog/searchresults.aspx?search=wedding&top_category=reception', 'did not redirect to the correct URL')
        except:
            raise
            
    def tearDown(self):
        init.tearDown(self.driver)
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
