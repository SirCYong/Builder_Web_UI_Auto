# -*- coding: utf-8 -*-
# auth: CY
from Page.Element import is_element_present
from Page.web.get_now_time import bug_photo


def logout(driver):
    driver.find_element_by_id("dropdownMenu-set").click()
    driver.find_element_by_xpath("//a[contains(text(),'注销')]").click()
    try:
        is_element_present(driver, ('xpath', "//button[contains(text(),'登录')]"))
    except Exception as e:
        print(e)
        print('注销失败')
        bug_photo(driver)
        return False
