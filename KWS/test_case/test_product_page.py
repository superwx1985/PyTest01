'''
Created on 2014年12月10日

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
        'KWS - (Product Page) - Verify when I select options or input text, I should see a live Scene7 rendering of my selections.'
        try:
            driver = self.driver
            br = driver.br
            br.get(driver.baseURL + '/personalized-napkins-beverage.aspx')
            time.sleep(1)
            KWS_module.click_personalized_button(driver)
            wait_element.wait_for_element_disappear(br, 'id', 'theknot.busydiv', 10)
            wait_element.try_to_click(br, 'css selector', 'div#persCollapse1 a[data-color-swatch-js-safe-value="I Do"] img', 3)
            KWS_module.click_header_in_personalization_modal(driver, 2)
            wait_element.try_to_click(br, 'css selector', 'div#persCollapse2 a[data-color-swatch-js-safe-value="Grass"] img', 3)
            KWS_module.click_header_in_personalization_modal(driver, 3)
            wait_element.try_to_click(br, 'css selector', 'div#persCollapse3 a[data-color-swatch-js-safe-value="Black"] img', 3)
            KWS_module.click_header_in_personalization_modal(driver, 5)
            wait_element.try_to_enter(br, 'css selector', 'input[id="Line 1"]', 3, 'Line 1')
            wait_element.try_to_enter(br, 'css selector', 'input[id="Line 2"]', 3, 'Line 2')
            KWS_module.click_header_in_personalization_modal(driver, 4)
            wait_element.try_to_click(br, 'css selector', 'div#persCollapse4 a[data-color-swatch-js-safe-value="Classic"] img', 3)
            KWS_module.click_header_in_personalization_modal(driver, 6)
            wait_element.try_to_enter(br, 'css selector', 'input#PersonalizationQuantity', 3, '2')
            js = 'document.getElementById("tk_modal_personalization_container").scrollTop=100'
            br.execute_script(js)
            wait_element.wait_for_element_disappear(br, 'css selector', '#theknot.busydiv', 10)
            wait_element.wait_for_element_visible(br, 'xpath', '//img[@src="//theknot.scene7.com/is/image/TheKnot?src=ir{TheKnotRender/11518?&obj=imprint&color=82b741&decal&pos=-.1,-1.2&src=ir{TheKnotRender/foil?obj=foil&decal&src=is{TheKnot/MAIN?&$IMGsrc=i_do&$IMGsize=500,500&$font1=Galaxie Copernicus&$phrase1=Line 1&$phrase2=Line 2&$phrase1fs=108&$phrase2fs=108}&show&res=150&illum=1&color=000000&req=object}&res=300}&$400px$"]', 5, True)
        except:
            raise

    def test_02(self):
        'KWS - (Product Page) - Verify personalization details should be passed to my shopping cart.'
        try:
            driver = self.driver
            br = driver.br
            br.get(driver.baseURL + '/colorblock-tote.aspx')
            time.sleep(1)
            KWS_module.select_option(driver, 0, 'Black')
            KWS_module.click_personalized_button_optional(driver)
            KWS_module.click_header_in_personalization_modal(driver, 2)
            wait_element.try_to_enter(br, 'id', 'Initial', 3, 'X')
            KWS_module.click_header_in_personalization_modal(driver, 3)
            wait_element.try_to_click(br, 'css selector', 'div#persCollapse3 a[data-color-swatch-js-safe-value="White"] img', 3)
            KWS_module.click_header_in_personalization_modal(driver, 4)
            wait_element.try_to_click(br, 'css selector', 'div#persCollapse4 a[data-color-swatch-js-safe-value="Red"] img', 3)
            KWS_module.click_header_in_personalization_modal(driver, 5)
            wait_element.try_to_enter(br, 'css selector', 'input#PersonalizationQuantity', 3, '1')
            KWS_module.click_save_button_in_personalization_modal(driver)
            # wait_element.wait_for_element_visible(br, 'css selector', 'div.panel.cart.panel-default', 10)
            br.get(driver.baseURL + '/cart/shoppingcart.aspx')
            wait_element.wait_for_element_visible(br, 'xpath', '//div[@class="olr" and text()="Black"]', 3, True)
            wait_element.wait_for_element_visible(br, 'xpath', '//ul/li[contains(text(),"Initial") and contains(text(),"X")]', 3, True)
            wait_element.wait_for_element_visible(br, 'xpath', '//ul/li[contains(text(),"Inside Thread Color:") and contains(text(),"White")]', 3, True)
            wait_element.wait_for_element_visible(br, 'xpath', '//ul/li[contains(text(),"Outside Thread Color:") and contains(text(),"Red")]', 3, True)

            time.sleep(5)
        except:
            raise
            
    def tearDown(self):
        init.tearDown(self.driver)
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
    # suppresses a superfluous ResourceWarning which was being emitted at the time of writing.  It may have disappeared by the time you read this; feel free to try removing it!
