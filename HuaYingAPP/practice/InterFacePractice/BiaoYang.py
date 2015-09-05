# encoding:utf-8
import urllib
import urllib2
import httplib
class Tt1():



    #表扬
    def biaoYang(self):
        web_url='http://192.168.1.241:8080/zhsq/client/owner_repair!save.action'

        values = {'token':'6m3ou41429594424828','stewardId':'402881714e0a715e014e0a7479600000,402881714e0a715e014e0a9943bf000b,402881714e0a715e014e0a99cb63000c,402881714e0a715e014e0a751d910001,402881714e0a715e014e0a77ed6a0002,402881714e0a715e014e0a7a333d0003,402881ea4e09af57014e09b2651f0000','ownerRepair.owner.id':'402881714dc2e54c014dd0c979a90002',
                  'ownerRepair.member.id':'4028813c4cda5ee7014cda77c5fc0001','ownerRepair.ownerName':'王伟高',
                  'ownerRepair.OwnerPhone':'15093492821','ownerRepair.ownerAddr':'宏江中央广场','ownerRepair.imageContent':'','ownerRepair.repairDescribe':'保安、保洁等物业管理人员都很负责任2222','ownerRepair.useFlag':5}
        data1=urllib.urlencode(values)
        req=urllib2.Request(web_url,data1)
        rep=urllib2.urlopen(req)
        paga=rep.read()

        print paga
    #查看表扬
    def chaKanBiaoYang(self):
        # web_url='http://192.168.1.241:8080/zhsq/client/owner_repair!listByProcessFlag.action'
        web_url='http://192.168.1.241:9080/zhsqitfe/client/owner_repair!listByProcessFlag.action'
        values = {'token':'6m3ou41429594424828','ownerRepair.owner.id':'402881714dc2e54c014dd0c979a90002','ownerRepair.useFlag':5,'ownerRepair.processFlag':0,'pager.pageNumber':1,'pager.pageSize':'','pager.orderBy':'','pager.order':''}
        # values = {'token':'6m3ou41429594424828','ownerRepair.owner.id':'402881714dc2e54c014dd0c979a90002','ownerRepair.useFlag':5,'ownerRepair.processFlag':0,'pager.pageNumber':'','pager.pageSize':1,'pager.orderBy':'','pager.order':''}

        data1=urllib.urlencode(values)
        req=urllib2.Request(web_url,data1)
        rep=urllib2.urlopen(req)
        paga=rep.read()
        print paga
    #获取物业角色列表
    def getWuYeJueSeList(self):
        web_url='http://192.168.1.241:9080/zhsqitfe/client/owner_repair!getStewardListByMember.action'
        values = {'token':'6m3ou41429594424828','steward.roleType':100}

        data1=urllib.urlencode(values)
        req=urllib2.Request(web_url,data1)
        rep=urllib2.urlopen(req)
        paga=rep.read()
        print paga




pp=Tt1()
# pp.biaoYang()
pp.chaKanBiaoYang()
# pp.getWuYeJueSeList()


