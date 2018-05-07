# -*- coding: utf-8 -*-
# auth:CY
import unittest
from configparser import ConfigParser
from selenium import webdriver as browse_driver
from Page.web.logout import logout
from Page.web.web_login import web_login
from run_path import setting_path


class WebLogin(unittest.TestCase):
    def setUp(self):
        config = ConfigParser()
        config.read(setting_path())
        # option = browse_driver.ChromeOptions()
        # option.add_argument('disable-infobars')
        # 上面两行代表这 早chrome 浏览器时，可以忽略掉 chrome 正在受到自动软件的控制（只有在chrome 才会生效）
        self.browser = browse_driver.Firefox()
        self.browser.maximize_window()
        self.browser.get(config.get('testUrl', 'url'))
        self.username = config.get('operation', 'username')
        self.password = config.get('operation', 'password')

    def tearDown(self):
        self.browser.close()

    def test_01_login(self):
        web_login(self.browser, self.username, self.password)
        logout(self.browser)




