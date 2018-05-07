# -*- coding: utf-8 -*-
# Author:CY
# U:
import unittest
from configparser import ConfigParser
from time import sleep

from appium import webdriver as android_driver

from Page.android.android_login import android_login
from Page.android.get_udid import get_android_udid, get_android_version
from Page.android.handle_permissions_popovers import handle_permissions_popovers, agree_with_permissions
from Page.android.start_appium import start_android_appium
from Page.android.stop_appium import stop_android_appium
from run_path import file_path, setting_path


class AndroidLogin(unittest.TestCase):
    def setUp(self):
        conf = ConfigParser()
        self.file_path = file_path('1')
        conf.read(setting_path())
        self.username = conf.get('teamLeader', 'Zhenglinlin')
        self.password = conf.get('operation', 'password')
        self.username1 = conf.get('management', 'yangyinghua')
        device_name = get_android_udid()
        stop_android_appium()
        sleep(2)
        start_android_appium(device_name)
        desired_caps = {
            'platformName': 'Android',
            'deviceName': device_name,
            'platformVersion': get_android_version(),
            'appPackage': conf.get('android', 'appPackage'),
            'appActivity': conf.get('android', 'appActivity')
            # 'automationName':  'uiautomator2'
        }
        self.driver = android_driver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(3)
        handle_permissions_popovers(self.driver)
        android_login(self.driver, self.username, self.password)
        agree_with_permissions(self.driver)

    def test_01_asa(self):
        print('1')

    def tearDown(self):
        print('*************')
        pass
if __name__ == '__main__':
    unittest.main()


