#coding=utf-8
__author__='lynn'
from public.getyaml import getyaml
from config.setting import *
import unittest
import ddt
from public.logs.log import loger,get_log

from pagobj.loginpage import loginpage
from pagobj.base import base
from public.getdriver import *
from public.screenshot import insert_img
import sys

import yaml
with open(logindata,encoding='utf-8') as f:
     login_value=yaml.load(f)

import logging

@ddt.ddt
class autotest(unittest.TestCase):

    driver=None
    ch=None
    ch2=None



    def setUp(self):
        if autotest.driver:
            autotest.driver.close()
        autotest.driver=getdriver()
        self.li=loginpage(autotest.driver)
        self.li.open_brow()
        autotest.ch=logging.StreamHandler()
        loger.addHandler(autotest.ch)
        autotest.ch2=logging.StreamHandler(sys.__stdout__)
        loger.addHandler(autotest.ch2)

    def tearDown(self):
        loger.removeHandler(autotest.ch)
        loger.removeHandler(autotest.ch2)


    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.close()
            cls.driver.quite()


    @ddt.data(*login_value)
    def test_login(self,datayaml):
        """
        登录测试
        :param datayaml: 加载login_data登录测试数据
        :return:
        """

        # loger=get_log("login")

        loger.info(f"当前执行测试用例ID-> {datayaml['id']} ; 测试点-> {datayaml['detail']}")
        # 调用登录方法
        # login_pg=bs
        login_pg =self.li


        login_pg.user_login(datayaml["data"]['user'],datayaml['data']['password'])


        if datayaml['screenshot']=='user_pawd_success':
            loger.info(f"检查点>{login_pg.login_success()}")
            self.assertEqual(login_pg.login_success(),datayaml['check'][0],f"成功登录，返回实际结果是->: {login_pg.login_success()}")
            loger.info(f"成功登录，返回实际结果是->: {login_pg.login_success()}")
            insert_img(self.driver, datayaml['screenshot'])
            loger.info("-----> 开始执行退出流程操作")
            login_pg.log_exit()
            loger.info(f"检查点-> 找到{login_pg.exit_success()}元素,表示退出成功！")
            self.assertEqual(login_pg.exit_success(),'登录',f"退出登录，返回实际结果是->: {login_pg.exit_success()}")
            loger.info(f"退出登录，返回实际结果是->: {login_pg.exit_success()}")
        elif datayaml["screenshot"]=='user_pawd_empty':
            loger.info("检查点>帐号和密码为空登录")
            self.assertEqual(login_pg.user_empty(),datayaml['check'][0],f"异常登录，返回实际结果是->: {login_pg.user_empty()}")
            loger.info(f"异常登录，返回实际结果是->: {login_pg.user_empty()}")
            insert_img(self.driver, datayaml['screenshot'])

        elif datayaml["screenshot"] == 'user_empty':
            loger.info(f"检查点>: {login_pg.user_empty()}")
            self.assertEqual(login_pg.user_empty(), datayaml['check'][0], f"异常登录，返回实际结果是->: {login_pg.user_empty()}")
            loger.info(f"异常登录，返回实际结果是->: {login_pg.user_empty()}")
        elif datayaml["screenshot"] == 'pawd_empty':
            loger.info(f"检查点>{login_pg.password_empty()}")
            self.assertEqual(login_pg.password_empty(), datayaml['check'][0], f"异常登录，返回实际结果是->: {login_pg.password_empty()}")
            loger.info(f"异常登录，返回实际结果是->: {login_pg.password_empty()}")
            insert_img(self.driver, datayaml['screenshot'])
        else:
            loger.info(f"检查点>{login_pg.user_password_error()}")
            self.assertEqual(login_pg.user_password_error(), datayaml['check'][0],f"异常登录，返回实际结果是->: {login_pg.user_password_error()}")
            loger.info(f"异常登录，返回实际结果是->: {login_pg.user_password_error()}")
            insert_img(self.driver, datayaml['screenshot'])

if __name__ == "__main__":
    unittest.main()
    '''
    suite.addTest(autotest('test_login'))
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''

