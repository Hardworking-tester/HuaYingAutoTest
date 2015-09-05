# encoding:utf-8
from appium import webdriver
from time import sleep

class BasicServices():

    def startApplication(self):
        desired_caps={'platformName':'Android','platformVersion':'4.4','deviceName':'HUAWEI C8817E','appPackage':'com.bd.community','appActivity':'com.bd.community.SplashActivity','unicodeKeyboard':True,'resetKeyboard':True}

        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        sleep(5)
        # self.driver.find_element_by_id("com.bd.community:id/login_loginaccount").send_keys("15093492821")#用户名输入框
        # sleep(2)
        # self.driver.find_element_by_id("com.bd.community:id/edittext").send_keys("11111111")#密码输入框
        # sleep(2)
        # self.driver.find_element_by_id("com.bd.community:id/login").click()#登录按钮
        # sleep(5)

    #投诉建议业务
    def touSu(self):
        for m in range(1,11):
            try:
                self.driver.find_element_by_id("com.bd.community:id/fl_tousu").click()
                sleep(3)
                self.driver.find_element_by_id("com.bd.community:id/et_describe").send_keys(u'投诉建议'+str(m))
                #上传图片
                for i in range(5):
                    self.driver.find_element_by_id("com.bd.community:id/iv_getImg_05").click()
                    self.driver.find_element_by_id("com.bd.community:id/dialog_select_native").click()
                    picture_list=self.driver.find_elements_by_id("com.android.documentsui:id/icon_thumb")
                    picture_list[i].click()
                    sleep(2)
                self.driver.find_element_by_id("com.bd.community:id/tv_commit").click()
                sleep(20)
                print "第%s次投诉建议流程操作完成" %m
            except Exception,e:
                print e
                print "第%s次投诉建议流程出现问题" %m


    #报修业务
    def baoXiu(self):
        for m in range(1,11):
            try:
                self.driver.find_element_by_id("com.bd.community:id/fl_wuye").click()
                sleep(3)
                self.driver.find_element_by_id("com.bd.community:id/et_describe").send_keys(u"报修"+str(m))
                #上传图片
                for i in range(5):
                    self.driver.find_element_by_id("com.bd.community:id/iv_getImg_05").click()
                    self.driver.find_element_by_id("com.bd.community:id/dialog_select_native").click()
                    picture_list=self.driver.find_elements_by_id("com.android.documentsui:id/icon_thumb")
                    picture_list[i].click()
                    sleep(2)
                self.driver.find_element_by_id("com.bd.community:id/tv_commit").click()
                sleep(20)
                print "第%s次报修流程操作完成" %m
            except Exception,e:
                print e
                print "第%s次报修建议流程出现问题" %m

    #房屋租售业务
    def houseHire(self):
        for m in range(1,11):
            try:
                self.driver.find_element_by_id("com.bd.community:id/home_tab_fwsq").click()
                sleep(2)
                self.driver.find_element_by_id("com.bd.community:id/tv_room_sale").click()
                sleep(2)
                self.driver.find_element_by_id("com.bd.community:id/et_describe").send_keys(u"房屋租售"+str(m))
                #上传图片
                for i in range(5):
                    self.driver.find_element_by_id("com.bd.community:id/iv_getImg_05").click()
                    self.driver.find_element_by_id("com.bd.community:id/dialog_select_native").click()
                    picture_list=self.driver.find_elements_by_id("com.android.documentsui:id/icon_thumb")
                    picture_list[i].click()
                    sleep(2)
                self.driver.find_element_by_id("com.bd.community:id/tv_commit").click()
                sleep(20)
                print "第%s次房屋租售流程操作完成" %m
            except Exception,e:
                print e
                print "第%s次房屋租售建议流程出现问题" %m
    #表扬
    def biaoYang(self):
        for m in range(1,11):
            try:
                self.driver.find_element_by_id("com.bd.community:id/home_tab_fwsq").click()
                sleep(2)
                self.driver.find_element_by_id("com.bd.community:id/tv_biaoyang").click()
                sleep(2)
                self.driver.find_element_by_id("com.bd.community:id/et_describe").send_keys(u"表扬"+str(m))
                #上传图片
                for i in range(5):
                    self.driver.find_element_by_id("com.bd.community:id/iv_getImg_05").click()
                    self.driver.find_element_by_id("com.bd.community:id/dialog_select_native").click()
                    picture_list=self.driver.find_elements_by_id("com.android.documentsui:id/icon_thumb")
                    picture_list[i].click()
                    sleep(2)
                self.driver.find_element_by_id("com.bd.community:id/tv_commit").click()
                sleep(20)
                print "第%s次表扬流程操作完成" %m
            except Exception,e:
                print e
                print "第%s次表扬建议流程出现问题" %m

    #装修申请
    def zhuangxiuShenQing(self):
        for m in range(1,11):
            try:
                self.driver.find_element_by_id("com.bd.community:id/home_tab_fwsq").click()
                sleep(2)
                self.driver.find_element_by_id("com.bd.community:id/tv_tousu_baoxiu").click()
                sleep(2)
                self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'装修申请')]").click()
                sleep(2)
                self.driver.find_element_by_id("com.bd.community:id/et_describe").send_keys(u'装修申请'+str(m))
                #上传图片
                for i in range(5):
                    self.driver.find_element_by_id("com.bd.community:id/iv_getImg_05").click()
                    self.driver.find_element_by_id("com.bd.community:id/dialog_select_native").click()
                    picture_list=self.driver.find_elements_by_id("com.android.documentsui:id/icon_thumb")
                    picture_list[i].click()
                    sleep(2)
                self.driver.find_element_by_id("com.bd.community:id/tv_commit").click()
                sleep(20)
                self.driver.find_element_by_id("com.bd.community:id/jzfw_top_layout_01").click()
                print "第%s次装修申请流程操作完成" %m
            except Exception,e:
                print e
                print "第%s次装修申请建议流程出现问题" %m















pp=BasicServices()
pp.startApplication()
pp.baoXiu()
pp.touSu()
pp.houseHire()
pp.biaoYang()
pp.zhuangxiuShenQing()