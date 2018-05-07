# -*- coding: utf-8 -*-
# auth:CY
# update 2018-02-26
import unittest
from configparser import ConfigParser
from selenium import webdriver as browse_driver
from Page.random_data import get_people_name
from Page.web.approve_workflow import approve_workflow
from Page.web.attendance_machine import attendance_machine_login
from Page.web.logout import logout
from Page.web.setting_area import setting_area, delete_area, setting_attendance_machine
from Page.web.update_PM import update_PM, project_delay
from Page.web.web_login import web_login
from run_path import setting_path


class SettingArea(unittest.TestCase):
    def setUp(self):
        config = ConfigParser()
        config.read(setting_path())
        self.browser = browse_driver.Firefox()
        self.browser.maximize_window()
        url = config.get('testUrl', 'url')
        print(url)
        self.browser.get(config.get('testUrl', 'url'))
        self.username = config.get('projectManager', 'taohui')
        self.password = config.get('operation', 'password')
        self.manager_username = config.get('management', 'Hujinping')
        self.area_name = get_people_name()
        web_login(self.browser, self.username, self.password)

    def tearDown(self):
        self.browser.close()

    def test_01_setting_area(self):
        # 增加编辑区域
        setting_area(self.browser, self.area_name)

    def test_02_delete_area(self):
        # 删除区域
        delete_area(self.browser)

    # def test_03_update_PM(self):
    #     logout(self.browser)
    #     web_login(self.browser, self.manager_username, self.password)
    #     update_PM(self.browser)

    def test_04_project_delay(self):
        # 项目延期
        project_delay(self.browser)

    def test_05_setting_attendance_machine(self):
        # 等待梁天明解决顺序问题，和选择工程区域与目标区域不一致的问题,有问题
        setting_attendance_machine(self.browser, get_people_name())

    def test_06_attendance_machine_login(self):
        attendance_machine_login(self.browser)




