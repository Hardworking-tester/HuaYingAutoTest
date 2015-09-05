# encoding:utf-8
from Action import YaoQingFangKe
from Data import  ReadExcel,get_number_by_data,GetElement,Get_ExcelPath_SheetName,GetData
from appium import webdriver
import unittest
from time import sleep
class YaoQingFangKeTest(unittest.TestCase):

    def setUp(self):
        desired_caps={'platformName':'Android','platformVersion':'4.4','deviceName':'SM-G3608','appPackage':'com.dinghe.dingding.community','appActivity':'.SplashActivity','resetKeyboard':True}
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.s=YaoQingFangKe.YaoQingFangKe(self.driver)
        sleep(10)
    def testYaoQingFangKe(self):
        excel_path=Get_ExcelPath_SheetName.Get_ExcelPath_SheetName().getExcelPath("F:\Community_DD\Data\\fangke.xls","excelpath_sheetname")
        sheet_name_list=Get_ExcelPath_SheetName.Get_ExcelPath_SheetName().GetSheetName("F:\Community_DD\Data\\fangke.xls","excelpath_sheetname")
        pp=self.s
        driver=pp.getElement_Method_Data(excel_path,sheet_name_list)
        print driver
        self.assertSuccess(driver)

    def assertSuccess(self,driver):
        driver.keyevent(4)
        element_count=driver.find_elements_by_id("com.dinghe.dingding.community:id/tv_caozuo")
        if element_count.__len__()>0:
            print "success yaoqingfangke"
        else:
            print "failed yaoqingfangke"


    def tearDown(self):
        self.driver.quit()

