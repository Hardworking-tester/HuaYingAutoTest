# encoding:utf-8
from Data import get_number_by_data,ReadExcel,Get_ExcelPath_SheetName
class GetData():

    def getData(self,element_key,path_excel,name_sheet_list):
        # path_excel=Get_ExcelPath_SheetName.Get_ExcelPath_SheetName().getExcelPath("F:\\Community_DD\\Data\\zhuce.xls","excelpath_sheetname")
        # name_sheet=(Get_ExcelPath_SheetName.Get_ExcelPath_SheetName().GetSheetName("F:\\Community_DD\\Data\\zhuce.xls","excelpath_sheetname"))[2]
        sheet=ReadExcel.ReadExcel().getTableBySheetName(path_excel,name_sheet_list[2])
        row_col_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(path_excel,name_sheet_list[2],element_key)
        data=sheet.cell_value(row_col_list[0]+1,(row_col_list[1]))
        if type(data)==float:
            return  int(data)
        else:
            return data
