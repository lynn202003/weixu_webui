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
with open(rolelistdata,encoding='utf-8') as f:
    rolelist_value=yaml.load(f)
with open(logindata,encoding="utf-8") as j:
    login_value=yaml.load(j)

@ddt.ddt
class roletest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = getdriver()
        loginsucess=loginpage(self.driver)
        loginsucess.open_brow()
        loginsucess.user_login(login_value[5]["data"]['user'],login_value[5]['data']['password'])

    def test_rolelist(self):
        loger = get_log('rolelist')
        loger.info(f"当前执行测试用例ID->{rolelist_value[0]['id']} ; 测试点-> {rolelist_value[0]['detail']}")
        #创建新角色

        # driver=getdriver()
        rolepg=rolelist(self.driver)
        rolepg.click_Account_manag()
        rolepg.click_role_list()
        rolepg.click_create_role()
        rolepg.create_role(rolelist_value[0]['data']['rolename'],rolelist_value[0]['data']['roledesc'])
        if rolelist_value[0]['screenshot']=='creat_role_sucess':
            loger.info(f"检查点>{rolepg.create_role_sucess_name()},{rolepg.create_role_sucess_show()}")
            self.assertEqual(rolepg.create_role_sucess_name(),rolelist_value[0]['check'][0],f"角色创建成功，返回实际结果是->: {rolepg.create_role_sucess_name()}")
            loger.info(f"角色创建成功，返回实际结果是->: {rolepg.create_role_sucess_name()}")
            insert_img(self.driver, rolelist_value[0]['screenshot'])
        #编辑新角色
        rolepg.click_edit_role()
        rolepg.edit_role(rolelist_value[1]['data']['rolename'],rolelist_value[1]['data']['roledesc'])
        if rolelist_value[1]['screenshot']=='edit_role_sucess':
            loger.info(f"检查点>{rolepg.create_role_sucess_name()},{rolepg.create_role_sucess_show()}")
            self.assertEqual(rolepg.create_role_sucess_name(),rolelist_value[1]['check'][0],f"角色创建成功，返回实际结果是->: {rolepg.create_role_sucess_name()}")
            loger.info(f"角色创建成功，返回实际结果是->: {rolepg.create_role_sucess_name()}")
            insert_img(self.driver, rolelist_value[1]['screenshot'])
        #删除新创建的角色
        rolepg.click_del()
        rolepg.double_del()



'''
    @ddt.data(*rolelist_value)
    def test_rolelist(self,datayaml):
        loger.info(f"当前执行测试用例ID-> {datayaml['id']} ; 测试点-> {datayaml['detail']}")
        #创建新角色

        # driver=getdriver()
        rolepg=rolelist(self.driver)
        rolepg.click_Account_manag()
        rolepg.click_role_list()
        rolepg.click_create_role()
        rolepg.create_role(datayaml['data']['rolename'],datayaml['data']['roledesc'])
        if datayaml['screenshot']=='creat_role_sucess':
            loger.info(f"检查点>{rolepg.create_role_sucess_name()},{rolepg.create_role_sucess_show()}")
            self.assertEqual(rolepg.create_role_sucess_name(),datayaml['check'][0],f"角色创建成功，返回实际结果是->: {rolepg.create_role_sucess_name()}")
            loger.info(f"角色创建成功，返回实际结果是->: {rolepg.create_role_sucess_name()}")
            insert_img(self.driver, datayaml['screenshot'])

        rolepg.click_edit_role()
        rolepg.edit_role(datayaml[1]['data']['rolename'],datayaml[1]['data']['roledesc'])
        if datayaml[1]['screenshot']=='edit_role_sucess':
            loger.info(f"检查点>{rolepg.create_role_sucess_name()},{rolepg.create_role_sucess_show()}")
            self.assertEqual(rolepg.create_role_sucess_name(),datayaml[1]['check'][0],f"角色创建成功，返回实际结果是->: {rolepg.create_role_sucess_name()}")
            loger.info(f"角色创建成功，返回实际结果是->: {rolepg.create_role_sucess_name()}")
            insert_img(self.driver, datayaml[1]['screenshot'])

'''



if __name__ == '__main__':

    unittest.main()
    # import unittest.suite as suite
    # import unittest.loader as loader
    # import unittest.runner as runner
    # suite = suite.TestSuite()  # create Test Suite
    # tests = loader.TestLoader().loadTestsFromTestCase(roletest)  # get tests from Test Class
    # suite.addTests(tests)  # add tests to Test Suite
    # runner.TextTestRunner().run(suite)

