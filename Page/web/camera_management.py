# -*- coding: utf-8 -*-
# auth: cy
import random
from Page.Element import get_element, get_elements, is_element_present
from Page.random_data import random_str
from Page.web.into_level import into_two_level


def camera_management(driver):
    into_two_level(driver, '设备管理')
    driver.find_element_by_xpath("//a[contains(text(),'摄像头')]").click()
    num = random_str(4) + str(random.randint(1000000, 9999999))
    random_ip = "rtsp://" + "192.168.1.%d" % random.randint(1, 255)
    # 增加摄像头
    driver.find_elements_by_xpath("//button[contains(text(),'新增')]")[3].click()
    get_element(driver, ('xpath', "//input[@placeholder='请输入摄像头设备号']")).send_keys(num)
    get_element(driver, ('xpath', "//option[contains(text(),'253112612')]")).click()
    camera_element = "//*[@id='sxt']/form/div[4]/select/option[%d]" % random.randint(1, 2)
    get_element(driver, ('xpath', camera_element)).click()
    get_element(driver, ('xpath', "//input[@placeholder='请输入rtsp地址']")).send_keys(random_ip)
    driver.find_element_by_xpath("//button[contains(text(),'确认')]").click()
    get_elements(driver, ('xpath', "//input[@placeholder='请输入设备号筛选']"))[1].send_keys(num)
    get_elements(driver, ('xpath', "//button[contains(text(),'筛选')]"))[3].click()
    assert str(num) == get_element(driver, ('xpath', "//*[@id='sxt-table']/tbody/tr[1]/td[2]")).text, "不在location中,新增失败"
    # 更新摄像头
    get_element(driver, ('xpath', "//*[@id='sxt-table']/tbody/tr/td[6]/a")).click()
    num1 = random_str(4) + str(random.randint(1000000, 9999999))
    get_element(driver, ('xpath', "//input[@placeholder='请输入摄像头设备号']")).clear()
    get_element(driver, ('xpath', "//input[@placeholder='请输入摄像头设备号']")).send_keys(num1)
    driver.find_elements_by_xpath("//button[contains(text(),'确认')]")[1].click()
    get_elements(driver, ('xpath', "//input[@placeholder='请输入设备号筛选']"))[1].clear()
    get_elements(driver, ('xpath', "//input[@placeholder='请输入设备号筛选']"))[1].send_keys(num1)
    get_elements(driver, ('xpath', "//button[contains(text(),'筛选')]"))[3].click()
    assert str(num1) == get_element(driver, ('xpath', "//*[@id='sxt-table']/tbody/tr[1]/td[2]")).text, "不在location中,新增失败"
    # 删除闸机
    get_element(driver, ('xpath', "//*[@id='sxt-table']/tbody/tr/td[1]")).click()
    get_elements(driver, ('xpath', "//button[contains(text(),'删除')]"))[3].click()
    get_elements(driver, ('xpath', "//button[contains(text(),'确认')]"))[2].click()
    get_element(driver, ('id', "success")).click()
    assert is_element_present(driver, ('xpath', "//td[@colspan='6']")), "删除闸机失败"











