# -*- coding: utf-8 -*-
# auth: cy
import random
from time import sleep

from Page.Element import get_element, get_elements


def select_city(driver):
    # 省
    all_province = driver.find_elements_by_xpath("//*[@id='chtsx']/div[1]/select/option")
    element1 = "//*[@id='chtsx']/div[1]/select/option[%d]" % random.randint(2, len(all_province))
    driver.find_element_by_xpath(element1).click()
    sleep(0.5)
    # 市
    all_city = driver.find_elements_by_xpath("//*[@id='chtsx']/div[2]/select/option")
    element2 = "//*[@id='chtsx']/div[2]/select/option[%d]" % random.randint(2, len(all_city))
    driver.find_element_by_xpath(element2).click()
    sleep(0.5)
    # 区
    all_district = driver.find_elements_by_xpath("//*[@id='chtsx']/div[3]/select/option")
    element3 = "//*[@id='chtsx']/div[3]/select/option[%d]" % random.randint(1, len(all_district))
    driver.find_element_by_xpath(element3).click()


def select_city_choice(driver):
    # 省
    all_province = driver.find_elements_by_xpath("//*[@id='cgcgk']/div[1]/select/option")
    element1 = "//*[@id='cgcgk']/div[1]/select/option[%d]" % random.randint(2, len(all_province))
    driver.find_element_by_xpath(element1).click()
    sleep(0.5)
    # 市
    all_city = driver.find_elements_by_xpath("//*[@id='cgcgk']/div[2]/select/option")
    element2 = "//*[@id='cgcgk']/div[2]/select/option[%d]" % random.randint(2, len(all_city))
    driver.find_element_by_xpath(element2).click()
    sleep(0.5)
    # 区
    all_district = driver.find_elements_by_xpath("//*[@id='cgcgk']/div[3]/select/option")
    element3 = "//*[@id='cgcgk']/div[3]/select/option[%d]" % random.randint(1, len(all_district))
    driver.find_element_by_xpath(element3).click()


def sub_select_city_choice(driver):
    # 省
    all_province = len(get_elements(driver, ('xpath', "//div[@id='fbqydd']/div[1]/select/option")))
    element_1 = "//div[@id='fbqydd']/div[1]/select/option[%d]" % random.randint(2, all_province)
    get_element(driver, ('xpath', element_1)).click()
    sleep(0.5)
    # 市
    all_city = len(get_elements(driver, ('xpath', "//div[@id='fbqydd']/div[2]/select/option")))
    if all_city > 1:
        element_2 = "//div[@id='fbqydd']/div[2]/select/option[%d]" % random.randint(2, all_city)
        get_element(driver, ('xpath', element_2)).click()
    else:
        element_2 = "//div[@id='fbqydd']/div[2]/select/option[%d]" % random.randint(1, all_city)
        get_element(driver, ('xpath', element_2)).click()
    sleep(0.5)
    # 区
    all_district = len(get_elements(driver, ('xpath', "//div[@id='fbqydd']/div[3]/select/option")))
    if all_district > 1:
        element_3 = "//div[@id='fbqydd']/div[3]/select/option[%d]" % random.randint(2, all_district)
        get_element(driver, ('xpath', element_3))
    else:
        element_3 = "//div[@id='fbqydd']/div[3]/select/option[%d]" % random.randint(1, all_district)
        get_element(driver, ('xpath', element_3))
