# -*- coding: utf-8 -*-
# auth: CY
import getpass
import random
import unittest
from configparser import ConfigParser
from time import sleep

from selenium import webdriver as browse_driver

from Page.Element import is_element_present
from Page.random_data import get_mobile, getPeopleName, getRandomName, getDistrictCode
from Page.web.forget_password import forget_password, account_setting, change_phone_number
from Page.web.logout import logout
from Page.web.personal_information import work_experience, personal_certificate, add_education_experience, \
    family_information, basic_information
from Page.web.verify_real_name import verify_real_name
from Page.web.web_login import web_login
from Page.web.web_regfast import web_employee_registration, web_workman_register
from run_path import setting_path


class PersonalInformation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config = ConfigParser()
        cls.path = setting_path()
        cls.file_path = r'C:\Users\%s\Desktop\UIAutotest\Page\file\1.jpg' % (str(getpass.getuser()))
        config.read(cls.path)
        url = config.get('testUrl', 'perfurl')
        cls.password = config.get('operation', 'password')
        # 随机姓名
        cls.people_name = getPeopleName()
        # 随机身份证
        cls.identity = getDistrictCode()
        cls.browser = browse_driver.Firefox()
        cls.browser.maximize_window()
        cls.browser.get(url)
        cls.mobile = get_mobile()
        cls.code = 11111
        web_workman_register(cls.browser, cls.mobile, cls.code, cls.password)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()

    def test_02_verify_name(self):
        # 实名认证
        verify_real_name(self.browser, self.people_name, self.identity, self.file_path, self.file_path)
        logout(self.browser)

    def test_03_work_experience(self):
        web_login(self.browser, self.mobile, self.password)
        # 工作经历
        work_experience(self.browser)

    def test_04_personal_certificate(self):
        sleep(1)
        # 我的证书
        personal_certificate(self.browser, self.file_path)

    def test_05_add_education(self):
        sleep(1)
        # 教育经历
        add_education_experience(self.browser)

    def test_06_family_information(self):
        sleep(1)
        # 家庭信息
        family_information(self.browser)

    def test_07_basic_information(self):
        sleep(1)
        # 基本信息
        basic_information(self.browser)



