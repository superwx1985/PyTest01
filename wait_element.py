'''
Created on 2014年11月11日

@author: viwang
'''
# -*- coding: utf-8 -*-
# from selenium import webdriver
import time, datetime
from selenium.common import exceptions
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


def wait_for_text_present(dr, text, time_, print_=False):
    if not isinstance(text, str):
        raise TypeError('invalid locater')
    dr.implicitly_wait(1)
    elements = []
    for i in range(0, time_):
        time.sleep(1)
        elements = dr.find_elements_by_xpath('//*[contains(text(),"' + text + '")]')
        if print_:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'waiting for [%s] present... %rs: %r present' % (text, i, len(elements)))
        if len(elements) > 0:
            break
    dr.implicitly_wait(10)
    assert(len(elements) > 0), 'no such text ==> "' + text + '"'
    if print_:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'text [%s] presented' % text)
    return elements


def wait_for_element_present(dr, by, value, time_, print_=False):
    elements = []
    dr.implicitly_wait(1)
    for i in range(0, time_):
        time.sleep(1)
        elements = dr.find_elements(by, value)
        if print_:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'waiting for [%s|%s] present... %rs: %r' % (by, value, i, len(elements)))
        if len(elements) > 0:
            break
    dr.implicitly_wait(10)
    assert(len(elements) > 0), 'no such element'
    if print_:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'element [%s|%s] presented' % (by, value))
    return elements

def wait_for_element_visible(dr, by, value, time_, print_=False):
    elements = []
    visible_elements = []
    dr.implicitly_wait(1)
    
    for i in range(0, time_):
        time.sleep(1)
        elements = dr.find_elements(by, value)
        if len(elements) > 0:
            for element in elements:
                if element.is_displayed():
                    visible_elements.append(element)
        if print_:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'waiting for [%s|%s] display... %rs: %r/%r' % (by, value, i, len(visible_elements), len(elements)))
        if len(visible_elements) > 0:
            break
    dr.implicitly_wait(10)
    assert(len(elements) > 0), 'no such element'
    assert(len(visible_elements) > 0), 'the element is invisible'
    if print_:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'element [%s|%s] displayed' % (by, value))
    return visible_elements

def wait_for_element_disappear(dr, by, value, time_, print_=False):
    elements = []
    visible_elements = []
    dr.implicitly_wait(1)
    for i in range(0, time_):
        time.sleep(1)
        elements = dr.find_elements(by, value)
        if print_:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'waiting for [%s|%s] disappear... %rs: %r/%r' % (by, value, i, len(visible_elements), len(elements)))
        if len(elements) == 0:
            break
        else:
            for element in elements:
                if element.is_displayed():
                    visible_elements.append(element)
            if len(visible_elements) == 0:
                break
    dr.implicitly_wait(10)
    assert(len(visible_elements) == 0), 'element has not disappeared '
    if print_:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'element [%s|%s] disappeared' % (by, value))
    return visible_elements

def try_to_click(dr, by, value, time_):
    elements = wait_for_element_visible(dr, by, value, time_)
    if len(elements) > 1:
        raise exceptions.ElementNotSelectableException('mutliple elements found')
    else:
        elements[0].click()

def try_to_enter(dr, by, value, time_, text):
    elements = wait_for_element_visible(dr, by, value, time_)
    if len(elements) > 1:
        raise exceptions.ElementNotSelectableException('mutliple elements found')
    else:
        elements[0].clear()
        elements[0].send_keys(text)

def wait_for_page_redirect(dr, new_url, time_, print_=False, old_url=None):
    if old_url is None:
        old_url = dr.current_url
    for i in range(0, time_):
        if print_:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'waiting for [%s] redirected... %rs' % (new_url, i))
        if new_url == dr.current_url:
            break
        time.sleep(1)
    assert(new_url == dr.current_url), 'redirect failed'
    if print_:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'redirected to [%s]' % (new_url))
    return new_url
        

if __name__ == '__main__':
    pass
