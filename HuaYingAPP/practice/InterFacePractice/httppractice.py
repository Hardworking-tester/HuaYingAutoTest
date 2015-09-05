#encoding:utf-8
from suds.client import Client


url="http://www.106818.com/ws/LinkWS.asmx?wsdl"

client=Client(url)

client.service.SelSum('SY0134','82342367')

req=str(client.last_sent())
print req
print "--------------------------------------------------"
response=str(client.last_received())

print response
