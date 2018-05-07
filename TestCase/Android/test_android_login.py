# -*- coding: utf-8 -*-
# Author:CY
# U: 2018年4月9日
import unittest
from configparser import ConfigParser
from time import sleep
from appium import webdriver as android_driver
from Page.android.android_login import android_login, android_logout, android_employee_registration
from Page.android.get_udid import get_android_udid, get_android_version
from Page.android.handle_permissions_popovers import handle_permissions_popovers, agree_with_permissions
from Page.android.start_appium import start_android_appium
from Page.android.stop_appium import stop_android_appium
from Page.random_data import get_people_name, get_mobile
from run_path import file_path, setting_path


class AndroidLogin(unittest.TestCase):
    def setUp(self):
        conf = ConfigParser()
        self.file_path = file_path('1')
        conf.read(setting_path())
        self.username = conf.get('teamLeader', 'Zhenglinlin')
        self.password = conf.get('operation', 'password')
        self.username1 = conf.get('management', 'yangyinghua')
        appPackage = conf.get('android', 'appPackage')
        appActivity = conf.get('android', 'appActivity')
        print(appPackage + '\n' + appActivity)
        self.people = get_people_name()
        self.mobile = get_mobile()
        device_name = get_android_udid()
        stop_android_appium()
        sleep(2)
        start_android_appium(device_name)
        desired_caps = {
            'platformName': 'Android',
            'deviceName': device_name,
            'platformVersion': get_android_version(),
            'appPackage': 'com.zld.zld_face_rec_app',
            'appActivity': '.Login.LaunchActivity',
            # 'appPackage': appPackage,
            # 'appActivity': appActivity,
            'chromeOptions': {
                'androidProcess': 'com.zld.zld_face_rec_app'
            },
            'showChromedriverLog': True,
            'recreateChromeDriverSessions': True,
            # 'automationName':  'Uiautomator2'
        }
        self.driver = android_driver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(3)
        # handle_permissions_popovers(self.driver)

    def test_01_android_login(self):
        android_login(self.driver, self.username, self.password)
        android_logout(self.driver)

    def test_02_android_register(self):
        android_employee_registration(self.driver, '杭州富众', self.people, self.mobile)

    def tearDown(self):
        self.driver.quit()
