# -*- coding: utf-8 -*-
# Author:CY
# U:
import getpass
import unittest
from configparser import ConfigParser
from selenium import webdriver as browse_driver

from Page.random_data import getRandomName
from Page.web.setting_team import add_team
from Page.web.web_login import web_login
from run_path import setting_path


class SettingTeam(unittest.TestCase):
    def setUp(self):
        conf = ConfigParser()
        self.path = setting_path()
        conf.read(self.path)
        self.username = conf.get('projectManager', 'taohui')
        self.password = conf.get('operation', 'password')
        url = conf.get('testUrl', 'perfurl')
        self.browser = browse_driver.Firefox()
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)
        # 需要特别说明的是：隐性等待对整个driver的周期都起作用，所以只要设置一次即可，
        self.browser.get(url)
        web_login(self.browser, self.username, self.password)
        self.team_name = getRandomName()
        pass

    def tearDown(self):
        self.browser.close()
        pass

    def test_01_setting_team(self):
        # 增加删除班组
        add_team(self.browser, self.team_name)







