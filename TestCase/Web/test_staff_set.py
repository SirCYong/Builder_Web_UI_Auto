# -*- coding: utf-8 -*-
# auth: cy
# update 2018-03-30
import getpass
import random
import unittest
from configparser import ConfigParser
from time import sleep

from selenium import webdriver as browse_driver

from Page.Element import is_element_present, get_element, is_element_present_3s
from run_path import setting_path


class StaffSet(unittest.TestCase):
    def setUp(self):
        conf = ConfigParser()
        self.path = setting_path()
        self.file_path = r'C:\Users\%s\Desktop\UIAutotest\Page\file\1.jpg' % (str(getpass.getuser()))
        conf.read(self.path)
        self.username = conf.get('operation', 'username')
        self.password = conf.get('operation', 'password')
        url = conf.get('testUrl', 'url')
        self.browser = browse_driver.Firefox()
        self.browser.maximize_window()
        # 需要特别说明的是：隐性等待对整个driver的周期都起作用，所以只要设置一次即可，
        # 我曾看到有人把隐性等待当成了sleep在用，走哪儿都来一下…
        self.browser.get(url)
        from Page.web.web_login import web_login
        web_login(self.browser, self.username, self.password)
        pass

    def tearDown(self):
        self.browser.close()
        pass

    def test_01_SetManager(self):

        # 设置项目经理
        # 先获取职员当前是什么职位，然后对其进行设置角色，最后还原他的初始职位
        self.browser.find_element_by_xpath("//a[contains(text(),'职员管理')]").click()
        if is_element_present_3s(self.browser, ('xpath', "//a[contains(text(),'›')]"), 1):
            sleep(0.5)
            get_element(self.browser, ('xpath', "//a[contains(text(),'›')]")).click()
        num = self.browser.find_elements_by_class_name("bs-checkbox>input")  # 获取当前页的所有选中框
        random_num = random.randint(1, len(num))
        # 被选择人的姓名
        name_element = ".//*[@id='company-staff-table']/tbody/tr[%s]/td[2]/a" % random_num
        name = self.browser.find_element_by_xpath(name_element).text
        print(name)
        information_element = ".//*[@id='company-staff-table']/tbody/tr[%s]/td[2]/a" % random_num
        self.browser.find_element_by_xpath(information_element).click()
        sleep(1)
        # 职务
        get_role = self.browser.find_element_by_xpath(".//*[@id='basic']/div/div[2]/div[5]/div/span").text
        print(get_role)
        # 关闭按钮
        self.browser.find_element_by_class_name("layui-layer-ico.layui-layer-close.layui-layer-close1").click()
        # 选中人
        people_element = ".//*[@id='company-staff-table']/tbody/tr[%s]/td[1]/input" % random_num
        for i in range(1, 6):
            if i > 1:
                sleep(1)
                get_element(self.browser, ('xpath', "//a[contains(text(),'›')]")).click()
            sleep(0.5)
            self.browser.find_element_by_xpath(people_element).click()
            sleep(0.5)
            self.browser.find_element_by_xpath("//button[contains(text(),'角色设置')]").click()  # 点击角色设置
            role_element = ".//*[@id='lay-role-set']/div[2]/div[2]/select/option[%d]" % i
            get_element(self.browser, ('xpath', role_element)).click()
            sleep(0.5)
            self.browser.find_element_by_xpath("//a[contains(text(),'确定')]").click()
            sleep(0.5)
        if is_element_present_3s(self.browser, ('xpath', "//a[contains(text(),'›')]"), 1):
            sleep(0.5)
            get_element(self.browser, ('xpath', "//a[contains(text(),'›')]")).click()
        self.browser.find_element_by_xpath(people_element).click()
        self.browser.find_element_by_xpath("//button[contains(text(),'角色设置')]").click()  # 点击角色设置
        old_role_element = "//option[contains(text(),'%s')]" % get_role
        self.browser.find_elements_by_xpath(old_role_element)[1].click()
        self.browser.find_element_by_xpath("//a[contains(text(),'确定')]").click()
        assert self.browser.find_element_by_class_name("layui-layer-content.layui-layer-padding").text == '成功'


