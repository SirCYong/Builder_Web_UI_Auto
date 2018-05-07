# -*- coding: utf-8 -*-
# auth cy
import unittest
from configparser import ConfigParser
from selenium import webdriver as browse_driver
from Page.web.attendance_machine import attendance_machine
from Page.web.brake_machine import brake_machine
from Page.web.camera_management import camera_management
from Page.web.location_card_management import location_card
from Page.web.logout import logout
from Page.web.web_login import web_login
from run_path import setting_path, file_path


class DeviceManagement(unittest.TestCase):
    def setUp(self):
        conf = ConfigParser()
        self.path = setting_path()
        self.file_path = file_path('1')
        conf.read(self.path)
        self.username = conf.get('projectManager', 'taohui')
        self.password = conf.get('operation', 'password')
        self.username1 = conf.get('management', 'yangyinghua')
        url = conf.get('testUrl', 'url')
        self.browser = browse_driver.Firefox()
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)
        self.browser.get(url)
        web_login(self.browser, self.username, self.password)

    def tearDown(self):
        self.browser.close()
        pass

    def test_01_attendance_machine(self):
        # 增加考勤卡
        attendance_machine(self.browser, '曹永')

    def test_02_location_card(self):
        # 定位卡
        location_card(self.browser, '周磊')

    def test_03_brake_machine(self):
        # 闸机
        brake_machine(self.browser)

    def test_04_camera_management(self):
        camera_management(self.browser)
