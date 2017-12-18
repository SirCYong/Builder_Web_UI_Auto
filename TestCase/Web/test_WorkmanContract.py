# -*- coding: utf-8 -*-
# auth: CY
import getpass
import unittest
from configparser import ConfigParser
from selenium import webdriver as browse_driver
from Page.random_data import get_mobile, getPeopleName, getDistrictCode, temporary_mobile_number, \
    get_temporary_mobile_number
from Page.web.approve_workflow import approve_workflow
from Page.web.logout import logout
from Page.web.verify_real_name import verify_real_name
from Page.web.web_login import web_login
from Page.web.web_regfast import web_workman_register
from Page.web.workman_contract import workman_contract, workers_review, workman_contract_piece, \
    change_workman_contract_date, edit_workers_contract, termination_of_the_contract
from run_path import setting_path


class WorkmanContract(unittest.TestCase):
    def setUp(self):
        config = ConfigParser()
        self.path = setting_path()
        self.file_path = r'C:\Users\%s\Desktop\UIAutotest\Page\file\1.jpg' % (str(getpass.getuser()))
        config.read(self.path)
        url = config.get('testUrl', 'url')
        self.username = config.get('labor', 'Wuhuigang')
        self.username1 = config.get('projectManager', 'taohui')
        self.password = config.get('operation', 'password')
        # 随机姓名
        self.people_name = getPeopleName()
        # 随机身份证
        # 工件名称
        self.artifact = self.people_name + '的工件'
        self.identity = getDistrictCode()
        self.browser = browse_driver.Firefox()
        self.browser.maximize_window()
        self.browser.get(url)
        self.mobile = get_mobile()
        self.new_password = 654321
        self.code = 11111

    def test_01_workman_contract_time(self):
        # 工人注册
        web_workman_register(self.browser, self.mobile, self.code, self.password)
        temporary_mobile_number(self.people_name)
        # 实名认证
        verify_real_name(self.browser, self.people_name, self.identity, self.file_path, self.file_path)
        logout(self.browser)
        # 劳务经理登陆
        web_login(self.browser, self.username, self.password)
        workman_contract(self.browser, self.people_name)

    def test_02_workman_contract_piece(self):
        # 工人注册
        web_workman_register(self.browser, self.mobile, self.code, self.password)
        # 实名认证
        verify_real_name(self.browser, self.people_name, self.identity, self.file_path, self.file_path)
        logout(self.browser)
        # 劳务经理登陆
        web_login(self.browser, self.username, self.password)
        workman_contract_piece(self.browser, self.artifact, self.people_name)

    def test_03_change_workman_contract_date(self):
        # 用工合同期限修改
        web_login(self.browser, self.username, self.password)
        change_workman_contract_date(self.browser)

    def test_04_edit_contract(self):
        web_login(self.browser, self.username, self.password)
        workers_name = get_temporary_mobile_number()
        edit_workers_contract(self.browser, workers_name, self.file_path)

    def test_05_terminating_contract(self):
        web_login(self.browser, self.username, self.password)
        workers_name = get_temporary_mobile_number()
        termination_of_the_contract(self.browser, workers_name)

    def tearDown(self):
        self.browser.close()


