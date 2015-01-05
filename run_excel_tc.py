'''
Created on 2014骞�12鏈�22鏃�

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, datetime, threading, os
import wait_element, import_test_data, connect_db
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS import init
from KWS.my_test_case import MyTestCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def change_digit_to_string(data):
    if isinstance(data, (int, float)):
        new_data = str(round(data))
    elif isinstance(data, str):
        new_data = data
    else:
        raise Exception('please check the input data')
    return new_data

def change_string_to_int(data):
    if data is None or data == '':
        new_data = data
    elif isinstance(data, (int, float)):
        new_data = round(data)
    elif isinstance(data, str):
        if data.isdigit():
            new_data = int(data)
        else:
            float_data = data.split(sep='.')
            if len(float_data) == 2 and float_data[0].isdigit() and float_data[1].isdigit():
                new_data = round(float(data))     
            else:
                raise Exception('please check the input data')
    else:
        raise Exception('please check the input data')
    return new_data
    
    if isinstance(data, (int, float)):
        new_data = str(round(data))
    elif isinstance(data, (str)):
        new_data = data
    else:
        raise Exception('please check the input data')
    return new_data

def run_excel_tc(excel_file, base_ot=10, print_=False, tcid=1, level=0, dr=None, debug=False, asserted=[], failed=[], err=[]):
    # err = err_
    # failed = failed_
    # tcid = tcid_
    id_ = str(tcid) + '-' + str(level) + '-' + str(0)
    try:
        raise Exception('test')
        data = import_test_data.get_excle_data(excel_file, 'TC')
        config_ = import_test_data.get_excle_data(excel_file, 'Config')
        server = change_digit_to_string(config_['B2'])
        database = change_digit_to_string(config_['B3'])
        user = change_digit_to_string(config_['B4'])
        pwd = change_digit_to_string(config_['B5'])
        trusted = change_digit_to_string(config_['B6'])
        # ff_profile = 'C:\\Users\\viwang\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\yj7r4nzk.tester'
        if level == 0:
            assert(config_['A1'] != '' and config_['B1'] != ''), 'missing browser config'
            chromeoption1 = webdriver.ChromeOptions()
            chromeoption1._arguments = ['test-type', "start-maximized", "no-default-browser-check"]
            if config_['A1'] == 'local browser':
                if config_['B1'] == 'INTERNETEXPLORER':
                    dr = webdriver.Ie()
                    dr.maximize_window()
                elif config_['B1'] == 'FIREFOX':
                    # dr = webdriver.Firefox(firefox_profile=webdriver.FirefoxProfile(ff_profile))
                    dr = webdriver.Firefox()
                    dr.maximize_window()
                elif config_['B1'] == 'CHROME':
                    dr = webdriver.Chrome(chrome_options=chromeoption1)
            elif config_['A1'] == 'remote browser':
                assert(config_['D1'] != '' and config_['F1'] != ''), 'missing remote browser config'
                ip = change_digit_to_string(config_['D1'])
                port = change_digit_to_string(config_['F1'])
                if config_['B1'] == 'INTERNETEXPLORER':
                    dr = webdriver.Remote(command_executor='http://' + ip + ':' + port + '/wd/hub', desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
                    dr.maximize_window()
                elif config_['B1'] == 'FIREFOX':
                    dr = webdriver.Remote(command_executor='http://' + ip + ':' + port + '/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
                    dr.maximize_window()
                elif config_['B1'] == 'CHROME':
                    dr = webdriver.Remote(command_executor='http://' + ip + ':' + port + '/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
                    dr.maximize_window()
                elif config_['B1'] == 'SAFARI':
                    dr = webdriver.Remote(command_executor='http://' + ip + ':' + port + '/wd/hub', desired_capabilities=DesiredCapabilities.SAFARI)
            else:
                raise Exception('no such driver, please check your setting')
            dr.implicitly_wait(base_ot)
        current_window = dr.current_window_handle
        if level == 0:
            asserted = []
            failed = []
            err = []
            print('====================\t' + excel_file + '\t====================')
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), str(tcid) + '-' + str(level) + '-0', 'start TC')
        else:
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), str(tcid) + '-' + str(level) + '-0', 'jump to share TC ==> ' + excel_file)

        for row in range(1, data['rows'] + 1):
            if data['H' + str(row)] == 1:
                continue
            id_ = str(tcid) + '-' + str(level) + '-' + str(row)
            if data['A' + str(row)] != '':
                step_id = data['A' + str(row)]
            else:
                step_id = '  '
            if data['B' + str(row)] != '':
                step_name = data['B' + str(row)]
            else:
                step_name = '    '
            if print_:
                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), id_, step_id + '    ' + step_name + '    ' + data['C' + str(row)])
            
            if data['C' + str(row)] in ('action'):
                continue
            
            elif data['C' + str(row)] == 'go to url':
                assert(data['E' + str(row)] != ''), 'missing value in "locator" column'
                dr.get(data['E' + str(row)])

            elif data['C' + str(row)] == 'click':
                assert(data['D' + str(row)] != '' and data['E' + str(row)] != ''), 'missing value in "by" or "locator" column'
                ot = change_string_to_int(data['G' + str(row)])
                if ot in ('', None):
                    ot = base_ot
                wait_element.try_to_click(dr, data['D' + str(row)], data['E' + str(row)], ot)

            elif data['C' + str(row)] == 'enter':
                assert(data['D' + str(row)] != '' and data['E' + str(row)] != ''), 'missing value in "by" or "locator" column'
                assert(data['F' + str(row)] != ''), 'missing data'
                ot = change_string_to_int(data['G' + str(row)])
                if ot in ('', None):
                    ot = base_ot
                data_ = change_digit_to_string(data['F' + str(row)])
                wait_element.try_to_enter(dr, data['D' + str(row)], data['E' + str(row)], ot, data_)

            elif data['C' + str(row)] == 'verify text':
                assert(data['F' + str(row)] != ''), 'missing data'
                ot = change_string_to_int(data['G' + str(row)])
                data_ = change_digit_to_string(data['F' + str(row)])
                if ot in ('', None):
                    ot = base_ot
                try:
                    wait_element.wait_for_text_present(dr, data_, ot, print_)
                    asserted.append((id_, 'text presented ==> [%s]' % data_))
                except AssertionError as e:
                    print('assert failed: ',(id_, str(e)))
                    failed.append((id_, str(e)))
                    
            elif data['C' + str(row)] == 'verify element':
                assert(data['D' + str(row)] != '' and data['E' + str(row)] != ''), 'missing value in "by" or "locator" column'
                ot = change_string_to_int(data['G' + str(row)])
                if ot in ('', None):
                    ot = base_ot
                locator = change_digit_to_string(data['E' + str(row)])
                try:
                    wait_element.wait_for_element_visible(dr, data['D' + str(row)], locator, ot, print_)
                    asserted.append((id_, 'element visible ==> [%s|%s]' % (data['D' + str(row)], data['E' + str(row)])))
                except AssertionError as e:
                    print('assert failed: ',(id_, str(e)))
                    failed.append((id_, str(e)))
                    
            elif data['C' + str(row)] == 'switch to':
                if data['E' + str(row)] != '':
                    dr.switch_to.window(data['E' + str(row)])
                else:
                    for window in dr.window_handles:
                        if window != current_window:
                            dr.switch_to.window(window)

            elif data['C' + str(row)] == 'verify DB':
                assert(data['F' + str(row)] != ''), 'missing data'
                try:
                    sql_str = data['F' + str(row)]
                    result = connect_db.run_sql(server=server, database=database, user=user, pwd=pwd, trusted=trusted, sql_str=sql_str)
                    assert(result), 'no such record'
                    print('DB record existed ==> (SQL in cell [F%s])' % str(row))
                    asserted.append((id_, 'DB record existed ==> (SQL in cell [F%s])' % str(row)))
                except AssertionError as e:
                    print('assert failed: ',(id_, str(e)))
                    failed.append((id_, str(e)))

            elif data['C' + str(row)] == 'share step':
                assert(data['E' + str(row)] != ''), 'missing value in "locator" column'
                ot = change_string_to_int(data['G' + str(row)])
                if ot in ('', None):
                    ot = base_ot
                sub_result = run_excel_tc(excel_file=data['E' + str(row)], base_ot=ot, print_=print_, tcid=tcid, level=level + 1, dr=dr, asserted=asserted, failed=failed, err=err)
                asserted = sub_result[0]
                failed = sub_result[1]
                err = sub_result[2]
            else:
                raise Exception('invalid action ==> "' + data['C' + str(row)] + '"')

    except Exception as e:
        err.append((id_, e))
        #raise Exception('test')
        if debug == True:
            raise
    finally:
        if level != 0:
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), str(tcid) + '-' + str(level) + '-E', 'leave share TC ==> ' + excel_file)
            level -= 1
            return asserted, failed, err
        elif dr == None:
            print('cannot get the SS and final URL, because webdriver dose not exist')
        else:
            SSname = 'D:\\vic_test_data\\KWS_test\\result_' + datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.%f") + '_SS.png'
            dr.get_screenshot_as_file(SSname)
            print('SS was saved as %s\nThe final URL is "%s"' % (SSname, dr.current_url))
            dr.quit()
        if debug == False or err is None:
            return asserted, failed, err
    

if __name__ == '__main__':
    bace_dir = os.path.dirname(__file__)
    result = (None, None, None)
    result = run_excel_tc(excel_file=bace_dir + '\\TC\\test.xlsx', base_ot=3, print_=True, debug=True)
    print('asserted: %r\tfailed: %r\terror: %r' % (len(result[0]), len(result[1]), len(result[2])))
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), result)
    print('%s\n%s\n%s' %(result[0],result[1],result[2]))
    time.sleep(1)
