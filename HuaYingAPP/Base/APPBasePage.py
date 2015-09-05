# encoding:utf-8
from appium import webdriver
from time import sleep
class APPBasePage(object):
    def __init__(self,driver):
        self.driver=driver
        self.timeWait=2
        # print self.driver


    def find_element(self,how,what):
        # print how,what
        return self.driver.find_element(how,what)

    def find_elements(self,how,what,index):
        # print how,what
        return self.driver.find_elements(how,what)[index]

    def get_text(self,located_element):

        return located_element.text

    def click_element(self,located_element):

        located_element.click()
        sleep(self.timeWait)

    def huaDong(self,startX,startY,endX,endY):
        self.driver.swipe(startX,startY,endX,endY)
        sleep(self.timeWait)
    def send_data(self,located_element,send_data):
        print send_data
        located_element.send_keys(send_data)
        try:
            self.driver.hide_keyboard()
        except:
            pass
        # sleep(self.timeWait)