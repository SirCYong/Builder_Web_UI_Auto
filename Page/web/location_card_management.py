# -*- coding: utf-8 -*-
# auth: cy
import random
from time import sleep

from selenium.webdriver.common.keys import Keys

from Page.Element import get_element, get_elements, is_element_present
from Page.web.into_level import into_two_level


def location_card(driver, people):
    into_two_level(driver, '设备管理')
    driver.find_element_by_xpath("//a[contains(text(),'定位卡')]").click()
    num = random.randint(1000000, 9999999)
    # 增加定位卡
    driver.find_elements_by_xpath("//button[contains(text(),'新增')]")[1].click()
    get_element(driver, ('xpath', "//input[@placeholder='请输入6-10定位卡卡号']")).send_keys(num)
    sleep(0.1)
    driver.find_element_by_xpath("//button[contains(text(),'确认')]").click()
    get_element(driver, ('xpath', "//input[@placeholder='请输入定位卡号或姓名筛选']")).send_keys(num)
    get_elements(driver, ('xpath', "//button[contains(text(),'筛选')]"))[1].click()
    assert str(num) == get_element(driver, ('xpath', "//*[@id='dwk-table']/tbody/tr/td[2]")).text, "不在location中,新增失败"
    # 增加并且绑定人
    num1 = random.randint(1000000, 9999999)
    driver.find_elements_by_xpath("//button[contains(text(),'新增')]")[1].click()
    get_element(driver, ('xpath', "//input[@placeholder='请输入6-10定位卡卡号']")).clear()
    get_element(driver, ('xpath', "//input[@placeholder='请输入6-10定位卡卡号']")).send_keys(num1)
    get_element(driver, ('xpath', "//span[@class='select2-selection__placeholder']")).click()
    get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(people)
    sleep(0.5)
    get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(Keys.ENTER)
    sleep(0.1)
    driver.find_element_by_xpath("//button[contains(text(),'确认')]").click()
    if is_element_present(driver, ('xpath', "//div[contains(text(),'该用户已绑定定位卡')]")):
        # 解绑定位卡
        sleep(6)
        get_element(driver, ('xpath', "//input[@placeholder='请输入定位卡号或姓名筛选']")).clear()
        get_element(driver, ('xpath', "//input[@placeholder='请输入定位卡号或姓名筛选']")).send_keys(people)
        get_elements(driver, ('xpath', "//button[contains(text(),'筛选')]"))[1].click()
        sleep(1)
        for i in range(len(get_elements(driver, ('xpath', "//*[@id='dwk-table']/tbody/tr"))), 0, -1):
            unbind_element = "//*[@id='dwk-table']/tbody/tr[%d]/td[10]/a" % i
            get_element(driver, ('xpath', unbind_element)).click()
            sleep(0.1)
            get_element(driver, ('xpath', "//*[@id='dwk']/form/div[4]/button[3]")).click()
            assert is_element_present(driver, ('xpath', "//i[@class='layui-layer-ico layui-layer-ico1']")), "解绑考勤卡失败"
        sleep(0.5)
        # 输入空格 查看全部
        get_element(driver, ('xpath', "//input[@placeholder='请输入定位卡号或姓名筛选']")).clear()
        get_element(driver, ('xpath', "//input[@placeholder='请输入定位卡号或姓名筛选']")).send_keys(' ')
        sleep(0.5)
        get_elements(driver, ('xpath', "//button[contains(text(),'筛选')]"))[1].click()
        driver.find_elements_by_xpath("//button[contains(text(),'新增')]")[1].click()
        sleep(0.5)
        get_element(driver, ('xpath', "//input[@placeholder='请输入6-10定位卡卡号']")).send_keys(num1)
        get_element(driver, ('xpath', "//span[@class='select2-selection__placeholder']")).click()
        get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(people)
        sleep(0.5)
        get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//button[contains(text(),'确认')]").click()
    get_element(driver, ('xpath', "//input[@placeholder='请输入定位卡号或姓名筛选']")).clear()
    get_element(driver, ('xpath', "//input[@placeholder='请输入定位卡号或姓名筛选']")).send_keys(num1)
    get_elements(driver, ('xpath', "//button[contains(text(),'筛选')]"))[1].click()
    sleep(1)
    assert people == get_element(driver, ('xpath', "//*[@id='dwk-table']/tbody/tr/td[3]")).text, "定位卡绑定人失败"
    for i in range(len(get_elements(driver, ('xpath', "//*[@id='dwk-table']/tbody/tr"))), 0, -1):
        location_element = "//*[@id='dwk-table']/tbody/tr[%d]/td[1]/input" % i
        get_element(driver, ('xpath', location_element)).click()
        driver.find_elements_by_xpath("//button[contains(text(),'删除')]")[1].click()
        get_elements(driver, ('xpath', "//button[contains(text(),'确认')]"))[3].click()
        get_element(driver, ('id', "success")).click()
        if is_element_present(driver, ('xpath', "//div[contains(text(),'无法删除已经绑定用户的定位卡，请重新选择用户，或者先解绑')]")):
            sleep(7)
            unbind_element = "//*[@id='dwk-table']/tbody/tr[%d]/td[10]/a" % i
            get_element(driver, ('xpath', unbind_element)).click()
            get_element(driver, ('xpath', "//*[@id='dwk']/form/div[4]/button[3]")).click()
            get_element(driver, ('xpath', location_element)).click()
            sleep(0.5)
            get_elements(driver, ('xpath', "//button[contains(text(),'删除')]"))[1].click()
            sleep(0.5)
            get_elements(driver, ('xpath', "//button[contains(text(),'确认')]"))[3].click()
            get_element(driver, ('id', "success")).click()
    assert is_element_present(driver, ('xpath', "//td[@colspan='10']")), "定位卡删除失败"







