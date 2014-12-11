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

    
class MyTest(MyTestCase):
    
    def setUp(self):
        #self.environment = 3
        #self.browser = 2
        self.driver = init.Driver(self.environment, self.browser)
        self.err = []
        print('\nenvironment=%s, browser=%s' % (self.environment, self.browser))
         
    def test_list_page_01_Search_Bar(self):
        'KWS - (List Page) - Verify the search result returned is related to search condition.'
        try:
            driver = self.driver
            br = driver.br
            br.get(driver.baseURL)
            KWS_module.search(driver, 'Paper Fan')
            wait_element.wait_for_text_present(br, 'Paper Fan', 10, True)
        except:
            raise

    def test_list_page_02_Facets(self):
        'KWS - (List Page) - Verify facets (left nav) appear on subsubcategory pages and work well'
        try:
            driver = self.driver
            br = driver.br
            br.get(driver.baseURL + '/catalog/searchresults.aspx?search=wedding')
            wait_element.wait_for_element_display(br, 'id', 'chkFilter_top_category_0', 10, True)
            br.find_element_by_xpath('//span[contains(text(),"reception")]').click()
            time.sleep(2)
            self.assertEqual(driver.br.current_url, driver.baseURL + '/catalog/searchresults.aspx?search=wedding&top_category=reception', 'did not redirect to the correct URL')
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
