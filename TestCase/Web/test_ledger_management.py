# -*- coding: utf-8 -*-
# auth:CY
# update 2018年4月8日
import unittest
from configparser import ConfigParser
from selenium import webdriver as browse_driver
from Page.web.ledger_managemnent import upload_file_document_library
from Page.web.web_login import web_login
from run_path import setting_path, file_path


class LedgerManagement(unittest.TestCase):
    def setUp(self):
        # # 实例化一个火狐配置文件
        # fp = browse_driver.FirefoxProfile()
        # # 设置各项参数，参数可以通过在浏览器地址栏中输入about:config查看。
        # # 设置成0代表下载到桌面，1代表浏览器默认下载路径；设置成2则可以保存到指定目录
        # fp.set_preference("browser.download.folderList", 2)
        # # 是否显示开始,(个人实验，不管设成True还是False，都不显示开始，直接下载)
        # fp.set_preference("browser.download.manager.showWhenStarting", False)
        # # 下载到指定目录
        # fp.set_preference("browser.download.dir", test_report_path())  # 路径名称文件夹设置成英文，不然不能下载到指定目录
        # # 不询问下载路径；后面的参数为要下载页面的Content-type的值
        # fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")
        config = ConfigParser()
        config.read(setting_path())
        self.file_path = file_path('1')
        # self.driver = browse_driver.Firefox(firefox_profile=fp)
        self.driver = browse_driver.Firefox()
        self.driver.maximize_window()
        self.driver.get(config.get('testUrl', 'url'))
        self.username = config.get('projectManager', 'taohui')
        self.password = config.get('operation', 'password')
        web_login(self.driver, self.username, self.password)

    def tearDown(self):
        self.driver.close()

    def test_01_upload_fix_file(self):
        upload_file_document_library(self.driver)


