# -*- coding:utf-8 -*-
# auth:cy
from time import sleep

from Page.Element import get_element, get_elements, is_element_present
from Page.random_data import setting_input_time
from Page.web.get_now_time import bug_photo, get_future_date
from Page.web.into_level import into_one_level, into_two_level


def update_PM(driver):
    into_one_level(driver, '工程面板')
    sleep(1)
    get_elements(driver, ('xpath', "//a[contains(text(),'设置')]"))[1].click()
    sleep(1)
    get_element(driver, ('xpath', "//button[contains(text(),'修改项目经理')]")).click()
    get_element(driver, ('xpath', "//select[@class='form-control input-sm']/option[2]")).click()
    get_element(driver, ('xpath', "//button[@class='btn btn-primary btn-sm']")).click()
    get_element(driver, ('id', 'success')).click()
    try:
        '更新成功' == get_element(driver, ('id', 'LAY_demo2')).text
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def project_delay(driver):
    try:
        into_one_level(driver, '工程面板')
        sleep(1)
        get_elements(driver, ('xpath', "//a[contains(text(),'设置')]"))[1].click()
        into_two_level(driver, '项目设置')
        sleep(0.5)
        get_element(driver, ('xpath', "//button[contains(text(),'项目延期')]")).click()
        sleep(1)
        num = 300
        setting_input_time(driver)
        get_element(driver, ('xpath', "//input[@placeholder='选择日期需大于原总包合同结束时间']")).send_keys(get_future_date(num))
        get_element(driver, ('xpath', "//button[contains(text(),'提交申请')]")).click()
        sleep(0.5)
        get_element(driver, ('id', 'success')).click()
        while 1:
            if is_element_present(driver, ('xpath', "//div[contains(text(),'延期时间必须大于总包合同的竣工日期')]")):
                sleep(0.1)
                get_element(driver, ('xpath', "//span[@class='layui-layer-setwin']/a")).click()
                get_element(driver, ('xpath', "//input[@placeholder='选择日期需大于原总包合同结束时间']")).clear()
                num += 20
                get_element(driver, ('xpath', "//input[@placeholder='选择日期需大于原总包合同结束时间']")).send_keys(get_future_date(num))
                get_element(driver, ('xpath', "//button[contains(text(),'提交申请')]")).click()
                sleep(0.5)
                get_element(driver, ('id', 'success')).click()
            else:
                break
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False



