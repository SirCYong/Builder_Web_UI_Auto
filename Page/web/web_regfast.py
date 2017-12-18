# -*- coding: utf-8 -*-
# Author:CY
# U:
from time import sleep
from selenium.webdriver.common.keys import Keys

from Page.Element import get_element, get_elements, is_element_present_3s
from Page.random_data import get_mobile
from Page.web.get_now_time import bug_photo


def web_workman_register(browser, mobile, code, password):
    # 工人注册
    """

    :param browser:
    :param mobile:
    :param code:
    :param password:
    :return:
    """
    try:
        browser.find_element_by_xpath("//button[contains(text(),'注册')]").click()
        sleep(1)
        get_element(browser, ('id', 'username')).send_keys(mobile)
        browser.find_element_by_xpath("//span[contains(text(),'点击获取验证码')]").click()
        new_mobile = get_mobile()
        if is_element_present_3s(browser, ('xpath', "//div[contains(text(),'此号码已经存在，无需注册')]"), 3):
            get_element(browser, ('id', 'username')).send_keys(new_mobile)
            browser.find_element_by_xpath("//span[contains(text(),'点击获取验证码')]").click()
            get_elements(browser, ('xpath', "//input[@placeholder='短信校验码']"))[0].send_keys(code)
            get_element(browser, ('id', "password")).send_keys(password)
            get_element(browser, ('id', 'repassword')).send_keys(password)
            sleep(1)
            get_element(browser, ('id', 'repassword')).click()
            get_element(browser, ('xpath', "//input[@class='agree-input']")).click()
            browser.find_element_by_xpath("//button[contains(text(),'创建账户')]").click()
            sleep(2)
            browser.find_element_by_xpath("//button[contains(text(),'登录')]").click()
            get_element(browser, ('id', "username")).send_keys(mobile)
            get_element(browser, ('id', "password")).send_keys(password)
            get_element(browser, ('id', "loginButton")).click()
            sleep(3)
        else:
            get_elements(browser, ('xpath', "//input[@placeholder='短信校验码']"))[0].send_keys(code)
            get_element(browser, ('id', "password")).send_keys(password)
            get_element(browser, ('id', 'repassword')).send_keys(password)
            sleep(1)
            get_element(browser, ('id', 'repassword')).click()
            get_element(browser, ('xpath', "//input[@class='agree-input']")).click()
            browser.find_element_by_xpath("//button[contains(text(),'创建账户')]").click()
            sleep(0.5)
            if is_element_present_3s(browser,
                                     ('xpath', "//span[@class='text-muted tel-tip' and contains(text(),'必须填写')]"),
                                     2):
                get_element(browser, ('id', 'username')).clear()
                get_element(browser, ('id', 'username')).send_keys(mobile)
                get_elements(browser, ('xpath', "//input[@placeholder='短信校验码']"))[0].clear()
                get_elements(browser, ('xpath', "//input[@placeholder='短信校验码']"))[0].send_keys(code)
                get_element(browser, ('id', "password")).clear()
                get_element(browser, ('id', "password")).send_keys(password)
                get_element(browser, ('id', 'repassword')).clear()
                get_element(browser, ('id', 'repassword')).send_keys(password)
                sleep(0.5)
                get_element(browser, ('id', 'repassword')).click()
                sleep(0.1)
                browser.find_element_by_xpath("//button[contains(text(),'创建账户')]").click()
                sleep(2)
            browser.find_element_by_xpath("//button[contains(text(),'登录')]").click()
            get_element(browser, ('id', "username")).send_keys(mobile)
            get_element(browser, ('id', "password")).send_keys(password)
            get_element(browser, ('id', "loginButton")).click()
        return mobile
    except Exception as e:
        print(e)
        print("工人注册失败")
        assert False


def web_employee_registration(browser, name, mobile, password, company_name):
    # 企业员工注册
    """

    :param browser:
    :param name:
    :param mobile:
    :param password:
    :param company_name:
    :return:
    """
    browser.find_element_by_xpath("//button[contains(text(),'注册')]").click()
    sleep(0.5)
    browser.find_element_by_xpath("//div[contains(text(),'企业员工')]").click()
    get_element(browser, ('xpath', "//input[@data-pattern-message='请输入正确的手机号码']")).send_keys(mobile)
    get_elements(browser, ('xpath', "//span[contains(text(),'点击获取验证码')]"))[0].click()
    if is_element_present_3s(browser, ('xpath', "//div[contains(text(),'此号码已经存在，无需注册')]"), 5):
        get_element(browser, ('id', 'username')).send_keys(get_mobile())
    get_element(browser, ('xpath', "//input[@placeholder='短信校验码']")).send_keys('11111')
    get_element(browser, ('xpath', "//input[@data-tip='请输入真实姓名']")).send_keys(name)
    get_element(browser, ('id', "password1")).send_keys(password)
    get_element(browser, ('xpath', "//input[@data-tip='请再新输入密码']")).send_keys(password)
    get_element(browser, ('xpath', "//b[@role='presentation']")).click()
    get_element(browser, ('xpath', "//input[@class='select2-search__field' and @type='search']")).send_keys(
        company_name)
    sleep(0.5)
    get_element(browser, ('xpath', "//input[@class='select2-search__field' and @type='search']")).send_keys(Keys.ENTER)
    get_element(browser, ('xpath', "//input[@class='agree-input']")).click()
    get_element(browser, ('xpath', "//button[contains(text(),'创建账户')]")).click()
    if '成功:公司职员注册' == get_element(browser, ('xpath', "//div[contains(text(),'成功:公司职员注册')]")).text:
        pass
    else:
        print("失败:公司职员注册")
        bug_photo(browser)
        assert False
    sleep(2)
    browser.find_element_by_xpath("//button[contains(text(),'登录')]").click()
    get_element(browser, ('id', "username")).send_keys(mobile)
    get_element(browser, ('id', "password")).send_keys(password)
    get_element(browser, ('id', "loginButton")).click()



