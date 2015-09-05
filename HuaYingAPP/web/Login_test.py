#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from Action import Login
class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.url="http://www.xebest.com"
        self.s=Login.Login(self.driver,self.url)


    def testlogin(self):
        pp=self.s
        pp.openweb()
        pp.getoperateElementMethodAndData()
        # br=self.driver
        # br.find_element_by_link_text(u"请登录")
        print "wwg"

    def tearDown(self):
        # self.driver.quit()
        pass
if __name__=='__main__':
    unittest.main()