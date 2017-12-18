# -*- coding: utf-8 -*-
# auth : cy
import random
from time import sleep

from selenium.webdriver.common.keys import Keys
from Page.Element import get_element, get_elements
from Page.random_data import setting_input_time, getCompanyName
from Page.web.get_now_time import get_now_dates, bug_photo, get_future_date, get_pass_dates
from Page.web.into_level import into_one_level, into_two_level
from Page.web.select_city import select_city, select_city_choice, sub_select_city_choice


def general_contract(driver, contract_name, contract_awarding, contracting, project_name):
    """

    :param driver:
    :param contract_name:合同名称
    :param contract_awarding: 发包方
    :param contracting: 总承包方
    :param project_name: 工程名称
    :return:
    """
    driver.implicitly_wait(5)
    try:
        into_one_level(driver, '任务面板')
        sleep(0.5)
        into_two_level(driver, '发起申请')
        # WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//div[contains(text(),'新建总包合同')")).click()
        driver.find_element_by_xpath("//div[contains(text(),'新建总包合同')]").click()
        # get_element(driver, ('XPATH', "//div[contains(text(),'新建总包合同'")).click()
        sleep(0.5)
        driver.find_element_by_xpath("//input[@placeholder='请输入合同名称']").send_keys(contract_name)
        sleep(0.5)
        # 发包方
        get_element(driver, ('id', 'select2-fbfName-container')).click()
        get_element(driver, ('xpath', "//input[@type='search']")).send_keys(contract_awarding)
        sleep(0.5)
        get_element(driver, ('xpath', "//input[@type='search']")).send_keys(Keys.ENTER)
        # 承包方
        get_element(driver, ('id', "select2-cbfName-container")).click()
        driver.find_element_by_xpath("//input[@type='search']").send_keys(contracting)
        sleep(0.5)
        driver.find_element_by_xpath("//input[@type='search']").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//input[@placeholder='请输入工程名称']").send_keys(project_name)
        select_city(driver)
        driver.find_element_by_xpath("//input[@placeholder='请输入工程详细地址']").send_keys('南京路168号')
        driver.find_element_by_xpath("//input[@placeholder='类目（必填）']").send_keys('建筑')
        driver.find_element_by_xpath("//input[@placeholder='年份（必填）']").click()
        driver.find_element_by_xpath("//span[@class='year active']").click()
        driver.find_element_by_xpath("//input[@placeholder='编号（必填）']").send_keys(random.randint(10000, 99999))
        project_information = '土方开挖，土方回填，钢筋工程，模板工程，混凝土工程，砌体工程，装饰装修工程等'
        contract_scope = "售楼部的美女，工程部的汉，项目部的光棍满街转！财务的花，预算的草，施工队的和尚到处跑！食堂的饭，宿舍的床，搞工程的女人吓死郎！"
        driver.find_elements_by_xpath("//textarea[@placeholder='必填']")[0].send_keys(project_information)
        driver.find_elements_by_xpath("//textarea[@placeholder='必填']")[1].send_keys(contract_scope)
        setting_input_time(driver)
        driver.find_element_by_xpath("//input[@placeholder='选择日期不得晚于计划竣工日期']").send_keys(get_now_dates())
        driver.find_element_by_xpath("//input[@placeholder='选择日期不得早于今天']").send_keys(get_future_date(300))
        driver.find_elements_by_xpath("//input[@placeholder='必填']")[0].send_keys(random.randint(100, 200))
        driver.find_elements_by_xpath("//input[@placeholder='必填']")[1].send_keys(random.randint(100000, 999999))
        driver.find_element_by_xpath("//input[@placeholder='请输入项目经理姓名']").send_keys("暂无")
        driver.find_element_by_xpath("//input[@placeholder='选择日期不得晚于当前日期']").send_keys(get_now_dates())
        select_city_choice(driver)
        driver.find_elements_by_xpath("//input[@placeholder='必填']")[2].send_keys("南京路256号")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        print(get_element(driver, ('id', "LAY_demo2")).text)
        assert get_element(driver, ('id', "LAY_demo2")).text == "成功"
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def contract_workflow(driver, contract_name, information):
    """

    :param information: 错误提示
    :param driver:
    :param contract_name: 合同名称
    :return:
    """
    into_one_level(driver, '任务面板')
    sleep(0.5)
    into_two_level(driver, '我的任务')
    get_element(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr[1]/td[8]/a")).click()
    get_element(driver, ('xpath', "//button[@class='btn btn-sm btn-success']")).click()
    get_element(driver, ('xpath', "//textarea")).send_keys('s')
    get_element(driver, ('xpath', "//a[@class='layui-layer-btn0']")).click()
    sleep(10)
    driver.find_element_by_xpath("//a[contains(text(),'我审核过的')]").click()
    sleep(2)
    contract_name += '签订审核'
    element_len = get_elements(driver, ('xpath', "//*[@id='task-mytask-table']/tbody/tr"))
    title_text = []
    for i in range(1, len(element_len)):
        element = "//*[@id='task-mytask-table']/tbody/tr[%d]/td[4]" % i
        text = get_element(driver, ('xpath', element)).text
        title_text.insert(i, text)
        print(title_text)
    information += '签订失败'
    assert contract_name in title_text, "%s" % information


def subcontract(driver, project_name, labor_company, sub_contract, labor_people):
    """
    :param driver: 驱动
    :param project_name: 工程名称
    :param labor_company: 劳务公司
    :param sub_contract: 分包合同名称
    :param labor_people: 劳务经理
    :return:
    """
    try:
        into_one_level(driver, '任务面板')
        sleep(0.5)
        into_two_level(driver, '发起申请')
        driver.find_element_by_xpath("//div[contains(text(),'新建分包合同')]").click()
        driver.find_element_by_xpath("//span[contains(text(),'输入工程名称')]").click()
        get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(project_name)
        sleep(0.5)
        get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(Keys.ENTER)
        sleep(1)
        driver.find_element_by_xpath("//span[contains(text(),'输入公司关键字查找')]").click()
        get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(labor_company)
        sleep(0.5)
        get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(Keys.ENTER)
        # 分包合同名称
        get_elements(driver, ('xpath', "//input[@placeholder='必填']"))[0].send_keys(sub_contract)
        information = "地基与基础、建筑装饰装修、建筑幕墙、钢结构、机电设备安装、电梯安装、消防设施、建筑防水、防腐保温、园林古建筑、爆破与拆除、电信工程、管道工程等"
        get_element(driver, ('xpath', "//textarea[@placeholder='必填']")).send_keys(information)
        setting_input_time(driver)
        get_element(driver, ('xpath', "//input[@placeholder='选择日期不得晚于计划竣工日期']")).send_keys(get_now_dates())
        get_element(driver, ('xpath', "//input[@placeholder='选择日期不得早于今天']")).send_keys(get_future_date(299))
        driver.find_element_by_xpath("//span[contains(text(),'输入姓名查找')]").click()
        get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(labor_people)
        sleep(1)
        get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(Keys.ENTER)
        get_elements(driver, ('xpath', "//input[@placeholder='必填']"))[1].send_keys(random.randint(10000, 99999))
        QA_standard(driver, random.randint(0, 1))
        remuneration_pay(driver, random.randint(0, 1))
        the_contract_comes_into_effect(driver, random.randint(0, 1))
        material_equipment_management(driver, random.randint(0, 1))
        sub_insurance(driver, random.randint(0, 1))
        dispute_resolution(driver, random.randint(0, 1))
        laws_and_regulations(driver, random.randint(0, 1))
        sleep(0.5)
        driver.find_element_by_xpath("//button[contains(text(),'完成')]").click()
        print(get_element(driver, ('id', "LAY_demo2")).text)
        assert get_element(driver, ('id', "LAY_demo2")).text == "成功"
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def labor_remuneration(driver, switch):
    if switch:
        # 暂停
        print('选中劳务报酬计算')
        price_0 = random.randint(3000, 90000)
        price_1 = random.randint(3000, 90000)
        price_2 = random.randint(3000, 90000)
        price_3 = random.randint(3000, 90000)
        get_element(driver, ('xpath', "//input[@placeholder='请输入整数']")).send_keys(price_0)
        # 选择工种
        work_type = "//*[@id='work-type']/option"
        work_type_element = "//*[@id='work-type']/option[%d]" % random.randint(2, len(work_type))
        get_element(driver, ('xpath', work_type_element)).click()
        get_elements(driver, ('xpath', "//div[@class='col-sm-6']/input[@placeholder='']"))[1].send_keys(price_1)
        get_elements(driver, ('xpath', "//div[@class='col-sm-6']/input[@placeholder='']"))[2].send_keys(price_2)
        get_elements(driver, ('xpath', "//div[@class='col-sm-6']/input[@placeholder='']"))[3].send_keys(price_3)
    else:
        pass


def QA_standard(driver, switch):
    # 质量标准
    if switch:
        qa_element = "//div[@id='sub_contract']/form/div[6]/div[2]/div/div/select/option[%s]" % str(random.randint(2, 3))
        get_element(driver, ('xpath', qa_element)).click()
    else:
        pass


def remuneration_pay(driver, switch):
    # 劳务报酬中间支付
    if switch:
        price = random.randint(3000, 50000)
        price_1 = random.randint(3000, 50000)
        price_2 = random.randint(3000, 50000)
        get_element(driver, ('xpath', "//div[contains(text(),'元')]/input[@class='form-num form-control input-sm']")).send_keys(price)
        get_element(driver, ('xpath', "//option[contains(text(),'现金')]")).click()
        get_elements(driver, ('xpath', "//button[contains(text(),'添加')]"))[2].click()
        setting_input_time(driver)
        get_elements(driver, ('xpath', "//input[@class='need form-control input-sm text-center form-date']"))[
            0].send_keys(get_pass_dates(60))
        get_elements(driver, ('xpath', "//input[@class='need form-control input-sm text-center form-date']"))[
            1].send_keys(get_pass_dates(30))
        get_elements(driver, ('xpath', "//div[contains(text(),'元')]/input[@class='need form-control input-sm']"))[
            0].send_keys(price_1)
        get_elements(driver, ('xpath', "//div[contains(text(),'元')]/input[@class='need form-control input-sm']"))[
            1].send_keys(price_2)
    else:
        pass


def the_contract_comes_into_effect(driver, switch):
    #   合同生效
    if switch:
        # 选择城市
        sub_select_city_choice(driver)
        get_element(driver, ('xpath', "//input[@placeholder='选择日期不得晚于当前日期']")).send_keys(get_now_dates())
        conditions_element = "//div[@id='sub_contract']/form/div[8]/div[2]/div[3]/div/select/option[%d]" % random.randint(
            2, 3)
        get_element(driver, ('xpath',  conditions_element)).click()
    else:
        pass


def material_equipment_management(driver, switch):
    # 材料设备管理
    if switch:
        get_element(driver, ('xpath', "//input[@placeholder='请输入供应设备到期时间']")).send_keys(random.randint(20, 99))
        get_element(driver, ('xpath', "//input[@placeholder='请输入0-100范围内整数']")).send_keys(random.randint(1, 99))
        get_elements(driver, ('xpath', "//button[contains(text(),'添加')]"))[-1].click()
        get_elements(driver, ('xpath', "//input[@class='need form-control input-sm text-center']"))[0].send_keys(
            getCompanyName()[2:-4])
        get_elements(driver, ('xpath', "//input[@class='need form-control input-sm text-center']"))[1].send_keys(
            getCompanyName()[2:-4])
        get_elements(driver, ('xpath', "//input[@class='need form-control input-sm form-num text-center']"))[
            0].send_keys(random.randint(200, 300))
        get_elements(driver, ('xpath', "//input[@class='need form-control input-sm form-num text-center']"))[
            1].send_keys(random.randint(200, 300))
    else:
        pass


def sub_insurance(driver, switch):
    # 保险
    if switch:
        information = "劳务分包人施工开始前，工程承包人应获得发包人为施工场地内的自有人员及第三人人员生命财产办理的保险，且不需劳务分包人支付保险费用。"
        information_1 = "即负责承建该项工程的施工单位，可分为总承包人和分承包人"
        get_elements(driver, ('xpath', "//textarea[@class='form-control input-sm']"))[1].send_keys(information)
        get_elements(driver, ('xpath', "//textarea[@class='form-control input-sm']"))[2].send_keys(information_1)
    else:
        pass


def dispute_resolution(driver, switch):
    # 争议解决方式
    if switch:
        a = random.randint(1, 2)
        if a == 1:
            get_element(driver, ('xpath', "//div[@id='arg']/input[@value='仲裁']")).click()
            get_element(driver, ('xpath', "//textarea[@placeholder='请输入仲裁委员会地址']")).send_keys('南门保安室')
        elif a == 2:
            get_element(driver, ('xpath', "//div[@id='arg']/input[@value='起诉']")).click()
    else:
        pass


def laws_and_regulations(driver, switch):
    # 法律法规
    if switch:
        for i in range(5):
            get_elements(driver, ('xpath', "//input[@class='zblaw-item']"))[i].click()
            sleep(0.1)
    else:
        pass










