#coding=utf-8
__auto__='lynn'
from selenium import webdriver
# from public.getdriver import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from public.logs.log import loger
from config.setting import *
import time

class base():
    def __init__(self,driver):
        self.driver=driver

    def open_brow(self):
        self.driver.get(URL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(1)

    def close_brow(self):
        self.driver.close()
        #time.sleep(10)


#查找一个元素
    def find_element(self,*locator):
        try:
            element=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
            return element

        except:
            loger.error(f'页面中未能找到元素{locator}', exc_info=1)

#查找多个元素
    def find_elements(self,*locator):
        try:
            elements=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(locator))
            return elements
        except:
            loger.error(f'页面中未能找到元素{locator}', exc_info=1)
#输入内容
    def sendkeys(self,values,*locator):
        try:
            self.find_element(*locator).send_keys(values)
        except:
            loger.error(f"输入内容错误:{values}")
#点击操作
    def click_button(self,*locator):
        try:
            self.find_element(*locator).click()
        except:
            loger.error("点击失败")
#获取某个元素的text
    def get_text(self,*locator):
        try:
            get_text=self.find_element(*locator).text
            return get_text
        except:
            loger.error(f"获取元素{get_text}text失败")

#清除文本框内容
    def clear_text(self,*locator):
        self.find_element(*locator).clear()
