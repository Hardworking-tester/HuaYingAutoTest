#encoding:utf-8
import xlrd
from Data import ReadExcel,get_number_by_data
from selenium.webdriver.common.by import By
class GetOperateElement():
    def getElmentList(self):
        login_excel_path=r"F:\AutotestCode\Data\login_data.xls"
        login_sheetname="objname_locatemethod_locatedata"
        sheet=ReadExcel.ReadExcel().getTableBySheetName(login_excel_path,login_sheetname)
        login_element_list=[]
        how_what_operateMethod_list=[]
        login_element_rows=sheet.nrows
        for i in range(login_element_rows):
            login_element_list.append(sheet.cell_value(i,0))

        login_element_list.pop(0)
        for element in login_element_list:
            how_what_operateMethod_list.append(self.getLocateMethodAndValue(login_element_list,element))

        return how_what_operateMethod_list
        # print login_element_list

    #得到需要定位的元素的方法以及定位所需的值
    def getLocateMethodAndValue(self,login_data_list,login_object):
        login_excel_path=r"F:\AutotestCode\Data\login_data.xls"
        login_sheetname="objname_locatemethod_locatedata"
        sheet=ReadExcel.ReadExcel().getTableBySheetName(login_excel_path,login_sheetname)
        row_col_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(login_excel_path,login_sheetname,login_object)
        old_how=sheet.cell_value(row_col_list[0],(row_col_list[1]+1))
        what=sheet.cell_value(row_col_list[0],(row_col_list[1]+2))
        #在这里增加一个字典是因为如果直接把By.ID写在excel里的话，取出来不能用
        locate_method_dict={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT}
        new_how=locate_method_dict[old_how]
        how_what=[]
        how_what.append(login_object)
        how_what.append(new_how)
        how_what.append(what)
        how_what.append(self.getOperateMethod(login_object))
        return how_what
        # print how_what
    def getOperateMethod(self,login_object):
        login_excel_path=r"F:\AutotestCode\Data\login_data.xls"
        login_sheetname="operate_method"
        sheet=ReadExcel.ReadExcel().getTableBySheetName(login_excel_path,login_sheetname)
        row_col_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(login_excel_path,login_sheetname,login_object)
        operate_method=sheet.cell_value(row_col_list[0],(row_col_list[1]+1))
        return operate_method

