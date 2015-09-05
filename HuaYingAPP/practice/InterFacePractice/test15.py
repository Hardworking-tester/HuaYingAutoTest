#encoding:utf-8
import urllib
import urllib2
import re

from practice.InterFacePractice import test13


class Tt1():

    data_list=['402881714ddc43d4014ddc6b4f450009','402881714ddc43d4014ddc6bb90c000b','402881714ddc43d4014ddc6ccd4e000d','402881714ddc43d4014ddc7266060014',
               '402881714ddc43d4014ddc734157001e',
                   '402881714ddc43d4014ddc73a38f0020','402881714ddc43d4014ddc76ea3b0027','402881714ddc43d4014ddc77927d002d','402881714ddc43d4014ddc7818bc002f',
                   '402881714ddc43d4014ddca398e60051','402881714ddc43d4014de02a983e0068','402881714ddc43d4014de02dde5f006c','402881714de051c7014de1733377001e',
                   '402881714de051c7014de5b762e9002d','402881714de051c7014de5bc4d040035','402881714df525a3014df52d18b40000','402881714df525a3014df52d89170002',
                   '402881714df525a3014df53349680004','402881714df525a3014df533aba60006','402881714df525a3014df5341b200008','402881714df525a3014df5353ac3000a',
                   '402881714df525a3014df53610d6000c','402881714df525a3014df53765800010','402881714df525a3014df53828b60015',
                   '402881714df525a3014df5389a860017','402881714df525a3014df5396fa90019','402881714e003512014e0966a10d03a2']

    #收藏商品
    def shouCang(self):
        # headers1 = {"Content-Type":"application/x-www-form-urlencoded",
        #    "Connection":"Keep-Alive","Referer":"http://192.168.1.240:8080/zhsq/client/owner_repair!save.action"}
        # url1 = '/zhsq/client/owner_repair!save.action'
        picture='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'+'.jpg'
        # web_url='http://192.168.1.116:8080/zhsqitfe/client/article!getArticleCategoryList.action'
        web_url='http://192.168.1.241:8080/zhsq/client/owner_collection!save.action'
        data_count=0
        data_list=['402881714ddc43d4014ddc6b4f450009','402881714ddc43d4014ddc6bb90c000b','402881714ddc43d4014ddc6ccd4e000d','402881714ddc43d4014ddc7266060014',
               '402881714ddc43d4014ddc734157001e',
                   '402881714ddc43d4014ddc73a38f0020','402881714ddc43d4014ddc76ea3b0027','402881714ddc43d4014ddc77927d002d','402881714ddc43d4014ddc7818bc002f',
                   '402881714ddc43d4014ddca398e60051','402881714ddc43d4014de02a983e0068','402881714ddc43d4014de02dde5f006c','402881714de051c7014de1733377001e',
                   '402881714de051c7014de5b762e9002d','402881714de051c7014de5bc4d040035','402881714df525a3014df52d18b40000','402881714df525a3014df52d89170002',
                   '402881714df525a3014df53349680004','402881714df525a3014df533aba60006','402881714df525a3014df5341b200008','402881714df525a3014df5353ac3000a',
                   '402881714df525a3014df53610d6000c','402881714df525a3014df53765800010','402881714df525a3014df53828b60015',
                   '402881714df525a3014df5389a860017','402881714df525a3014df5396fa90019','402881714e003512014e0966a10d03a2']
        # values =  {'token':'6m3ou41429594424828','categoryId':'402881714d9d74ff014dacbe516c003e','ownerId':'402881714d9d74ff014daca6cab10020','pager.pageNumber':1,'pager.pageSize':'','pager.orderBy':'','pager.order':''}
        for i in self.data_list:
            values = {'token':'6m3ou41429594424828','ownerId':'402881714dc2e54c014dd0c979a90002','goodsId':i}
            data1=urllib.urlencode(values)
            req=urllib2.Request(web_url,data1)
            rep=urllib2.urlopen(req)
            paga=rep.read()

            # print paga
            if paga=='0':
                data_count=data_count+1
                ui= test13.GetData().getDataFromMysql(i)
                print "收藏的商品名称为:%s，id为：%s" %(ui,i)
            else:
                print "商品：%s收藏失败，id为：%s" %(ui,i)
            # del i
        print "本次一共收藏了 %s 件商品" %data_count



        # data1=urllib.urlencode(values)
        # req=urllib2.Request(web_url,data1)
        # rep=urllib2.urlopen(req)
        # paga=rep.read()
        # print paga
    #查看收藏的商品
    def chaKanShouCang(self):
        web_url='http://192.168.1.241:9080/zhsqitfe/client/owner_collection!getList.action'
        values = {'token':'6m3ou41429594424828','ownerId':'402881714dc2e54c014dd0c979a90002','pager.pageNumber':21,'pager.pageSize':100,'pager.orderBy':'','pager.order':''}

        data1=urllib.urlencode(values)
        req=urllib2.Request(web_url,data1)
        rep=urllib2.urlopen(req)
        paga=rep.read()
        # print paga
        data=re.findall('"name":(.*?),"createDate":',paga)
        print "读取到的收藏的商品数量为：%s" %data.__len__()
        for product in data:
            print product

    #取消收藏
    def quXiaoShouCang(self):
        data_count=0
        web_url='http://192.168.1.241:8080/zhsq/client/owner_collection!delete.action'
        for m in self.data_list:
            values = {'token':'6m3ou41429594424828','ownerId':'402881714dc2e54c014dd0c979a90002','goodsId':m}

            data1=urllib.urlencode(values)
            req=urllib2.Request(web_url,data1)
            rep=urllib2.urlopen(req)
            paga=rep.read()
            # print paga
            if paga=='0':
                data_count=data_count+1
            else:
                print type(paga)
        print "本次一共取消收藏了 %s 件商品" %data_count
    #获取我的收藏的所有的ID
    def getShouCangId(self):
        web_url='http://192.168.1.241:9080/zhsqitfe/client/owner_collection!getCollectionIds.action'
        values = {'token':'6m3ou41429594424828','ownerId':'402881714dc2e54c014dd0c979a90002'}

        data1=urllib.urlencode(values)
        req=urllib2.Request(web_url,data1)
        rep=urllib2.urlopen(req)
        paga=rep.read()
        print paga

pp=Tt1()
# pp.shouCang()
# pp.chaKanShouCang()
# pp.quXiaoShouCang()
pp.getShouCangId()



