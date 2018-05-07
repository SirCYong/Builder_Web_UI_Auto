# -*- coding:utf-8 -*-
# Auth cy
from time import sleep

from Page.Element import get_element, get_elements, get_element_3s
from Page.web.get_now_time import bug_photo
from Page.web.into_level import into_one_level, into_two_level


def approve_workflow(driver, task_type, many_people=1):
    into_one_level(driver, '任务面板')
    sleep(0.5)
    into_two_level(driver, '我的任务')
    sleep(1)
    if task_type == '修改总包合同结束时间':
        update_contract_element = "//button[contains(text(),'%s')]" % str(task_type)
        get_element(driver, ('xpath', update_contract_element)).click()
    elif task_type == '工件完成工作流':
        update_contract_element = "//button[contains(text(),'%s')]" % str(task_type)
        get_element(driver, ('xpath', update_contract_element)).click()
    elif task_type == '请假工作流':
        update_contract_element = "//button[contains(text(),'%s')]" % str(task_type)
        get_element(driver, ('xpath', update_contract_element)).click()
    elif task_type == '加班工作流':
        update_contract_element = "//button[contains(text(),'%s')]" % str(task_type)
        get_element(driver, ('xpath', update_contract_element)).click()
    elif task_type == '修正工人考勤异常':
        update_contract_element = "//button[contains(text(),'%s')]" % str(task_type)
        get_element(driver, ('xpath', update_contract_element)).click()
    elif task_type == '修改用工合同结束时间':
        update_contract_element = "//button[contains(text(),'%s')]" % str(task_type)
        get_element(driver, ('xpath', update_contract_element)).click()
    # 点击详情
    if many_people == 1:
        try:
            get_element(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr[1]/td[9]/a")).click()
            sleep(1)
            # 点击通过
            get_element(driver, ('xpath', "//button[@class='btn btn-sm btn-success']")).click()
            # 输入备注
            get_element(driver, ('xpath', "//textarea")).send_keys('s')
            # 点击确定
            get_element(driver, ('xpath', "//a[@class='layui-layer-btn0']")).click()
        except Exception as e:
            print(e)
            bug_photo(driver)
            assert False
    elif many_people == 2:
        get_element(driver, ('xpath', "//i[@class='glyphicon']")).click()
        sleep(1)
        get_element(driver, ('xpath', "//button[contains(text(),'通过')]")).click()
        get_element(driver, ('xpath', "//textarea[@placeholder='必填']")).send_keys('ss')
        get_element(driver, ('xpath', "//a[contains(text(),'确定')]")).click()
    sleep(4)
    get_element(driver, ('xpath', "//a[contains(text(),'我审核过的')]")).click()
    sleep(3)
    if task_type == '修改总包合同结束时间':
        contract_name = '关于浙江如舞亚更工程的总包合同结束时间修改审核'
        element_len = get_elements(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr"))
        title_text = []
        for i in range(1, len(element_len)+1):
            element = "//*[@id='task-mytask-table']/tbody/tr[%d]/td[4]" % i
            text = get_element(driver, ('xpath', element)).text
            title_text.insert(i, text)
            print(title_text)
        task_type += '签订失败'
        assert contract_name in title_text, "%s" % task_type
    elif task_type == '工件完成工作流':
        update_contract_element = "//button[contains(text(),'%s')]" % str(task_type)
        get_element(driver, ('xpath', update_contract_element)).click()
        contract_name = '测试工件完成审核', '123完成审核'
        sleep(0.5)
        element_len = get_elements(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr"))
        title_text = []
        for i in range(1, len(element_len)+1):
            element = "//*[@id='task-mytask-table']/tbody/tr[%d]/td[4]" % i
            text = get_element(driver, ('xpath', element)).text
            title_text.insert(i, text)
            print(title_text)
        task_type += '签订失败'
        if contract_name[0] in title_text:
            pass
        elif contract_name[1] in title_text:
            pass
        else:
            print(task_type)
            assert False
    # 请假工作流
    elif task_type == '请假工作流':
        update_contract_element = "//button[contains(text(),'%s')]" % str(task_type)
        get_element(driver, ('xpath', update_contract_element)).click()
        try:
            if many_people == 2:
                time_of_duration = '0 天 0 时 1 分', '0 天 0 时 0 分', '0 天 0 时 2 分'
                for i in range(1, 4):
                    element = "//*[@id='task-mytask-table']/tbody/tr[%s]/td[7]" % 1
                    time_text = get_element(driver, ('xpath', element)).text
                    sleep(0.5)
                    print(time_text, '', time_of_duration)
                    assert time_text in time_of_duration
            elif many_people == 1:
                get_elements(driver, ('xpath', "//a[@class='table-a-link']"))[0].click()
                sleep(1)
                text = get_elements(driver, ('xpath', "//div[@class='tsk-inp col-xs-8']"))[3].text
                contract_name = '曹永,', '李嘉鑫,', '吕心泳,'
                assert text in contract_name, '我审核的没有数据' + text
        except Exception as e:
            print(e)
            bug_photo(driver)
            assert False
    #  加班工作流
    elif task_type == '加班工作流':
        update_contract_element = "//button[contains(text(),'%s')]" % str(task_type)
        get_element(driver, ('xpath', update_contract_element)).click()
        time_of_duration = '0 天 0 时 1 分', '0 天 0 时 0 分', '0 天 0 时 2 分'
        element = "//*[@id='task-mytask-table']/tbody/tr[%s]/td[7]" % 1
        time_text = get_element(driver, ('xpath', element)).text
        sleep(0.5)
        print(time_text, 'in', time_of_duration)
        assert time_text in time_of_duration, time_text + 'not_in' + time_of_duration
    # 修正工人考勤异常
    elif task_type == '修正工人考勤异常':
        update_contract_element = "//button[contains(text(),'%s')]" % str(task_type)
        get_element(driver, ('xpath', update_contract_element)).click()
        if many_people == 1:
            get_elements(driver, ('xpath', "//a[@class='table-a-link']"))[0].click()
            sleep(1)
            text = get_elements(driver, ('xpath', "//div[@class='tsk-inp col-xs-8']"))[3].text
            contract_name = '曹永', '李嘉鑫', '吕心泳'
            assert text in contract_name, '我审核的没有数据' + text
        elif many_people == 2:
            time_of_duration = '0 天 0 时 1 分', '0 天 0 时 0 分', '0 天 0 时 2 分'
            for i in range(1, 4):
                element = "//*[@id='task-mytask-table']/tbody/tr[%s]/td[7]" % i
                time_text = get_element(driver, ('xpath', element)).text
                sleep(0.5)
                assert time_text in time_of_duration
    # 修改用工合同结束时间
    elif task_type == '修改用工合同结束时间':
        update_contract_element = "//button[contains(text(),'%s')]" % str(task_type)
        get_element(driver, ('xpath', update_contract_element)).click()
        contract_name = '曹永用工合同结束时间审核'
        element_len = get_elements(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr"))
        title_text = []
        for i in range(1, len(element_len) + 1):
            element = "//*[@id='task-mytask-table']/tbody/tr[%d]/td[4]" % i
            text = get_element_3s(driver, ('xpath', element), 20).text
            title_text.insert(i, text)
            print(title_text)
        task_type += '签订失败'
        try:
            assert contract_name in title_text
        except Exception as e:
            print(task_type)
            print(e)
            bug_photo(driver)
            assert False


