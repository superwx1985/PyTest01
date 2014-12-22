'''
Created on 2014年12月22日

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, datetime, threading, wait_element
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS import import_test_data, init
from KWS.my_test_case import MyTestCase
from selenium.webdriver.common.action_chains import ActionChains

def run_excel_tc(br, excel_file, sheet,err_ = [],failed_ = []):
    err=err_
    failed=failed_
    try:
        current_window = br.current_window_handle
        data = import_test_data.get_excle_data(excel_file, sheet)
        print (1, 'start test ==>',excel_file,sheet)
        for row in range(2, data['rows'] + 1):
            print (row, data['C' + str(row)])
            if data['C' + str(row)] == 'go to url':
                assert(data['D' + str(row)] != ''), 'missing locator'
                br.get(data['D' + str(row)])
            elif data['C' + str(row)] == 'enter':
                assert(data['D' + str(row)] != ''), 'missing locator'
                assert(data['E' + str(row)] != ''), 'missing data'
                locator = data['D' + str(row)].split('|')
                if isinstance(data['F' + str(row)], (int, float)):
                    ot = round(data['F' + str(row)])
                elif data['F' + str(row)].isdigit():
                    ot = int(data['F' + str(row)])
                else:
                    ot = 10
                if isinstance(data['E' + str(row)], (int, float)):
                    data_ = str(round(data['E' + str(row)]))
                else:
                    data_ = data['E' + str(row)]
                wait_element.try_to_enter(br, locator[0], locator[1], ot, data_)
            elif data['C' + str(row)] == 'click':
                assert(data['D' + str(row)] != ''), 'missing locator'
                locator = data['D' + str(row)].split('|')
                if isinstance(data['F' + str(row)], (int, float)):
                    ot = round(data['F' + str(row)])
                elif data['F' + str(row)].isdigit():
                    ot = int(data['F' + str(row)])
                else:
                    ot = 10
                wait_element.try_to_click(br, locator[0], locator[1], ot)
            elif data['C' + str(row)] == 'verify text':
                try:
                    assert(data['E' + str(row)] != ''), 'missing data'
                    if isinstance(data['F' + str(row)], (int, float)):
                        ot = round(data['F' + str(row)])
                    elif data['F' + str(row)].isdigit():
                        ot = int(data['F' + str(row)])
                    else:
                        ot = 10
                    wait_element.wait_for_text_present(br, data['E' + str(row)], ot, True)
                except AssertionError as err_:
                    failed.append(err_)
                except Exception as err_:
                    err.append(err_)
            elif data['C' + str(row)] == 'switch to':
                if data['D' + str(row)] != '':
                    br.switch_to.window(data['D' + str(row)])
                else:
                    for window in br.window_handles:
                        if window != current_window:
                            br.switch_to.window(window)
            elif data['C' + str(row)] == 'share step':
                assert(data['D' + str(row)] != ''), 'missing locator'
                locator = data['D' + str(row)].split('|')
                result = run_excel_tc(br, excel_file=locator[0], sheet=locator[1],err_=err,failed_=failed)
                for j in result[1]:
                    failed.append(j)
                for j in result[0]:
                    err.append(j)
            else:
                raise Exception('invalid action ==> "' + data['C' + str(row)] + '"')

    except AssertionError as e:
        failed.append(e)
    except Exception as e:
        err.append(e)


    return err,failed
if __name__ == '__main__':
    try:
        br = webdriver.Chrome()
        a = run_excel_tc(br, excel_file='D:/viwang/workspace/PyTest01/vic_test/test.xlsx', sheet='Sheet1')
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