# -*- coding: utf-8 -*-
import time, unittest, datetime, threading
import import_test_data, wait_element, http_api, connect_db
from KWS import init
from selenium import webdriver
from KWS.test_case.public import KWS_module
from KWS.my_test_case import MyTestCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions 

url = 'http://retailerapi-qa-1048811846.us-east-1.elb.amazonaws.com/retailer/v1/registry'
headers = {'access-key':'839d35cd515746b5167d494f856e4ef0','Content-Type':'application/json; charset=utf-8'}
url_params = {'apikey':'ca7f6e91ee8134de9717707d86b29100'}
body = '''{
"RetailerRegistryCode": "vic15010406",
"RegistrantFirstName": "Zacharey",
"RegistrantLastName": "Hayes",  
"RegistrantEmail": "vic15010406@gmail.com",
"CoRegistrantFirstName": "Millie",
"CoRegistrantLastName": "Lily",
"CoRegistrantEmail": "aaa@gmail.com",
"City": "TALLAHASSEE",
"State": "FL",
"Zip": "510000",
"EventTypeId": 1,
"EventDate": "2015-01-28",
"EventDescription": "",
"ReferralStatusCode": "",
"RegistryClickId": "",
"AltRetailerRegistryCode": "",
"ModifiedDate": "2014-12-04"
}'''

response, content = http_api.http_api(url=url,url_params=url_params,headers=headers,body=body,print_=True)
print(response)
print(content)

server='testregistrydb.cx63o2hqi2wj.us-east-1.rds.amazonaws.com'
database='TestRegistry'
user='SQLQAUser'
pwd='abc123!'
trusted='no'
sql_str = "SELECT TOP 1 * FROM [TestRegistry].[dbo].[RawRetailerRegistry] where RetailerRegistryCode = 'vic15010406'"
result = connect_db.run_sql(server=server, database=database, user=user, pwd=pwd, trusted=trusted, sql_str=sql_str)
for i in result:
    print(i)
assert(result[0]['RetailerRegistryCode'] == 'vic15010406' and result[0]['RegistrantEmail']=='vic15010406@gmail.com')
