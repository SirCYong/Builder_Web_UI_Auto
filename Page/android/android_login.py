# -*- coding:utf-8 -*-
# auth:cy
from time import sleep

from Page.Element import get_element, is_element_present, get_elements, is_element_present_3s
from Page.android.handle_permissions_popovers import agree_with_permissions
from Page.web.get_now_time import bug_photo


def android_login(driver, username, password):
    try:
        get_element(driver, ('id', "com.zld.zld_face_rec_app:id/et_name")).send_keys(username)
        get_element(driver, ('id', "com.zld.zld_face_rec_app:id/et_pwd")).send_keys(password)
        get_element(driver, ('id', "com.zld.zld_face_rec_app:id/btn_login")).click()
        # 通过定位 点击第一个班组
        sleep(2)
        driver.tap([(0, 231), (1080, 420)], 100)
        sleep(1)
        agree_with_permissions(driver)
        sleep(1)
        assert is_element_present_3s(driver, ('id', "com.zld.zld_face_rec_app:id/fl_message")), '登陆失败'
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def android_logout(driver):
    try:
        get_element(driver, ('id', 'com.zld.zld_face_rec_app:id/ll_account')).click()
        get_element(driver, ('id', 'com.zld.zld_face_rec_app:id/btn_sign_out')).click()
        get_element(driver, ('id', 'com.zld.zld_face_rec_app:id/tv_positive_btn')).click()
        assert is_element_present_3s(driver, ('id', 'com.zld.zld_face_rec_app:id/et_name')), '登出失败'
    except Exception as e:
        print(e)


def android_employee_registration(driver, company_name, people, mobile):
    get_element(driver, ('id', 'com.zld.zld_face_rec_app:id/tv_register')).click()
    webview_employee_register(driver, company_name, people, mobile)


def webview_employee_register(driver, company_name, people, mobile, code='11111', password='123456'):
    print(driver.current_context)
    sleep(1)
    contexts = driver.contexts
    print(contexts)
    sleep(2)
    driver.switch_to.context(contexts[-1])
    print(driver.current_context)
    get_element(driver, ('xpath', "//input[@placeholder='请选择公司名称']")).click()
    get_element(driver, ('xpath', "//input[@placeholder='请输入公司名称']")).send_keys(company_name)
    get_element(driver, ('xpath', "//i[contains(text(),'搜索')]")).click()
    get_elements(driver, ('xpath', "//div[@class='radio-content']"))[0].click()
    get_element(driver, ('xpath', "//i[contains(text(),'确定')]")).click()
    get_element(driver, ('xpath', "//input[@placeholder='请输入您的真实姓名']")).send_keys(people)
    get_element(driver, ('xpath', "//input[@placeholder='请输入正确的帐号（手机号）']")).send_keys(mobile)
    get_element(driver, ('xpath', "//button[contains(text(),'点击获取')]")).click()
    get_element(driver, ('xpath', "//button[contains(text(),'确定')]")).click()
    get_element(driver, ('xpath', "//input[@placeholder='请输入校验码']")).send_keys(code)
    get_element(driver, ('xpath', "//input[@placeholder='请输入6-16位密码']")).send_keys(password)
    get_element(driver, ('xpath', "//input[@placeholder='再次输入密码以确认']")).send_keys(password)
    get_element(driver, ('xpath', "//button[contains(text(),'立即注册')]")).click()
    get_element(driver, ('xpath', "//button[contains(text(),'确定')]")).click()
    sleep(1)
    driver.switch_to.context(contexts[0])





