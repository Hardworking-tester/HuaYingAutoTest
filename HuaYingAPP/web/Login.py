#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import Case
from Base import WebBasePage
import GegNeedOperateElment,GetSendData
import time
class Login(WebBasePage):




    def openweb(self):
        self.open()



    def getoperateElementMethodAndData(self):
        how_what_list=GegNeedOperateElment.GetOperateElement().getElmentList()
        print how_what_list
        for method_data_list in how_what_list:
            html_object=method_data_list[0]
            how=method_data_list[1]
            what=method_data_list[2]
            operate_method=method_data_list[3]
            self.locateElement(html_object,how,what,operate_method)



    def locateElement(self,html_object,how,what,operate_method):
        located_element=self.find_element(how,what)
        if operate_method=='click':
            self.extend_click_element(located_element)
        elif operate_method=='sendkey':
            send_data=GetSendData.GetSendData().getData(html_object)
            self.extend_send_data(located_element,send_data)

    def extend_click_element(self,located_element):
        self.click_element(located_element)

    def extend_send_data(self,located_element,send_data):
        self.send_data(located_element,send_data)




