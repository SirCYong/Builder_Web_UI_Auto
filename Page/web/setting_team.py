# -*- coding:utf-8 -*-
# auth cy
from time import sleep

from Page.Element import get_element, get_elements, is_element_present
from Page.random_data import getRandomName
from Page.web.get_now_time import bug_photo
from Page.web.into_level import into_one_level, into_two_level


def add_team(driver, team_name):
    into_one_level(driver, '工程面板')
    sleep(1)
    into_two_level(driver, '组织构架')
    # 新增班组按钮
    get_element(driver, ('xpath', "//button[@class='btn btn-primary btn-sm']")).click()
    sleep(1)
    get_elements(driver, ('xpath', "//input[@class='form-control input-sm']"))[2].clear()
    # 输入班组名称
    get_elements(driver, ('xpath', "//input[@class='form-control input-sm']"))[2].send_keys(team_name)
    # 选择班组长
    get_element(driver, ('xpath', "//*[@id='add-team']/form/div[3]/div/select/option[2]")).click()
    # 选择质量员
    get_element(driver, ('xpath', "//*[@id='add-team']/form/div[4]/div/select/option[2]")).click()
    # 确定
    get_element(driver, ('xpath', "//*[@id='add-team']/form/div[5]/div/button[1]")).click()
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
    get_elements(driver, ('xpath', "//input[@class='form-control input-sm']"))[2].clear()
    # 输入新的班组名称
    get_elements(driver, ('xpath', "//input[@class='form-control input-sm']"))[2].send_keys(new_team_name)
    # 确定
    get_element(driver, ('xpath', "//*[@id='add-team']/form/div[5]/div/button[1]")).click()
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



