#encoding:utf-8

import httplib
import json
conn = httplib.HTTPConnection("http://192.168.1.240:8080")
headers = {"Content-type":"application/json"} #application/x-www-form-urlencoded
params = {'charset':"utf-8","token":"sdffdsfsd82342367",'ownerRepair.owner.id':'1','ownerRepair.member.id':'2','ownerRepair.ownerName':'wwg',
          'ownerRepair.ownerPhone':'18638135380','ownerRepair.ownerAddr':'','ownerRepair.imageContent':'','ownerRepair.describe':'wwg','ownerRepair.useFlag':'1','ownerRepair.processFlag':'0'}
conn.request("POST", "/zhsq/client/owner_repair!save.action", json.JSONEncoder().encode(params), headers)
response = conn.getresponse()
data = response.read()
if response.status == 200:
    print 'success'
    print data
else:
    print 'fail'
conn.close()




url = 'http://192.168.1.240:8080/zhsq/client/owner_repair!save.action'
values = {"token":"sdffdsfsd82342367",'ownerRepair.owner.id':'1','ownerRepair.member.id':'2','ownerRepair.ownerName':'wwg',
          'ownerRepair.ownerPhone':'18638135380','ownerRepair.ownerAddr':'','ownerRepair.imageContent':'','ownerRepair.describe':'wwg','ownerRepair.useFlag':'1','ownerRepair.processFlag':'0'}
