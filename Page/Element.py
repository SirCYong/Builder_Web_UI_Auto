# -*- coding: utf-8 -*-
# auth: CY

from selenium.webdriver.support.wait import WebDriverWait


def get_element(driver: object, element_meta_data: object) -> object:
    """

    :param element_meta_data:
    :type element_meta_data:
    :param driver:
    :type driver:
    :return:
    :rtype:
    :rtype: element
    """
    by = element_meta_data[0]
    by = by.upper()
    value = element_meta_data[1]
    try:
        if by == 'IOS_UIAUTOMATION':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_ios_uiautomation(value))
        if by == 'ANDROID_UIAUTOMATOR':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_android_uiautomator(value))
        if by == 'ACCESSIBILITY_ID':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_accessibility_id(value))
        if by == 'ID':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(value))
        if by == 'XPATH':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(value))
        if by == 'LINK_TEXT':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_link_text(value))
        if by == 'PARTIAL_LINK_TEXT':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_partial_link_text(value))
        if by == 'NAME':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_name(value))
        if by == 'TAG_NAME':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_tag_name(value))
        if by == 'CLASS_NAME':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name(value))
        if by == 'CSS_SELECTOR':
            return WebDriverWait(driver, 10).until(lambda x: x.find_element_by_css_selector(value))
        else:
            # print(u'元素的定位type不正确，请检查xml的type是否符合要求.')
            # run_info_log(u'元素的定位type不正确，请检查xml的type是否符合要求.', GlobalVarClass.get_log_file())
            raise
    except Exception as e:
        # print(u'没有找到(' + by + u":" + value + u')元素')
        # run_info_log(str(traceback.format_exc()), GlobalVarClass.get_log_file())
        # run_info_log(e, GlobalVarClass.get_log_file())
        raise


def get_elements(driver, element_meta_data):
    """
    :param testcase_name:
    :param element_meta_data:
    :type element_meta_data:
    :param driver:
    :type driver:
    :return:
    :rtype:
    :rtype: element
    """
    by = element_meta_data[0]
    by = by.upper()
    value = element_meta_data[1]
    try:
        if by == 'IOS_UIAUTOMATION':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_ios_uiautomation(value))
        if by == 'ANDROID_UIAUTOMATOR':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_android_uiautomator(value))
        if by == 'ACCESSIBILITY_ID':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_accessibility_id(value))
        if by == 'RESOURCE_ID':
            return  WebDriverWait(driver, 10).until(lambda x: x.find_element_by_resource_id(value))
        if by == 'ID':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_id(value))
        if by == 'XPATH':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_xpath(value))
        if by == 'LINK_TEXT':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_link_text(value))
        if by == 'PARTIAL_LINK_TEXT':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_partial_link_text(value))
        if by == 'NAME':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_name(value))
        if by == 'TAG_NAME':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_tag_name(value))
        if by == 'CLASS_NAME':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_class_name(value))
        if by == 'CSS_SELECTOR':
            return WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_css_selector(value))
        else:
            # print('元素的定位type不正确，请检查xml的type是否符合要求.')
            # run_info_log('元素的定位type不正确，请检查xml的type是否符合要求.', GlobalVarClass.get_log_file())
            raise
    except Exception as e:
        # print(u'没有找到(' + by + u":" + value + u')元素')
        # run_info_log(str(traceback.format_exc()), GlobalVarClass.get_log_file())
        # run_info_log(e, GlobalVarClass.get_log_file())
        raise


def is_element_present(driver: object, locator: object) -> object:
    try:
        get_element(driver, locator)
        return True
    except Exception as e:
        print(e)
        return False


def get_element_3s(driver: object, element_meta_data: object, time_sum) -> object:
    """

    :param element_meta_data:
    :type element_meta_data:
    :param driver:
    :type driver:
    :return:
    :rtype:
    :rtype: element
    """
    by = element_meta_data[0]
    by = by.upper()
    value = element_meta_data[1]
    time_sum = int(time_sum)
    try:
        if by == 'IOS_UIAUTOMATION':
            return WebDriverWait(driver, time_sum).until(lambda x: x.find_element_by_ios_uiautomation(value))
        if by == 'ANDROID_UIAUTOMATOR':
            return WebDriverWait(driver, time_sum).until(lambda x: x.find_element_by_android_uiautomator(value))
        if by == 'ACCESSIBILITY_ID':
            return WebDriverWait(driver, time_sum).until(lambda x: x.find_element_by_accessibility_id(value))
        if by == 'ID':
            return WebDriverWait(driver, time_sum).until(lambda x: x.find_element_by_id(value))
        if by == 'XPATH':
            return WebDriverWait(driver, time_sum).until(lambda x: x.find_element_by_xpath(value))
        if by == 'LINK_TEXT':
            return WebDriverWait(driver, time_sum).until(lambda x: x.find_element_by_link_text(value))
        if by == 'PARTIAL_LINK_TEXT':
            return WebDriverWait(driver, time_sum).until(lambda x: x.find_element_by_partial_link_text(value))
        if by == 'NAME':
            return WebDriverWait(driver, time_sum).until(lambda x: x.find_element_by_name(value))
        if by == 'TAG_NAME':
            return WebDriverWait(driver, time_sum).until(lambda x: x.find_element_by_tag_name(value))
        if by == 'CLASS_NAME':
            return WebDriverWait(driver, time_sum).until(lambda x: x.find_element_by_class_name(value))
        if by == 'CSS_SELECTOR':
            return WebDriverWait(driver, time_sum).until(lambda x: x.find_element_by_css_selector(value))
        else:
            # print(u'元素的定位type不正确，请检查xml的type是否符合要求.')
            # run_info_log(u'元素的定位type不正确，请检查xml的type是否符合要求.', GlobalVarClass.get_log_file())
            raise
    except Exception as e:
        # print(u'没有找到(' + by + u":" + value + u')元素')
        # run_info_log(str(traceback.format_exc()), GlobalVarClass.get_log_file())
        # run_info_log(e, GlobalVarClass.get_log_file())
        raise


def is_element_present_3s(driver: object, locator: object, time) -> object:
    try:
        get_element_3s(driver, locator, time)
        return True
    except Exception as e:
        print(e)
        return False
