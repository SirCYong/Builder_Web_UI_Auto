# -*- coding: utf-8 -*-
# auth: CY
# update 2018-03-30
import getpass
import unittest
from configparser import ConfigParser
from selenium import webdriver as browse_driver
from websocket import create_connection
from Page.api.BuilderBaseFunc import BuilderBaseFunc, get_ws_driver
from Page.api.builder_api import login, workflow_process_create
from Page.random_data import get_mobile, get_people_name, getDistrictCode, save_mobile_number, \
    get_save_mobile_number
from Page.web.logout import logout
from Page.web.verify_real_name import verify_real_name
from Page.web.web_login import web_login
from Page.web.web_regfast import web_workman_register
from Page.web.workman_contract import termination_of_the_contract, verify_worker_exists, evaluation_of_worker
from run_path import setting_path, file_path


class WorkmanContract(unittest.TestCase):
    def setUp(self):
        config = ConfigParser()
        self.path = setting_path()
        self.file_path = file_path('1')
        config.read(self.path)
        url = config.get('testUrl', 'url')
        self.ws_url = config.get('testUrl', 'ws_test_url')
        self.username = config.get('labor', 'Wuhuigang')
        self.username1 = config.get('operation', 'username')
        self.password = config.get('operation', 'password')
        # 随机姓名
        self.people_name = get_people_name()
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
        save_mobile_number(self.mobile)
        # 实名认证

        verify_real_name(self.browser, self.people_name, self.identity, self.file_path, self.file_path)
        logout(self.browser)
        # 劳务经理登陆
        ws_driver = get_ws_driver(self.ws_url)
        sid = login(ws_driver, self.username, self.password)
        workflow_process_create(ws_driver, sid['data']['sid'], login(ws_driver, self.mobile, self.password)['data']['user_id'])

    def test_02_evaluation_worker(self):
        # 评价工人
        web_login(self.browser, self.username, self.password)
        workers_mobile = get_save_mobile_number()
        ws_driver = get_ws_driver(self.ws_url)
        evaluation_of_worker(self.browser, login(ws_driver, workers_mobile, self.password)['data']['realname'])

    def test_03_modify_comments(self):
        # 修改评价
        web_login(self.browser, self.username, self.password)
        workers_mobile = get_save_mobile_number()
        ws_driver = get_ws_driver(self.ws_url)
        evaluation_of_worker(self.browser, login(ws_driver, workers_mobile, self.password)['data']['realname'], '修改评价')

    # def test_02_workman_contract_piece(self):
    #     # 工人注册
    #     web_workman_register(self.browser, self.mobile, self.code, self.password)
    #     # 实名认证
    #     verify_real_name(self.browser, self.people_name, self.identity, self.file_path, self.file_path)
    #     logout(self.browser)
    #     # 劳务经理登陆
    #     web_login(self.browser, self.username, self.password)
    #     workman_contract_piece(self.browser, self.artifact, self.people_name)
    #
    # def test_03_change_workman_contract_date(self):
    #     # 用工合同期限修改
    #     web_login(self.browser, self.username, self.password)
    #     change_workman_contract_date(self.browser)
    #
    # def test_04_edit_contract(self):
    #     # 合同编辑
    #     web_login(self.browser, self.username, self.password)
    #     workers_name = get_temporary_mobile_number()
    #     edit_workers_contract(self.browser, workers_name, self.file_path)

    def test_05_terminating_contract(self):
        # 合同终止
        web_login(self.browser, self.username, self.password)
        workers_name = get_save_mobile_number()
        ws_driver = get_ws_driver(self.ws_url)
        termination_of_the_contract(self.browser, login(ws_driver, workers_name, self.password)['data']['realname'])

    def test_06_out_of_date_workers(self):
        # 对过期的工人发起合同
        ws_driver = get_ws_driver(self.ws_url)
        sid = login(ws_driver, self.username, self.password)
        workers_name = get_save_mobile_number()
        user = login(ws_driver, workers_name, self.password)
        workflow_process_create(ws_driver, sid['data']['sid'], user['data']['user_id'], 0)
        web_login(self.browser, self.username1, self.password)
        verify_worker_exists(self.browser, user['data']['realname'])

    def tearDown(self):
        self.browser.close()


