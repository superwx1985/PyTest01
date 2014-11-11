# -*- coding: utf-8 -*-
import time, threading, unittest
from selenium import webdriver
from KWS.test_case.public import KWS_module


if False:
    br = webdriver.Firefox()
    br.get(KWS_module.baseURL)


class Mytest(unittest.TestCase):
    
    def setUp(self):
        #environment = 1  # 1=qa, 2=stg, 3=live
        #browser = 3  # 1=ie, 2=ff, 3=chrome, 4=remote_chrome, 5=remote_mac, 6=remote_ff
        #self.driver = KWS_module.Driver(1, 3)
        self.err=[]

            
    def test_smoke_test_1(self):
        'checkout as guest via CC'
        try:
            #driver = self.driver
            print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_1 start')
            print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_1 end')
        except:
            raise
        finally:
            pass
            #SSname='D:\\vic_test_data\\KWS_test\\result_' + time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + '_SS.png'
            #self.driver.br.get_screenshot_as_file(SSname)
            #print('SS was saved as %s' %SSname)
            
    def test_smoke_test_2(self):
        'checkout as user via CC'
        try:
            #driver = self.driver
            print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_2 start')
            print(time.strftime('%Y-%m-%d %H:%M:%S'), threading.currentThread(), 'smoke_test_2 end')
        except:
            raise
        finally:
            pass
            #SSname='D:\\vic_test_data\\KWS_test\\result_' + time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + '_SS.png'
            #self.driver.br.get_screenshot_as_file(SSname)
            #print('SS was saved as %s' %SSname)
 

    def tearDown(self):
        #input(time.strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(threading.currentThread()) + ' ' + 'case 1 has finished, press any key to continue\n')
        #self.driver.br.quit()
        pass

def make_TC_suite():
    suite = unittest.TestSuite()
    #suite.addTest(Mytest('test_smoke_test_2'))
    suite.addTest(Mytest('sample1'))
    return suite


if __name__ == '__main__':
    def make_TC_suite():
        suite = unittest.TestSuite()
        suite.addTest(Mytest('test_smoke_test_1'))
        suite.addTest(Mytest('test_smoke_test_2'))
        return suite
    suite = make_TC_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
    def multiple_threads(self):
        #t1=threading.Thread(target=test_smoke_test_1)
        #t1.start()
        #t1.join()
        pass


