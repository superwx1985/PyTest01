'''
Created on 2014年12月10日

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, unittest, datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from KWS.test_case.public import KWS_module
from KWS import verification
from KWS import init
from KWS.my_test_case import MyTestCase
from selenium.webdriver.common.action_chains import ActionChains
from KWS import import_test_data

class MyTest(MyTestCase):
    
    def setUp(self):
        # self.environment = 1
        # self.browser = 3
        self.driver = init.Driver(self.environment, self.browser)
        # self.err = []
        print('\nenvironment=%s, browser=%s' % (self.environment, self.browser))
         
    def test_personalization_image(self):
        'KWS - (Product Page) - Verify when I select options or input text, I should see a live Scene7 rendering of my selections.'
        try:
            driver = self.driver
            br = driver.br
            br.get(driver.baseURL + '/personalized-napkins-beverage.aspx')
            time.sleep(1)
            br.find_element_by_css_selector('div.prod-buttons.text-center.btn-group-lg button').click()
            verification.wait_for_element_present(br,'css selector','div#persCollapse1 a[data-color-swatch-js-safe-value="I Do"] img',10)
            verification.wait_for_element_disappear(br,'css selector','#theknot.busydiv',10)
            WebDriverWait(br,30).until(lambda x: x.find_element_by_css_selector('div#persCollapse1 a[data-color-swatch-js-safe-value="I Do"] img').is_displayed())
            br.find_element_by_css_selector('div#persCollapse1 a[data-color-swatch-js-safe-value="I Do"] img').click()
            br.find_element_by_css_selector('#persaccordion>div:nth-of-type(2) h2>a').click()
            WebDriverWait(br,30).until(lambda x: x.find_element_by_css_selector('div#persCollapse2 a[data-color-swatch-js-safe-value="Grass"] img').is_displayed())
            br.find_element_by_css_selector('div#persCollapse2 a[data-color-swatch-js-safe-value="Grass"] img').click()
            br.find_element_by_css_selector('#persaccordion>div:nth-of-type(3) h2>a').click()
            WebDriverWait(br,30).until(lambda x: x.find_element_by_css_selector('div#persCollapse3 a[data-color-swatch-js-safe-value="Black"] img').is_displayed())
            br.find_element_by_css_selector('div#persCollapse3 a[data-color-swatch-js-safe-value="Black"] img').click()
            br.find_element_by_css_selector('#persaccordion>div:nth-of-type(4) h2>a').click()
            WebDriverWait(br,30).until(lambda x: x.find_element_by_css_selector('div#persCollapse4 a[data-color-swatch-js-safe-value="Classic"] img').is_displayed())
            br.find_element_by_css_selector('div#persCollapse4 a[data-color-swatch-js-safe-value="Classic"] img').click()
            br.find_element_by_css_selector('#persaccordion>div:nth-of-type(5) h2>a').click()
            WebDriverWait(br,30).until(lambda x: x.find_element_by_css_selector('input[id="Line 1"]').is_displayed())
            br.find_element_by_css_selector('input[id="Line 1"]').clear()
            br.find_element_by_css_selector('input[id="Line 1"]').send_keys('Line 1')
            br.find_element_by_css_selector('input[id="Line 2"]').clear()
            br.find_element_by_css_selector('input[id="Line 2"]').send_keys('Line 2')
            br.find_element_by_css_selector('#persaccordion>div:nth-of-type(6) h2>a').click()
            WebDriverWait(br,30).until(lambda x: x.find_element_by_css_selector('input#PersonalizationQuantity').is_displayed())
            br.find_element_by_css_selector('input#PersonalizationQuantity').click()
            #verification.wait_for_element_present(br,'css selector','#theknot.busydiv',10)
            js = 'document.getElementById("tk_modal_personalization_container").scrollTop=100'
            br.execute_script(js)
            verification.wait_for_element_disappear(br,'css selector','#theknot.busydiv',10)

        except:
            raise

    def atest_02(self):
        '02'
        try:
            driver = self.driver
            br = driver.br
           
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
    # suppresses a superfluous ResourceWarning which was being emitted at the time of writing.  It may have disappeared by the time you read this; feel free to try removing it!
