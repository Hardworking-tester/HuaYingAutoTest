# encoding:utf-8
import unittest
from Action import Login
from Data import get_number_by_data,ReadExcel,GetElement,Get_ExcelPath_SheetName
from appium import webdriver
from time import sleep
class LoginTest(unittest.TestCase):

    def setUp(self):
        desired_caps={'platformName':'Android','platformVersion':'4.4','deviceName':'SM-G3608','appPackage':'com.dinghe.dingding.community','appActivity':'SplashActivity','resetKeyboard':True}
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.s=Login.Login(self.driver)
        sleep(5)

    def testLogin(self):
        pp=self.s
        excel_path=Get_ExcelPath_SheetName.Get_ExcelPath_SheetName().getExcelPath("F:\\Community_DD\\Data\\login.xls","excelpath_sheetname")
        sheet_name_list=Get_ExcelPath_SheetName.Get_ExcelPath_SheetName().GetSheetName("F:\\Community_DD\\Data\\login.xls","excelpath_sheetname")
        driver=pp.getElement_Method_Data(excel_path,sheet_name_list)
        self.assertLoginSuccess(driver)
    def assertLoginSuccess(self,driver):

        if driver.find_element_by_id("com.dinghe.dingding.community:id/tab_mine"):
            print '登录成功'
        else:
            print '登录失败'

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()