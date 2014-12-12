'''
Created on 2014年9月10日

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, random, datetime, wait_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from KWS import import_test_data


def login_in_header(driver, data_id=1):
    wait_element.try_to_click(driver.br, 'id', 'lnkLogin', 5)
    fill_account_in_login_modal(driver, data_id)

def fill_account_in_login_modal(driver, data_id=1):
    data = import_test_data.get_csv_data('D:/viwang/workspace/PyTest01/KWS/test_data/KWS account.csv')
    # print('%s/%s' % (data[data_id][1], data[data_id][2]))
    wait_element.try_to_enter(driver.br, 'id', 'txtUsername', 5, data[data_id][1])
    wait_element.try_to_enter(driver.br, 'id', 'txtPassword', 5, data[data_id][2])
    wait_element.try_to_click(driver.br, 'id', 'divLoginButton', 5)
    # print(driver.br.title)
    # print(driver.br.current_url)
    # print(driver.br.find_element_by_id('lnkMyAccount').text)

def fill_address_in_address_modal(driver, data_id=1):
    wait_element.wait_for_element_visible(driver.br, 'id', 'mybillshipModalLabel', 30)
    if not(driver.br.find_element_by_id('chkOneAddress').is_selected()):
        wait_element.try_to_click(driver.br, 'css selector', '#chkOneAddress+label', 5)
    if driver.br.find_element_by_id('CAMCheckbox1').is_selected():
        wait_element.try_to_click(driver.br, 'css selector', '#CAMCheckbox1+label', 5)
    data = import_test_data.get_csv_data('D:/viwang/workspace/PyTest01/KWS/test_data/address.csv')
    # print('%s/%s/%s/%s/%s/%s/%s/%s/%s/%s' % (data[data_id][0], data[data_id][1], data[data_id][2], data[data_id][3], data[data_id][4], data[data_id][5], data[data_id][6], data[data_id][7], data[data_id][8], data[data_id][9]))
    wait_element.try_to_enter(driver.br, 'xpath', '//div[@id="tkBillingAddress"]//input[@name="FirstName"]', 5, data[data_id][1])
    wait_element.try_to_enter(driver.br, 'xpath', '//div[@id="tkBillingAddress"]//input[@name="LastName"]', 5, data[data_id][2])
    wait_element.try_to_enter(driver.br, 'xpath', '//div[@id="tkBillingAddress"]//input[@name="Email"]', 5, data[data_id][3])
    wait_element.try_to_enter(driver.br, 'xpath', '//div[@id="tkBillingAddress"]//input[@name="Address1"]', 5, data[data_id][4])
    wait_element.try_to_enter(driver.br, 'xpath', '//div[@id="tkBillingAddress"]//input[@name="Address2"]', 5, data[data_id][5])
    wait_element.try_to_enter(driver.br, 'xpath', '//div[@id="tkBillingAddress"]//input[@name="City"]', 5, data[data_id][6])
    wait_element.try_to_enter(driver.br, 'xpath', '//div[@id="tkBillingAddress"]//input[@name="State"]', 5, data[data_id][7])
    wait_element.try_to_enter(driver.br, 'xpath', '//div[@id="tkBillingAddress"]//input[@name="ZipCode"]', 5, data[data_id][8])
    wait_element.try_to_enter(driver.br, 'xpath', '//div[@id="tkBillingAddress"]//input[@name="Phone"]', 5, data[data_id][9])
    wait_element.try_to_click(driver.br, 'id', 'SaveAndContinue', 5)

def change_quantity(driver, quantity=10):
    while True:
        if driver.br.find_element_by_id('ctl00_MainContentArea_ctl00_ctl00_ctl00_txtQty').is_displayed():
            break
        else:
            wait_element.try_to_click(driver.br, 'xpath', '//a[contains(text(),"QUANTITY")]', 5)
            time.sleep(1)
    wait_element.try_to_enter(driver.br, 'id', 'ctl00_MainContentArea_ctl00_ctl00_ctl00_txtQty', 5, quantity)    

def change_option(driver, value, option=0):
    while True:
        if driver.br.find_element_by_xpath('//select[@id="tkDropdown' + '0' + '"]').is_displayed():
            break
        else:
            driver.br.find_element_by_xpath('//a[contains(text(),"CHOOSE AN OPTION")]').click()
            time.sleep(2)
    # WebDriverWait(br, 2).until(lambda x: x.find_element_by_xpath('//select[@id="tkDropdown0"]').is_displayed())
    driver.br.find_element_by_xpath('//select[@id="tkDropdown' + str(option) + '"]').click()
    driver.br.find_element_by_xpath('//select[@id="tkDropdown' + str(option) + '"]/option[text()="' + value + '"]').click()
    

def add_product_paddle_fan_Brown(driver, quantity=10):
    driver.br.get(driver.baseURL + '/paddle-fan.aspx')
    change_quantity(driver, quantity)
    select_option(driver, 0, 'Brown')
    click_add_button(driver)

def add_product_beer(driver, quantity=10):
    driver.br.get(driver.baseURL + '/engravable-beer-mug.aspx')
    change_quantity(driver, quantity)
    while True:
        driver.br.find_elements('id', 'ctl00_MainContentArea_ctl00_ctl00_ctl00_addToCartPersonalized')[1].click()
        time.sleep(5)
        if driver.br.find_element_by_id('tk_modal_container').is_displayed():
            break
        else:
            driver.br.find_elements('id', 'ctl00_MainContentArea_ctl00_ctl00_ctl00_addToCartPersonalized')[1].click()
            time.sleep(5)
    # WebDriverWait(driver.br, 10).until(lambda x: x.find_element_by_id('tk_modal_container').is_displayed())
    # WebDriverWait(driver.br, 30).until_not(lambda x: x.find_element_by_id('spinner').is_displayed())
    WebDriverWait(driver.br, 10).until(lambda x: x.find_element_by_xpath('//a[@data-color-swatch-js-safe-value="Garamond"]/img').is_displayed())
    driver.br.find_element_by_xpath('//a[@data-color-swatch-js-safe-value="Garamond"]/img').click()
    driver.br.find_elements_by_class_name('steplabel')[1].click()
    time.sleep(2)
    driver.br.find_element_by_id('Line 1').clear()
    driver.br.find_element_by_id('Line 1').send_keys('Line 1')
    driver.br.find_element_by_id('Line 2').clear()
    driver.br.find_element_by_id('Line 2').send_keys('Line 2')
    # ActionChains(driver.br).context_click(driver.br.find_elements('class name','steplabel')[2]).perform() #点击右键
    time.sleep(1)
    # driver.br.find_element_by_id('tk_modal_container').click()
    driver.br.find_element_by_id('addFromPersonalizationModal').click()

def search(driver, kw):
    driver.br.find_element_by_id('ctl00_tkShared_Header_txtHeaderSearchBox').send_keys(kw)
    driver.br.find_element_by_css_selector('.tk_searchbtn.btn.btn-default').click()
    # driver.br.find_element_by_link_text('Engravable Beer Mug').click()

def shopping_cart_checkout_as_user(driver, data_id=1, data_id2=1):
    fill_account_in_login_modal(driver, data_id)
    fill_address_in_address_modal(driver, data_id2)
    if driver.browser == 5:
        input('please accept the alert on the test driver, then press any key to continue')
    elif driver.browser == 0:
        # driver.br.get('javascript:document.getElementById("overridelink").click();')
        driver.br.switch_to_alert().accept()


def shopping_cart_checkout_as_guest(driver, data_id=1):
    if 'shoppingcart.aspx' in driver.br.current_url:
        wait_element.try_to_click(driver.br, 'xpath', '//button[contains(text(),"PROCEED TO CHECKOUT")]', 10)
    wait_element.try_to_click(driver.br, 'id', 'divCheckoutAsGuestButton', 10)
    fill_address_in_address_modal(driver, data_id)
    if driver.browser == 5:
        input('please accept the alert on the test driver, then press any key to continue')
    elif driver.browser == 0:
        driver.br.switch_to_alert().accept()

def checkout_via_credit_card(driver, data_id=1):
    WebDriverWait(driver.br, 60).until(lambda x: x.find_element_by_xpath('//p[text()="Total:"]').is_displayed())
    WebDriverWait(driver.br, 60).until_not(lambda x: x.find_element_by_id('data_loading').is_displayed())
    time.sleep(1)
    data = import_test_data.get_csv_data('D:/viwang/workspace/PyTest01/KWS/test_data/CC info.csv')
    wait_element.try_to_enter(driver.br, 'id', 'ccNumber', 5, data[data_id][1])
    wait_element.try_to_enter(driver.br, 'id', 'ccName', 5, data[data_id][2])
    wait_element.try_to_enter(driver.br, 'name', 'ccv', 5, data[data_id][3])
    wait_element.try_to_click(driver.br, 'xpath', '//select[@id="ccExpMonth"]/option[@value="' + data[data_id][4] + '"]', 5)
    wait_element.try_to_click(driver.br, 'xpath', '//select[@name="expYear"]/option[@value="' + data[data_id][5] + '"]', 5)
    submit_button = wait_element.wait_for_element_visible(driver.br, 'xpath', '//button[contains(text(),"SUBMIT ORDER")]', 5)
    submit_button[random.randint(0, 1)].click()
    tracking_number = wait_element.wait_for_element_visible(driver.br, 'css selector', 'span.text-info.underline strong', 10)
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'cc', tracking_number[0].text)
        
def checkout_via_paypal(driver):
    WebDriverWait(driver.br, 60).until(lambda x: x.find_element_by_xpath('//p[text()="Total:"]').is_displayed())
    WebDriverWait(driver.br, 60).until_not(lambda x: x.find_element_by_id('data_loading').is_displayed())
    time.sleep(3)
    driver.br.find_element_by_css_selector('img[alt=Paypal]').click()
    WebDriverWait(driver.br, 60).until_not(lambda x: x.find_element_by_id('data_loading').is_displayed())
    time.sleep(3)
    while 'paypal' not in driver.br.current_url:
        driver.br.find_element_by_css_selector('img[alt=Paypal]').click()
        WebDriverWait(driver.br, 60).until_not(lambda x: x.find_element_by_id('data_loading').is_displayed())
        time.sleep(3)  
    elements = driver.br.find_elements_by_tag_name('input')
    for element in elements:
        if element.get_attribute('id') == 'login_email': 
            driver.br.find_element_by_id('login_email').clear()
            driver.br.find_element_by_id('login_email').send_keys('lyi@xogrp.com')
            driver.br.find_element_by_id('login_password').clear()
            driver.br.find_element_by_id('login_password').send_keys('testtest')
            time.sleep(1)
            driver.br.find_element_by_id('submitLogin').click()
            time.sleep(1)
            driver.br.find_element_by_id('continue').click()
            break
        elif element.get_attribute('id') == 'email':
            driver.br.find_element_by_id('email').clear()
            driver.br.find_element_by_id('email').send_keys('lyi@xogrp.com')
            driver.br.find_element_by_id('password').clear()
            driver.br.find_element_by_id('password').send_keys('testtest')
            time.sleep(1)
            driver.br.find_element_by_css_selector('.btn.full.continue').click()
            time.sleep(1)
            driver.br.find_element_by_id('confirmButtonTop').click()
            break
    time.sleep(10)
    try:
        print('alert present >>>\n%s' % driver.br.switch_to_alert().text)
        driver.br.switch_to_alert().accept()
        print('accept alert')
    except Exception as err:
        print('no alert present >>>\n%s' % err)
    WebDriverWait(driver.br, 60).until(lambda x: x.find_element_by_xpath('//p[text()="Total:"]').is_displayed())
    WebDriverWait(driver.br, 60).until_not(lambda x: x.find_element_by_id('data_loading').is_displayed())
    time.sleep(3)
    driver.br.find_elements_by_xpath('//button[contains(text(),"SUBMIT ORDER")]')[random.randint(0, 1)].click()
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'paypal', driver.br.find_element_by_css_selector('span.text-info.underline strong').text)
    

def checkout_via_amazon(driver):
    WebDriverWait(driver.br, 60).until(lambda x: x.find_element_by_xpath('//p[text()="Total:"]').is_displayed())
    WebDriverWait(driver.br, 60).until_not(lambda x: x.find_element_by_id('data_loading').is_displayed())
    time.sleep(3)
    nowwindow = driver.br.current_window_handle
    driver.br.find_element_by_css_selector('#payWithAmazon img').click()
    time.sleep(10)
    allwindow = driver.br.window_handles
    for x in allwindow:
        if x == nowwindow:
            continue
        driver.br.switch_to_window(x)
        if driver.br.title == 'Amazon Payments: Sign In':
            break
    driver.br.find_element_by_id('ap_email').clear()
    driver.br.find_element_by_id('ap_email').send_keys('viwang@xogrp.com')
    driver.br.find_element_by_id('ap_password').clear()
    driver.br.find_element_by_id('ap_password').send_keys('testtest')
    driver.br.find_element_by_id('signInSubmit').click()
    driver.br.switch_to_window(nowwindow)
    WebDriverWait(driver.br, 60).until(lambda x: x.find_element_by_css_selector('.btn.btn-default').is_displayed())
    time.sleep(3)
    WebDriverWait(driver.br, 60).until(lambda x: x.find_element_by_xpath('//p[text()="Total:"]').is_displayed())
    WebDriverWait(driver.br, 60).until_not(lambda x: x.find_element_by_id('data_loading').is_displayed())
    time.sleep(3)
    driver.br.find_element_by_css_selector('.buffer.text-right button').click()
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'Amazon', driver.br.find_element_by_css_selector('span.text-info.underline strong').text)

def click_add_button(driver):
    driver.br.find_element_by_id('ctl00_MainContentArea_ctl00_ctl00_ctl00_addToCart').click()
    
def click_personalized_button(driver):
    wait_element.try_to_click(driver.br, 'css selector', 'div.prod-buttons.text-center.btn-group-lg button', 5)
    wait_element.wait_for_element_visible(driver.br, 'id', 'tk_modal_personalization_container', 5)

def click_add_button_optional(driver):
    wait_element.try_to_click(driver.br, 'id', 'ctl00_MainContentArea_ctl00_ctl00_ctl00_addWithoutPersonalization', 5)

def click_personalized_button_optional(driver):
    wait_element.try_to_click(driver.br, 'css selector', 'div.prod-buttons.text-center.btn-group-lg button#ctl00_MainContentArea_ctl00_ctl00_ctl00_addToCartPersonalized', 10)
    wait_element.wait_for_element_visible(driver.br, 'id', 'tk_modal_personalization_container', 5)

def click_header_in_personalization_modal(driver, number):
    wait_element.try_to_click(driver.br, 'css selector', '#persaccordion>div:nth-of-type(' + str(number) + ') h2>a', 5)

def select_option(driver, number, option):
    wait_element.try_to_click(driver.br, 'xpath', '//select[@id="tkDropdown' + str(number) + '"]/option[text()="' + str(option) + '"]', 5)
    
def click_save_button_in_personalization_modal(driver):
    wait_element.try_to_click(driver.br, 'id', 'addFromPersonalizationModal', 5)
    
def click_checkout_button_in_mini_cart(driver):
    wait_element.wait_for_element_visible(driver.br, 'css selector', 'div.panel.cart.panel-default', 10)
    wait_element.try_to_click(driver.br, 'id', 'checkoutbtn', 5)
