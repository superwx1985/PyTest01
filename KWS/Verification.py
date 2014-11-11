'''
Created on 2014年11月11日

@author: viwang
'''
# -*- coding: utf-8 -*-
#from selenium import webdriver


def verification_text_persent(driver, kw):
    try:
        driver.br.find_element_by_xpath('//*[contains(text(),"'+kw+'")]')
        return True
    except:
        raise


