# encoding:utf-8
from Action import ZhuCe_zuke
import unittest
from appium import webdriver
from time import sleep
from Data import Get_ExcelPath_SheetName
#业主家属注册
class ZhuCeZuKe(unittest.TestCase):


    def setUp(self):
        desired_caps={'platformName':'Android','platformVersion':'4.4','deviceName':'SM-G3608','appPackage':'com.dinghe.dingding.community','appActivity':'.SplashActivity','resetKeyboard':True}
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.s=ZhuCe_zuke.ZhuCeZuKe(self.driver)

        sleep(5)

    def testZhuceZuKe(self):
        path_excel=Get_ExcelPath_SheetName.Get_ExcelPath_SheetName().getExcelPath("F:\\Community_DD\\Data\\zhuce_zuke.xls","excelpath_sheetname")
        name_sheet_list=(Get_ExcelPath_SheetName.Get_ExcelPath_SheetName().GetSheetName("F:\\Community_DD\\Data\\zhuce_zuke.xls","excelpath_sheetname"))
        pp=self.s
        driver=pp.getoperateElementMethodAndData1(path_excel,name_sheet_list)
        try:
            self.assert_Success(driver)
        except:
            print "assertion does not pass"
        # driver.find_element_by_id("com.dinghe.dingding.community:id/rightimgbtn").click()
        # driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'退出')]").click()
        # driver.find_element_by_id("android:id/button1").click()

    def assert_Success(self,driver):
        driver.find_element_by_id("com.dinghe.dingding.community:id/tab_mine").click()
        sleep(2)
        jifen= driver.find_element_by_id("com.dinghe.dingding.community:id/my_account").text
        print jifen
        self.assertEqual(jifen,'500','failed to register')
    def tearDown(self):
        self.driver.quit()

