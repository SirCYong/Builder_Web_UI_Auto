# -*- coding: utf-8 -*-
# auth: CY
from Page.Element import get_element


def into_one_level(driver, text):
    element = "//a[contains(text(), '%s')]" % text
    get_element(driver, ('xpath', element)).click()


def into_two_level(driver, text):
    element = "//a[contains(text(), '%s')]" % text
    get_element(driver, ('xpath', element)).click()