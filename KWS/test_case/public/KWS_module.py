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

def go_to_homepage(driver):
    driver.br.get(driver.baseURL)

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

def shopping_cart_checkout_as_guest(driver, address=1):
    wait_element.try_to_click(driver.br, 'xpath', '//button[contains(text(),"PROCEED TO CHECKOUT")]', 10)
    wait_element.try_to_click(driver.br, 'id', 'divCheckoutAsGuestButton', 10)
    fill_address_in_address_modal(driver, address)
    if driver.browser == 5:
        input('please accept the alert on the test driver, then press any key to continue')
    elif driver.browser == 0:
        driver.br.switch_to_alert().accept()

def shopping_cart_checkout_as_user(driver, user=1, address=1):
    wait_element.try_to_click(driver.br, 'xpath', '//button[contains(text(),"PROCEED TO CHECKOUT")]', 10)
    fill_account_in_login_modal(driver, user)
    fill_address_in_address_modal(driver, address)
    if driver.browser == 5:
        input('please accept the alert on the test driver, then press any key to continue')
    elif driver.browser == 0:
        # driver.br.get('javascript:document.getElementById("overridelink").click();')
        driver.br.switch_to_alert().accept()

def checkout_via_credit_card(driver, ccinfo=1):
    wait_element.wait_for_element_visible(driver.br, 'xpath', '//p[text()="Total:"]', 30)
    #WebDriverWait(driver.br, 60).until(lambda x: x.find_element_by_xpath('//p[text()="Total:"]').is_displayed())
    wait_element.wait_for_element_disappear(driver.br, 'id', 'data_loading', 30)
    #WebDriverWait(driver.br, 60).until_not(lambda x: x.find_element_by_id('data_loading').is_displayed())
    #time.sleep(1)
    data = import_test_data.get_csv_data('D:/viwang/workspace/PyTest01/KWS/test_data/CC info.csv')
    wait_element.try_to_enter(driver.br, 'id', 'ccNumber', 5, data[ccinfo][1])
    wait_element.try_to_enter(driver.br, 'id', 'ccName', 5, data[ccinfo][2])
    wait_element.try_to_enter(driver.br, 'name', 'ccv', 5, data[ccinfo][3])
    wait_element.try_to_click(driver.br, 'xpath', '//select[@id="ccExpMonth"]/option[@value="' + data[ccinfo][4] + '"]', 5)
    wait_element.try_to_click(driver.br, 'xpath', '//select[@name="expYear"]/option[@value="' + data[ccinfo][5] + '"]', 5)
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
            wait_element.try_to_enter(driver.br, 'id', 'login_email', 5, 'lyi@xogrp.com')
            wait_element.try_to_enter(driver.br, 'id', 'login_password', 5, 'testtest')
            wait_element.try_to_click(driver.br, 'id', 'submitLogin', 5)
            wait_element.try_to_click(driver.br, 'id', 'continue', 5)
            break
        elif element.get_attribute('id') == 'email':
            wait_element.try_to_enter(driver.br, 'id', 'email', 5, 'lyi@xogrp.com')
            wait_element.try_to_enter(driver.br, 'id', 'password', 5, 'testtest')
            wait_element.try_to_click(driver.br, 'css selector', '.btn.full.continue')
            wait_element.try_to_click(driver.br, 'id', 'confirmButtonTop', 5)
            break
    time.sleep(10)
    try:
        print('alert present >>>\n%s' % driver.br.switch_to_alert().text)
        driver.br.switch_to_alert().accept()
        print('accept alert')
    except Exception as err:
        print('no alert open >>>\n%s' % err)
    WebDriverWait(driver.br, 60).until(lambda x: x.find_element_by_xpath('//p[text()="Total:"]').is_displayed())
    WebDriverWait(driver.br, 60).until_not(lambda x: x.find_element_by_id('data_loading').is_displayed())
    #time.sleep(3)
    submit_button = wait_element.wait_for_element_visible(driver.br, 'xpath', '//button[contains(text(),"SUBMIT ORDER")]', 5)
    submit_button[random.randint(0, 1)].click()
    tracking_number = wait_element.wait_for_element_visible(driver.br, 'css selector', 'span.text-info.underline strong', 10)
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'paypal', tracking_number[0].text)
    

def checkout_via_amazon(driver):
    WebDriverWait(driver.br, 60).until(lambda x: x.find_element_by_xpath('//p[text()="Total:"]').is_displayed())
    WebDriverWait(driver.br, 60).until_not(lambda x: x.find_element_by_id('data_loading').is_displayed())
    time.sleep(3)
    nowwindow = driver.br.current_window_handle
    wait_element.try_to_click(driver.br, 'css selector', '#payWithAmazon img', 5)
    time.sleep(10)
    allwindow = driver.br.window_handles
    for x in allwindow:
        if x == nowwindow:
            continue
        driver.br.switch_to_window(x)
        if driver.br.title == 'Amazon Payments: Sign In':
            break
    wait_element.try_to_enter(driver.br, 'id', 'ap_email', 5, 'viwang@xogrp.com')
    wait_element.try_to_enter(driver.br, 'id', 'ap_password', 5, 'testtest')
    wait_element.try_to_click(driver.br, 'id', 'signInSubmit', 5)
    driver.br.switch_to_window(nowwindow)
    WebDriverWait(driver.br, 60).until(lambda x: x.find_element_by_css_selector('.btn.btn-default').is_displayed())
    time.sleep(3)
    WebDriverWait(driver.br, 60).until(lambda x: x.find_element_by_xpath('//p[text()="Total:"]').is_displayed())
    WebDriverWait(driver.br, 60).until_not(lambda x: x.find_element_by_id('data_loading').is_displayed())
    time.sleep(3)
    driver.br.find_element_by_css_selector('.buffer.text-right button').click()
    tracking_number = wait_element.wait_for_element_visible(driver.br, 'css selector', 'span.text-info.underline strong', 10)
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'amazon', tracking_number[0].text)

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
