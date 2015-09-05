# encoding:utf-8
from Base.APPBasePage import APPBasePage
from Data import get_number_by_data,ReadExcel,Get_ExcelPath_SheetName,GetElement,GetData
class Login(APPBasePage):

    #得到定位元素的数据：元素名称、定位方式、定位数据、操作方法、是否需要定位到多个元素组后再次定位该元素
    def getElement_Method_Data(self,excel_path,sheet_name_list):
        how_what_method_list=GetElement.GetElement().getElementList(excel_path,sheet_name_list)
        for data_list in how_what_method_list:
            element_name=data_list[0]
            locate_how=data_list[1]
            locate_what=data_list[2]
            operate_method=data_list[3]
            moreLocate_flag=data_list[4]
            if moreLocate_flag==0:
                self.locateElement(locate_how,locate_what,operate_method,excel_path,sheet_name_list,element_name)
            else:
                self.locatedElements(locate_how,locate_what,operate_method,excel_path,sheet_name_list,element_name,moreLocate_flag)

        return self.driver

    def locateElement(self,locate_how,locate_what,operate_method,excel_path,sheet_name_list,element_name):
        located_element=self.find_element(locate_how,locate_what)
        if operate_method=='click':
            self.extend_click_element(located_element)
        elif operate_method=='sendkey':
            send_data=GetData.GetData().getData(element_name,excel_path,sheet_name_list)
            self.extend_send_data(located_element,send_data)

    def locatedElements(self,locate_how,locate_what,operate_method,excel_path,sheet_name_list,element_name,moreLocate_flag):
        located_element=self.find_elements(locate_how,locate_what,moreLocate_flag)
        if operate_method=='click':
            self.extend_click_element(located_element)
        elif operate_method=='sendkey':
            send_data=GetData.GetData().getData(element_name,excel_path,sheet_name_list)
            print send_data
            self.extend_send_data(located_element,send_data)

    def extend_click_element(self,located_element):
        self.click_element(located_element)

    def extend_send_data(self,located_element,send_data):
        self.send_data(located_element,send_data)