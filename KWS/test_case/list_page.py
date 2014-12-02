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
         
    def test_Search_Bar(self):
        'KWS - (List Page) - Verify the search result returned is related to search condition.'
        try:
            driver = self.driver
            driver.br.get(driver.baseURL)
            KWS_module.search(driver, 'Paper Fan')
            verification.verification_text_present(driver, 'Paper Fan')
        except:
            raise

    def test_Facets(self):
        'KWS - (List Page) - Verify facets (left nav) appear on subsubcategory pages and work well'
        try:
            driver = self.driver
            driver.br.get(driver.baseURL + '/catalog/searchresults.aspx?search=wedding')
            verification.verification_element_present(driver, css='label[title="Click to filter results"]')
            driver.br.find_element_by_xpath('//span[contains(text(),"reception")]').click()
            time.sleep(2)
            self.assertEqual(driver.br.current_url, driver.baseURL + '/catalog/searchresults.aspx?search=wedding&top_category=reception', 'did not redirect to the correct URL')
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
