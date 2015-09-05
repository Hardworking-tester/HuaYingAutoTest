#encoding:utf-8
from Data import ReadExcel
from Log import SendLog
import urllib2,urllib

class HttpPost():

    def getPostUrl(self,row_index,col_index):
        """
        得到提交请求的地址
        """
        excel_path="E:\\testData\\interface_test.xls"
        post_url=ReadExcel.ReadExcel().getValue(excel_path,row_index,col_index)
        return post_url
    def getPostData(self,row_index,col_index):
        """
        得到提交请求的数据
        """
        excel_path="E:\\testData\\interface_test.xls"
        post_data=ReadExcel.ReadExcel().getValue(excel_path,row_index,col_index)
        return post_data

    def getRows(self):
        """
        得到本次测试内容的总行数
        """
        excel_path="E:\\testData\\interface_test.xls"
        rows=ReadExcel.ReadExcel().getExcelRows(excel_path)
        return rows
    def sendPostRepuest(self):
        """
        发送post请求并接受返回内容
        """
        rows=self.getRows()
        for i in range(1,rows):
            post_url=self.getPostUrl(i,0)
            first_post_data=eval(self.getPostData(i,1))
            post_data=urllib.urlencode(first_post_data)
            req=urllib2.Request(post_url,post_data)
            rep=urllib2.urlopen(req)
            result=rep.read()
            self.writeLog(post_url,post_data,result)
    def writeLog(self,post_url,post_data,result):
        """
        把请求地址，发送数据，接口返回值写入log
        """
        log=SendLog.ResultLog().writeLog()
        log.info("测试地址为：%s，发送的测试数据为：%s，返回的测试结果为：%s" %(post_url.encode('utf-8'),post_data.encode('utf-8'),result))




pp=HttpPost()
pp.sendPostRepuest()
