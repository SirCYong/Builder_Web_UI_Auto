# -*- coding: utf-8 -*-
# auth:CY
import getpass
import random
import unittest
from configparser import ConfigParser
from time import sleep
from selenium import webdriver as browse_driver
from Page.Element import is_element_present, get_element, is_element_present_3s
from Page.random_data import random_str
from Page.web.get_now_time import bug_photo
from Page.web.web_login import web_login
from run_path import setting_path


class CompanyInformation(unittest.TestCase):
    def setUp(self):
        conf = ConfigParser()
        self.path = setting_path()
        self.file_path = r'C:\Users\%s\Desktop\UIAutotest\Page\file\1.jpg' % (str(getpass.getuser()))
        conf.read(self.path)
        self.username = conf.get('management', 'Hujinping')
        self.password = conf.get('management', 'password')
        url = conf.get('testUrl', 'url')
        self.browser = browse_driver.Firefox()
        self.browser.maximize_window()
        self.browser.get(url)
        self.certificate_number = random_str(6)
        pass

    def tearDown(self):
        self.browser.close()
        pass

    def test_add_company_information(self):
        web_login(self.browser, self.username, self.password)
        try:
            self.browser.find_element_by_xpath("//button[contains(text(),'新增')]").click()
            # 资质专业
            a = ['公路工程施工总承包资质', '铁路工程施工总承包资质', '港口与航道工程施工总承包资质', '地质专业']
            self.browser.find_element_by_xpath(".//*[@id='add-zizhi']/form/div[4]/input").send_keys(a[random.randint(0, 3)])
            # 证书号码
            self.browser.find_element_by_xpath(".//*[@id='add-zizhi']/form/div[6]/input").send_keys(self.certificate_number)
            # 发证机关
            c = '政府'
            self.browser.find_element_by_xpath(".//*[@id='add-zizhi']/form/div[8]/input").send_keys(c)
            # 有效期
            d = random.randint(1, 9)
            self.browser.find_element_by_xpath("//input[@placeholder='年']").send_keys(d)
            # 复审时间
            self.browser.find_element_by_xpath("//input[@placeholder='选择日期不得早于今天']").click()
            self.browser.find_element_by_xpath("html/body/div[5]/div[3]/table/tbody/tr[6]/td[7]/div").click()
            # 证书正面
            get_element(self.browser, ('id', 'file1')).send_keys(self.file_path)
            # 证书反面
            get_element(self.browser, ('id', 'file2')).send_keys(self.file_path)
            sleep(1)
            get_element(self.browser, ('xpath', "//button[contains(text(),'确认')]")).click()
            self.browser.refresh()
            new_elem = "//td[contains(text(),%s)]" % self.certificate_number
            sleep(0.5)
            select_companys_name = self.browser.find_elements_by_xpath(new_elem)
            certificate_number_list = []
            j = 2
            # 获取所有的证书号码
            for i in range(int(len(select_companys_name) / 6)):
                certificate_number_list.insert(i, self.browser.find_elements_by_xpath(new_elem)[j].text)
                j += 6
            print(certificate_number_list)
            assert self.certificate_number in certificate_number_list, "资质未增加成功"
            information_element = "//tr[@data-index='0']"
            sleep(0.5)
            self.browser.find_elements_by_xpath(information_element)[0].click()
            # 验证图片是否上传成功
            if is_element_present_3s(self.browser, ('xpath', "//div[1]/img[@style='display: none;']"), 3):
                print("图片未上传成功")
                assert False
            else:
                pass
            # 删除证书
            get_element(self.browser, ('xpath', "//button[contains(text(),'删除')]")).click()
            get_element(self.browser, ('id', "success")).click()
            assert is_element_present(self.browser, ('xpath', "//div[@id='LAY_demo2']")), "未弹出删除成功框"
            sleep(3)
            certificate_number_list_1 = []
            j = 2
            sleep(1)
            new_select_companys_name = self.browser.find_elements_by_xpath(new_elem)
            # 获取所有的证书号码
            for i in range(int(len(new_select_companys_name) / 6)):
                certificate_number_list_1.insert(i, self.browser.find_elements_by_xpath(new_elem)[j].text)
                j += 6
            print(certificate_number_list_1)
            if self.certificate_number in certificate_number_list_1:
                print("删除证书失败")
                assert False
            else:
                pass
        except Exception as e:
            print(e)
            bug_photo(self.browser)
            assert False
