# -*- coding: utf-8 -*-
# Author:CY
# U:

from Page.Element import get_element, is_element_present_3s
from Page.web.get_now_time import screenshot_path


def web_login(driver, username, password):
    driver.find_element_by_xpath("//button[contains(text(),'登录')]").click()
    get_element(driver, ('id', "username")).send_keys(username)
    get_element(driver, ('id', "password")).send_keys(password)
    get_element(driver, ('id', "loginButton")).click()
    if is_element_present_3s(driver, ('id', "LAY_demo2"), '2'):
        assert get_element(driver, ('id', "LAY_demo2")).text == "成功:登录", "不在登陆页面，或者网速过慢，请重试"
    elif is_element_present_3s(driver, ('xpath', "//input[@placeholder='输入验证码']"), '2'):
        driver.find_element_by_xpath("//input[@placeholder='输入验证码']").send_keys('tttt')
        driver.find_element_by_id("loginButton").click()
    else:
        if is_element_present_3s(driver, ('id', "username"), '1'):
            driver.find_element_by_xpath("//button[contains(text(),'登录')]").click()
            get_element(driver, ('id', "username")).clear()
            get_element(driver, ('id', "username")).send_keys(username)
            get_element(driver, ('id', "password")).clear()
            get_element(driver, ('id', "password")).send_keys(password)
            get_element(driver, ('id', "loginButton")).click()
            if is_element_present_3s(driver, ('id', "LAY_demo2"), '2'):
                pass
            else:
                driver.get_screenshot_as_file(screenshot_path())
                assert False, "登陆失败"
    if is_element_present_3s(driver, ('xpath', "//input[@placeholder='输入验证码']"), '2'):
        driver.find_element_by_xpath("//input[@placeholder='输入验证码']").send_keys('tttt')
        driver.find_element_by_id("loginButton").click()




