# -*- coding: utf-8 -*-
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time, threading, unittest


chromeoption1 = webdriver.ChromeOptions()
chromeoption1._arguments = ['test-type', "start-maximized", "no-default-browser-check"]
ff_profile = 'C:\\Users\\viwang\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\yj7r4nzk.tester'

br=webdriver.Chrome(chrome_options=chromeoption1)
#br = webdriver.Firefox(firefox_profile=webdriver.FirefoxProfile(ff_profile))
#br=webdriver.Remote(command_executor='http://172.25.20.19:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
br.maximize_window()
br.get('https://weddingshop.theknot.com/personalized-napkins-beverage.aspx')

br.find_element_by_css_selector(':not(#ctl00_MainContentArea_ctl00_ctl00_ctl00_btn_AddToCart)>#ctl00_MainContentArea_ctl00_ctl00_ctl00_addToCartPersonalized.btn.btn-primary').click()
br.find_element_by_css_selector('#persaccordion>div:nth-of-type(2) h2>a').click()
#br.find_element_by_id('Napkin Colors').click()
#time.sleep(1)
#===============================================================================
# br.find_element_by_css_selector('[value="MATE 90088 N PLM 254"]').click()
# time.sleep(1)
# br.find_element_by_css_selector('#persaccordion>div:nth-of-type(5) h2>a').click()
# time.sleep(1)
# br.find_element_by_id('Line 1').send_keys('Line1')
# br.find_element_by_css_selector('#persaccordion>div:nth-of-type(6) h2>a').click()
# time.sleep(10)
#===============================================================================

value = br.find_element_by_css_selector('#PersonalizationImage').text()

print(value)

    
input('finished')
    
br.close()
