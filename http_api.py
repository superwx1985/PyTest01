'''
Created on 2015年1月4日

@author: viwang
'''
# -*- coding: utf-8 -*-
import httplib2
from urllib.parse import urlencode

def http_api(url,url_params=None,headers=None,body=None,print_=False):
    if url_params:
        url=url+'?'
        for key, value in url_params.items():
            url = url+key+'='+value+'&'
        url=url.rstrip('&')
    if body:
        if isinstance(body, dict):
            body = urlencode(body)
        else:
            body = body
        #body = str(data).replace('\'', '\"')
    if print_:
        print('url ==> %s\nheaders ==> %s\nbody ==> %s' %(url,headers,body))
    h = httplib2.Http()
    response, content = h.request(url, 'POST', headers=headers, body=body)
    str_content = content.decode('utf-8')
    return response, str_content


if __name__ == '__main__':
    url = 'http://retailerapi-qa-1048811846.us-east-1.elb.amazonaws.com/retailer/v1/registry'
    headers = {'access-key':'839d35cd515746b5167d494f856e4ef0','Content-Type':'application/json; charset=utf-8'}
    url_params = {'apikey':'ca7f6e91ee8134de9717707d86b29100'}
    body = '''{
"RetailerRegistryCode": "vic15010405",
"RegistrantFirstName": "Zacharey",
"RegistrantLastName": "Hayes",  
"RegistrantEmail": "vic15010405@gmail.com",
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
    response, content = http_api(url=url,url_params=url_params,headers=headers,body=body,print_=False)
    print(response)
    print(content)
