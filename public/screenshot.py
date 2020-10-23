#coding=utf-8

__author__ = 'lynn'


import os,sys
path = os.path.dirname(os.path.abspath(__file__))#获取当前文件路径



def insert_img(driver,file_name):
    """
    截图
    :param driver: 启动浏览器
    :param file_name: 截图文件名
    :return: 返回指定路径的截图文件

    """
    file_path = os.path.join(path, 'screenshots/')  # 拼接截图保存路径
    print(file_path+file_name+'.png')
    return  driver.get_screenshot_as_file(file_path+file_name+'.png')#指定路径的截图文件


