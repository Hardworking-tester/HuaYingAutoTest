# encoding:utf-8
from appium import webdriver
from time import sleep
desired_caps={'platformName':'Android','platformVersion':'4.4','deviceName':'SM-G3608','appPackage':'com.dinghe.dingding.community','appActivity':'.SplashActivity','unicodeKeyboard':True,'resetKeyboard':True}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(10)


# driver.find_element_by_id("com.dinghe.dingding.community:id/tv_liangpintuangou").click()
# sleep(2)
# # print driver.page_source
# driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'猪肉1')]").click()
# print driver.page_source
# driver.quit()

driver.get_screenshot_as_file("F:\\testresult\\pp.jpg")