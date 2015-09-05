# encoding:utf-8
from appium import webdriver
from Base.APPBasePage import APPBasePage
from Data import GetData,GetElement,ReadExcel,Get_ExcelPath_SheetName

#业主家属注册
class ZhuCeYeZhuJiaShu(APPBasePage):

    #得到定位元素的数据：元素名称、定位方式、定位数据、操作方法、是否需要定位到多个元素组后再次定位该元素
    def getoperateElementMethodAndData1(self,path_excel,name_sheet_list):

        how_what_list=GetElement.GetElement().getElementList(path_excel,name_sheet_list)
        # print how_what_list
        for method_data_list in how_what_list:
            app_object=method_data_list[0]
            how=method_data_list[1]
            what=method_data_list[2]
            operate_method=method_data_list[3]
            moreLocateFlag=method_data_list[4]

            if moreLocateFlag==0:
                self.locateElement(app_object,how,what,operate_method,path_excel,name_sheet_list)
            else:
                self.locateElements(app_object,how,what,operate_method,moreLocateFlag,path_excel,name_sheet_list)
        return self.driver
    #定位单个元素
    def locateElement(self,app_object,how,what,operate_method,path_excel,name_sheet_list):
        located_element=self.find_element(how,what)
        # print located_element
        # print operate_method
        if operate_method=='click':
            self.extend_click_element(located_element)
        elif operate_method=='sendkey':
            send_data=GetData.GetData().getData(app_object,path_excel,name_sheet_list)
            self.extend_send_data(located_element,send_data)

    #定位元素组
    def locateElements(self,app_object,how,what,operate_method,index,path_excel,name_sheet_list):
        located_element=self.find_elements(how,what,index)
        # print located_element
        # print operate_method
        if operate_method=='click':
            self.extend_click_element(located_element)
        elif operate_method=='sendkey':
            send_data=GetData.GetData().getData(app_object,path_excel,name_sheet_list)
            self.extend_send_data(located_element,send_data)


    def extend_click_element(self,located_element):
        self.click_element(located_element)

    def extend_send_data(self,located_element,send_data):
        self.send_data(located_element,send_data)