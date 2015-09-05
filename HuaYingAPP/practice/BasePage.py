#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class BasePage():
    def __init__(self,webdriver1,url):
        self.driver=webdriver1
        self.url=url

    def open(self):
        self.driver.get(self.url)

    def findelement(self,how,what):
        return self.driver.find_element(how,what)


    def close21(self):
        self.driver.close()

class extendPage(BasePage):

    def openurl(self):
        self.open()

    def clickelement(self):
        self.findelement(how=By.LINK_TEXT,what=u"请登录").click()
    def inputname(self):
        self.findelement(how=By.ID,what="userName").send_keys("192519517@qq.com")
    def inputpassword(self):
        self.findelement(how=By.ID,what="password").send_keys("wwg06157715")
    def clickButton(self):
        self.findelement(how=By.ID,what='imgLogin')
def main():
    driver2=webdriver.Firefox()
    weburl="http://www.xebest.com"
    s=extendPage(webdriver1=driver2,url=weburl)
    s.openurl()
    s.clickelement()
    s.inputname()
    s.inputpassword()
    s.clickButton()
    s.close21()

if __name__=='__main__':
    main()