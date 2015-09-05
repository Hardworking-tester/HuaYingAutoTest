#encoding:utf-8
from pyadb import ADB
from appium import webdriver
import os
from time import sleep

desired_caps={"platformName":"Android","platformVersion":"4.4.4","deviceName":"HUAWEI C8817E","appPackage":"com.bd.community","appActivity":"com.bd.community.SplashActivity",'unicodeKeyboard':True,
'resetKeyboard':True}
# desired_caps={"platformName":"Android","platformVersion":"4.4.4","deviceName":"SM-G3608","appPackage":"com.bd.community","appActivity":"com.bd.community.SplashActivity"}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(5)
# print driver.network_connection#获取设备网络状态
driver.find_element_by_id("com.bd.community:id/login_loginaccount").send_keys("wwg2")#用户名输入框
sleep(2)
# os.popen("adb shell")
# os.popen("ime set com.baidu.input_huawei/.ImeService")
# sleep(20)
driver.find_element_by_id("com.bd.community:id/login_loginpassword").send_keys("1")#密码输入框
sleep(2)
driver.find_element_by_id("com.bd.community:id/loginRememberMeCheckBox").click()#是否记住密码复选框
driver.find_element_by_id("com.bd.community:id/login").click()#登录按钮
sleep(3)
driver.find_element_by_id("com.bd.community:id/fl_shopping").click()
sleep(3)
driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'猪蹄')]").click()
# print driver.page_source
# sleep(3)
# print driver.contexts


# driver.find_element_by_id("com.bd.community:id/login_register").click()
# driver.find_element_by_id("com.bd.community:id/zcone_re2").click()
# sleep(2)
# driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'五行嘉园')]").click()
# sleep(2)
# driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'二单元')]").click()
# sleep(2)
# driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'1901')]").click()
# sleep(2)
# driver.find_element_by_id("com.bd.community:id/zhuce_next1").click()
# sleep(2)
# driver.find_element_by_id("com.bd.community:id/zcone_sfqr_Et1").send_keys(1)
# driver.find_element_by_id("com.bd.community:id/zcone_sfqr_Et2").send_keys(3)
# driver.find_element_by_id("com.bd.community:id/zcone_sfqr_Et3").send_keys(5)
# driver.find_element_by_id("com.bd.community:id/zcone_sfqr_Et4").send_keys(3)
# driver.find_element_by_id("com.bd.community:id/zhuce_two_next").click()
# sleep(3)
# driver.find_element_by_id("com.bd.community:id/zcone_three_name").send_keys(u"王伟高")

# driver.keyevent(82)
# driver.find_element_by_id("com.bd.community:id/main_te6").click()
# sleep(2)
# driver.find_element_by_id("android:id/button1").click()
# driver.find_element_by_id("com.bd.community:id/home_tab_fwsq").click()
# sleep(2)
# driver.find_element_by_id("com.bd.community:id/tv_wuye_fee").click()
# sleep(2)
# driver.find_element_by_id("com.bd.community:id/et_start_time").click()
# sleep(2)
# # driver.tap([(143,827)])
# driver.find_element_by_xpath("//android.widget.NumberPicker[contains(@text,'2019年')]/android.widget.Button[contains(@index,'请输入邮箱或手机号码')]").click()
# # element1=driver.find_element_by_xpath("//android.widget.EditText[contains(@index,'请输入邮箱或手机号码')]").send_keys('192519517@qq.com')
