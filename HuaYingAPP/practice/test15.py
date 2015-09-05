# encoding:utf-8
from appium import webdriver
from time import sleep
from Data import get_number_by_data,ReadExcel


desired_caps={'platformName':'Android','platformVersion':'4.4','deviceName':'SM-G3608','appPackage':'com.dinghe.dingding.community','appActivity':'.SplashActivity','unicodeKeyboard':True,'resetKeyboard':True}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(10)
driver.find_element_by_id("com.dinghe.dingding.community:id/tv_fangwuzushou").click()
sleep(2)
driver.find_element_by_id("com.dinghe.dingding.community:id/et_describe").send_keys('我要租售房子'.decode('utf-8'))

sleep(2)
# driver.find_element_by_id("com.dinghe.dingding.community:id/iv_getImg_05").click()
# sleep(2)
driver.find_element_by_id("com.dinghe.dingding.community:id/tv_commit").click()
driver.get_screenshot_as_file("F:\\testresult\\pp.jpg")
#
# sleep(2)
#
# driver.find_element_by_id("com.dinghe.dingding.community:id/tab_mine").click()
# driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'我的账号')]").click()
# sleep(2)
# driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'房屋租售')]").click()
# pp=driver.find_elements_by_id("com.dinghe.dingding.community:id/tv_content")
