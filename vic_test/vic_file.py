'''
Created on 2014年9月24日

@author: viwang
'''
# -*- coding: utf-8 -*-

#file = open('text1.txt', mode='r')  # 相对路径
file= open('D:/viwang/workspace/PyTest01/vic_test/text1.txt', mode='r') #绝对路径
#file= open('D:\\viwang\\workspace\\PyTest01\\vic_test\\text1.txt', mode='r') #注意斜杠的两种写法
data = file.readlines()
file.close()
       
for line in data:
        print(line)


#===============================================================================
# import csv
# with open('csv1.csv', mode='r', newline='') as csvfile: 
# # 用with是用来保证运行中出错也可以正确关闭文件的，mode是指定打开方式，newline是指定换行符处理方式
#     data = csv.reader(csvfile, delimiter=',', quotechar='|') 
# # delimiter指定分隔符，默认是','，quotechar指定引用符，默认是'"'，这里指定了'|'，意思是两个'|'直接的内容会无视换行，分隔等符号，直接输出为一个元素
#     for line in data:
#         print(line)
#         for column in line:
#             print(column)
#===============================================================================

#===============================================================================
# from xml.dom import minidom 
# 
# dom = minidom.parse('xml1.xml')
# root = dom.documentElement
# elements=root.getElementsByTagName('item')
# for x in elements:
#     print(x.nodeName,x.getAttribute('id'))
# element = root.getElementsByTagName('caption')[0]
# print(element.firstChild.data)
#===============================================================================










