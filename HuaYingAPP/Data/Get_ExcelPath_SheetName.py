# encoding:utf-8
import ReadExcel
class Get_ExcelPath_SheetName():

    def getExcelPath(self,excelpath,sheetName):

        excel_path=excelpath
        sheet_name=sheetName
        table=ReadExcel.ReadExcel().getTableBySheetName(excel_path,sheet_name)
        excelpath=table.cell_value(1,0)

        return excelpath


    def GetSheetName(self,excelpath,sheetName):
        excel_path=excelpath
        sheet_name=sheetName
        table=ReadExcel.ReadExcel().getTableBySheetName(excel_path,sheet_name)
        sheetname=[]
        rows=table.nrows
        for i in range(1,rows):
            sheetname.append(table.cell_value(i,1))

        return sheetname


