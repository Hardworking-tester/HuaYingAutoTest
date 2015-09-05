#encoding:utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'HONOR H30-L02'
# desired_caps['app'] = r'D:\tmall_4.9.2_10002119.apk'
# desired_caps['app'] = r'D:\eshop.apk'
# desired_caps['app'] = r'D:\epay.apk'
desired_caps['appPackage'] = 'com.xebest'
desired_caps['appActivity'] = 'com.xebest.activity.SplashActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(10)
# driver.install_app(r"D:\epay.apk")
# driver.close_app()
# element1=driver.find_element_by_xpath("//android.widget.EditText[contains(@index,'请输入邮箱或手机号码')]")#.send_keys('192519517@qq.com')
# element1=driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.xebest:id/login_input_name']")#.send_keys('192519517@qq.com')
# print element1.text
# time.sleep(5)
# driver.find_element_by_id("com.xebest:id/login_input_name").send_keys("192519517@qq.com")#用户名
# time.sleep(2)
# driver.find_element_by_id("com.xebest:id/login_input_password").send_keys("wwg06157715")#密码
# time.sleep(2)
# driver.find_element_by_id("com.xebest:id/login_btn").click()#登录按钮
# time.sleep(10)
# driver.find_element_by_id("com.xebest:id/navi_item_wode").click()
# time.sleep(10)
# element1=driver.find_element_by_id("com.xebest:id/wode_yue")
# driver.long_press(element1)
# TouchAction(driver).long_press(element1,duration=10000).perform()
# print driver.is_app_installed("com.xebest")
# driver.lock(5)
# elements=driver.find_elements_by_class_name("android.widget.EditText")
# driver.find_element_by_class_name("android.widget.EditText").send_keys("192519517@qq.com")
# driver.find_element_by_class_name("android.widget.EditText").send_keys("wwg06157715")
# print elements[0].text
# print elements[1].text
# print elements.__len__()
# element1=driver.find_element_by_class_name("android.widget.Button")
# print elements


# elements[0].send_keys("192519517@qq.com")
# elements[1].send_keys("wwg06157715")
# element1=driver.find_element_by_xpath("//android.widget.EditText[1]")
# element2=driver.find_element_by_xpath("//android.widget.EditText[2]")
# print element1
# print element2
#正确的xpath定位方式
elements=driver.find_elements_by_xpath("//android.widget.EditText")
elements[0].send_keys("192519517@qq.com")
elements[1].send_keys("wwg06157715")
print elements