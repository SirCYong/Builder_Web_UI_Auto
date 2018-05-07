# -*- coding: utf-8 -*-
# Author:CY
# U: 2018年4月3日
import getpass
import unittest
from configparser import ConfigParser
from selenium import webdriver as browse_driver
from Page.random_data import get_people_name
from Page.web.approve_workflow import approve_workflow
from Page.web.by_applying_for import initiate_artifacts, to_apply_for_leave, batch_add_workman, request_for_overtime, \
    change_time_of_attendance
from Page.web.logout import logout
from Page.web.web_login import web_login
from run_path import setting_path


class ByApplyingFor(unittest.TestCase):
    def setUp(self):
        conf = ConfigParser()
        self.path = setting_path()
        self.file_path = r'C:\Users\%s\Desktop\UIAutotest\Page\file\1.jpg' % (str(getpass.getuser()))
        conf.read(self.path)
        self.username = conf.get('teamLeader', 'Zhenglinlin')
        self.password = conf.get('operation', 'password')
        self.username1 = conf.get('projectManager', 'taohui')
        url = conf.get('testUrl', 'url')
        self.browser = browse_driver.Firefox()
        self.browser.maximize_window()
        self.browser.get(url)
        web_login(self.browser, self.username, self.password)

    def tearDown(self):
        self.browser.close()
        pass

    def test_01_to_apply_for_leave(self):
        # 单人请假工作流
        to_apply_for_leave(self.browser, self.file_path, get_people_name())
        logout(self.browser)
        web_login(self.browser, self.username1, self.password)
        approve_workflow(self.browser, '请假工作流')

    def test_02_batch_add_workman(self):
        # 批量请假工作流
        batch_add_workman(self.browser, self.file_path, get_people_name())
        logout(self.browser)
        web_login(self.browser, self.username1, self.password)
        approve_workflow(self.browser, '请假工作流', 2)

    def test_03_initiate_artifacts(self):
        # 工件完成工作流
        initiate_artifacts(self.browser, self.file_path)
        logout(self.browser)
        web_login(self.browser, self.username1, self.password)
        approve_workflow(self.browser, '工件完成工作流')

    def test_04_request_for_overtime(self):
        # 加班工作流
        request_for_overtime(self.browser, get_people_name(), self.file_path)
        logout(self.browser)
        web_login(self.browser, self.username1, self.password)
        approve_workflow(self.browser, '加班工作流')

    def test_05_change_time_of_attendance(self):
        many_people = 2
        # 修改出勤时间工作流
        change_time_of_attendance(self.browser, get_people_name(), self.file_path, many_people)
        logout(self.browser)
        web_login(self.browser, self.username1, self.password)
        approve_workflow(self.browser, '修正工人考勤异常', many_people)


