# -*- coding: utf-8 -*-
# auth: cy
# update ： 2018年4月3日
import random
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from Page.Element import get_element, get_elements, is_element_present_3s
from Page.web.into_level import into_one_level, into_two_level
from run_path import file_path


def upload_file_document_library(driver):
    # 台账管理，上传专项检查文件、 查看文件上传是否成功、
    into_one_level(driver, '工程面板')
    sleep(1)
    into_two_level(driver, '台账管理')
    sleep(0.5)
    # 获取所有的文件夹
    folder_number = len(get_elements(driver, ('xpath', "//div[@class='col-sm-2 text-center type-item']/p")))
    # 文件夹的名称
    for i in range(folder_number):
        folder_name = get_elements(driver, ('xpath', "//div[@class='col-sm-2 text-center type-item']/p"))[i].text
        print(folder_name)
        element = "//p[contains(text(),'%s')]" % folder_name
        get_element(driver, ('xpath', element)).click()
        if folder_name in ('考勤记录表', '工资单', '银行代发'):

            get_elements(driver, ('xpath', "//div[@class='col-sm-2 text-center type-item search-month-name']"))[
                0].click()
        upload_and_delete_file(driver)
        driver.refresh()
        sleep(1)


def upload_and_delete_file(driver):
    file_type_list = ('xlsx', 'docx', 'pdf', 'png', 'pptx', 'zip', 'jpg')
    # 随机选取一个文件夹
    file_type = random.choice(file_type_list)
    a = file_path(file_type)
    print(a)
    get_element(driver, ('xpath', "//input[@type='file']")).send_keys(a)
    element = "//p[contains(text(),'%s.%s')]" % (file_type, file_type)
    #  判断文件状态
    assert is_element_present_3s(driver, ('xpath', element), 6), "上传%s文件失败" % file_type
    sleep(0.5)
    #  删除文件状态
    if is_element_present_3s(driver, ('xpath', element)):
        # 右击文件
        sleep(1)
        ActionChains(driver).context_click(get_element(driver, ('xpath', element))).perform()
        sleep(0.3)
        get_element(driver, ('xpath', "//a[contains(text(),'删除')]")).click()
    else:
        pass
    if is_element_present_3s(driver, ('xpath', element)):
        print('删除失败')
        assert False
    else:
        print('删除成功')



