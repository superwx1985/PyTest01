'''
Created on 2014年12月22日

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, datetime, threading, wait_element, os
from KWS import run_excel_tc
from selenium import webdriver

def get_tc(tc_dir, print_=False):
    tcs = []
    lists=os.listdir(tc_dir)
    for file in lists:
        if file[file.rfind('.')+1:] in ('xlsx','xls') and file[0:4].lower() == 'test':
            tcs.append((tc_dir+file,file))
    if (print_):
        print(tcs)
    return tcs
def batch_run_excel(tcs, ot=10):
    print('========== BEGIN ==========\n')
    run=[]
    passed=[]
    failed=[]
    err=[]
    tcid=1
    tcs_result=[]
    for tc in tcs:
        try:
            br = webdriver.Chrome()
            tc_result = run_excel_tc.run_excel_tc(br, excel_file=tc[0], sheet='Sheet1',ot=ot ,tcid_=tcid)
            #print('failed: %r\terror: %r' %(len(result[0]),len(result[1])))
            #print('failed:\n%r' %result[0])
            #print('error:\n%r' %result[1])
        finally:
            try:
                SSname = 'D:\\vic_test_data\\KWS_test\\result_' + datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.%f") + '_SS.png'
                br.get_screenshot_as_file(SSname)
                print('SS was saved as %s\nThe final URL is "%s"' % (SSname, br.current_url),'\n')
            except Exception as e:
                print('cannot get the SS and final URL, because:',e,'\n')
            br.quit()
            time.sleep(1)
            tcid+=1
            tcs_result.append((tc[1],tc_result))
    #print('\n\n',tcs_result,'\n\n')
    print('\n\n========== test result ==========\n')
    for i in tcs_result:
        run.append(i[0])
        if len(i[1][1]) == 0 and len(i[1][2]) == 0:
            passed.append((i[0],i[1][0],i[1][1],i[1][2]))
        elif len(i[1][2])>0:
            err.append((i[0],i[1][0],i[1][1],i[1][2]))
        else:
            failed.append((i[0],i[1][0],i[1][1],i[1][2]))
    print('run: %r    passed: %r    failed: %r    error: %r\n' %(len(run),len(passed),len(failed),len(err)))
    print('========== run ==========\n\n%r\n' %run)
    if len(passed)>0:
        print('========== passed ==========\n')
        for i in passed:
            print(i[0])
            print('> asserted step:\t',i[1])
            print('> failed step:\t\t',i[2])
            print('> error step:\t\t',i[3],'\n')
    if len(failed)>0:
        print('========== failed ==========\n')
        for i in failed:
            print(i[0])
            print('> asserted step:\t',i[1])
            print('> failed step:\t\t',i[2])
            print('> error step:\t\t',i[3],'\n')
    if len(err)>0:
        print('========== error ==========\n')
        for i in err:
            print(i[0])
            print('> asserted step:\t',i[1])
            print('> failed step:\t\t',i[2])
            print('> error step:\t\t',i[3],'\n')
    print('========== END ==========\n')
        
if __name__ == '__main__':
    tcs = get_tc('D:\\viwang\\workspace\\PyTest01\\KWS\\test_case\\')
    batch_run_excel(tcs,ot=1)