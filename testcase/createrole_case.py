#coding=utf-8
__author__='lynn'
from public.getyaml import getyaml
from pagobj.rolelistpage import rolelist
import unittest
import ddt
from public.logs.log import loger,get_log
from config.setting import *
from public.screenshot import insert_img
from pagobj.loginpage import loginpage
from public.getdriver import *
import yaml
import time
with open(createroledata,encoding='utf-8') as f:
    rolelist_value=yaml.load(f)
    #通过yaml文件找到正确的用户名和密码
with open(logindata,encoding="utf-8") as j:
    login_value=yaml.load(j)
    ph = login_value[5]["data"]['user']
    pwd = login_value[5]['data']['password']

@ddt.ddt
class roletest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = getdriver()
        loginsucess=loginpage(self.driver)
        loginsucess.open_brow()
        # 调用登录方法
        loginsucess.user_login(ph,pwd)

    @classmethod
    def tearDownClass(self):
        self.driver.close()


    @ddt.data(*rolelist_value)
    def test_rolelist(self,datayaml):
        # loger = get_log('createrole')
        loger.info(f"当前执行测试用例ID-> {datayaml['id']} ; 测试点-> {datayaml['detail']}")

        # driver=getdriver()
        rolepg=rolelist(self.driver)
        rolepg.click_Account_manag()
        rolepg.click_role_list()
        rolepg.click_create_role()
        # 调用创建角色方法
        rolepg.create_role(datayaml['data']['rolename'],datayaml['data']['roledesc'])

        if datayaml["screenshot"]=='rolename_empty':
            loger.info(f"检查点>{rolepg.rolename_empty()}")
            self.assertEqual(rolepg.rolename_empty(), datayaml['check'][0],f"角色名称为空，返回实际结果是->: {rolepg.rolename_empty()}")
            loger.info(f"角色名称为空，返回实际结果是->: {rolepg.rolename_empty()}")
            insert_img(self.driver, datayaml['screenshot'])
            rolepg.click_cancal()

        else:
            loger.info(f"检查点>{rolepg.create_role_sucess_name()},{rolepg.create_role_sucess_show()}")
            self.assertEqual(rolepg.create_role_sucess_name(),datayaml['check'][0],f"成功创建，角色名称返回实际结果是->: {rolepg.create_role_sucess_name()}")
            self.assertEqual(rolepg.create_role_sucess_show(),datayaml['check'][1],f'成功创建,角色说明返回实际结果是->: {rolepg.create_role_sucess_show()}')
            loger.info(f"成功创建，返回实际结果是->: {rolepg.create_role_sucess_name()},{rolepg.create_role_sucess_show()}")
            insert_img(self.driver,datayaml['screenshot'])
            rolepg.click_del()
            rolepg.double_del()

if __name__ == '__main__':

    unittest.main()
    # import unittest.suite as suite
    # import unittest.loader as loader
    # import unittest.runner as runner
    # suite = suite.TestSuite()  # create Test Suite
    # tests = loader.TestLoader().loadTestsFromTestCase(roletest)  # get tests from Test Class
    # suite.addTests(tests)  # add tests to Test Suite
    # runner.TextTestRunner().run(suite)

