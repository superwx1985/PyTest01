# -*- coding: utf-8 -*-
import HTMLTestRunner, unittest, time, re, random, multiprocessing, threading, sys, os, datetime, send_report
from KWS.test_case import test_payment, test_list_page, test_just_for_test

def discover_TC(pyname='*smoke_test.py', TC_folder='D:/viwang/workspace/PyTest01/KWS/test_case/'):
    suite = unittest.defaultTestLoader.discover(start_dir=TC_folder, pattern=pyname, top_level_dir=TC_folder)
    return suite

#===============================================================================
# #各种快速获取TC的方法
# def make_TC_suite():
#     suite = unittest.TestSuite()
#     suite.addTest(unittest.makeSuite(test_smoke_test.Mytest))
#     return suite
# 
# def discover_TC():
#     TC_folder = 'D:/viwang/workspace/PyTest01/KWS/test_case/'
#     suite = unittest.defaultTestLoader.discover(TC_folder, pattern='*smoke_test.py', top_level_dir='d:/viwang/workspace/PyTest01/KWS/')
#     return suite
# def get_tc_from_name(package='test_case.test_smoke_test',names=['test_smoke_test_CC','test_smoke_test_Paypal','test_smoke_test_Amazon']):
#     def get_module_from_packagename(name):
#         __import__(name)
#         return sys.modules[name]
#     module_smoket_test = get_module_from_packagename(package)
#     for name in names:
#         suite_smoket_test = unittest.loader.findTestCases(module_smoket_test, prefix=name)
#         suite.addTests(suite_smoket_test)
#===============================================================================

def RunCase(suite, multi=0):  # 0为单线程，非0为多线程
    reportname = 'D:\\vic_test_data\\KWS_test\\result_' + datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.%f") + '.html'  # 定义个报告存放路径，支持相对路径
    fp = open(reportname, 'wb')
    if multi == 0:
        # 定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(
                                               stream=fp,
                                               title='KWS automation test',
                                               title2=str(suite),
                                               description='Detail list'
                                               )
        runner.run(suite)
    else:
        proclist = []
        s = 1
        for i in suite:
            runner = HTMLTestRunner.HTMLTestRunner(
                                                   stream=fp,
                                                   title='KWS automation test',
                                                   title2=str(i),
                                                   description='Detail list'
                                                   )
            # proc = multiprocessing.Process(target=runner.run, args=(i,))    #多进程运行，windows下会冲突
            proc = threading.Thread(target=runner.run, args=(i,))  # 多线程运行
            proclist.append(proc)
            s += 1
        for proc in proclist: proc.start()
        for proc in proclist: proc.join()
    fp.close()
    return reportname

#####################################################################################################################

TC_folder = 'D:/viwang/workspace/PyTest01/KWS/test_case/'
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'BEGIN')
suite = unittest.TestSuite()

def suite1():
    suite = unittest.TestSuite()
    suite.addTest(test_payment.MyTest('test_01', 1, 2))
    suite.addTest(test_payment.MyTest('test_02', 1, 2))
    return suite

def suite2():
    suite = unittest.TestSuite()
    suite.addTest(test_payment.MyTest('test_03', 1, 1))
    suite.addTest(test_payment.MyTest('test_04', 1, 3))
    return suite

def suite3():
    suite = unittest.TestSuite()
    # suite.addTest(test_payment.MyTest('sample1',1,3))
    suite.addTest(test_payment.MyTest('test_05', 1, 3))
    suite.addTest(test_payment.MyTest('test_06', 1, 3))
    return suite

# suite = discover_TC('*list_page*')
# suite.addTest(test_just_for_test.MyTest('test_01', 1, 3))
#suite.addTest(test_list_page.MyTest('test_01', 1, 3))
#suite.addTest(test_list_page.MyTest('test_02', 1, 2))

#suite.addTest(suite1())     #这样可以把几个 testcase 组合成一组
#suite.addTest(suite2())
suite.addTest(suite3())

print('test suite: ', suite)
reportname = RunCase(suite, 0)  # 第二位参数代表是否用多线程运行

print('report was saved as:\n' + reportname)
send_report.send_report('D:/vic_test_data/KWS_test/')
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"), 'END')




#===============================================================================
# now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
# reportname = 'D:\\vic_test_data\\KWS_test\\result_' + now + '.html'  # 定义个报告存放路径，支持相对路径
# fp = open(reportname, 'wb')
#  
# # 定义测试报告
# runner = HTMLTestRunner.HTMLTestRunner(
#                                        stream=fp,
#                                        title='KWS automation test',
#                                        description='Detail list'
#                                        )
#  
# # 运行测试用例
# runner.run(suite)
# fp.close()  # 关闭报告文件
# send_report.send_report('D:/vic_test_data/KWS_test/')
#  
#send_reportY-%m-%d %H:%M:%S'), 'END')
#===============================================================================

