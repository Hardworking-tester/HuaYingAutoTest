# encoding:utf-8
from Data import ReadExcel,get_number_by_data,Get_ExcelPath_SheetName
from  appium.webdriver.common.mobileby import By
class GetElement():

    #得到定位的元素列表以及定位所需的数据,返回的内容包括：元素名称、定位方式，定位所需数据，操作方式，是否需要先定位到元素列表之后再去定位元素
    def getElementList(self,excel_path,name_sheet_list):
        zhuce_excelpath=excel_path
        zhuce_sheet_name=name_sheet_list[0]
        zhuce_element_list=[]
        zhuce_how_what_method_list=[]
        table=ReadExcel.ReadExcel().getTableBySheetName(zhuce_excelpath,zhuce_sheet_name)
        countrows=table.nrows
        for i in range(countrows):
            zhuce_element_list.append(table.cell_value(i,0))
        zhuce_element_list.pop(0)
        # print zhuce_element_list
        for element in zhuce_element_list:
            zhuce_how_what_method_list.append(self.getLocatDataAndMethod(element,zhuce_element_list,excel_path,name_sheet_list))
        # print zhuce_how_what_method_list
        return zhuce_how_what_method_list

    #得到定位所需的数据：定位方式以及定位数据
    def getLocatDataAndMethod(self,element,zhuce_element_list,excel_path,name_sheet_list):
        # path_excel=Get_ExcelPath_SheetName.Get_ExcelPath_SheetName().getExcelPath("F:\\Community_DD\\Data\\zhuce.xls","excelpath_sheetname")
        # name_sheet=(Get_ExcelPath_SheetName.Get_ExcelPath_SheetName().GetSheetName("F:\\Community_DD\\Data\\zhuce.xls","excelpath_sheetname"))[0]
        sheeet=ReadExcel.ReadExcel().getTableBySheetName(excel_path,name_sheet_list[0])
        row_col_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(excel_path,name_sheet_list[0],element)
        old_how=sheeet.cell_value(row_col_index[0],(row_col_index[1]+1))
        what=sheeet.cell_value(row_col_index[0],(row_col_index[1]+2))
        #在这里增加一个字典是因为如果直接把By.ID写在excel里的话，取出来不能用
        locate_method_dict={'id':By.ID,'css':By.CLASS_NAME,'xpath':By.XPATH,'linktext':By.LINK_TEXT,'swipe':'swipe'}
        new_how=locate_method_dict[old_how]
        how_what=[]
        how_what.append(element)
        how_what.append(new_how)
        how_what.append(what)
        how_what.append(self.getOperateMethod(element,excel_path,name_sheet_list))
        how_what.append(self.assertMoreLocate(element,excel_path,name_sheet_list))
        return how_what

    #判断元素是否需要定位到元素列表后再按照排序去找元素
    def assertMoreLocate(self,element,excel_path,name_sheet_list):
        # path_excel=Get_ExcelPath_SheetName.Get_ExcelPath_SheetName().getExcelPath("F:\\Community_DD\\Data\\zhuce.xls","excelpath_sheetname")
        # name_sheet=(Get_ExcelPath_SheetName.Get_ExcelPath_SheetName().GetSheetName("F:\\Community_DD\\Data\\zhuce.xls","excelpath_sheetname"))[0]
        sheet=ReadExcel.ReadExcel().getTableBySheetName(excel_path,name_sheet_list[0])
        row_col_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(excel_path,name_sheet_list[0],element)
        isMoreLocate=sheet.cell_value(row_col_list[0],(row_col_list[1]+3))
        second_Locate_Index=""
        if isMoreLocate=='Y':
            second_Locate_Index=int(sheet.cell_value(row_col_list[0],(row_col_list[1]+4)))
            return second_Locate_Index
        else:
            return 0

    def getOperateMethod(self,element,excel_path,name_sheet_list):

        # path_excel=Get_ExcelPath_SheetName.Get_ExcelPath_SheetName().getExcelPath("F:\\Community_DD\\Data\\zhuce.xls","excelpath_sheetname")
        # name_sheet=(Get_ExcelPath_SheetName.Get_ExcelPath_SheetName().GetSheetName("F:\\Community_DD\\Data\\zhuce.xls","excelpath_sheetname"))[1]
        sheet=ReadExcel.ReadExcel().getTableBySheetName(excel_path,name_sheet_list[1])
        row_col_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(excel_path,name_sheet_list[1],element)
        operate_method_data=sheet.cell_value(row_col_list[0],(row_col_list[1]+1))
        return operate_method_data


