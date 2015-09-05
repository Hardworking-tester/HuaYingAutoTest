#encoding:utf-8
from time import sleep
class BasePage(object):
    def __init__(self,web_driver,web_url):
        self.driver=web_driver
        self.url=web_url
        self.timewait=5

    def open(self):
        self.driver.get(self.url)

    def find_element(self,how,what):

        return self.driver.find_element(how,what)

    def click_element(self,located_element):

        located_element.click()
        sleep(self.timewait)

    def send_data(self,located_element,send_data):
        located_element.send_keys(send_data)
        sleep(self.timewait)

    def close_webdriver(self):
        self.driver.close()