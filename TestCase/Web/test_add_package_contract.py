# -*- coding: utf-8 -*-
# auth: cy
import getpass
import unittest
from configparser import ConfigParser
from selenium import webdriver as browse_driver

from Page.random_data import getContractName
from Page.web.logout import logout
from Page.web.new_general_contract import general_contract, contract_workflow, subcontract
from Page.web.web_login import web_login
from run_path import setting_path


class AddPackageContract(unittest.TestCase):
    def setUp(self):
        conf = ConfigParser()
        self.path = setting_path()
        self.file_path = r'C:\Users\%s\Desktop\UIAutotest\Page\file\1.jpg' % (str(getpass.getuser()))
        conf.read(self.path)
        self.username = conf.get('operation', 'username')
        self.password = conf.get('operation', 'password')
        self.Hujinping = conf.get('management', "Hujinping")
        self.labor_management = conf.get('management', 'labor_management')
        url = conf.get('testUrl', 'url')
        self.browser = browse_driver.Firefox()
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)
        self.browser.get(url)
        text = getContractName()
        # 总包合同名称
        self.package_contract = text + '合同'
        # 总包工程名称
        self.project_name = '中国' + text + '工程'
        # 分包工程名称
        self.subcontracting_project_name = '分包' + self.project_name
        # 劳务经理的名字
        self.labor_name = "吴汇钢"
        web_login(self.browser, self.username, self.password)
        pass

    def tearDown(self):
        self.browser.close()
        pass

    def test_01_general_contract(self):
        # 发包方
        contract_awarding = '苑通生态建设有限公司'
        # 承包方 第一管理层 胡金平18969026106
        contracting = '杭州智链达数据有限公司'
        # 分包方 劳务经理的名字记的更改
        # 总包合同
        general_contract(self.browser, self.package_contract, contract_awarding, contracting, self.project_name)
        logout(self.browser)
        web_login(self.browser, self.username, self.password)
        subcontracting = '杭州富众人力有限公司'
        subcontract(self.browser, self.project_name, subcontracting, self.subcontracting_project_name, self.labor_name)


