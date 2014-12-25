'''
Created on 2014骞�12鏈�22鏃�

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, datetime, threading, os
import wait_element, import_test_data
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS import init
from KWS.my_test_case import MyTestCase
from selenium.webdriver.common.action_chains import ActionChains

def run_excel_tc(br, excel_file, ot=10, level=0, tcid_=1, asserted=[], failed=[], err=[]):
    # err = err_
    # failed = failed_
    tcid = tcid_
    id_ = str(tcid) + '-' + str(level) + '-' + str(0)
    try:
        current_window = br.current_window_handle
        data = import_test_data.get_excle_data(excel_file, 'TC')
        config_ = import_test_data.get_excle_data(excel_file, 'TC')
        br.implicitly_wait(ot)
        if level == 0:
            asserted = []
            failed = []
            err = []
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), str(tcid) + '-' + str(level) + '-0', 'start TC ==> ' + excel_file)
        else:
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), str(tcid) + '-' + str(level) + '-0', 'jump to share TC ==> ' + excel_file)

        for row in range(1, data['rows'] + 1):
            id_ = str(tcid) + '-' + str(level) + '-' + str(row)
            if data['A' + str(row)] != '':
                step_id = data['A' + str(row)]
            else:
                step_id = '  '
            if data['B' + str(row)] != '':
                step_name = data['B' + str(row)]
            else:
                step_name = '    '
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), id_, step_id + '    ' + step_name + '    ' + data['C' + str(row)])
            if data['C' + str(row)] in ('action', ''):
                pass
            elif data['C' + str(row)] == 'go to url':
                assert(data['D' + str(row)] != ''), 'missing locator'
                br.get(data['D' + str(row)])
            elif data['C' + str(row)] == 'enter':
                assert(data['D' + str(row)].count('|') == 1), 'please check the locator, must have one, and only one "|" as separator'
                assert(data['E' + str(row)] != ''), 'missing data'
                locator = data['D' + str(row)].split('|')
                if isinstance(data['F' + str(row)], (int, float)):
                    ot = round(data['F' + str(row)])
                elif data['F' + str(row)].isdigit():
                    ot = int(data['F' + str(row)])
                if isinstance(data['E' + str(row)], (int, float)):
                    data_ = str(round(data['E' + str(row)]))
                else:
                    data_ = data['E' + str(row)]
                wait_element.try_to_enter(br, locator[0], locator[1], ot, data_)
            elif data['C' + str(row)] == 'click':
                assert(data['D' + str(row)].count('|') == 1), 'please check the locator, must have one, and only one "|" as separator'
                locator = data['D' + str(row)].split('|')
                if isinstance(data['F' + str(row)], (int, float)):
                    ot = round(data['F' + str(row)])
                elif data['F' + str(row)].isdigit():
                    ot = int(data['F' + str(row)])
                wait_element.try_to_click(br, locator[0], locator[1], ot)
            elif data['C' + str(row)] == 'verify text':
                assert(data['E' + str(row)] != ''), 'missing data'
                if isinstance(data['F' + str(row)], (int, float)):
                    ot = round(data['F' + str(row)])
                elif data['F' + str(row)].isdigit():
                    ot = int(data['F' + str(row)])
                try:
                    wait_element.wait_for_text_present(br, data['E' + str(row)], ot, True)
                    asserted.append((id_, 'text present ==> %r' % data['E' + str(row)]))
                except AssertionError as e:
                    failed.append((id_, str(e)))
            elif data['C' + str(row)] == 'verify element':
                assert(data['D' + str(row)].count('|') == 1), 'please check the locator, must have one, and only one "|" as separator'
                locator = data['D' + str(row)].split('|')
                if isinstance(data['F' + str(row)], (int, float)):
                    ot = round(data['F' + str(row)])
                elif data['F' + str(row)].isdigit():
                    ot = int(data['F' + str(row)])
                try:
                    wait_element.wait_for_element_visible(br, locator[0], locator[1], ot, True)
                    asserted.append((id_, 'element visible ==> %r' % data['D' + str(row)]))
                except AssertionError as e:
                    failed.append((id_, str(e)))
            elif data['C' + str(row)] == 'switch to':
                if data['D' + str(row)] != '':
                    br.switch_to.window(data['D' + str(row)])
                else:
                    for window in br.window_handles:
                        if window != current_window:
                            br.switch_to.window(window)
            elif data['C' + str(row)] == 'share step':
                assert(data['D' + str(row)] != ''), 'missing locator'
                sub_result = run_excel_tc(br, excel_file=data['D' + str(row)], ot=ot, level=level + 1, asserted=asserted, failed=failed, err=err)
                asserted = sub_result[0]
                failed = sub_result[1]
                err = sub_result[2]
            else:
                raise Exception('invalid action ==> "' + data['C' + str(row)] + '"')
            
    except Exception as e:
        err.append((id_, e))
        raise #for debug
    if level != 0:
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'leave share TC ==> ' + excel_file)
        level -= 1
    return asserted, failed, err

if __name__ == '__main__':
    try:
        bace_dir = os.path.dirname(__file__)
        br = webdriver.Chrome()
        result = run_excel_tc(br, excel_file=bace_dir + '/TC/test.xls', ot=3)
        print('asserted: %r\tfailed: %r\terror: %r' % (len(result[0]), len(result[1]), len(result[2])))
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), result)
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
