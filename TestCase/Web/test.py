# -*- coding: utf-8 -*-
# Author:CY
# U:
import getpass
import os
import unittest
from configparser import ConfigParser
from time import sleep

from selenium import webdriver as browse_driver

from Page.random_data import get_mobile, getCompanyName, getPeopleName, getDistrictCode
from Page.web.approve_workflow import approve_workflow
from Page.web.attendance_machine import attendance_machine
from Page.web.brake_machine import brake_machine
from Page.web.by_applying_for import initiate_artifacts, to_apply_for_leave, batch_add_workman, request_for_overtime, \
    change_time_of_attendance
from Page.web.camera_management import camera_management
from Page.web.location_card_management import location_card
from Page.web.logout import logout
from Page.web.new_general_contract import general_contract, contract_workflow, subcontract
from Page.web.select_city import select_city
from Page.web.set_role import set_role
from Page.web.setting_area import setting_attendance_machine
from Page.web.verify_real_name import verify_real_name
from Page.web.web_login import web_login
from Page.web.web_regfast import web_employee_registration, web_workman_register
from Page.web.workman_contract import change_workman_contract_date


class CyGoHome(unittest.TestCase):
    def setUp(self):
        conf = ConfigParser()
        self.path = r'C:\Users\%s\Desktop\UIAutotest\TeseCase\Web\setting.ini' % (str(getpass.getuser()))
        self.file_path = r'C:\Users\%s\Desktop\UIAutotest\Page\file\1.jpg' % (str(getpass.getuser()))
        conf.read(self.path)
        self.username = conf.get('labor', 'Wuhuigang')
        # self.username = conf.get('teamLeader', 'Zhenglinlin')
        self.password = conf.get('operation', 'password')
        self.username1 = conf.get('projectManager', 'taohui')
        url = conf.get('testUrl', 'perfurl')
        self.browser = browse_driver.Firefox()
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)
        # 需要特别说明的是：隐性等待对整个driver的周期都起作用，所以只要设置一次即可，
        # 我曾看到有人把隐性等待当成了sleep在用，走哪儿都来一下…
        self.browser.get(url)
        self.mobile = get_mobile()
        # self.mobile = 15308222551
        web_login(self.browser, self.username, self.password)
        change_workman_contract_date(self.browser,  self.file_path)
        logout(self.browser)
        web_login(self.browser, self.username1, self.password)
        approve_workflow(self.browser, '修改用工合同结束时间')


        # general_contract(self.browser, '总包合同', '杭州', '浙江', '测试试试试试')
        # select_city(self.browser)
        pass

    def tearDown(self):
        print('*************')
        self.browser.close()
        pass

    def testDse(self):
        # a = self.browser.find_elements_by_xpath("//*[@id='chtsx']/div[1]/select/option")
        # company_name = '中国卜办业或有限公司'
        # people_name = getPeopleName()
        # identity = getDistrictCode()
        # print(self.mobile)
        project_name = '测试试试试试'
        sub_project_name = '分包测试试试试试'

        # general_contract(self.browser, '总包合同', '杭州', '浙江', project_name)
        # logout(self.browser)
        # web_login(self.browser, self.username1, self.password)
        # contract_workflow(self.browser, '总包合同')
        # subcontract(self.browser, project_name, '杭州富众人力资源有限公司', sub_project_name, '盛大为')

        # web_employee_registration(self.browser, people_name, self.mobile, self.password, company_name)
        # web_regfast(self.browser, self.mobile, '11111', self.password)
        # web_login(self.browser, self.mobile, self.password)
        # verify_real_name(self.browser, people_name, identity, self.file_path, self.file_path)

        pass
if __name__ == '__main__':
    unittest.main()
