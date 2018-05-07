# -*- coding: utf-8 -*-
# auth cy
import random
import re
from time import sleep
from selenium.webdriver.common.keys import Keys
from Page.Element import get_element, get_elements, is_element_present, is_element_present_3s
from Page.random_data import setting_input_time
from Page.web.get_now_time import bug_photo, get_now_dates, get_future_date, get_pass_dates
from Page.web.into_level import into_one_level, into_two_level


def workman_contract(driver, people, out_of_date):
    try:
        into_one_level(driver, "任务面板")
        sleep(1)
        into_two_level(driver, "发起申请")
        get_element(driver, ('xpath', "//div[contains(text(),'新建用工合同')]")).click()
        get_element(driver, ('xpath', "//span[contains(text(),'计时工人用工合同')]")).click()
        project_element = "//select[@id='reproject-name']/option[2]"
        get_element(driver, ('xpath', project_element)).click()
        get_element(driver, ('xpath', "//*[@id='reproject-team']/option[2]")).click()
        get_element(driver, ('xpath', "//input[@placeholder='请输入正常出勤单价']")).send_keys(random.randint(10, 99))
        # get_element(driver, ('xpath', "//input[@placeholder='请输入加班单价']")).send_keys(random.randint(10, 99))
        # 选择工种
        work_type = "//*[@id='work-type']/option"
        work_type_element = "//*[@id='work-type']/option[%d]" % random.randint(2, len(work_type))
        get_element(driver, ('xpath', work_type_element)).click()
        get_element(driver, ('xpath', "//input[@placeholder='请输入姓名或身份证号查询']")).send_keys(people)
        sleep(0.5)
        workman_element = "//span[contains(text(),'%s')]" % people
        get_element(driver, ('xpath', "//input[@placeholder='请输入姓名或身份证号查询']")).send_keys(Keys.ENTER)
        sleep(1)
        get_elements(driver, ('xpath', workman_element))[0].click()
        information = "按工作时间长短付给你工资的工作。"
        get_element(driver, ('xpath', "//textarea[@placeholder='选填']")).send_keys(information)
        setting_input_time(driver)
        get_elements(driver, ('xpath', "//input[@placeholder='必填']"))[0].send_keys('08:00')
        get_elements(driver, ('xpath', "//input[@placeholder='必填']"))[1].send_keys('18:00')
        if out_of_date:
            get_element(driver, ('xpath', "//input[@placeholder='小于用工合同结束日期']")).send_keys(get_pass_dates(2))
        else:
            get_element(driver, ('xpath', "//input[@placeholder='小于用工合同结束日期']")).send_keys(get_now_dates())
        get_element(driver, ('xpath', "//input[@placeholder='选择日期不得大于分包合同结束日期']")).send_keys(get_future_date(180))
        get_elements(driver, ('xpath', "//input[@placeholder='必填']"))[2].send_keys('10')
        get_element(driver, ('xpath', "//button[contains(text(),'完成')]")).click()
        assert is_element_present(driver, (
            'xpath', "//div[contains(text(),'成功')]/i[@class='layui-layer-ico layui-layer-ico1' ]"))
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def workers_review(driver, worker_name):
    try:
        into_one_level(driver, "任务面板")
        sleep(0.5)
        into_two_level(driver, "我的任务")
        get_element(driver, ('xpath', "//button[contains(text(),'签订用工合同')]")).click()
        get_element(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr[1]/td[9]/a")).click()
        get_element(driver, ('xpath', "//button[@class='btn btn-sm btn-success']")).click()
        get_element(driver, ('xpath', "//textarea")).send_keys('s')
        get_element(driver, ('xpath', "//a[@class='layui-layer-btn0']")).click()
        sleep(10)
        driver.find_element_by_xpath("//a[contains(text(),'我审核过的')]").click()
        sleep(2)
        worker_name += '用工合同签订审核'
        element_len = get_elements(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr"))
        title_text = []
        for i in range(1, len(element_len)):
            element = "//*[@id='task-mytask-table']/tbody/tr[%d]/td[4]" % i
            text = get_element(driver, ('xpath', element)).text
            title_text.insert(i, text)
            print(title_text)
        information = '用工合同签订失败'
        assert worker_name in title_text, "%s" % information
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def workman_contract_piece(driver, artifact_name, people):
    try:
        into_one_level(driver, "任务面板")
        sleep(1)
        into_two_level(driver, "发起申请")
        get_element(driver, ('xpath', "//div[contains(text(),'新建用工合同')]")).click()
        get_element(driver, ('xpath', "//span[contains(text(),'计件工人用工合同')]")).click()
        project_element = "//select[@id='reproject-name']/option[2]"
        get_element(driver, ('xpath', project_element)).click()
        get_element(driver, ('xpath', "//*[@id='reproject-team']/option[2]")).click()
        get_elements(driver, ('xpath', "//input[@placeholder='必填']"))[0].send_keys(artifact_name)
        address = ['上海', '北京', '广州', '杭州', '无锡', '苏州', '徐州']
        get_elements(driver, ('xpath', "//input[@placeholder='必填']"))[1].send_keys(
            address[random.randint(0, len(address)-1)])
        get_elements(driver, ('xpath', "//input[@placeholder='必填']"))[2].send_keys(random.randint(88, 188))
        get_elements(driver, ('xpath', "//input[@placeholder='必填']"))[3].send_keys(random.randint(199, 399))
        get_element(driver, ('xpath', "//textarea[@placeholder='选填']")).send_keys('优秀的完成')
        # 选择工种
        work_type = "//*[@id='work-type']/option"
        work_type_element = "//*[@id='work-type']/option[%d]" % random.randint(2, len(work_type))
        get_element(driver, ('xpath', work_type_element)).click()
        setting_input_time(driver)
        get_element(driver, ('id', 'select2-piece-worker-Name-container')).click()
        get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(people)
        sleep(0.5)
        get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(Keys.ENTER)
        get_elements(driver, ('xpath', "//input[@placeholder='必填']"))[4].send_keys('08:30')
        get_elements(driver, ('xpath', "//input[@placeholder='必填']"))[5].send_keys('17:30')
        get_element(driver, ('xpath', "//input[@placeholder='小于用工合同结束日期' ]")).send_keys(get_pass_dates(2))
        get_element(driver, ('xpath', "//input[@placeholder='选择日期不得大于分包合同结束日期']")).send_keys(get_future_date(180))
        get_elements(driver, ('xpath', "//input[@placeholder='必填']"))[6].send_keys(random.randint(1, 30))
        get_element(driver, ('xpath', "//button[contains(text(),'完成')]")).click()
        assert is_element_present(driver, (
            'xpath', "//div[contains(text(),'成功')]/i[@class='layui-layer-ico layui-layer-ico1' ]"))
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def change_workman_contract_date(driver):
    try:
        now_date = get_future_date(90)
        into_one_level(driver, "任务面板")
        sleep(1)
        into_two_level(driver, "发起申请")
        get_element(driver, ('xpath', "//div[contains(text(),'用工合同期限修改')]")).click()
        get_elements(driver, ('xpath', "//input[@class='form-control input-sm']"))[0].click()
        get_element(driver, ('id', 'realname')).send_keys('曹永')
        get_element(driver, ('id', 'realsearch')).click()
        sleep(0.5)
        get_element(driver, ('xpath', "//*[@id='lay-user-f']/tbody/tr/td[1]/input")).click()
        get_element(driver, ('xpath', "//a[contains(text(),'确定')]")).click()
        sleep(0.5)
        setting_input_time(driver)
        get_element(driver, ('xpath', "//input[@placeholder='请选择日期']")).send_keys(now_date)
        get_element(driver, ('xpath', "//button[contains(text(),'提交申请')]")).click()
        get_element(driver, ('id', "success")).click()
        assert is_element_present(driver, (
            'xpath', "//div[contains(text(),'成功')]/i[@class='layui-layer-ico layui-layer-ico1' ]"))
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def edit_workers_contract(driver, workers_name, photo_path):
    try:
        into_one_level(driver, '工程面板')
        sleep(0.5)
        into_two_level(driver, '工人管理')
        # 查询工人姓名
        get_element(driver, ('xpath', "//div[@id='table-toolbar']/input")).send_keys(workers_name)
        # 搜索
        get_element(driver, ('xpath', "//div[@id='table-toolbar']/button")).click()
        get_element(driver, ('xpath', "//a[contains(text(),'合同详情') and @class='table-a-link']")).click()
        sleep(0.5)
        a = get_element(driver, ('xpath', "//*[@id='laborContract']/p[3]")).text
        get_element(driver, ('xpath', "//button[contains(text(),'内容编辑')]")).click()
        if is_element_present_3s(driver, ('xpath', "//input[@placeholder='请输入正常出勤单价']"), 3):
            pass
        else:
            driver.refresh()
            if is_element_present(driver, ('xpath', "//button[contains(text(),'内容编辑')]")):
                sleep(1)
                get_element(driver, ('xpath', "//button[contains(text(),'内容编辑')]")).click()
            else:
                pass
        sleep(0.5)
        get_element(driver, ('xpath', "//input[@placeholder='请输入正常出勤单价']")).clear()
        sleep(0.5)
        new_unit_price = random.randint(1, 200)
        get_element(driver, ('xpath', "//input[@placeholder='请输入正常出勤单价']")).send_keys(new_unit_price)
        sleep(0.1)
        get_element(driver, ('xpath', "//textarea[@placeholder='选填']")).clear()
        assert_information = '验证数据'
        get_element(driver, ('xpath', "//textarea[@placeholder='选填']")).send_keys(assert_information)
        setting_input_time(driver)
        get_element(driver, ('xpath', "//input[@placeholder='选择日期不得大于分包合同结束日期']")).clear()
        get_element(driver, ('xpath', "//input[@placeholder='选择日期不得大于分包合同结束日期']")).send_keys(get_future_date(150))
        get_element(driver, ('xpath', "//div[@id='uploadFile2']/input[1]")).send_keys(photo_path)
        sleep(3)
        get_element(driver, ('xpath', "//button[contains(text(),'完成')]")).click()
        assert is_element_present(driver, ('id', 'LAY_demo2'))
        sleep(7)
        until_price = "//span[contains(text(),'单价:%s元/小时')]" % new_unit_price
        print(until_price)
        assert is_element_present(driver, ('xpath', until_price)), "工人单价未更新"
        workers_information = "//span[contains(text(),'内容:%s')]" % assert_information
        assert is_element_present(driver, ('xpath', workers_information)), "工作内容未更新"
        reg = r"(从)(.+)(进)"
        data = re.findall(reg, a)
        workers_contract_time = "//div[@id='laborContract']/p[contains(text(),'1.用工日期从%s进场始至%s日止')]" % (data[0][1], str(get_future_date(150)))
        assert is_element_present(driver, ('xpath', workers_contract_time)), "工人合同时间未更新"
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def termination_of_the_contract(driver, workers_name):
    try:
        into_one_level(driver, '工程面板')
        sleep(0.5)
        into_two_level(driver, '工人管理')
        # 查询工人姓名
        get_element(driver, ('xpath', "//div[@id='table-toolbar']/input")).send_keys(workers_name)
        # 搜索
        get_element(driver, ('xpath', "//div[@id='table-toolbar']/button")).click()
        get_element(driver, ('xpath', "//a[contains(text(),'查看详情') and @class='table-a-link']")).click()
        get_elements(driver, ('xpath', "//a[contains(text(),'查看详情') and @class='table-a-link']"))[1].click()
        sleep(1.5)
        get_element(driver, ('xpath', "//button[contains(text(),'合同终止')]")).click()
        get_element(driver, ('id', 'success')).click()
        assert get_element(driver, ('xpath', "//div[@id='LAY_demo2']")).text == '成功'
        sleep(3)
        get_element(driver, ('xpath', "//div[@id='table-toolbar']/input")).send_keys(workers_name)
        get_element(driver, ('xpath', "//div[@id='table-toolbar']/button")).click()
        sleep(1)
        if is_element_present_3s(driver, ('xpath', "//a[contains(text(),'查看详情') and @class='table-a-link']"), 2):
            assert False, '终止合同后，还可以搜到工人'
        else:
            pass
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def verify_worker_exists(driver, workers_name):
    #  平台运维验证工人是否存在
    try:
        into_one_level(driver, '运维面板')
        sleep(0.5)
        into_two_level(driver, '注册用户管理')
        # 查询工人姓名
        get_element(driver, ('xpath', "//input[@placeholder='工人姓名']")).send_keys(workers_name)
        # 搜索
        get_element(driver, ('xpath', "//button[contains(text(),'搜索')]")).click()
        if is_element_present_3s(driver, ('xpath', "//tbody/tr/td[2]/a"), 3):
            get_element(driver, ('xpath', "//tbody/tr/td[2]/a")).click()
            sleep(1)
            role = get_element(driver, ('xpath', "//*[@id='basic']/div/div[2]/div[4]/div/span")).text
            print(role)
            assert role == '签约工人'
        else:
            print('签订终止合同工人的合同失败')
            assert False
        sleep(1.5)
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def evaluation_of_worker(driver, workers_name, status='立即添加评价'):
    try:
        into_one_level(driver, '工程面板')
        sleep(0.5)
        into_two_level(driver, '工人管理')
        # 查询工人姓名
        get_element(driver, ('xpath', "//div[@id='table-toolbar']/input")).send_keys(workers_name)
        # 搜索
        get_element(driver, ('xpath', "//div[@id='table-toolbar']/button")).click()
        get_element(driver, ('xpath', "//a[contains(text(),'查看详情') and @class='table-a-link']")).click()
        get_elements(driver, ('xpath', "//a[contains(text(),'查看详情') and @class='table-a-link']"))[1].click()
        sleep(1.5)
        if status == '立即添加评价':
            get_element(driver, ('xpath', "//button[contains(text(),'评价')]")).click()
        elif status == '修改评价':
            get_element(driver, ('xpath', "//button[contains(text(),'修改评价')]")).click()
        else:
            print('使用方法不正确')
        leavel = ('很差', '差', '一般', '好', '很好')
        level = []
        for i in range(3):
            level.insert(i, random.choice(leavel))
            # 技能水平 工作态度 团队精神
            element = "//img[@title='%s']" % level[i]
            get_elements(driver, ('xpath', element))[i].click()
        if status == '立即添加评价':
            get_element(driver, ('xpath', "//textarea[@placeholder='请输入评价']")).send_keys('good')
            get_element(driver, ('xpath', "//button[contains(text(),'保存')]")).click()
            sleep(2)
            if is_element_present_3s(driver, ('xpath', "//p[contains(text(),'good')]"), 2):
                pass
            else:
                bug_photo(driver)
                assert False
        elif status == '修改评价':
            get_element(driver, ('xpath', "//textarea[@placeholder='请输入评价']")).clear()
            get_element(driver, ('xpath', "//textarea[@placeholder='请输入评价']")).send_keys('again good')
            get_element(driver, ('xpath', "//button[contains(text(),'保存')]")).click()
            sleep(2)
            if is_element_present_3s(driver, ('xpath', "//p[contains(text(),'again good')]"), 2):
                pass
            else:
                bug_photo(driver)
                assert False
        else:
            print('使用方法不正确')
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False




