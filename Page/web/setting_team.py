# -*- coding:utf-8 -*-
# auth cy
# update 2018-02-26
from time import sleep

from selenium.webdriver.common.keys import Keys

from Page.Element import get_element, get_elements, is_element_present, is_element_present_3s
from Page.api.builder_api import employee_register, set_user_group, login
from Page.random_data import getRandomName, get_phone_number
from Page.web.by_applying_for import employee_operation_the_all_workflow
from Page.web.get_now_time import bug_photo
from Page.web.into_level import into_one_level, into_two_level
from Page.web.logout import logout
from Page.web.web_login import web_login


def add_team(driver, team_name):
    # 增删查改 班组
    into_one_level(driver, '工程面板')
    sleep(1)
    into_two_level(driver, '组织构架')
    # 新增班组按钮
    get_element(driver, ('xpath', "//button[@class='btn btn-primary btn-sm']")).click()
    sleep(1)
    get_element(driver, ('xpath', "//input[@class='form-control input-sm']")).clear()
    # 输入班组名称
    get_element(driver, ('xpath', "//input[@class='form-control input-sm']")).send_keys(team_name)
    # 选择班组长
    get_element(driver, ('id', "select2-team-leader-container")).click()
    get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys('郑琳琳')
    sleep(0.5)
    get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(Keys.ENTER)
    # 确定
    get_element(driver, ('xpath', "//button[contains(text(),'确定')]")).click()
    sleep(1)
    team_name_element = "//div[contains(text(),'%s')]" % team_name
    if is_element_present(driver, ('xpath', team_name_element)):
        pass
    else:
        bug_photo(driver)
        print('新增班组失败')
        assert False
    # 修改班组
    driver.find_element_by_xpath(team_name_element).click()
    get_element(driver, ('xpath', "//button[contains(text(),'修改班组')]")).click()
    new_team_name = getRandomName()
    sleep(1)
    get_element(driver, ('xpath', "//input[@class='form-control input-sm']")).clear()
    # 输入新的班组名称
    get_element(driver, ('xpath', "//input[@class='form-control input-sm']")).send_keys(new_team_name)
    # 确定
    get_element(driver, ('xpath', "//button[contains(text(),'确定')]")).click()
    sleep(1)
    new_team_name_element = "//div[contains(text(),'%s')]" % new_team_name
    if is_element_present(driver, ('xpath', new_team_name_element)):
        pass
    else:
        bug_photo(driver)
        print('新增班组失败')
        assert False
    get_element(driver, ('xpath', new_team_name_element)).click()
    get_element(driver, ('xpath', "//button[contains(text(),'删除班组')]")).click()
    get_element(driver, ('xpath', "//a[@class='layui-layer-btn0']")).click()
    sleep(1)
    if is_element_present(driver, ('xpath', team_name_element)):
        bug_photo(driver)
        print('新增班组失败')
        assert False
    else:
        pass


def edit_organizational_structure(driver, project_manager, project_labor, quality, number=1):
    # 编辑组织架构
    try:
        if number == 1:
            into_one_level(driver, '工程面板')
            sleep(1)
            into_two_level(driver, '组织构架')
            sleep(0.5)
        get_element(driver, ('xpath', "//button[contains(text(),'编辑')]")).click()
        old_project_manager = get_element(driver, ('xpath', "//span[@id='select2-project-manager-container']")).text
        get_element(driver, ('xpath', "//span[@id='select2-project-manager-container']")).click()
        get_element(driver, ('xpath', "//input[@type='search']")).send_keys(project_manager)
        sleep(1)
        get_element(driver, ('xpath', "//input[@type='search']")).send_keys(Keys.ENTER)
        sleep(0.5)
        old_project_labor = get_element(driver, ('xpath', "//span[@id='select2-project-labor-container']")).text
        get_element(driver, ('xpath', "//span[@id='select2-project-labor-container']")).click()
        get_element(driver, ('xpath', "//input[@type='search']")).send_keys(project_labor)
        sleep(1)
        get_element(driver, ('xpath', "//input[@type='search']")).send_keys(Keys.ENTER)
        old_quality = get_element(driver, ('xpath', "//span[@id='select2-quality-container']")).text
        get_element(driver, ('xpath', "//span[@id='select2-quality-container']")).click()
        get_element(driver, ('xpath', "//input[@type='search']")).send_keys(quality)
        sleep(1)
        get_element(driver, ('xpath', "//input[@type='search']")).send_keys(Keys.ENTER)
        get_element(driver, ('xpath', "//button[contains(text(),'确定')]")).click()
        element = "//a[@class='layui-layer-ico layui-layer-close layui-layer-close1']"
        if is_element_present_3s(driver, ('xpath', "//div[@id='LAY_demo2']"), 1):
            print('更新成功')
        #     pass
        # elif len(get_elements(driver, ('xpath', element))) > 1:
        #     get_elements(driver, ('xpath', element))[1].click()
        #     get_elements(driver, ('xpath', element))[0].click()
        #     logout(driver)
        #     employee_operation_the_all_workflow(driver, 1)
        #     print('存在工作流')
        #     get_element(driver, ('xpath', "")).click()
        else:
            print('更新失败')
            assert False
        return old_project_manager, old_project_labor, old_quality
    except Exception as e:
        print(e)


def add_manager_for_organizational_structure(driver, ws_driver):
    # 编辑新的组织架构
    company_labor = {'data': {'company_id': 3}}
    company_manager = {'data': {'company_id': 2}}
    group = '项目经理', '劳务经理', '质量员'
    name_list = []
    pwd = 123456
    for i in range(len(group)):
        mobile = get_phone_number()
        if group[i] == '劳务经理':
            company = company_labor
        else:
            company = company_manager
        # 注册职员
        employee_register(ws_driver, company, mobile)
        # 获取 user_id
        clerk = login(ws_driver, mobile, pwd)
        name_list.insert(i, clerk['data']['realname'])
        # 获取 平台运维 sid
        operation_sid = login(ws_driver, '18888888888', pwd)['data']['sid']
        # 设置角色
        set_user_group(ws_driver, operation_sid, clerk['data']['user_id'], group[i])
    print(name_list)
    old_name = edit_organizational_structure(driver, name_list[0], name_list[1], name_list[2])
    j = 0
    for h in name_list:
        print(h, 'and', (list(old_name))[j])
        if h == (list(old_name))[j]:
            assert False, "编辑组织架构失败"
        else:
            pass
        j += 1
    print(old_name)
    # 恢复以前的组织架构
    sleep(5)
    print('开始恢复')
    edit_organizational_structure(driver, old_name[0], old_name[1], old_name[2], 2)
    sleep(3)
    old_manage_name = "//a[contains(text(),'%s')]" % old_name[0]
    old_labor_name = "//a[contains(text(),'%s')]" % old_name[1]
    old_qa_name = "//a[contains(text(),'%s')]" % old_name[2]
    if is_element_present_3s(driver, ('xpath', old_manage_name)) \
            and is_element_present_3s(driver, ('xpath', old_labor_name)) \
            and is_element_present_3s(driver, ('xpath', old_qa_name)):
        print("恢复成功")
    else:
        assert False, "恢复失败"
