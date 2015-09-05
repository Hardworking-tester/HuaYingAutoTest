#encoding:utf-8
from selenium import webdriver
import time
import random
from Mysql import GetData
init_experience=GetData().getDataFromMysql()
print ("初始的用户经验值为：%d" %init_experience)
br=webdriver.Firefox()
br.get("http://192.168.1.88:8080/app/")
# br.maximize_window()
time.sleep(2)
br.find_element_by_css_selector("input[type='radio'][value='1']").click()
br.find_element_by_id("login2").send_keys('18638135380')
br.find_element_by_id("pwd").send_keys("123abc")
br.find_element_by_id("commit2").click()
time.sleep(2)

br.find_element_by_css_selector("input[type='button'][value='查看经验值']").click()
time.sleep(2)
try:
    for i in range(1,1001):
        #生成随机数
        m=random.randint(1,6)
        # print m
        # print "---------------------------------------"
        if m==1:
        #报修
            br.find_element_by_id("fuwu").find_element_by_css_selector("option[value='1']").click()
            br.find_element_by_css_selector("input[type='button'][value='提交']").click()
            time.sleep(2)
            second_experience=init_experience+50
            init_experience=second_experience
        #缴纳物业费
        elif m==2:
            br.find_element_by_id("fuwu").find_element_by_css_selector("option[value='2']").click()
            br.find_element_by_css_selector("input[type='button'][value='提交']").click()
            time.sleep(2)
            second_experience=init_experience+100
            init_experience=second_experience
        #缴纳停车费
        elif m==3:
            br.find_element_by_id("fuwu").find_element_by_css_selector("option[value='3']").click()
            br.find_element_by_css_selector("input[type='button'][value='提交']").click()
            time.sleep(2)
            second_experience=init_experience+100
            init_experience=second_experience
        #投诉
        elif m==4:
            br.find_element_by_id("fuwu").find_element_by_css_selector("option[value='4']").click()
            br.find_element_by_css_selector("input[type='button'][value='提交']").click()
            time.sleep(2)
            second_experience=init_experience+50
            init_experience=second_experience
        #表扬
        elif m==5:
            br.find_element_by_id("fuwu").find_element_by_css_selector("option[value='5']").click()
            br.find_element_by_css_selector("input[type='button'][value='提交']").click()
            time.sleep(2)
            second_experience=init_experience+100
            init_experience=second_experience
        #访客通
        elif m==6:
            br.find_element_by_id("fuwu").find_element_by_css_selector("option[value='6']").click()
            br.find_element_by_css_selector("input[type='button'][value='提交']").click()
            second_experience=init_experience+10
            init_experience=second_experience
        br.refresh()
        time.sleep(2)
        end_experience=GetData().getDataFromMysql()
        if init_experience==end_experience:
            if m==1:
                print ("本次为第%d次执行程序，本次执行的功能为：报修，本次增加的经验值为50，本次程序执行完，用户的总经验值为：%d" %(i,end_experience))
            elif m==2:
                print ("本次为第%d次执行程序，本次执行的功能为：缴纳物业费，本次增加的经验值为100，本次程序执行完，用户的总经验值为：%d" %(i,end_experience))
            elif m==3:
                print ("本次为第%d次执行程序，本次执行的功能为：缴纳停车费，本次增加的经验值为100，本次程序执行完，用户的总经验值为：%d" %(i,end_experience))
            elif m==4:
                print ("本次为第%d次执行程序，本次执行的功能为：投诉，本次增加的经验值为50，本次程序执行完，用户的总经验值为：%d" %(i,end_experience))
            elif m==5:
                print ("本次为第%d次执行程序，本次执行的功能为：表扬，本次增加的经验值为100，本次程序执行完，用户的总经验值为：%d" %(i,end_experience))
            elif m==6:
                print ("本次为第%d次执行程序,本次执行的功能为：访客通，本次增加的经验值为10，本次程序执行完，用户的总经验值为：%d" %(i,end_experience))

except Exception,e:
    print e