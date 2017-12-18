# -*- coding: utf-8 -*-
# Author:CY
# U:
import getpass
import unittest
from configparser import ConfigParser
from time import sleep

from appium import webdriver as android_driver

from Page.android.android_login import android_login
from Page.android.get_udid import get_android_udid
from Page.android.start_appium import start_android_appium
from Page.android.stop_appium import stop_android_appium


class AndroidLogin(unittest.TestCase):
    def setUp(self):
        conf = ConfigParser()
        self.path = r'C:\Users\%s\Desktop\UIAutotest\TeseCase\Web\setting.ini' % (str(getpass.getuser()))
        self.file_path = r'C:\Users\%s\Desktop\UIAutotest\Page\file\1.jpg' % (str(getpass.getuser()))
        conf.read(self.path)
        self.username = conf.get('teamLeader', 'username')
        self.password = conf.get('operation', 'password')
        self.username1 = conf.get('management', 'yangyinghua')
        device_name = get_android_udid()
        stop_android_appium()
        sleep(2)
        start_android_appium(device_name)
        desired_caps = {
            'platformName': 'Android',
            'deviceName': device_name,
            'platformVersion': '7.1.1',
            'appPackage': 'cn.zlddata.zldtest',
            'appActivity': 'cn.zlddata.zldtest.MainActivity'
        }
        self.driver = android_driver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(3)
        android_login(self.driver, self.username, self.password)

    def test_01_asa(self):
        print('1')

    def tearDown(self):
        print('*************')
        pass
if __name__ == '__main__':
    unittest.main()


