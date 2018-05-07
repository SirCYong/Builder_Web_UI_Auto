# -*- coding: utf-8 -*-
# auth: cy
from Page.Element import is_element_present


def set_role(driver, num):
    # 跳转到最后一页
    if is_element_present(driver, ('xpath', "//a[contains(text(),'‹')]")):
        driver.find_element_by_xpath("//a[contains(text(),'‹')]").click()
    # 选择最后一个人
    driver.find_elements_by_xpath("//input[@name='btSelectItem']")[-1].click()
    # 点击角色设置
    driver.find_element_by_xpath("//button[contains(text(),'角色设置')]").click()
    # 选择需要设置的角色
    # num 1 代表管理层；2 企业运维；3 项目经理；4 劳务经理；5 班组长；6 质量员
    role_element = ".//*[@id='lay-role-set']/div[2]/div[2]/select/option[%d]" % num
    driver.find_element_by_xpath(role_element).click()
    driver.find_element_by_xpath("//a[contains(text(),'确定')]").click()

