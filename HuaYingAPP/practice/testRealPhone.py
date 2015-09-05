#encoding:utf-8
from appium import webdriver
import os
from time import sleep
desired_caps={"platformName":"Android","platformVersion":"4.4.4","deviceName":"HUAWEI C8817E","appPackage":"com.jiudao.ccare","appActivity":".MainActivity"}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
print driver.contexts
sleep(5)
# driver.switch_to.context("webview")
# element=driver.find_element_by_id("username")
# print element
# print driver.page_source
# sleep(5)
# element=driver.find_element_by_xpath("//android.webkit.WebView[contains(@index,0)]//android.view.View[contains(@index,1)]//android.widget.EditText[contains(@index,1)]")
# element.send_keys("wwg")
element=driver.find_element_by_id("username")
print element






from appium import webdriver
import time
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '4.4.2'
# # desired_caps['deviceName'] = 'Android Emulator'
# desired_caps['deviceName'] = 'HONOR H30-L02'
# desired_caps['appPackage'] = 'com.xebest'
# desired_caps['appActivity'] = 'com.xebest.activity.SplashActivity'
#
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# time.sleep(5)
# print driver.context
# driver.find_element_by_id("com.xebest:id/login_input_name").send_keys("192519517@qq.com")#用户名
# time.sleep(2)
# driver.find_element_by_id("com.xebest:id/login_input_password").send_keys("wwg06157715")#密码
# time.sleep(2)
# driver.find_element_by_id("com.xebest:id/login_btn").click()#登录按钮
# time.sleep(10)
# print driver.get_window_size()['width']
# print driver.get_window_size()['height']
# driver.find_element_by_id("com.xebest:id/public_head_mxcx").click()
# driver.tap([(571,182)])
# time.sleep(5)
# driver.press_keycode(4)
# driver.keyevent(4)
# driver.find_element_by_id("com.xebest:id/yue_tixian").click()#提现按钮
# driver.find_element_by_id("com.xebest:id/tixian_money").send_keys("0.01")#提现金额输入框
# driver.find_element_by_id("com.xebest:id/tixian_payTypePwd").send_keys("wwg004218")#提现密码输入框
# driver.hide_keyboard()#由于调出的输入法阻挡元素定位，所以需要在点击按钮之前把输入法隐藏
# driver.find_element_by_id("com.xebest:id/tixian_btn_queren").click()#确认提现按钮
