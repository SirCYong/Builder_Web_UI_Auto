# -*- coding: utf-8 -*-
# auth: cy
import random
from Page.Element import get_element, get_elements, is_element_present
from Page.random_data import random_str
from Page.web.into_level import into_two_level


def brake_machine(driver):
    into_two_level(driver, '设备管理')
    driver.find_element_by_xpath("//a[contains(text(),'闸机')]").click()
    num = random_str(4) + str(random.randint(1000000, 9999999))
    random_ip = "192.168.1.%d" % random.randint(1, 255)
    # 增加闸机
    driver.find_elements_by_xpath("//button[contains(text(),'新增')]")[2].click()
    get_element(driver, ('xpath', "//input[@placeholder='请输入闸机设备号']")).send_keys(num)
    get_element(driver, ('xpath', "//option[contains(text(),'hpface联调闸机')]")).click()
    get_element(driver, ('xpath', "//input[@placeholder='请输入闸机IP']")).send_keys(random_ip)
    driver.find_element_by_xpath("//button[contains(text(),'确认')]").click()
    get_element(driver, ('xpath', "//input[@placeholder='请输入设备号筛选']")).send_keys(num)
    get_elements(driver, ('xpath', "//button[contains(text(),'筛选')]"))[2].click()
    assert str(num) == get_element(driver, ('xpath', "//*[@id='zj-table']/tbody/tr[1]/td[2]")).text, "不在location中,新增失败"
    # 更新闸机
    get_element(driver, ('xpath', "//*[@id='zj-table']/tbody/tr/td[5]/a")).click()
    num1 = random_str(4) + str(random.randint(1000000, 9999999))
    get_element(driver, ('xpath', "//input[@placeholder='请输入闸机号码']")).clear()
    get_element(driver, ('xpath', "//input[@placeholder='请输入闸机号码']")).send_keys(num1)
    driver.find_elements_by_xpath("//button[contains(text(),'确认')]")[1].click()
    get_element(driver, ('xpath', "//input[@placeholder='请输入设备号筛选']")).clear()
    get_element(driver, ('xpath', "//input[@placeholder='请输入设备号筛选']")).send_keys(num1)
    get_elements(driver, ('xpath', "//button[contains(text(),'筛选')]"))[2].click()
    assert str(num1) == get_element(driver, ('xpath', "//*[@id='zj-table']/tbody/tr[1]/td[2]")).text, "不在location中,新增失败"
    # 删除闸机
    get_element(driver, ('xpath', "//*[@id='zj-table']/tbody/tr/td[1]")).click()
    get_elements(driver, ('xpath', "//button[contains(text(),'删除')]"))[2].click()
    get_elements(driver, ('xpath', "//button[contains(text(),'确认')]"))[2].click()
    get_element(driver, ('id', "success")).click()
    assert is_element_present(driver, ('xpath', "//td[@colspan='5']")), "删除闸机失败"











