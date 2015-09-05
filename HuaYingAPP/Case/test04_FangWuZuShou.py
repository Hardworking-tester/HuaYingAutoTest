# encoding:utf-8
import unittest
from Action import FangWuZuShou
from Data import get_number_by_data,ReadExcel,GetElement,Get_ExcelPath_SheetName
from appium import webdriver
from time import sleep
class FangWZShouTest(unittest.TestCase):

    def setUp(self):
        desired_caps={'platformName':'Android','platformVersion':'4.4','deviceName':'SM-G3608','appPackage':'com.dinghe.dingding.community','appActivity':'SplashActivity','unicodeKeyboard':True,'resetKeyboard':True}
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.s=FangWuZuShou.FangWuZuShou(self.driver)
        sleep(10)

    def testFangWuZuShou(self):
        pp=self.s
        excel_path=Get_ExcelPath_SheetName.Get_ExcelPath_SheetName().getExcelPath("F:\\Community_DD\\Data\\fangwuzushou.xls","excelpath_sheetname")
        sheet_name_list=Get_ExcelPath_SheetName.Get_ExcelPath_SheetName().GetSheetName("F:\\Community_DD\\Data\\fangwuzushou.xls","excelpath_sheetname")
        driver=pp.getElement_Method_Data(excel_path,sheet_name_list)
        print driver
        self.assertSuccess(driver)
    def assertSuccess(self,driver):
        driver.find_element_by_id("com.dinghe.dingding.community:id/tab_mine").click()
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'我的账号')]").click()
        sleep(2)
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'房屋租售')]").click()
        count_jilu=driver.find_elements_by_id("com.dinghe.dingding.community:id/tv_content")
        if count_jilu.__len__()>0:
            print "success submit fagnwuzuzhou"
        else:
            print "failed submit fagnwuzuzhou"
        driver.keyevent(4)
    def tearDown(self):
        self.driver.quit()

