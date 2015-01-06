'''
Created on 2014年12月22日

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, datetime, threading, os
import run_excel_tc, wait_element
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
def batch_run_excel(tcs, base_ot=10, print_=False, debug=False):
    print('====================\tbegin\t====================\n')
    run=[]
    passed=[]
    failed=[]
    err=[]
    tcid=1
    tcs_result=[]
    print('begin to run %s TC:' %len(tcs))
    i=1
    for tc in tcs:
        print('%s\t%s'%(i,tc[1]))
        i+=1
    print()
    for tc in tcs:
        tc_result = run_excel_tc.run_excel_tc(excel_file=tc[0],base_ot=base_ot, print_=print_, tcid=tcid, debug=debug)
        time.sleep(1)
        tcid+=1
        tcs_result.append((tc[1],tc_result))
    print('\n\n',tcs_result,'\n\n')
    print('\n\n====================\tresult\t====================\n')
    for i in tcs_result:
        run.append(i[0])
        if len(i[1][1]) == 0 and len(i[1][2]) == 0:
            passed.append((i[0],i[1][0],i[1][1],i[1][2]))
        elif len(i[1][2])>0:
            err.append((i[0],i[1][0],i[1][1],i[1][2]))
        else:
            failed.append((i[0],i[1][0],i[1][1],i[1][2]))
    print('run: %r    passed: %r    failed: %r    error: %r\n' %(len(run),len(passed),len(failed),len(err)))
    #print('====================\trun\t====================\n\n%r\n' %run)
    if len(passed)>0:
        print('====================\tpassed\t====================\n')
        for i in passed:
            print(i[0])
            print('> asserted step:\t',i[1])
            print('> failed step:\t\t',i[2])
            print('> error step:\t\t',i[3],'\n')
    if len(failed)>0:
        print('====================\tfailed\t====================\n')
        for i in failed:
            print(i[0])
            print('> asserted step:\t',i[1])
            print('> failed step:\t\t',i[2])
            print('> error step:\t\t',i[3],'\n')
    if len(err)>0:
        print('====================\terror\t====================\n')
        for i in err:
            print(i[0])
            print('> asserted step:\t',i[1])
            print('> failed step:\t\t',i[2])
            print('> error step:\t\t',i[3],'\n')
    print('====================\tend\t====================\n')
        
if __name__ == '__main__':
    bace_dir = os.path.dirname(__file__)
    tcs = get_tc(bace_dir+'\\TC\\')
    batch_run_excel(tcs,base_ot=5,print_=True,debug=False)