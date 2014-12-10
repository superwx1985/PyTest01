'''
Created on 2014年11月11日

@author: viwang
'''
# -*- coding: utf-8 -*-
# from selenium import webdriver
import time, datetime

#===========================================================================
# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"
#===========================================================================


def wait_for_text_present(br, text, time_):
    if not isinstance(text, str):
        raise Exception('Invalid locater')
    br.implicitly_wait(1)
    for i in range(0, time_):
        time.sleep(1)
        elements = br.find_elements_by_xpath('//*[contains(text(),"' + text + '")]')
        # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), '%rs: %r presented' %(i,len(elements)))
        if len(elements) > 0:
            break
    br.implicitly_wait(10)
    return elements

def wait_for_element_present(br, by, value, time_):
    br.implicitly_wait(1)
    for i in range(0, time_):
        time.sleep(1)
        elements = br.find_elements(by, value)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'wait_for_element_present %rs: %r presented' % (i, len(elements)))
        if len(elements) > 0:
            break
    br.implicitly_wait(10)
    return elements

def wait_for_element_disappear(br, by, value, time_):
    br.implicitly_wait(1)
    for i in range(0, time_):
        time.sleep(1)
        elements = br.find_elements(by, value)
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'wait_for_element_disappear %rs: %r presented' % (i, len(elements)))
        if len(elements) == 0:
            break
    br.implicitly_wait(10)
    return elements

def verification_text_present(br, text, time_):
    elements = wait_for_text_present(br, text, time_)
    assert(len(elements) > 0), 'No such text'
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'text "%s" is present' % text)

def verification_element_present(br, by, value, time_):
    elements = wait_for_element_present(br, by, value, time_)
    assert(len(elements) > 0), 'No such element'
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'element "%s: %s" is present' % (by, value))
    
if __name__ == '__main__':
    pass
