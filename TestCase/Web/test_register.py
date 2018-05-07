# -*- coding: utf-8 -*-
# auth: CY
import getpass
import random
import unittest
from configparser import ConfigParser
from selenium import webdriver as browse_driver
from websocket import create_connection

from Page.Element import is_element_present
from Page.api.BuilderBaseFunc import BuilderBaseFunc
from Page.api.builder_api import login, company_list
from Page.random_data import get_mobile, get_people_name, getRandomName, getDistrictCode, save_mobile_number, \
    get_save_mobile_number
from Page.web.forget_password import forget_password, account_setting, change_phone_number
from Page.web.logout import logout
from Page.web.verify_real_name import verify_real_name
from Page.web.web_login import web_login
from Page.web.web_regfast import web_employee_registration, web_workman_register
from run_path import setting_path, file_path


class Register(unittest.TestCase):
    def setUp(self):
        config = ConfigParser()
        self.path = setting_path()
        self.file_path = file_path('1')
        config.read(self.path)
        url = config.get('testUrl', 'url')
        ws_url = config.get('testUrl', 'ws_test_url')
        ws = create_connection("ws://%s/wsapi" % ws_url)
        self.ws_driver = BuilderBaseFunc(ws, ws_url)
        self.username = config.get('operation', 'username')
        self.password = config.get('operation', 'password')
        # 随机姓名
        self.people_name = get_people_name()
        # 随机身份证
        self.identity = getDistrictCode()
        self.browser = browse_driver.Firefox()
        self.browser.maximize_window()
        self.browser.get(url)
        self.mobile = get_mobile()
        self.new_password = 654321
        self.code = 11111
        self.get_new_mobile = get_mobile()

    def test_01_WorkerRegister(self):
        # 工人注册
        web_workman_register(self.browser, self.mobile, self.code, self.password)
        save_mobile_number(self.mobile)
        # 实名认证
        verify_real_name(self.browser, self.people_name, self.identity, self.file_path, self.file_path)
        logout(self.browser)

        # 账号设置
        account_setting(self.browser, self.mobile, self.password)
        # 更换手机号
        change_phone_number(self.browser, self.mobile, self.get_new_mobile, self.password)

    def test_02_forget_password(self):
        mobile = get_save_mobile_number()
        # 忘记密码
        forget_password(self.browser, mobile, self.new_password, self.code)

    def test_03_update_password(self):
        mobile = get_save_mobile_number()
        web_login(self.browser, mobile, self.new_password)



    def test_02_EmployeeRegistration(self):
        # 通过企业运维sid 获取所有的公司名称
        sid = login(self.ws_driver, self.username, self.password)
        all_company_info = company_list(self.ws_driver, sid['data']['sid'])
        all_company_name = []
        h = 0
        for i in all_company_info['data']['company']:
            print(i)
            all_company_name.insert(h, i["name"])
            h += 1
        company_name = all_company_name[random.randint(0, len(all_company_name)-1)]
        web_employee_registration(self.browser, self.people_name, self.mobile, self.password, company_name)
        # 实名认证
        verify_real_name(self.browser, self.people_name, self.identity, self.file_path, self.file_path)
        logout(self.browser)

    def tearDown(self):
        self.browser.close()
