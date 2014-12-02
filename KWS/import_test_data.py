'''
Created on 2014年12月2日

@author: viwang
'''
# -*- coding: utf-8 -*-

import csv

def get_csv_data(filename='D:/viwang/workspace/PyTest01/vic_test/csv1.csv'):
    csv_data = []
    with open(filename, mode='r', newline='') as file:  # 用with是用来保证运行中出错也可以正确关闭文件的，mode是指定打开方式，newline是指定换行符处理方式
        data = csv.reader(file, delimiter=',', quotechar='|')  # delimiter指定分隔符，默认是','，quotechar指定引用符，默认是'"'，这里指定了'|'，意思是两个'|'直接的内容会无视换行，分隔等符号，直接输出为一个元素
        for line in data:
            # print(line)
            csv_data.append(line)
    return csv_data


def get_txt_data(filename='D:/viwang/workspace/PyTest01/vic_test/text1.txt'):
    with open(filename, mode='r') as file:
        data = file.readlines()
    return data     
    # for line in data:print(line)
            
if __name__ == '__main__':
    print(get_csv_data('D:/viwang/workspace/PyTest01/KWS/test_data/KWS account.csv'))
    print(get_txt_data())