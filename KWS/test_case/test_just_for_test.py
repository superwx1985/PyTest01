'''
Created on 2014年11月11日

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, unittest, datetime, threading, wait_element
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS import import_test_data, init
from KWS.my_test_case import MyTestCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MyTest(MyTestCase):
    def setUp(self):
        # environment = 1  # 1=qa, 2=stg, 3=live
        browser = 2  # 1=ie, 2=ff, 3=chrome, 4=remote_chrome, 5=remote_mac, 6=remote_ff
        self.driver = init.setUp_(self.environment, self.browser)
        
    def atest_01(self):
        '01'
        try:
            br = self.driver.br
            data = self.tc
            data = import_test_data.get_excle_data('D:/test.xlsx', 'Sheet1')
            for i in range(2,data['rows']+1):
                print (i,data['C'+str(i)])
                if data['C'+str(i)] == 'go to url':
                    assert(data['D'+str(i)] != ''), 'missing locator'
                    br.get(data['D'+str(i)])
                elif data['C'+str(i)] == 'enter':
                    assert(data['D'+str(i)] != ''), 'missing locator'
                    assert(data['E'+str(i)] != ''), 'missing data'
                    locator = data['D'+str(i)].split('|')
                    if isinstance(data['F'+str(i)], (int,float)):
                        ot=round(data['F'+str(i)])
                    elif data['F'+str(i)].isdigit():
                        ot=int(data['F'+str(i)])
                    else:
                        ot=10
                    wait_element.try_to_enter(br, locator[0], locator[1], ot, data['E'+str(i)])
                elif data['C'+str(i)] == 'click':
                    assert(data['D'+str(i)] != ''), 'missing locator'
                    locator = data['D'+str(i)].split('|')
                    if isinstance(data['F'+str(i)], (int,float)):
                        ot=round(data['F'+str(i)])
                    elif data['F'+str(i)].isdigit():
                        ot=int(data['F'+str(i)])
                    else:
                        ot=10
                    wait_element.try_to_click(br, locator[0], locator[1], ot)
                elif data['C'+str(i)] == 'verify test':
                    assert(data['E'+str(i)] != ''), 'missing data'
                    if isinstance(data['F'+str(i)], (int,float)):
                        ot=round(data['F'+str(i)])
                    elif data['F'+str(i)].isdigit():
                        ot=int(data['F'+str(i)])
                    else:
                        ot=10
                    wait_element.wait_for_text_present(br, data['E'+str(i)], ot, True)
                else:
                    print('WTF')
            print('end')

        except:
            raise

    def test_02(self):
        pass
        try:
            assert(1==0),'fff'
        except:
            raise
            
    def tearDown(self):
        init.tearDown(self.driver)
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
    #suppresses a superfluous ResourceWarning which was being emitted at the time of writing.  It may have disappeared by the time you read this; feel free to try removing it!
