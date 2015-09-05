# encoding:utf-8
from appium import webdriver
from time import sleep
# from selenium import webdriver
# desired_caps={'platformName':'Android','platformVersion':'4.4','deviceName':'Android Emulator','appPackage':'com.bd.community','appActivity':'com.bd.community.SplashActivity'}
# desired_caps={'platformName':'Android','platformVersion':'4.4.2','deviceName':'HONOR H30-L02','appPackage':'com.bd.community','appActivity':'com.bd.community.SplashActivity'}
# desired_caps={'platformName':'Android','platformVersion':'4.4.4','deviceName':'SM-G3608','appPackage':'com.bd.community','appActivity':'com.bd.community.SplashActivity'}
# desired_caps={'platformName':'Android','platformVersion':'4.1','deviceName':'MI 2','appPackage':'com.bd.community','appActivity':'com.bd.community.SplashActivity'}
desired_caps={'platformName':'Android','platformVersion':'4.4.4','deviceName':'HUAWEI C8817E','appPackage':'com.bd.community','appActivity':'com.bd.community.SplashActivity','unicodeKeyboard':True,'resetKeyboard':True}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
sleep(5)
for i in range(1,11):
    driver.find_element_by_id("com.bd.community:id/login_loginaccount").send_keys("15093492821")#用户名输入框
    sleep(2)
    driver.find_element_by_id("com.bd.community:id/edittext").send_keys("11111111")#密码输入框
    sleep(2)
    # driver.find_element_by_id("com.bd.community:id/loginRememberMeCheckBox").click()#是否记住密码复选框
    driver.find_element_by_id("com.bd.community:id/login").click()#登录按钮
    sleep(5)
    driver.swipe(13,871,346,853)
    sleep(2)
    driver.find_element_by_id("com.bd.community:id/main_te6").click()
    sleep(2)
    driver.find_element_by_id("android:id/button1").click()
    sleep(2)
    print "第%s次登录退出动作完成" %i
# driver.switch_to.context('WEBVIEW_com.bd.community')
# elements=driver.find_element_by_id("addCartItemButton")
# elements.click()
# elements.click()
# print elements
# print driver.contexts
# print driver.current_context