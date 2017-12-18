# -*- coding: utf-8 -*-
# auth: CY
import getpass
import random
import unittest
from configparser import ConfigParser
from selenium import webdriver as browse_driver

from Page.Element import is_element_present
from Page.random_data import get_mobile, getPeopleName, getRandomName, getDistrictCode
from Page.web.forget_password import forget_password, account_setting, change_phone_number
from Page.web.logout import logout
from Page.web.verify_real_name import verify_real_name
from Page.web.web_regfast import web_employee_registration, web_workman_register
from run_path import setting_path


class Register(unittest.TestCase):
    def setUp(self):
        config = ConfigParser()
        self.path = setting_path()
        self.file_path = r'C:\Users\%s\Desktop\UIAutotest\Page\file\1.jpg' % (str(getpass.getuser()))
        config.read(self.path)
        url = config.get('testUrl', 'url')
        self.password = config.get('operation', 'password')
        # 随机姓名
        self.people_name = getPeopleName()
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
        # 实名认证
        verify_real_name(self.browser, self.people_name, self.identity, self.file_path, self.file_path)
        logout(self.browser)
        # 忘记密码
        forget_password(self.browser, self.mobile, self.new_password, self.code)
        # 账号设置
        account_setting(self.browser, self.mobile, self.password)
        # 更换手机号
        change_phone_number(self.browser, self.mobile, self.get_new_mobile, self.password)

    def test_02_EmployeeRegistration(self):
        company_name = '苑通生态建设有限公司'
        web_employee_registration(self.browser, self.people_name, self.mobile, self.password, company_name)
        # 实名认证
        verify_real_name(self.browser, self.people_name, self.identity, self.file_path, self.file_path)

    def tearDown(self):
        self.browser.close()
