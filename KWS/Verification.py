'''
Created on 2014年11月11日

@author: viwang
'''
# -*- coding: utf-8 -*-
# from selenium import webdriver

def find_text(driver, text):
    if not isinstance(text, str):
        raise Exception('Invalid locater')
    elements = driver.br.find_elements_by_xpath('//*[contains(text(),"' + text + '")]')
    return elements

def verification_text_present(driver, text):
    elements = find_text(driver, text)
    assert(len(elements) > 0), 'No such text'
    
def find_elements(driver, ID=None, name=None, classname=None, css=None, xpath=None):
    if isinstance(ID, str):
        elements = driver.br.find_elements_by_id(ID)
    elif isinstance(name, str):
        elements = driver.br.find_elements_by_name(name)
    elif isinstance(classname, str):
        elements = driver.br.find_elements_by_class_name(classname)
    elif isinstance(css, str):
        elements = driver.br.find_elements_by_css_selector(css)
    elif isinstance(xpath, str):
        elements = driver.br.find_elements_by_xpath(xpath)
    else:
        raise Exception('Invalid locater')
    return elements

def verification_element_present(driver, ID=None, name=None, classname=None, css=None, xpath=None):
    elements = find_elements(driver, ID, name, classname, css, xpath)
    assert(len(elements) > 0), 'No such element'

