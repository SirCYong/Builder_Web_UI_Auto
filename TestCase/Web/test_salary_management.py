# -*- coding: utf-8 -*-
# auth:CY
# update 2018年4月2日
import getpass
import random
import unittest
from configparser import ConfigParser
from selenium import webdriver as browse_driver
from websocket import create_connection
from Page.api.BuilderBaseFunc import BuilderBaseFunc
from Page.api.builder_api import login, workflow_process_create
from Page.random_data import get_people_name, get_mobile, getDistrictCode
from Page.web.logout import logout
from Page.web.salary_management import new_payroll
from Page.web.verify_real_name import verify_real_name
from Page.web.web_login import web_login
from Page.web.web_regfast import web_workman_register
from Page.web.workman_contract import workman_contract
from run_path import setting_path, test_report_path


class SalaryManagement(unittest.TestCase):
    def setUp(self):
        # 实例化一个火狐配置文件
        fp = browse_driver.FirefoxProfile()
        # 设置各项参数，参数可以通过在浏览器地址栏中输入about:config查看。
        # 设置成0代表下载到桌面，1代表浏览器默认下载路径；设置成2则可以保存到指定目录
        fp.set_preference("browser.download.folderList", 2)
        # 是否显示开始,(个人实验，不管设成True还是False，都不显示开始，直接下载)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        # 下载到指定目录
        fp.set_preference("browser.download.dir", test_report_path())  # 路径名称文件夹设置成英文，不然不能下载到指定目录
        # 不询问下载路径；后面的参数为要下载页面的Content-type的值
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")
        config = ConfigParser()
        config.read(setting_path())
        self.file_path = r'C:\Users\%s\Desktop\UIAutotest\Page\file\1.jpg' % (str(getpass.getuser()))
        self.driver = browse_driver.Firefox(firefox_profile=fp)
        self.driver.maximize_window()
        self.driver.get(config.get('testUrl', 'url'))
        self.username = config.get('labor', 'Wuhuigang')
        self.password = config.get('operation', 'password')
        ws_url = config.get('testUrl', 'ws_test_url')
        ws = create_connection("ws://%s/wsapi" % ws_url)
        self.ws_driver = BuilderBaseFunc(ws, ws_url)
        self.payroll_name = get_people_name()
        self.mobile = get_mobile()
        self.code = '11111'
        self.people_name = get_people_name()
        # 随机身份证
        self.identity = getDistrictCode()

    def tearDown(self):
        self.driver.close()

    def test_01_new_payroll(self):
        money = random.randint(20, 1000)
        web_workman_register(self.driver, self.mobile, self.code, self.password)
        # 实名认证
        verify_real_name(self.driver, self.people_name, self.identity, self.file_path, self.file_path)
        logout(self.driver)
        # 劳务经理登陆
        sid = login(self.ws_driver, self.username, self.password)
        workflow_process_create(self.ws_driver, sid['data']['sid'],
                                login(self.ws_driver, self.mobile, self.password)['data']['user_id'])
        web_login(self.driver, self.username, self.password)
        new_payroll(self.driver, self.payroll_name, money)



