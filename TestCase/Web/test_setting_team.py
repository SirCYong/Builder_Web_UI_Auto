# -*- coding: utf-8 -*-
# Author:CY
# U: 2018-02-26
import getpass
import unittest
from configparser import ConfigParser
from selenium import webdriver as browse_driver
from websocket import create_connection

from Page.api.BuilderBaseFunc import BuilderBaseFunc
from Page.random_data import getRandomName
from Page.web.by_applying_for import employee_operation_the_all_workflow
from Page.web.logout import logout
from Page.web.setting_team import add_team, edit_organizational_structure, add_manager_for_organizational_structure
from Page.web.web_login import web_login
from run_path import setting_path, file_path


class SettingTeam(unittest.TestCase):
    def setUp(self):
        config = ConfigParser()
        self.path = setting_path()
        config.read(self.path)
        self.username = config.get('projectManager', 'taohui')
        self.operation = config.get('operation', 'username')
        self.password = config.get('operation', 'password')
        self.file_path = file_path('1')
        config.read(self.path)
        url = config.get('testUrl', 'url')
        ws_url = config.get('testUrl', 'ws_test_url')
        ws = create_connection("ws://%s/wsapi" % ws_url)
        self.ws_driver = BuilderBaseFunc(ws, ws_url)
        self.browser = browse_driver.Firefox()
        self.browser.maximize_window()
        self.browser.get(url)

        self.team_name = getRandomName()
        pass

    def tearDown(self):
        self.browser.close()
        pass

    def test_01_setting_team(self):
        web_login(self.browser, self.username, self.password)
        # 增加删除班组
        add_team(self.browser, self.team_name)

    def test_02_organizational_structure(self):
        # 清除 待处理任务
        employee_operation_the_all_workflow(self.browser, self.ws_driver, 1)
        logout(self.browser)
        employee_operation_the_all_workflow(self.browser, self.ws_driver, 2)
        logout(self.browser)
        # 平台运维登陆
        web_login(self.browser, self.operation, self.password)
        # 编辑组织架构
        add_manager_for_organizational_structure(self.browser, self.ws_driver)







