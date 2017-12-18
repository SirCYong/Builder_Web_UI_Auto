# -*- coding: utf-8 -*-
# auth cy
from time import sleep

from Page.Element import get_element, get_elements
from Page.web.get_now_time import bug_photo
from Page.web.web_login import web_login


def forget_password(driver, mobile, new_password, code):
    driver.find_element_by_xpath("//button[contains(text(),'登录')]").click()
    sleep(0.5)
    driver.find_element_by_xpath("//a[contains(text(),'忘记密码?')]").click()
    # 输入用户名
    sleep(0.1)
    get_element(driver, ('id', "user")).send_keys(mobile)
    # 输入新密码
    get_element(driver, ('id', "newPassWork")).send_keys(new_password)
    # 再次输入密码
    get_element(driver, ('xpath', "//input[@placeholder='请再次输入确认密码']")).send_keys(new_password)
    # driver.find_elements_by_xpath("//span[contains(text(),'点击获取验证码')]")[1].click()
    get_elements(driver, ('xpath', "//span[contains(text(),'点击获取验证码')]"))[1].click()
    # 输入验证码
    get_element(driver, ('xpath', ".//*[@id='forgetPass']/form/div[4]/div[2]/input")).send_keys(code)
    sleep(0.5)
    driver.find_elements_by_xpath("//button[contains(text(),'重置密码')]")[1].click()
    sleep(6)
    try:
        web_login(driver, mobile, new_password)
        print('重置密码，且登陆成功')
    except Exception as e:
        print(e)
        print("重置密码失败")
        assert False


def account_setting(driver, mobile, password):
    get_element(driver, ('id', 'dropdownMenu-set')).click()
    get_element(driver, ('xpath', "//a[@role='menuitem' and contains(text(),'账号设置') ]")).click()
    get_element(driver, ('id', 'user')).send_keys(mobile)
    get_element(driver, ('id', 'newPassWork')).send_keys(password)
    get_element(driver, ('xpath', "//input[@placeholder='请再次输入确认密码']")).send_keys(password)
    get_element(driver, ('xpath', "//span[contains(text(),'点击获取验证码') and @class='get-btn']")).click()
    get_element(driver, ('xpath', "//div[@class='col-sm-5']/input")).send_keys('11111')
    sleep(0.5)
    get_element(driver, ('xpath', "//button[@class='btn btn-sm btn-primary btn-reset']")).click()
    sleep(10)
    try:
        web_login(driver, mobile, password)
        print('重置密码，且登陆成功')
    except Exception as e:
        print(e)
        print("重置密码失败")
        assert False


def change_phone_number(driver, mobile, new_mobile, password):
    get_element(driver, ('id', 'dropdownMenu-set')).click()
    get_element(driver, ('xpath', "//a[@role='menuitem' and contains(text(),'更改手机号')]")).click()
    sleep(0.5)
    get_element(driver, ('xpath', "//input[@placeholder='请输入原手机号码']")).send_keys(mobile)
    get_elements(driver, ('xpath', "//span[contains(text(),'点击获取验证码') and @class='get-btn' ]"))[0].click()
    get_elements(driver, ('xpath', "//div[@class='col-sm-5']/input"))[0].send_keys('11111')
    get_elements(driver, ('xpath', "//button[contains(text(),'下一步')]"))[0].click()
    sleep(2)
    get_element(driver, ('xpath', "//input[@placeholder='请输入新手机号码']")).send_keys(new_mobile)
    get_elements(driver, ('xpath', "//span[contains(text(),'点击获取验证码') and @class='get-btn' ]"))[1].click()
    get_elements(driver, ('xpath', "//div[@class='col-sm-5']/input"))[1].send_keys('11111')
    get_elements(driver, ('xpath', "//button[contains(text(),'下一步')]"))[1].click()
    sleep(6)
    try:
        web_login(driver, new_mobile, password)
        print('重置密码，且登陆成功')
    except Exception as e:
        print(e)
        print("重置密码失败")
        bug_photo(driver)
        assert False




