# -*- coding:utf-8 -*-
# Auth cy
from time import sleep

from Page.Element import get_element, get_elements, get_element_3s
from Page.web.get_now_time import bug_photo
from Page.web.into_level import into_one_level, into_two_level


def approve_workflow(driver, task_type):
    into_one_level(driver, '任务面板')
    sleep(0.5)
    into_two_level(driver, '我的任务')
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
    elif task_type == '修改出勤时间工作流':
        update_contract_element = "//button[contains(text(),'%s')]" % str(task_type)
        get_element(driver, ('xpath', update_contract_element)).click()
    elif task_type == '修改用工合同结束时间':
        update_contract_element = "//button[contains(text(),'%s')]" % str(task_type)
        get_element(driver, ('xpath', update_contract_element)).click()
    # 点击详情
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
    sleep(10)
    driver.find_element_by_xpath("//a[contains(text(),'我审核过的')]").click()
    sleep(2)
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
        contract_name = '测试工件完成审核'
        sleep(0.5)
        element_len = get_elements(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr"))
        title_text = []
        for i in range(1, len(element_len)+1):
            element = "//*[@id='task-mytask-table']/tbody/tr[%d]/td[4]" % i
            text = get_element(driver, ('xpath', element)).text
            title_text.insert(i, text)
            print(title_text)
        task_type += '签订失败'
        assert contract_name in title_text, "%s" % task_type
    elif task_type == '请假工作流':
        update_contract_element = "//button[contains(text(),'%s')]" % str(task_type)
        try:
            get_element(driver, ('xpath', update_contract_element)).click()
        except Exception as e:
            print(e)
            bug_photo(driver)
            assert False
        contract_name = '曹永请假审核', '俞俊鑫、邵雪雷、郝梦影等人请假审核'
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
            bug_photo(driver)
            assert False
    elif task_type == '加班工作流':
        update_contract_element = "//button[contains(text(),'%s')]" % str(task_type)
        get_element(driver, ('xpath', update_contract_element)).click()
        contract_name = '俞俊鑫、邵雪雷、郝梦影等人加班审核'
        element_len = get_elements(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr"))
        title_text = []
        for i in range(1, len(element_len)+1):
            element = "//*[@id='task-mytask-table']/tbody/tr[%d]/td[4]" % i
            text = get_element(driver, ('xpath', element)).text
            title_text.insert(i, text)
            print(title_text)
        task_type += '签订失败'
        assert contract_name in title_text, "%s" % task_type
    elif task_type == '修改出勤时间工作流':
        update_contract_element = "//button[contains(text(),'%s')]" % str(task_type)
        get_element(driver, ('xpath', update_contract_element)).click()
        contract_name = '俞俊鑫、邵雪雷、郝梦影等人修改出勤时间审核'
        element_len = get_elements(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr"))
        title_text = []
        for i in range(1, len(element_len)+1):
            element = "//*[@id='task-mytask-table']/tbody/tr[%d]/td[4]" % i
            text = get_element(driver, ('xpath', element)).text
            title_text.insert(i, text)
            print(title_text)
        task_type += '签订失败'
        assert contract_name in title_text, "%s" % task_type
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


