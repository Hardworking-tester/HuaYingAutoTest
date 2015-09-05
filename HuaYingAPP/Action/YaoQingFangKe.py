# encoding:utf-8
from Data import GetData,Get_ExcelPath_SheetName,GetElement,ReadExcel,get_number_by_data
from appium import webdriver
from Base.APPBasePage import APPBasePage

#邀请访客功能
class YaoQingFangKe(APPBasePage):

    #得到定位元素的数据：元素名称、定位方式、定位数据、操作方法、是否需要定位到多个元素组后再次定位该元素
    def getElement_Method_Data(self,excel_path,sheet_name_list):
        how_what_method_list=GetElement.GetElement().getElementList(excel_path,sheet_name_list)
        for dataList in how_what_method_list:
            element_name=dataList[0]
            how=dataList[1]
            what=dataList[2]
            operate_method=dataList[3]
            more_locate_flag=dataList[4]
            if more_locate_flag==0:
                self.locateElement(element_name,how,what,operate_method,excel_path,sheet_name_list)
            else:
                self.locateElements(element_name,how,what,operate_method,more_locate_flag,excel_path,sheet_name_list)

        return self.driver

    def locateElement(self,element_name,how,what,operate_method,excel_path,sheet_name_list):
        located_element=self.find_element(how,what)
        if operate_method=='click':
            self.extendClick(located_element)
        elif operate_method=='sendkey':
            send_data=GetData.GetData().getData(element_name,excel_path,sheet_name_list)
            self.extendSendData(located_element,send_data)

    def locateElements(self,element_name,how,what,operate_method,more_locate_flag,excel_path,sheet_name_list):
        located_element=self.find_elements(how,what,more_locate_flag)
        if operate_method=='click':
            self.extendClick(located_element)
        elif operate_method=='sendkey':
            send_data=GetData.GetData().getData(element_name,excel_path,sheet_name_list)
            self.extendSendData(located_element,send_data)

    def extendClick(self,located_element):
        self.click_element(located_element)

    def extendSendData(self,located_element,send_data):
        self.send_data(located_element,send_data)