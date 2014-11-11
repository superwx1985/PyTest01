'''
Created on 2014年9月9日

@author: viwang
'''
# -*- coding: utf-8 -*-
#===============================================================================
# import pymssql
# 
# conn = pymssql.connect(host='GZ-VICWANG\MSSQLSERVER11',user='sa',password ='sa',database='test')
# cur=conn.cursor()
# cur.execute('SELECT TOP 100 * FROM cdsgus')
# print(cur.fetchone()[0])
# conn.close()
#===============================================================================

import pyodbc
cnxn = pyodbc.connect('Driver={SQL Server};Server=qadb01;Database=KnotCommerce;Trusted_Connection=yes;')
cursor = cnxn.cursor()
cursor.execute("SELECT top 100 * FROM [dbo].[CatalogEntry]")
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print (row.Name)
cnxn.close()