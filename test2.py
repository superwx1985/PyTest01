# -*- coding: utf-8 -*-
# coding=utf-8
import time, unittest, datetime, threading, wait_element
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS import import_test_data, init
from KWS.my_test_case import MyTestCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions 


def run_excel_tc(excel_file='D:/viwang/workspace/PyTest01/vic_test/test.xlsx', sheet='Sheet1'):
    try:
        #br = webdriver.Chrome()
        #current_window = br.current_window_handle
        data = import_test_data.get_excle_data(excel_file, sheet)
        err = []
        failed = []
        assert (1==0) 
        raise exceptions.WebDriverException('EEEE')
    except AssertionError as err_:
        failed.append(err_)
    except exceptions.WebDriverException as err_:
        err.append(err_)
    except Exception as err_:
        err.append(err_)
    return err,failed
    
if __name__ == '__main__':
    #unittest.main(warnings='ignore')
    a=run_excel_tc()
    print(a)