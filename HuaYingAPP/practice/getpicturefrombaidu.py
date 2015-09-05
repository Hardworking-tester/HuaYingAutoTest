# encoding:utf-8
import cookielib
import urllib2
import re
import uuid
class T1():
    """
    网络爬虫获取百度图片
    """
    def geturl(self):
        # url="http://image.baidu.com/channel?c=%E7%BE%8E%E9%A3%9F&t=%E5%85%A8%E9%83%A8&s=0"
        url="http://h.hiphotos.baidu.com/image/w%3D310/"
        # url="http://image.baidu.com/channel?c=%E7%BE%8E%E5%A5%B3#%E7%BE%8E%E5%A5%B3"

        req=urllib2.Request(url)
        pp=urllib2.urlopen(req)
        # pattern2=re.compile('"thumbLargeUrl" : "(.*?)"')
        pattern2=re.compile('"url":"(.*?)"')
        content=pp.read()
        items1=re.findall(pattern2,content)
        # items2=re.findall(pattern2,content)
        for i in items1:
            # print i
            picture_url=re.findall('(.*?\.jpg)',i)
            if picture_url.__len__() !=0:
                image_url=picture_url[0]
                print image_url
                self.getpicture(image_url)
                print "图片写入成功"

    def getpicture(self,imageurl):
        picture_name=self.generateFileName()+'.jpg'
        filename="D:\\picture"
        u=urllib2.urlopen(imageurl)
        data=u.read()
        picture_path=filename+'\\'+picture_name
        f=open(picture_path,'wb')
        f.write(data)
        f.flush()
        f.close()

    def generateFileName(self):
        return str(uuid.uuid1())

pp=T1()
pp.geturl()