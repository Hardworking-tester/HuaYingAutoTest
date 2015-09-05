#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
class Page(object):

    kb_url = 'http://www.xebest.com'
    def __init__(self, selenium_driver, base_url=kb_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent
        self.tabs = {}
    def _open(self,url):
        url = self.base_url
        self.driver.get(url)
        # assert self.on_page(),'Did not land on %s' % url
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    def open(self):
        self._open(self.url)
    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)
    def script(self,src):
        return self.driver.execute_script(src)
    def send_keys(self,loc,value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, '_%s' % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
                print '%s page does not have "%s" locator' %(self,loc)
class LoginPage(Page):
    url = 'http://www.xebest.com'
    login_link=(By.LINK_TEXT,u"请登录")
    username_loc = (By.ID,"userName")
    password_loc = (By.ID,"password")
    submit_loc = (By.ID,"imgLogin")
    #Action
    def open(self):
        self._open(self.url)
    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)
    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)
    def submit(self):
        self.find_element(*self.submit_loc).click()

def test_user_login(driver, username, password):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()
    sleep(3)
    # assert(username == 'pysetest'),u"用户名称不匹配，登录失败!"

def main():

        # Selenium
        driver = webdriver.Firefox()
        firstlink=u"请登录"
        username = '192519517@qq.com'
        password = 'wwg06157715'
        test_user_login(driver, username, password)

        driver.close()
if __name__ == '__main__':
        main()