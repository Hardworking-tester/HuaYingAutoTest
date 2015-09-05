#encoding:utf-8
from appium import webdriver
from appium.webdriver import webelement
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
# desired_caps['deviceName'] = 'Android Emulator'
desired_caps['deviceName'] = 'HONOR H30-L02'
# desired_caps['app'] = r'D:\tmall_4.9.2_10002119.apk'
desired_caps['appPackage'] = 'com.xebest'
desired_caps['appActivity'] = 'com.xebest.activity.SplashActivity'
# desired_caps['autoLaunch'] = 'false'
# desired_caps['appPackage'] = 'com.tmall.wireless'
# desired_caps['appActivity'] = 'com.tmall.wireless.module.search.favorite.TMSearchFavoriteActivity'
# desired_caps['appWaitPackage'] = 'com.tmall.wireless'
# desired_caps['appWaitActivity'] = 'com.tmall.wireless.module.search.favorite.TMSearchFavoriteActivity'
# desired_caps['appWaitActivity'] = 'com.tmall.wireless.module.launchalert.TMLaunchAlertActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
print driver.network_connection
# print driver.get_settings()
# driver.launch_app()


# driver.lock(5)
# driver.install_app("D:\\tmall_4.9.2_10002119.apk")
# driver.start_activity("com.tmall.wireless","com.tmall.wireless.module.launchalert.TMLaunchAlertActivity")
# driver.remove_app("com.xebest")
# print driver.current_context
# print driver.current_activity
# driver.find_element_by_id("com.xebest:id/login_input_name").send_keys("192519517@qq.com")#用户名
# element1=driver.find_element_by_id("com.xebest:id/login_input_name")
# driver.set_value(element1,"192519517@qq.com")
# time.sleep(2)
# driver.find_element_by_id("com.xebest:id/login_input_password").send_keys("wwg06157715")#密码
# time.sleep(2)
# driver.find_element_by_id("com.xebest:id/login_btn").click()#登录按钮
# time.sleep(10)
# driver.swipe(349,303,375,789)#滑动
# element1=driver.find_element_by_id("com.xebest:id/yue_fundsAvailable")
# element2=driver.find_element_by_id("com.xebest:id/yue_tixian")
# print driver.current_activity

# driver.background_app(5)

#driver.scroll(element1,element2)
# driver.drag_and_drop(element1,element2)
# driver.flick(349,303,375,789)
# print driver.app_strings("utf-8"
