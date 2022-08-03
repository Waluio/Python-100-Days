# -*- coding: utf-8 -*-
import http.client, urllib
conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
params = urllib.parse.urlencode({'key':'5005d98bbe6e42dbaff5fc0fa31d5d30','code':'hk00700'})
headers = {'Content-type':'application/x-www-form-urlencoded'}
conn.request('POST','/finance/index',params,headers)
res = conn.getresponse()
data = res.read()
print(data.decode('utf-8'))