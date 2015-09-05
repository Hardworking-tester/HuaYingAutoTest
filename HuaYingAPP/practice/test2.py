#encoding:utf-8
from appium import webdriver
import os
from time import sleep
desired_caps={"platformName":"Android","platformVersion":"4.4.4","deviceName":"HUAWEI C8817E","appPackage":"com.bd.community","appActivity":"com.bd.community.SplashActivity"}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(5)

driver.find_element_by_id("com.bd.community:id/login_loginaccount").send_keys("wwg2")#用户名输入框
sleep(2)

driver.find_element_by_id("com.bd.community:id/login_loginpassword").send_keys("1")#密码输入框
sleep(2)
driver.find_element_by_id("com.bd.community:id/loginRememberMeCheckBox").click()#是否记住密码复选框
driver.find_element_by_id("com.bd.community:id/login").click()#登录按钮
sleep(3)

driver.find_element_by_id("com.bd.community:id/fl_tousu").click()
sleep(3)
driver.find_element_by_id("com.bd.community:id/et_describe").send_keys("my name is hhh")
driver.find_element_by_id("com.bd.community:id/tv_commit").click()
sleep(5)
driver.find_element_by_id("com.bd.community:id/home_tab_gjzx").click()
driver.find_element_by_id("com.bd.community:id/home_tab_fwsq").click()
sleep(3)
driver.find_element_by_id("com.bd.community:id/tv_wuye_guanjia").click()
sleep(2)
driver.find_element_by_id("com.bd.community:id/jzfw_top_layout_01").click()
driver.find_element_by_id("com.bd.community:id/tv_room_sale").click()
driver.find_element_by_id("com.bd.community:id/et_describe").send_keys("wgsdfsafdsdf")
driver.find_element_by_id("com.bd.community:id/tv_commit").click()
sleep(5)
driver.find_element_by_id("com.bd.community:id/home_tab_sqsw").click()
sleep(1)
driver.find_element_by_id("com.bd.community:id/tv_zhanghao").click()
sleep(2)
elements=driver.find_elements_by_class_name("android.widget.TextView")
elements[1].click()
sleep(2)
driver.find_element_by_id("com.bd.community:id/jzfw_top_layout_01").click()
sleep(2)
elements[2].click()
sleep(2)
driver.find_element_by_id("com.bd.community:id/zbyh_top_layout_01").click()
sleep(2)
elements[3].click()
sleep(2)
driver.find_element_by_id("com.bd.community:id/zbyh_top_layout_01").click()
sleep(2)
elements[4].click()
driver.find_element_by_id("com.bd.community:id/zbyh_top_layout_01").click()
sleep(2)
elements[6].click()
driver.find_element_by_id("com.bd.community:id/jzfw_top_layout_01").click()
sleep(2)
driver.find_element_by_id("com.bd.community:id/person_account_top_layout_01").click()
sleep(2)
driver.find_element_by_id("com.bd.community:id/home_tab_sqxx").click()
sleep(2)