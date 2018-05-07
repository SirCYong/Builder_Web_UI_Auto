# -*- coding: utf-8 -*-
# auth: CY
import unittest
from configparser import ConfigParser
from time import sleep
from selenium import webdriver as browser_driver
from Page.Element import get_element
from Page.random_data import get_company_name, random_str, getRandomName, get_telephone
from Page.web.into_level import into_one_level, into_two_level
from Page.web.web_login import web_login
from run_path import setting_path


class NewCompany(unittest.TestCase):
    def setUp(self):
        conf = ConfigParser()
        conf.read(setting_path())
        self.username = conf.get('operation', 'username')
        self.password = conf.get('operation', 'password')
        self.url = conf.get('testUrl', 'url')
        self.driver = browser_driver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        web_login(self.driver, self.username, self.password)

    def tearDown(self):
        self.driver.quit()

    def test_NewCompany(self):
        company_name = get_company_name()
        into_one_level(self.driver, '运维面板')
        into_two_level(self.driver, '注册公司管理')
        self.driver.find_element_by_xpath("//button[contains(text(),'新增')]").click()
        self.driver.find_element_by_xpath("//input[@placeholder='企业名称']").send_keys(company_name)
        self.driver.find_element_by_xpath("//input[@placeholder='0000XX0000']").send_keys(random_str(18))
        # a = self.driver.find_element_by_xpath(".//*[@id='company-address']/div/div[1]/select")
        # a.find_element_by_xpath("//option[@value='北京市']").click()  # 方法1
        self.driver.find_element_by_xpath(".//*[@id='company-address']/div/div[1]/select/option[12]").click()  # 方法2 省
        # Select(a).select_by_value('内蒙古自治区')  # 方法3
        self.driver.find_element_by_xpath(".//*[@id='company-address']/div/div[2]/select/option[2]").click()  # 市
        self.driver.find_element_by_xpath(".//*[@id='company-address']/div/div[3]/select/option[3]").click()  # 区
        self.driver.find_element_by_xpath("//input[@placeholder='输入街道名称']").send_keys('南京路')
        self.driver.find_element_by_xpath("//input[@placeholder='门派号、小区名称、房间号']").send_keys('3号')
        information = '室内装潢及设计、园林绿化、园林绿化工程施工等'
        self.driver.find_element_by_xpath("//textarea[@placeholder='长度不超过500个字符']").send_keys(information)
        get_element(self.driver, ('xpath', "//input[@placeholder='企业固定电话格式 例：0759-7654321']")).send_keys(get_telephone())
        self.driver.find_element_by_xpath("//input[@placeholder='输入法人姓名']").send_keys(getRandomName())
        self.driver.find_element_by_xpath("//button[contains(text(),'完成')]").click()
        self.driver.refresh()
        sleep(2)
        elem = "//td[contains(text(),%s)]" % company_name
        get_element(self.driver, ('xpath', "//input[@placeholder='请输入公司名称筛选']")).send_keys(company_name)
        get_element(self.driver, ('xpath', "//button[contains(text(),'搜索')]")).click()
        sleep(1)
        new_company_name = self.driver.find_elements_by_xpath(elem)[0].text
        assert new_company_name == company_name
        get_element(self.driver, ('xpath', "//input[@placeholder='请输入公司名称筛选']")).clear()
        get_element(self.driver, ('xpath', "//input[@placeholder='请输入公司名称筛选']")).send_keys(company_name)
        get_element(self.driver, ('xpath', "//button[contains(text(),'搜索')]")).click()
        elem = "//td[contains(text(),%s)]" % company_name
        select_company_name = self.driver.find_element_by_xpath(elem).text
        assert select_company_name == company_name  # 全称查询公司
        self.driver.find_element_by_xpath("//input[@placeholder='请输入公司名称筛选']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='请输入公司名称筛选']").send_keys(company_name[1:3])
        self.driver.find_element_by_xpath("//button[contains(text(),'搜索')]").click()
        assert company_name in select_company_name
        new_elem = "//td[contains(text(),%s)]" % company_name
        sleep(0.5)
        select_companys_name = self.driver.find_elements_by_xpath(new_elem)
        company_name_list = []
        j = 0  # 公司的index 规律是每5个就是公司的text
        # 获取所有的公司名称
        for i in range(int(len(select_companys_name) / 5)):
            company_name_list.insert(i, self.driver.find_elements_by_xpath(new_elem)[j].text)
            j += 5
        print(company_name_list)
        assert company_name in company_name_list  # 包含这个字段的公司，在列表里面

