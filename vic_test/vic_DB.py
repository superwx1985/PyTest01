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
server='qadb01'
database='KnotCommerce'
user=''
pwd=''
trusted='yes'
conn_str = 'Driver={SQL Server};Server=%s;Database=%s;UID=%s;PWD=%s;Trusted_Connection=%s;'%(server, database, user, pwd, trusted)
sql_str = "SELECT top 10 * FROM [dbo].[CatalogEntry]"
connect = pyodbc.connect(conn_str)
cursor = connect.cursor()
cursor.execute(sql_str)
#result = cursor.fetchall()
#print(result)
#===============================================================================
# while 1:
#     row = cursor.fetchone()
#     if not row:
#         break
#     print (row.Name)
#===============================================================================
row_description = cursor.description
result = []
for row_value in cursor.fetchall():
    row = []
    for column in range(len(row_description)):
        row.append((column+1,row_description[column][0],row_value[column]))
    result.append(row)
connect.close()
for i in result:
    print(i)