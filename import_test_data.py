'''
Created on 2014年12月2日

@author: viwang
'''
# -*- coding: utf-8 -*-

import csv
import xlrd  # 读取excel数据，需安装xlrd
import os

bace_dir = os.path.dirname(__file__)

def get_csv_data(filename, print_=False):
    csv_data = []
    with open(filename, mode='r', newline='') as file:  # 用with是用来保证运行中出错也可以正确关闭文件的，mode是指定打开方式，newline是指定换行符处理方式
        data = csv.reader(file, delimiter=',', quotechar='|')  # delimiter指定分隔符，默认是','，quotechar指定引用符，默认是'"'，这里指定了'|'，意思是两个'|'直接的内容会无视换行，分隔等符号，直接输出为一个元素
        for line in data:
            if print_:
                print(line)
            csv_data.append(line)
    return csv_data

def get_txt_data(filename, print_=False):
    with open(filename, mode='r') as file:
        data = file.readlines()
    if print_:
        for line in data:print(line)
    return data

def get_excle_data(filename, sheet_name, print_=False):
    data = {}
    map_ = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
    with xlrd.open_workbook(filename) as workbook:
        sheet = workbook.sheet_by_name(sheet_name)
        data['file']=filename
        data['sheet']=sheet_name
        data['rows']=sheet.nrows
        data['columns']=sheet.ncols
        if print_:
            print('open excel file ==> %s\nload sheet ==> %s\nthis file has %s rows, %s columns' %(data['file'],data['sheet'],data['rows'],data['columns']))
        for r in range(0, sheet.nrows):
            rname= str(r+1)
            for c in range(0, sheet.ncols):
                x=c+1
                s=''
                while(True):
                    if x<27:
                        s=s+map_[x]
                        break
                    y = int(x/26)
                    if y > 26:
                        if x%26 == 0:
                            s=s+map_[26]
                            x = y-1
                            continue
                        s=s+map_[x%26]
                        x = y
                        continue
                    if x%26 == 0:
                        s=s+map_[26]+map_[y-1]
                    else:
                        s=s+map_[x%26]+map_[y]
                    x = y
                    if y<=26:
                        break
                cname=s[::-1]
                data[cname + rname] = sheet.cell(r, c).value
                if print_:
                    print('['+cname + str(r+1)+']'+str(sheet.cell(r,c).value)+'\t\t', end='')
                    if c+1 == sheet.ncols:
                        print('\n')
    return data

if __name__ == '__main__':
    pass
    # data=get_csv_data('D:/viwang/workspace/PyTest01/KWS/test_data/address.csv',True)
    # print(data[1][1])
    # get_txt_data('D:/viwang/workspace/PyTest01/vic_test/text1.txt', True)
    data = get_excle_data(bace_dir+'/TC/test.xlsx', 'Config' , True)
    #print(data['AB2'])
