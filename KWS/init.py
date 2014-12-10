'''
Created on 2014年12月10日

@author: viwang
'''
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

ff_profile = 'C:\\Users\\viwang\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\yj7r4nzk.tester'
chromeoption1 = webdriver.ChromeOptions()
chromeoption1._arguments = ['test-type', "start-maximized", "no-default-browser-check"]
#ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4'
#chromeoption1.add_argument('--user-agent='+ua);

class Driver(object):
    def __init__(self, environment, browser):
        self.environment = environment
        self.browser = browser
        if self.environment == 1: 
            self.baseURL = 'https://qa.weddingshop.theknot.com'
        elif self.environment == 2:
            self.baseURL = 'https://stg.weddingshop.theknot.com'
        elif self.environment == 3:
            self.baseURL = 'https://weddingshop.theknot.com'
        else:
            print('no such environment, please check your setting')
            exit()
        if self.browser == 1:
            self.br = webdriver.Ie()
            self.br.maximize_window()
        elif self.browser == 2:
            self.br = webdriver.Firefox(firefox_profile=webdriver.FirefoxProfile(ff_profile))
            self.br.maximize_window()
        elif self.browser == 3:
            self.br = webdriver.Chrome(chrome_options=chromeoption1)
        elif self.browser == 4:
            self.br = webdriver.Remote(command_executor='http://172.25.20.19:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
            self.br.maximize_window()
        elif self.browser == 5:
            self.br = webdriver.Remote(command_executor='http://172.26.11.121:4444/wd/hub', desired_capabilities=DesiredCapabilities.SAFARI)
        elif self.browser == 6:
            self.br = webdriver.Remote(command_executor='http://172.25.20.19:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
            self.br.maximize_window()
        elif self.browser == 7:
            self.br = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
            self.br.maximize_window()
        elif self.browser == 8:
            self.br = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
            self.br.maximize_window()
        else:
            print('no such driver, please check your setting')
            exit()  
        self.br.implicitly_wait(10)
