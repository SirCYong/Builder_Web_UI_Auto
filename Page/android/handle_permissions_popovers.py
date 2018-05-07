# -*- coding: utf-8 -*-
from time import sleep

from Page.Element import is_element_present, get_element, is_element_present_3s


def handle_permissions_popovers(driver):
    if is_element_present_3s(driver, ('xpath', "//android.widget.TextView[@text='第 1 项权限（共 2 项）']")):
        get_element(driver, ('xpath', "//android.widget.Button[@text='允许']")).click()
        sleep(1)
        if is_element_present_3s(driver, ('xpath', "//android.widget.TextView[@text='第 2 项权限（共 2 项）']")):
            get_element(driver, ('xpath', "//android.widget.Button[@text='允许']")).click()
        else:
            pass
    else:
        pass


def agree_with_permissions(driver):
    # 小米处理权限的方式 全部允许
    if is_element_present_3s(driver, ('id', 'android:id/button1'), 3):
        i = 0
        while 1:
            get_element(driver, ('id', "android:id/button1")).click()
            sleep(1)
            if i == 3:
                break
            i += 1

