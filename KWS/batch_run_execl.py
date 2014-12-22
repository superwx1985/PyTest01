'''
Created on 2014年12月22日

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, datetime, threading, wait_element, os
from KWS import run_excel_tc
from selenium import webdriver

def get_tc(tc_dir):
    tcs = []
    lists=os.listdir(tc_dir)
    for file in lists:
        if file[file.rfind('.')+1:] in ('xlsx','xls') and file[0:4].lower() == 'test':
            tcs.append((tc_dir+file,file))
    return tcs
def batch_run_excel(tcs):
    done=[]
    pass_=[]
    failed=[]
    error_=[]
    for tc in tcs:
        
        try:
            br = webdriver.Chrome()
            a = run_excel_tc.run_excel_tc(br, excel_file=tc[0], sheet='Sheet1')
            print(a)
            print('error: %r\tfailed: %r' %(len(a[0]),len(a[1])))
        finally:
            try:
                SSname = 'D:\\vic_test_data\\KWS_test\\result_' + datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.%f") + '_SS.png'
                br.get_screenshot_as_file(SSname)
                print('SS was saved as %s\nThe final URL is "%s"' % (SSname, br.current_url))
            except:
                print('cannot get the SS and final URL, because:')
                raise
            br.quit()
            time.sleep(1)
        
a = get_tc('D:\\viwang\\workspace\\PyTest01\\KWS\\test_case\\')
print(a)
batch_run_excel(a)