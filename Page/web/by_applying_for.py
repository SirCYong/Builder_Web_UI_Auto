# -*- coding:utf-8 -*-
# Auth cy
import random
from configparser import ConfigParser
from time import sleep

from selenium.webdriver.common.keys import Keys

from Page.Element import get_element, get_elements, is_element_present, is_element_present_3s
from Page.api.builder_api import login
from Page.random_data import setting_input_time
from Page.web.get_now_time import get_now_dates, bug_photo, get_tomorrow_dates, get_pass_dates
from Page.web.into_level import into_one_level
from Page.web.web_login import web_login
from run_path import setting_path


def initiate_artifacts(driver, file_path):
    # 工件审核
    into_one_level(driver, '任务面板')
    sleep(1)
    into_one_level(driver, '发起申请')
    get_element(driver, ('xpath', "//div[contains(text(),'工件审核')]")).click()
    sleep(0.5)
    get_elements(driver, ('xpath', "//i[@class='glyphicon glyphicon-plus']"))[0].click()
    input_element = "//*[@id='lay-user-f']/tbody/tr[1]/td[1]/input"
    get_element(driver, ('xpath', input_element)).click()
    get_element(driver, ('xpath', "//a[contains(text(),'确定')]")).click()
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
    get_element(driver, ('id', 'realname')).send_keys('李嘉鑫')
    get_element(driver, ('id', 'realsearch')).click()
    sleep(0.5)
    get_element(driver, ('xpath', "//*[@id='lay-user-f']/tbody/tr/td[1]/input")).click()
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
        sleep(3)
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
    # 请假类型
    element = "//select[@class='form-control input-sm']/option[%s]" % str(random.randint(1, 7))
    get_element(driver, ('xpath', element)).click()
    get_element(driver, ('id', 'leaveAdd')).click()
    sleep(0.5)
    for i in range(0, 3):
        elements = "//tr[@data-index='%s']/td/input" % i
        get_element(driver, ('xpath', elements)).click()
        sleep(0.1)
    get_element(driver, ('xpath', "//a[contains(text(),'确定')]")).click()
    setting_input_time(driver)
    get_elements(driver, ('xpath', "//input[@placeholder='选择日期在合同范围内']"))[0].send_keys(get_now_dates())
    get_elements(driver, ('xpath', "//input[@placeholder='选择日期在合同范围内']"))[1].send_keys(get_tomorrow_dates())
    get_element(driver, ('xpath', "//textarea[@class='form-control']")).send_keys(remark)
    get_element(driver, ('xpath', "//div[@id='uploadFile']/input")).send_keys(file_path)
    get_element(driver, ('xpath', "//button[contains(text(),'提交申请')]")).click()
    get_element(driver, ('id', "success")).click()
    sleep(1.5)
    into_one_level(driver, '我的任务')
    get_element(driver, ('xpath', "//a[contains(text(),'我发起的')]")).click()
    try:
        get_element(driver, ('xpath', "//button[contains(text(),'请假工作流')]")).click()
        sleep(3)
        get_element(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr[1]/td[8]/a")).click()
        assert_element = "//div[@class='tsk-inp col-xs-8' and contains(text(),'%s')]" % remark
        is_element_present(driver, ('xpath', assert_element))
    except Exception as e:
        print(e)
        print('工人已经存在请假工作流，无法继续发起')
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
    get_element(driver, ('xpath', "//a[contains(text(),'确定')]")).click()
    setting_input_time(driver)
    get_elements(driver, ('xpath', "//div[@class='col-sm-6']/input"))[0].send_keys(get_now_dates())
    get_element(driver, ('xpath', "//input[@placeholder='选择时间需小于加班结束时间']")).send_keys('20:00')
    get_element(driver, ('xpath', "//input[@placeholder='选择时间需大于加班开始时间']")).send_keys('21:00')
    get_element(driver, ('xpath', "//input[@placeholder='请输入加班费， 单位：元/小时']")).send_keys(random.randint(20, 50))
    get_element(driver, ('xpath', "//textarea[@class='form-control']")).send_keys(remark)
    get_element(driver, ('xpath', "//div[@id='uploadFile']/input")).send_keys(file_path)
    get_element(driver, ('xpath', "//button[contains(text(),'提交申请')]")).click()
    get_element(driver, ('id', "success")).click()
    sleep(0.5)
    i = 1
    while 1:
        if is_element_present_3s(driver, ('xpath', "//div[contains(text(),'创建失败')]")):
            sleep(1)
            get_element(driver, ('xpath', "//a[@class='layui-layer-ico layui-layer-close layui-layer-close1']")).click()
            sleep(0.2)
            get_elements(driver, ('xpath', "//div[@class='col-sm-6']/input"))[0].clear()
            get_elements(driver, ('xpath', "//div[@class='col-sm-6']/input"))[0].send_keys(get_pass_dates(i))
            i += 1
            get_element(driver, ('xpath', "//button[contains(text(),'提交申请')]")).click()
            get_element(driver, ('id', "success")).click()
            sleep(0.5)
            if is_element_present_3s(driver, ('id', "LAY_demo2")):
                break
        else:
            break
    into_one_level(driver, '我的任务')
    get_element(driver, ('xpath', "//a[contains(text(),'我发起的')]")).click()
    try:
        sleep(0.5)
        get_element(driver, ('xpath', "//button[contains(text(),'加班工作流')]")).click()
        get_element(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr[1]/td[8]/a")).click()
        assert_element = "//div[@class='tsk-inp col-xs-8' and contains(text(),'%s')]" % remark
        assert is_element_present(driver, ('xpath', assert_element))
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def change_time_of_attendance(driver, remark, file_path, people_number):
    """
    1 代表单人， 2代表多人
    """
    try:
        into_one_level(driver, '任务面板')
        sleep(1)
        into_one_level(driver, '发起申请')
        get_element(driver, ('xpath', "//div[contains(text(),'考勤异常修改')]")).click()
        get_elements(driver, ('xpath', "//i[@class='glyphicon glyphicon-plus']"))[0].click()
        sleep(0.5)
        if people_number == 1:
            get_element(driver, ('id', "realname")).send_keys('曹永')
            get_element(driver, ('id', "realsearch")).click()
            get_elements(driver, ('xpath', "//input[@name='btSelectItem']"))[0].click()
            get_element(driver, ('xpath', "//a[contains(text(),'确定')]")).click()
            sleep(0.5)

            get_element(driver, ('xpath', "//div[@id='uploadFile']/input")).send_keys(file_path)
        element = "//input[@name='btSelectItem']"
        if people_number == 2:
            for i in range(0, len(get_elements(driver, ('xpath', element))), 2):
                elements = "//input[@name='btSelectItem']"
                get_elements(driver, ('xpath', elements))[i].click()
                sleep(0.1)
            get_element(driver, ('xpath', "//a[contains(text(),'确定')]")).click()
        setting_input_time(driver)
        get_element(driver, ('xpath', "//textarea[@class='form-control']")).send_keys(remark)
        get_elements(driver, ('xpath', "//input[@class='form-control input-sm form-date']"))[0].send_keys(get_pass_dates(1))
        get_elements(driver, ('xpath', "//input[@class='form-control input-sm form-date-time2']"))[0].send_keys('08:00')
        get_elements(driver, ('xpath', "//input[@class='form-control input-sm form-date-time2']"))[1].send_keys('17:00')
        get_element(driver, ('xpath', "//button[contains(text(),'提交申请')]")).click()
        get_element(driver, ('id', "success")).click()
        sleep(0.5)
        # 工人个数
        worker_number = 5
        # 修改1天前的考勤异常
        day_num = 1

        while True:
            if is_element_present_3s(driver, ('xpath', "//div[contains(text(),'当前人员暂无考勤记录')]"), 2):
                print('考勤未生成昨天的数据，请查看定时任务是否开启')
                workers = random.sample(range(1, 15), worker_number)
                # 选择工人按钮
                get_element(driver, ('xpath', "//button[@id='attendanceUpdateData']")).click()
                # 清空选择
                get_element(driver, ('xpath', "//button[contains(text(),'清空选择')]")).click()
                if is_element_present_3s(driver, ('xpath', "//a[contains(text(),'›')]"), 1):
                    # 滑动到最下面
                    get_elements(driver, ('xpath', "//a[contains(text(),'›')]"))[0].send_keys(Keys.DOWN)
                    sleep(0.5)
                    get_elements(driver, ('xpath', "//a[contains(text(),'›')]"))[0].click()
                for i in range(worker_number):
                    get_elements(driver, ('xpath', element))[workers[i]].click()
                get_element(driver, ('xpath', "//a[contains(text(),'确定')]")).click()
                get_elements(driver, ('xpath', "//input[@class='form-control input-sm form-date']"))[0].clear()
                get_elements(driver, ('xpath', "//input[@class='form-control input-sm form-date']"))[0].send_keys(
                    get_pass_dates(day_num))
                day_num += 1
                get_element(driver, ('xpath', "//button[contains(text(),'提交申请')]")).click()
                get_element(driver, ('id', "success")).click()
                sleep(0.5)
            else:
                break
        into_one_level(driver, '我的任务')
        get_element(driver, ('xpath', "//a[contains(text(),'我发起的')]")).click()
        sleep(1)
        get_element(driver, ('xpath', "//button[contains(text(),'修正工人考勤异常')]")).click()
        get_element(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr[1]/td[8]/a")).click()
        assert_element = "//div[@class='tsk-inp col-xs-8' and contains(text(),'%s')]" % remark
        assert is_element_present(driver, ('xpath', assert_element))
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def operation_the_all_workflow(driver):
    # 全部通过工作流
    prompt = None
    into_one_level(driver, '任务面板')
    sleep(1)
    into_one_level(driver, '我的任务')
    while True:
        if is_element_present_3s(driver, ('xpath', "//button[contains(text(),'请假工作流')]")):
            get_element(driver, ('xpath', "//button[contains(text(),'请假工作流')]")).click()
        elif is_element_present_3s(driver, ('xpath', "//button[contains(text(),'工件完成工作流')]"), 1):
            get_element(driver, ('xpath', "//button[contains(text(),'工件完成工作流')]")).click()
        elif is_element_present_3s(driver, ('xpath', "//button[contains(text(),'加班工作流')]"), 1):
            get_element(driver, ('xpath', "//button[contains(text(),'加班工作流')]")).click()
        elif is_element_present_3s(driver, ('xpath', "//button[contains(text(),'修正工人考勤异常')]"), 1):
            get_element(driver, ('xpath', "//button[contains(text(),'修正工人考勤异常')]")).click()
        else:
            prompt = '暂无工作流'
        print(prompt)
        if prompt == '暂无工作流':
            break
        else:
            get_element(driver, ('xpath', "//button[contains(text(),'全选')]/i")).click()
            get_element(driver, ('xpath', "//button[contains(text(),'通过')]")).click()
            get_element(driver, ('xpath', "//textarea[@placeholder='必填']")).send_keys('all')
            get_element(driver, ('xpath', "//a[contains(text(),'确定')]")).click()
            driver.refresh()
            sleep(1.5)
            get_element(driver, ('xpath', "//button[contains(text(),'所有')]")).click()
            if is_element_present_3s(driver, ('xpath', "//a[contains(text(),'详情')]")):
                pass
            else:
                break


def employee_operation_the_all_workflow(driver, ws_driver, position):
    """

    :param ws_driver:
    :param driver:
    :param position: 1 项目经理 2 劳务经理
    :return:
    """
    conf = ConfigParser()
    path = setting_path()
    conf.read(path)
    pwd = 123456
    if position == 1:
        username = conf.get('projectManager', 'taohui')
        web_login(driver, username, pwd)
        login(ws_driver, username, pwd)
    elif position == 2:
        username = conf.get('labor', 'Wuhuigang')
        web_login(driver, username, pwd)
        login(ws_driver, username, pwd)
    else:
        print('请输入整数（1 ：项目经理 2： 劳务经理）')
    operation_the_all_workflow(driver)



