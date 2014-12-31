'''
Created on 2014年12月31日

@author: viwang
'''
# -*- coding: utf-8 -*-
import httplib2
from urllib.parse import urlencode


url = 'http://retailerapi-qa-1048811846.us-east-1.elb.amazonaws.com/retailer/v1/registry'
headers={'access-key':'839d35cd515746b5167d494f856e4ef0','Content-Type':'application/json; charset=utf-8'}
#===============================================================================
# url_params = {'apikey':'ca7f6e91ee8134de9717707d86b29100'}
# url=url+'?'
# for key, value in url_params.items():
#     url = url+key+'='+value+'&'
#===============================================================================
data = '{"RetailerRegistryCode": "vic14123105","DeletedDate": "2014-12-04"}'
if isinstance(data, dict):
    body = urlencode(data)
else:
    body = data
#body = str(data).replace('\'', '\"')

h = httplib2.Http('.cache')
response, content = h.request(url, 'DELETE', headers=headers, body=body)

str_content = content.decode('utf-8')
print(response)
print(str_content)