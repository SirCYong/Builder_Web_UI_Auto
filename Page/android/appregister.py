# -*-coding:utf-8 -*-
import unittest

from selenium.webdriver.support.wait import WebDriverWait

from Page.Element import get_element, get_elements
from Page.android.get_udid import get_android_udid, get_android_version, android_7_uninstall
from Page.android.start_appium import start_android_appium
from appium import webdriver
from time import sleep

from Page.android.stop_appium import stop_android_appium

device_name = get_android_udid()
stop_android_appium()
sleep(2)
start_android_appium(device_name)
desired_caps = {
    'platformName': 'Android',
    'deviceName': device_name,
    'platformVersion': get_android_version(),
    'appPackage': 'cn.zlddata.zldtest',
    'appActivity': 'cn.zlddata.zldtest.MainActivity',
    'unicodeKeyboard': True,
    'resetKeyboard': True
}
if get_android_version()[:3] == '7.0':
    android_7_uninstall()
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# driver.switch_to.alert.accept()

def forget(phone_num):
    # driver.wait_activity(desired_caps['appWaitActivity'], 10)
    # driver.contexts
    get_elements(driver, ('ACCESSIBILITY_ID', '忘记密码')).click()
    driver.find_element_by_accessibility_id("忘记密码 ").click()
    sleep(6)
    driver.find_elements_by_class_name("android.widget.EditText")[0].send_keys(phone_num)
    sleep(3)
    driver.find_element_by_accessibility_id("点击获取 ").click()
    driver.find_element_by_android_uiautomator("text(\"请输入校验码\")").send_keys("11111")
    sleep(5)
    driver.find_elements_by_class_name("android.widget.EditText")[2].send_keys("123456")
    driver.find_elements_by_class_name("android.widget.EditText")[3].send_keys("123456")
    driver.find_element_by_accessibility_id("重置密码 ").click()


def register_worker(phone_num):
    # driver.wait_activity(desired_caps['appWaitActivity'], 10)
    get_element(driver, ("accessibility_id", "新用户注册")).click()
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("新用户注册"))
    # driver.find_element_by_accessibility_id("新用户注册 ").click()
    sleep(3)
    driver.find_element_by_accessibility_id("我是工人").click()
    sleep(3)
    a = driver.contexts
    print(a)
    driver.switch_to.context(a[-1])
    driver.find_element_by_xpath("//android.widget.EditText[@content-desc='请输入正确的帐号（手机号）']").send_keys(phone_num)
    sleep(3)
    driver.find_element_by_xpath("//android.widget.Button[@content-desc='点击获取 ']").click()
    sleep(6)
    driver.find_element_by_accessibility_id("请输入校验码").send_keys("11111")
    driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='注册']/android.widget.EditText[3]").send_keys(
        "123456")
    driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='注册']/android.widget.EditText[4]").send_keys(
        "123456")
    driver.find_element_by_accessibility_id("立即注册 ").click()
    driver.find_element_by_accessibility_id("确定 ").click()
    sleep(3)
    # judge_test_case(driver.find_element_by_accessibility_id("新用户注册 "))


def register_company_user(phone_num, name):
    driver.wait_activity(desired_caps['appWaitActivity'], 10)
    driver.find_element_by_accessibility_id("新用户注册 ").click()
    sleep(6)
    driver.find_element_by_accessibility_id("我是职员").click()
    sleep(6)
    driver.find_element_by_xpath("//android.widget.EditText[@content-desc='请选择公司名称']").click()
    sleep(6)
    driver.find_element_by_xpath("//android.widget.EditText[@content-desc='请输入公司名称']").send_keys(u"杭州")
    sleep(3)
    driver.find_element_by_accessibility_id("搜索").click()
    sleep(6)
    driver.find_element_by_accessibility_id("请选择公司名称").click()
    sleep(6)
    driver.find_element_by_accessibility_id("确定").click()
    sleep(3)
    driver.find_element_by_accessibility_id("请输入您的真实姓名").send_keys(name)
    sleep(3)
    driver.find_element_by_accessibility_id("请输入正确的帐号（手机号）").send_keys(phone_num)
    sleep(3)
    driver.find_element_by_accessibility_id("点击获取 ").click()
    sleep(6)
    driver.find_element_by_accessibility_id("请输入校验码").send_keys("11111")
    sleep(6)
    driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='注册']/android.widget.EditText[5]").send_keys(
        "123456")
    driver.find_element_by_xpath("//android.webkit.WebView[@content-desc='注册']/android.widget.EditText[6]").send_keys(
        "123456")
    driver.find_element_by_accessibility_id("立即注册 ").click()
    sleep(3)
    driver.find_element_by_accessibility_id("确定 ").click()
    sleep(3)
    # judge_test_case(driver.find_element_by_accessibility_id("新用户注册 "))


if __name__ == '__main__':
    register_worker("13456780003")
    # forget("18658861628")
