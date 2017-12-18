# -*- coding:utf-8 -*-
# auth cy
import random
from time import sleep

import win32api

import win32gui

import win32con
from selenium.webdriver.common.action_chains import ActionChains

from Page.Element import get_element, get_elements, get_element_3s, is_element_present, is_element_present_3s
from Page.web.coordinates_postion import click_position
from Page.web.get_now_time import bug_photo
from Page.web.into_level import into_one_level, into_two_level


def setting_area(driver, area_name):
    into_one_level(driver, '工程面板')
    sleep(1)
    get_elements(driver, ('xpath', "//a[contains(text(),'设置')]"))[1].click()
    # 增加区域
    get_element(driver, ('xpath', "//div[contains(text(),'添加区域 ')]")).click()
    sleep(1)
    class_name = 'MozillaWindowClass'
    title_name = '杭州智链达建筑工人服务平台 - Mozilla FireFox'
    # 查找句柄
    hwnd = win32gui.FindWindow(class_name, title_name)
    click_position(hwnd, 146, 177)
    sleep(8)
    get_element(driver, ('xpath', "//button[contains(text(),'开始描点')]")).click()
    click_position(hwnd, 673, 453)
    sleep(0.5)
    click_position(hwnd, 1158, 468)
    sleep(0.5)
    click_position(hwnd, 701, 700)
    sleep(0.5)
    get_element(driver, ('xpath', "//button[contains(text(),'停止描点')]")).click()
    get_element(driver, ('xpath', "//textarea[@name='area-name']")).send_keys(area_name)
    get_element(driver, ('xpath', "//button[contains(text(),'保存')]")).click()
    get_element(driver, ('id', 'success')).click()
    project_area_elements = "//div[@class='select-area-util-item select-area-util-area']"
    area_names = []
    for i in range(len(get_elements(driver, ('xpath', project_area_elements)))):
        area_names.insert(i, get_elements(driver, ('xpath', project_area_elements))[i].text)
    try:
        area_name in area_names
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False
    project_element = "//div[@class='select-area-util-item select-area-util-area'and contains(text(),'%s')]" % area_name
    # 鼠标悬停在元素上面
    ActionChains(driver).move_to_element(get_element(driver, ('xpath', project_element))).perform()
    # 修改区域
    update_project_element = project_element + "/div/div[2]"
    sleep(1)
    get_element(driver, ('xpath', update_project_element)).click()
    click_position(hwnd, 146, 177)
    get_element(driver, ('xpath', "//button[contains(text(),'开始描点')]")).click()
    click_position(hwnd, 1163, 700)
    get_element(driver, ('xpath', "//button[contains(text(),'保存')]")).click()
    get_element(driver, ('id', 'success')).click()
    sleep(0.5)
    try:
        '成功' == get_element(driver, ('xpath', "//div[@class='layui-layer-content layui-layer-padding']")).text
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def delete_area(driver):
    # 删除区域
    into_one_level(driver, '工程面板')
    sleep(1)
    get_elements(driver, ('xpath', "//a[contains(text(),'设置')]"))[1].click()
    # 区域个数
    project_area_elements = "//div[@class='select-area-util-item select-area-util-area']"

    new_area_name = []
    number = int(len(get_elements(driver, ('xpath', project_area_elements))))
    for i in range(number):
        new_area_name.insert(i, get_elements(driver, ('xpath', project_area_elements))[i].text)
    project_element = "//div[@class='select-area-util-item select-area-util-area'and contains(text(),'%s')]" % \
                      new_area_name[number - 1]
    delete_project_element = project_element + "/div/div[3]"
    ActionChains(driver).move_to_element(get_element(driver, ('xpath', project_element))).perform()
    sleep(1)
    get_element(driver, ('xpath', delete_project_element)).click()
    get_element(driver, ('id', 'success')).click()
    new_number = int(len(get_elements(driver, ('xpath', project_area_elements))))
    if number == int(new_number + 1):
        print('删除区域成功')
    else:
        bug_photo(driver)
        assert False


def setting_attendance_machine(driver, attendance_machine_name):
    into_one_level(driver, '工程面板')
    sleep(1)
    get_elements(driver, ('xpath', "//a[contains(text(),'设置')]"))[1].click()
    into_two_level(driver, '考勤机设置')
    # 增加考勤机
    sleep(1)
    get_element(driver, ('xpath', "//button[contains(text(),'增加')]")).click()
    machine_type = "//*[@id='kqj-box']/form/div[1]/div/select/option[%d]" % random.randint(1, 3)
    get_element(driver, ('xpath', machine_type)).click()
    get_element(driver, ('xpath', "//div[@id='kqj-box']/form/div[4]/div/input")).send_keys('123456')
    get_element(driver, ('xpath', "//div[@id='kqj-box']/form/div[2]/div/input")).send_keys(attendance_machine_name)
    sleep(1)
    get_element(driver, ('xpath', "//*[@id='kqj-box']/form/div[3]/div/select/option[1]")).click()
    sleep(0.5)
    if is_element_present_3s(driver, ('xpath', "//button[contains(text(),'选择位置')]"), 3):
        sleep(0.5)
        get_element(driver, ('xpath', "//button[contains(text(),'选择位置')]")).click()
        class_name = 'MozillaWindowClass'
        title_name = '杭州智链达建筑工人服务平台 - Mozilla FireFox'
        # 查找句柄
        hwnd = win32gui.FindWindow(class_name, title_name)
        click_position(hwnd, 1299, 582)
        sleep(1)
        get_element(driver, ('xpath', "//a[@class='layui-layer-btn0']")).click()
    get_element(driver, ('xpath', "//button[@class='btn btn-primary']")).click()
    element_len = "//*[@id='engineering-set-table']/tbody/tr"
    number = len(get_elements(driver, ('xpath', element_len)))
    title_list = []
    if '添加成功' == get_element_3s(driver, ('id', "LAY_demo2"), 2).text:
        print('pass')
    else:
        bug_photo(driver)
        assert False
    for i in range(1, number + 1):
        name_elements = "//*[@id='engineering-set-table']/tbody/tr[%d]/td[1]/span" % i
        title_list.insert(i, get_element(driver, ('xpath', name_elements)).text)
    try:
        attendance_machine_name in title_list
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False
    # s删除考勤机
    # 删除按钮
    delete_element = "//*[@id='engineering-set-table']/tbody/tr[%d]/td[7]/a[2]" % len(
        get_elements(driver, ('xpath', element_len)))
    # 删除考勤机的名字
    delete_element_name = "//*[@id='engineering-set-table']/tbody/tr[%d]/td[1]/span" % len(
        get_elements(driver, ('xpath', element_len)))
    delete_name = get_element(driver, ('xpath', delete_element_name)).text
    get_element(driver, ('xpath', delete_element)).click()
    get_element(driver, ('id', 'success')).click()
    new_title_list = []
    sleep(1)
    for i in range(1, len(get_elements(driver, ('xpath', element_len))) + 1):
        name_elements = "//*[@id='engineering-set-table']/tbody/tr[%d]/td[1]/span" % i
        new_title_list.insert(i, get_element(driver, ('xpath', name_elements)).text)
    if delete_name in new_title_list:
        assert False
    else:
        print('删除成功')
