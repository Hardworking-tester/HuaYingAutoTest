#encoding:utf-8
from pyadb import ADB
from appium import webdriver
import os
from time import sleep
desired_caps={"platformName":"Android","platformVersion":"4.4.4","deviceName":"HUAWEI C8817E","appPackage":"com.android.chrome","appActivity":"com.google.android.apps.chrome.Main"}
# desired_caps={"platformName":"Android","platformVersion":"4.4.4","deviceName":"SM-G3608","appPackage":"com.bd.community","appActivity":"com.bd.community.SplashActivity"}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
print driver.contexts
print driver.current_context
driver.switch_to.context("WEBVIEW_1")
driver.find_element_by_id("com.android.chrome:id/search_box_text").send_keys("www.baidu.com")