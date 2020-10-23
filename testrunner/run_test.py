
# _*_ coding:utf-8 _*_
__author__ = 'lynn'

import os,sys
# import HTMLTestRunner
import unittest,time
from public.newreport import new_report
from public.sendemail import send_mail
from testrunner.HTMLtestrunner import HTMLTestRunner

path = os.path.join(os.path.dirname(os.getcwd()))#获取当前文件上层目录，即最外层目录

report_path=os.path.join(path, 'report')  # 测试报告保存路径
test_dir=os.path.join(path,'testcase')#测试用例路径

# 测试报告存放文件夹，如不存在，则自动创建一个report目录
# if not os.path.exists(path):os.makedirs(path + '/' + "screenshot")

def add_case(test_path=test_dir):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(test_path, pattern='*_case.py')
    # discover = unittest.defaultTestLoader.discover(test_path, pattern='login_case.py')
    return discover

def run_case(all_case,result_path=report_path):
    """执行所有的测试用例"""
    print(result_path)
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename =  result_path + '/' + now + 'result.html'
    fp = open(filename,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='this is first report', description='我是我们第一次测试报告')
    runner = HTMLTestRunner(stream=fp, title='运营后台UI自动化测试报告',
                            description='环境：windows 7 浏览器：chrome',
                            tester='lynn')


    runner.run(all_case)
    fp.close()

    report = new_report(result_path) #调用模块生成最新的报告
    send_mail(report) #调用发送邮件模块

if __name__ =="__main__":
    cases = add_case()
    run_case(cases)
