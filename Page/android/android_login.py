# -*- coding:utf-8 -*-
# auth:cy
from Page.Element import get_element


def android_login(driver, username, password):
    get_element(driver, ('xpath', "//android.widget.EditText[@text='请输入帐号']")).send_keys(username)
    get_element(driver, ('xpath', "//android.widget.EditText[@text='••••••••••']")).send_keys(password)
    get_element(driver, ('ACCESSIBILITY_ID', "登录 ")).click()
