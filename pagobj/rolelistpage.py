#coding=utf-8
from selenium import webdriver
from public.getyaml import getyaml
from config.setting import *
from pagobj.base import base
import time
from selenium.webdriver.common.by import By
yamldata=getyaml(rolelistyaml)
class rolelist(base):
    #点击帐号管理
    def click_Account_manag(self):
        self.click_button(By.CSS_SELECTOR,yamldata.get_elementinfo(0))
    #点击角色列表
    def click_role_list(self):
        self.click_button(By.CSS_SELECTOR,yamldata.get_elementinfo(1))
        #点击创建角色
    def click_create_role(self):
        self.click_button(By.XPATH,yamldata.get_elementinfo(2))
    #输入角色名称
    def send_role_name(self,rolename):
        self.sendkeys(rolename,By.XPATH,yamldata.get_elementinfo(3))
        #输入角色说明
    def send_role_show(self,roleshow):
        self.sendkeys(roleshow,By.XPATH,yamldata.get_elementinfo(4))
        #选择权限
    def click_power(self):
        self.click_button(By.XPATH,yamldata.get_elementinfo(5))
    #选择加入右侧
    def click_right(self):
        self.click_button(By.XPATH,yamldata.get_elementinfo(6))
     #点击确定
    def click_ok(self):
        self.click_button(By.XPATH,yamldata.get_elementinfo(8))
    #创建角色弹框点击取消按扭
    def click_cancal(self):
        self.click_button(By.XPATH,yamldata.get_elementinfo(14))
    #创建角色流程
    def create_role(self,rolename,roleshow):
        self.send_role_name(rolename)
        self.send_role_show(roleshow)
        self.click_power()
        self.click_right()
        self.click_ok()
        time.sleep(0.5)
    #点击编辑角色按扭
    def click_edit_role(self):
        self.click_button(By.CSS_SELECTOR,yamldata.get_elementinfo(9))

    # 编辑角色流程
    def edit_role(self, rolename, roleshow):
        self.find_element(By.XPATH,yamldata.get_elementinfo(3)).clear()#清除原角色名称文本内容
        self.send_role_name(rolename)
        self.find_element(By.XPATH,yamldata.get_elementinfo(4)).clear()#清除原角色说明文本内容
        self.send_role_show(roleshow)
        self.click_ok()
        time.sleep(0.5)

     #点击删除按扭
    def click_del(self):
        self.click_button(By.CSS_SELECTOR,yamldata.get_elementinfo(10))
     #点击二次确认弹框
    def double_del(self):
        self.click_button(By.XPATH,yamldata.get_elementinfo(11))
    #删除角色流程
    def del_role(self):
        self.click_del()
        self.double_del()
    #创建/编辑成功检查角色名称
    def create_role_sucess_name(self):
        return self.get_text(By.XPATH,yamldata.get_checkElementinfo(0))
    #创建/编辑成功检查角色说明
    def create_role_sucess_show(self):
        return self.get_text(By.XPATH,yamldata.get_checkElementinfo(1))
    #角色名称为空提示
    def rolename_empty(self):
        return self.get_text(By.XPATH,yamldata.get_checkElementinfo(2))








