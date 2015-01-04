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
            row = []
            for column in range(len(row_description)):
                row.append((column+1,row_description[column][0],row_value[column]))
            result.append(row)
    return result
result=run_sql(server='testregistrydb.cx63o2hqi2wj.us-east-1.rds.amazonaws.com', database='TestRegistry', user='SQLQAUser', pwd='abc123!', trusted='no', sql_str = "SELECT TOP 1 * FROM [TestRegistry].[dbo].[RawRetailerRegistry] where RetailerRegistryCode = 'vic14123106'")
for i in result:
    print(i)
