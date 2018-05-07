# -*- coding: utf-8 -*-
# auth : cy
from time import sleep

from Page.Element import is_element_present, get_element, is_element_present_3s
from Page.web.get_now_time import bug_photo


def verify_real_name(driver, name, identity, path1, path2):
    """

    :param driver:
    :param name: 姓名
    :param identity: 身份证号
    :param path1: 身份证正面路径
    :param path2:身份证反面路径
    :return:
    """
    sleep(1)
    get_element(driver, ('id', 'dropdownMenu-set')).click()
    if is_element_present_3s(driver, ('xpath', "//a[contains(text(),'实名认证')]"), 2):
        sleep(1)
        get_element(driver, ('xpath', "//a[contains(text(),'实名认证')]")).click()
    else:
        pass
    if is_element_present(driver, ('xpath', "//button[@class='zdy-btn-blue reg-btn']")):
        sleep(4)
        get_element(driver, ('xpath', "//button[@class='zdy-btn-blue reg-btn']")).click()
        get_element(driver, ('xpath', "//input[@placeholder='真实姓名(必须填写)']")).clear()
        get_element(driver, ('xpath', "//input[@placeholder='真实姓名(必须填写)']")).send_keys(name)
        get_element(driver, ('xpath', "//input[@placeholder='身份证号(必须填写)']")).send_keys(identity)
        get_element(driver, ('id', "file1")).send_keys(path1)
        get_element(driver, ('id', "file2")).send_keys(path2)
        driver.find_element_by_xpath("//button[contains(text(),'完成认证')]").click()
        sleep(5)
        if is_element_present(driver, ('xpath', "//a[contains(text(),'个人面板')]")):
            assert get_element(driver, ('id', 'dropdownMenu-set')).text == name, "认证失败"
        else:
            bug_photo(driver)
            assert False, "没跳转到实名认证后的页面"
    else:
        print("该用户已经实名认证")

