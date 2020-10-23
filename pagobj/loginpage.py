#coding-utf-8
from selenium import webdriver
from public.getyaml import getyaml
from config.setting import *
from pagobj.base import base
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

yamldata=getyaml(loginyaml)
class loginpage(base):
    #输入帐号
    def send_user(self,user):
        self.sendkeys(user,By.CSS_SELECTOR,yamldata.get_elementinfo(0))
    #输入密码
    def send_password(self,password):
        # self.sendkeys(password,yamldata.get_find_type(1),yamldata.get_elementinfo(1))
        self.sendkeys(password, By.CSS_SELECTOR, yamldata.get_elementinfo(1))
    #点击登录
    def clickbutton(self):
        self.click_button(By.CSS_SELECTOR,yamldata.get_elementinfo(3))


    #登录流程
    def user_login(self,user,password):
        self.send_user(user)
        self.send_password(password)
        self.clickbutton()
        time.sleep(1)


    #点击退出按扭
    def click_exit_button(self):
        self.click_button(By.XPATH,yamldata.get_elementinfo(5))

    #退出登录流程
    def log_exit(self):
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        # 先找到鼠标悬停的位置即元素,这里 move_to_element后面一直要写find_element，否则报错
        ActionChains(self.driver).move_to_element(self.find_element(By.CSS_SELECTOR,yamldata.get_elementinfo(4))).perform()
        time.sleep(2)
        self.click_button(By.XPATH, yamldata.get_elementinfo(5))


    #用户和密码错误提示
    def user_password_error(self):
        return self.get_text(By.CSS_SELECTOR,yamldata.get_checkElementinfo(0))
    #用户为空提示
    def user_empty(self):
        return self.get_text(By.CSS_SELECTOR,yamldata.get_checkElementinfo(1))
    #密码为空提示
    def password_empty(self):
        return self.get_text(By.CSS_SELECTOR,yamldata.get_checkElementinfo(2))

     #登录成功检查用户名
    def login_success(self):
        return self.get_text(By.CSS_SELECTOR,yamldata.get_checkElementinfo(3))
     #退出成功检查
    def exit_success(self):
        return self.get_text(By.CSS_SELECTOR,yamldata.get_checkElementinfo(4))



if __name__ == '__main__':
    a=loginpage()
    a.user_login("test","qwer1234")
    a.log_exit()