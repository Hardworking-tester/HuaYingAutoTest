#encoding:utf-8
import xlrd
from Data import ReadExcel,get_number_by_data
class GetSendData():
    def getData(self,element_key):
        login_excel_path=r"F:\AutotestCode\Data\login_data.xls"
        login_sheetname="username_password_data"
        sheet=ReadExcel.ReadExcel().getTableBySheetName(login_excel_path,login_sheetname)
        row_col_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(login_excel_path,login_sheetname,element_key)
        data=sheet.cell_value(row_col_list[0]+1,(row_col_list[1]))
        return data
