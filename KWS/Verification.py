'''
Created on 2014年11月11日

@author: viwang
'''
# -*- coding: utf-8 -*-
# from selenium import webdriver

def verification_text_persent(driver, kw):
    elements = driver.br.find_elements_by_xpath('//*[contains(text(),"' + kw + '")]')
    return elements

def verification_element_persent(driver, id=None, name=None, classname=None, css=None, xpath=None):
    if id != None:
        elements = driver.br.find_elements_by_id(id)
    elif name != None:
        elements = driver.br.find_elements_by_name(name)
    elif classname != None:
        elements = driver.br.find_elements_by_class_name(classname)
    elif css != None:
        elements = driver.br.find_elements_by_css_selector(css)
    elif xpath != None:
        elements = driver.br.find_elements_by_xpath(xpath)
    return elements



