# -*- coding:utf-8 -*-
# Auth cy
import random
from time import sleep

from Page.Element import get_element, get_elements, is_element_present
from Page.random_data import setting_input_time
from Page.web.get_now_time import get_now_dates, bug_photo, get_tomorrow_dates
from Page.web.into_level import into_one_level


def initiate_artifacts(driver, file_path):
    # 工件审核
    into_one_level(driver, '任务面板')
    sleep(1)
    into_one_level(driver, '发起申请')
    get_element(driver, ('xpath', "//div[contains(text(),'工件审核')]")).click()
    sleep(0.5)
    element = "//select[@class='form-control input-sm']/option[2]"
    try:
        get_element(driver, ('xpath', element)).click()
    except Exception as e:
        print(e)
        assert False, "没有此工件"
    get_element(driver, ('xpath', "//input[@placeholder='数量为整数']")).send_keys(random.randint(1, 9))
    setting_input_time(driver)
    get_element(driver, ('xpath', "//input[@placeholder='选择日期需小于或等于今天']")).send_keys(get_now_dates())
    get_elements(driver, ('xpath', "//div[@class='col-sm-6']/input[1]"))[2].send_keys('优秀')
    get_element(driver, ('xpath', "//input[@data-min-message='输入值不能小于0']")).send_keys(random.randint(1, 100))
    get_element(driver, ('xpath', "//div[@id='uploadFile']/input")).send_keys(file_path)
    get_element(driver, ('xpath', "//button[contains(text(),'提交申请')]")).click()
    sleep(0.5)
    get_element(driver, ('id', 'success')).click()
    sleep(1)
    try:
        '成功' == get_element(driver, ('xpath', "//div[@class='layui-layer-content layui-layer-padding']")).text
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def to_apply_for_leave(driver, file_path, remark):
    """

    :param driver:
    :param file_path: 附件路径
    :param remark: 备注
    :return:
    """
    into_one_level(driver, '任务面板')
    sleep(1)
    into_one_level(driver, '发起申请')
    get_element(driver, ('xpath', "//div[contains(text(),'请假申请')]")).click()
    sleep(0.5)
    element = "//select[@class='form-control input-sm']/option[%s]" % str(random.randint(1, 7))
    get_element(driver, ('xpath', element)).click()
    get_element(driver, ('id', 'leaveAdd')).click()
    get_element(driver, ('id', 'realname')).send_keys('曹永')
    get_element(driver, ('id', 'realsearch')).click()
    sleep(0.5)
    get_element(driver, ('xpath', "//*[@id='lay-user-f']/tbody/tr/td[1]/input")).click()
    get_element(driver, ('xpath', "//button[contains(text(),'添加至已选')]")).click()
    get_element(driver, ('xpath', "//a[contains(text(),'确定')]")).click()
    setting_input_time(driver)
    get_elements(driver, ('xpath', "//input[@placeholder='选择日期在合同范围内']"))[0].send_keys(get_now_dates())
    get_elements(driver, ('xpath', "//input[@placeholder='选择日期在合同范围内']"))[1].send_keys(get_tomorrow_dates())
    get_element(driver, ('xpath', "//textarea[@class='form-control']")).send_keys(remark)
    get_element(driver, ('xpath', "//div[@id='uploadFile']/input")).send_keys(file_path)
    get_element(driver, ('xpath', "//button[contains(text(),'提交申请')]")).click()
    get_element(driver, ('id', "success")).click()
    sleep(2)
    into_one_level(driver, '我的任务')
    get_element(driver, ('xpath', "//a[contains(text(),'我发起的')]")).click()
    try:
        get_element(driver, ('xpath', "//button[contains(text(),'请假工作流')]")).click()
        get_element(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr[1]/td[8]/a")).click()
        assert_element = "//div[@class='tsk-inp col-xs-8' and contains(text(),'%s')]" % remark
        assert is_element_present(driver, ('xpath', assert_element))
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def batch_add_workman(driver, file_path, remark):
    # 批量发起请假申请
    """

    :param driver:
    :param file_path: 附件路径
    :param remark: 备注信息
    :return:
    """
    into_one_level(driver, '任务面板')
    sleep(1)
    into_one_level(driver, '发起申请')
    get_element(driver, ('xpath', "//div[contains(text(),'请假申请')]")).click()
    sleep(0.5)
    element = "//select[@class='form-control input-sm']/option[%s]" % str(random.randint(1, 7))
    get_element(driver, ('xpath', element)).click()
    get_element(driver, ('id', 'leaveAdd')).click()
    sleep(0.5)
    element = "//*[@id='lay-user-f']/tbody/tr"
    for i in range(0, len(get_elements(driver, ('xpath', element))), 2):
        elements = "//tr[@data-index='%s']/td/input" % i
        get_element(driver, ('xpath', elements)).click()
        sleep(0.1)
    get_element(driver, ('xpath', "//button[contains(text(),'添加至已选')]")).click()
    get_element(driver, ('xpath', "//a[contains(text(),'确定')]")).click()
    setting_input_time(driver)
    get_elements(driver, ('xpath', "//input[@placeholder='选择日期在合同范围内']"))[0].send_keys(get_now_dates())
    get_elements(driver, ('xpath', "//input[@placeholder='选择日期在合同范围内']"))[1].send_keys(get_tomorrow_dates())
    get_element(driver, ('xpath', "//textarea[@class='form-control']")).send_keys(remark)
    get_element(driver, ('xpath', "//div[@id='uploadFile']/input")).send_keys(file_path)
    get_element(driver, ('xpath', "//button[contains(text(),'提交申请')]")).click()
    get_element(driver, ('id', "success")).click()
    sleep(0.5)
    into_one_level(driver, '我的任务')
    get_element(driver, ('xpath', "//a[contains(text(),'我发起的')]")).click()
    try:
        get_element(driver, ('xpath', "//button[contains(text(),'请假工作流')]")).click()
        get_element(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr[1]/td[8]/a")).click()
        assert_element = "//div[@class='tsk-inp col-xs-8' and contains(text(),'%s')]" % remark
        is_element_present(driver, ('xpath', assert_element))
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def request_for_overtime(driver, remark, file_path):
    """
    # 加班申请
    :param driver:
    :param remark:备注信息
    :param file_path: 附件路径
    :return:
    """
    into_one_level(driver, '任务面板')
    sleep(1)
    into_one_level(driver, '发起申请')
    get_element(driver, ('xpath', "//div[contains(text(),'加班申请')]")).click()
    get_element(driver, ('id', 'leaveAdd')).click()
    sleep(0.5)
    element = "//*[@id='lay-user-f']/tbody/tr"
    for i in range(0, len(get_elements(driver, ('xpath', element))), 2):
        elements = "//tr[@data-index='%s']/td/input" % i
        get_element(driver, ('xpath', elements)).click()
        sleep(0.1)
    get_element(driver, ('xpath', "//button[contains(text(),'添加至已选')]")).click()
    get_element(driver, ('xpath', "//a[contains(text(),'确定')]")).click()
    setting_input_time(driver)
    get_elements(driver, ('xpath', "//div[@class='col-sm-6']/input"))[0].send_keys(get_now_dates())
    get_element(driver, ('xpath', "//input[@placeholder='选择时间需小于加班结束时间']")).send_keys('20:00')
    get_element(driver, ('xpath', "//input[@placeholder='选择时间需大于加班开始时间']")).send_keys('21:00')
    overtime_type = "//select[@class='form-control input-sm']/option[%s]" % str(random.randint(1, 2))
    get_element(driver, ('xpath', overtime_type)).click()
    get_element(driver, ('xpath', "//textarea[@class='form-control']")).send_keys(remark)
    get_element(driver, ('xpath', "//div[@id='uploadFile']/input")).send_keys(file_path)
    get_element(driver, ('xpath', "//button[contains(text(),'提交申请')]")).click()
    get_element(driver, ('id', "success")).click()
    sleep(0.5)
    into_one_level(driver, '我的任务')
    get_element(driver, ('xpath', "//a[contains(text(),'我发起的')]")).click()
    try:
        get_element(driver, ('xpath', "//button[contains(text(),'加班工作流')]")).click()
        get_element(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr[1]/td[8]/a")).click()
        assert_element = "//div[@class='tsk-inp col-xs-8' and contains(text(),'%s')]" % remark
        assert is_element_present(driver, ('xpath', assert_element))
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def change_time_of_attendance(driver, remark, file_path):
    try:
        into_one_level(driver, '任务面板')
        sleep(1)
        into_one_level(driver, '发起申请')
        get_element(driver, ('xpath', "//div[contains(text(),'修改出勤时间')]")).click()
        get_element(driver, ('id', 'leaveAdd')).click()
        sleep(0.5)
        element = "//*[@id='lay-user-f']/tbody/tr"
        for i in range(0, len(get_elements(driver, ('xpath', element))), 2):
            elements = "//tr[@data-index='%s']/td/input" % i
            get_element(driver, ('xpath', elements)).click()
            sleep(0.1)
        get_element(driver, ('xpath', "//button[contains(text(),'添加至已选')]")).click()
        get_element(driver, ('xpath', "//a[contains(text(),'确定')]")).click()
        setting_input_time(driver)
        get_element(driver, ('xpath', "//input[@placeholder='选择日期不得小于当前日期']")).send_keys(get_now_dates())
        get_elements(driver, ('xpath', "//input[@placeholder='']"))[0].send_keys('08:00')
        get_elements(driver, ('xpath', "//input[@placeholder='']"))[1].send_keys('17:00')
        get_element(driver, ('xpath', "//textarea[@class='form-control']")).send_keys(remark)
        get_element(driver, ('xpath', "//div[@id='uploadFile']/input")).send_keys(file_path)
        get_element(driver, ('xpath', "//button[contains(text(),'提交申请')]")).click()
        get_element(driver, ('id', "success")).click()
        sleep(0.5)
        into_one_level(driver, '我的任务')
        get_element(driver, ('xpath', "//a[contains(text(),'我发起的')]")).click()
        get_element(driver, ('xpath', "//button[contains(text(),'修改出勤时间工作流')]")).click()
        get_element(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr[1]/td[8]/a")).click()
        assert_element = "//div[@class='tsk-inp col-xs-8' and contains(text(),'%s')]" % remark
        assert is_element_present(driver, ('xpath', assert_element))
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False
