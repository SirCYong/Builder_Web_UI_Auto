# -*- coding: utf-8 -*-
# auth : CY
from Page.Element import get_element
from Page.web.get_now_time import bug_photo


def workers_registration(driver, mobile, password):
    try:
        get_element(driver, ('accessibility_id', '新用户注册 ')).click()
        get_element(driver, ('accessibility_id', '我是工人')).click()
        get_element(driver, ('xpath', "//android.widget.EditText[@text='请输入正确的帐号（手机号）']")).send_keys(mobile)
        get_element(driver, ('xpath', "//android.widget.Button[@content-desc='点击获取 ']")).click()
        get_element(driver, ('xpath', "//android.widget.EditText[@text='请输入校验码']")).send_keys('11111')
        get_element(driver, ('xpath', "//android.widget.EditText[@text='••••••••••']")).send_keys(password)
        get_element(driver, ('xpath', "//android.widget.EditText[@text='•••••••••']")).send_keys(password)
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False




