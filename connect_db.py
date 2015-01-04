'''
Created on 2015年1月4日

@author: viwang
'''
# -*- coding: utf-8 -*-
import pyodbc

def run_sql(server, database, user='', pwd='', trusted='yes', sql_str=''):
    conn_str = 'Driver={SQL Server};Server=%s;Database=%s;UID=%s;PWD=%s;Trusted_Connection=%s;'%(server, database, user, pwd, trusted)
    with pyodbc.connect(conn_str) as connect:
        cursor = connect.cursor()
        cursor.execute(sql_str)
        row_description = cursor.description
        
        result = []
        for row_value in cursor.fetchall():
            row = {}
            for column in range(len(row_description)):
                row[row_description[column][0]]=row_value[column]
            result.append(row)
    return result
    
    #===========================================================================
    #     result = []
    #     for row_value in cursor.fetchall():
    #         row = []
    #         for column in range(len(row_description)):
    #             row.append((column+1,row_description[column][0],row_value[column]))
    #         result.append(row)
    # return result
    #===========================================================================

if __name__ == '__main__':
    server='testregistrydb.cx63o2hqi2wj.us-east-1.rds.amazonaws.com'
    database='TestRegistry'
    user='SQLQAUser'
    pwd='abc123!'
    trusted='yes'
    sql_str = "SELECT TOP 1 * FROM [TestRegistry].[dbo].[RawRetailerRegistry] where RetailerRegistryCode = 'vic15010407'"
    result = run_sql(server=server, database=database, user=user, pwd=pwd, trusted=trusted, sql_str=sql_str)
    for i in result:
        print(i)
    assert(result), 'no such record'