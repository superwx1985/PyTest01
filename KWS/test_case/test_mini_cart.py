'''
Created on 2014年12月12日

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, unittest, datetime, wait_element
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from KWS.test_case.public import KWS_module
from KWS import init
from KWS.my_test_case import MyTestCase
from selenium.webdriver.common.action_chains import ActionChains
from KWS import import_test_data

class MyTest(MyTestCase):
    
    def setUp(self):
        #self.environment = 3
        #self.browser = 2
        self.driver = init.Driver(self.environment, self.browser)
        # self.err = []
        print('\nenvironment=%s, browser=%s' % (self.environment, self.browser))
         
    def test_01_mini_cart_show_details(self):
        'KWS - (Mini Cart) - Verify product details should be shown on mini cart'
        try:
            driver = self.driver
            br = driver.br
            br.get(driver.baseURL + '/crystal-bride-tee.aspx')
            time.sleep(1)
            KWS_module.select_option(driver, 0, 'Green')
            KWS_module.select_option(driver, 1, '2X-Large')
            KWS_module.select_option(driver, 2, 'Loose-fit Tee')
            KWS_module.click_add_button(driver)
            #wait_element.wait_for_element_visible(br, 'css selector', 'div.panel.cart.panel-default', 10)
            wait_element.wait_for_element_visible(br, 'xpath', '//div[@class="panel-body"]/div/div[@id="divFlyDescription"]//a[text()="Crystal Bride Tee"]/../../..//div[contains(text(),"Green") and contains(text(),"2X-Large") and contains(text(),"Loose-fit Tee")]', 5, True)
        except:
            raise

    def test_02_mini_cart_checkout(self):
        'KWS - (Mini Cart) - Verify user can checkout via mini cart'
        try:
            driver = self.driver
            br = driver.br
            br.get(driver.baseURL + '/paddle-fan.aspx')
            time.sleep(1)
            KWS_module.select_option(driver, 0, 'Brown')
            KWS_module.click_add_button(driver)
            KWS_module.click_checkout_button_in_mini_cart(driver)
            KWS_module.fill_account_in_login_modal(driver)
            KWS_module.fill_address_in_address_modal(driver)
            wait_element.wait_for_page_redirect(br, 'https://qa.weddingshop.theknot.com/co/index.html', 30, True)
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