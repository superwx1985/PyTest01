# -*- coding: utf-8 -*-
import time, KWS_module, threading, unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

print(time.strftime('%Y-%m-%d %H:%M:%S'), 'start')
environment = 1  # 1=qa, 2=stg, 3=live
browser = 4  # 1=ie, 2=ff, 3=chrome, 4=remote_chrome, 5=remote_mac, 6=remote_ff
# br = KWS_module.setup(environment, browser)

if False:
    br = webdriver.Firefox()
    br.get(KWS_module.baseURL)

def c1(environment, browser):
    driver = KWS_module.Driver(environment, browser)
    print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'case 1 start')
    KWS_module.KWS_add_product_beer(driver, 2)
    KWS_module.KWS_go_to_shopping_cart_via_cart_flyout(driver)
    KWS_module.KWS_shopping_cart_checkout_as_guest(driver)
    KWS_module.KWS_checkout_via_credit_card(driver)
    input(time.strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(threading.currentThread()) + ' ' + 'case 1 has finished, press any key to continue\n')
    driver.br.quit()
    
    
def c2(environment, browser):
    driver = KWS_module.Driver(environment, browser)
    print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'case 2 start')
    KWS_module.KWS_add_product_paddle_fan(driver, 7)
    KWS_module.KWS_go_to_shopping_cart_via_cart_flyout(driver)
    KWS_module.KWS_shopping_cart_checkout_as_user(driver)
    KWS_module.KWS_checkout_via_credit_card(driver)
    input(time.strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(threading.currentThread()) + ' ' + 'case 2 has finished, press any key to continue\n')
    driver.br.quit()
    
    
def c3(environment, browser):
    driver = KWS_module.Driver(environment, browser)
    print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'case 3 start')
    KWS_module.KWS_add_product_beer(driver, 2)
    KWS_module.KWS_go_to_shopping_cart_via_cart_flyout(driver)
    KWS_module.KWS_shopping_cart_checkout_as_guest(driver)
    KWS_module.KWS_checkout_via_paypal(driver)
    input(time.strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(threading.currentThread()) + ' ' + 'case 3 has finished, press any key to continue\n')
    driver.br.quit()

    
def c4(environment, browser):
    driver = KWS_module.Driver(environment, browser)
    print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'case 4 start')
    KWS_module.KWS_add_product_paddle_fan(driver)
    KWS_module.KWS_go_to_shopping_cart_via_cart_flyout(driver)
    KWS_module.KWS_shopping_cart_checkout_as_user(driver)
    KWS_module.KWS_checkout_via_paypal(driver)
    input(time.strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(threading.currentThread()) + ' ' + 'case 4 has finished, press any key to continue\n')
    driver.br.quit()
    
    
def c5(environment, browser):
    driver = KWS_module.Driver(environment, browser)
    print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'case 5 start')
    KWS_module.KWS_add_product_beer(driver, 2)
    KWS_module.KWS_go_to_shopping_cart_via_cart_flyout(driver)
    KWS_module.KWS_shopping_cart_checkout_as_guest(driver)
    KWS_module.KWS_checkout_via_amazon(driver)
    input(time.strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(threading.currentThread()) + ' ' + 'case 5 has finished, press any key to continue\n')
    driver.br.quit()
    
 
def c6(environment, browser):
    driver = KWS_module.Driver(environment, browser)
    print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'case 6 start')
    KWS_module.KWS_add_product_paddle_fan(driver, 7)
    KWS_module.KWS_go_to_shopping_cart_via_cart_flyout(driver)
    KWS_module.KWS_shopping_cart_checkout_as_user(driver)
    KWS_module.KWS_checkout_via_amazon(driver)
    input(time.strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(threading.currentThread()) + ' ' + 'case 6 has finished, press any key to continue\n')
    driver.br.quit()

# driver1 = KWS_module.driver(1, 1)
# driver1.setup()
# driver2 = KWS_module.driver(1, 2)
# driver2.setup()
# driver3 = KWS_module.driver(1, 3)
# driver3.setup()
# t1 = threading.Thread(target=c3, args=(1,6))
# t2 = threading.Thread(target=c3, args=(1,1))
# t3 = threading.Thread(target=c6, args=(1,3))
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()

class Mytest(unittest.TestCase):
    def setUp(self):
        print('Start')

    def test_c1(self):
        t1 = threading.Thread(target=c6, args=(environment, browser))
        t1.start()
        t1.join()
    
    def tearDown(self):
        print('End')

if __name__ == '__main__':
    unittest.main()
# print('End')







