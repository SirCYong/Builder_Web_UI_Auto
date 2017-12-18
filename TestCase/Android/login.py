# encoding: utf-8
from time import sleep

from appium import webdriver

from Page.android.get_udid import get_android_udid
from Page.android.start_appium import start_android_appium
from Page.android.stop_appium import stop_android_appium

device_name = get_android_udid()
stop_android_appium()
start_android_appium(device_name)
desired_caps = {
    'platformName': 'Android',
    'deviceName': device_name,
    'platformVersion': '7.1.1',
    'appPackage': 'com.android.calculator2',
    'appActivity': 'com.android.calculator2.Calculator',
    'unicodeKeyboard': True,
    'resetKeyboard': True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(3)
a = driver.find_element_by_name('请输入帐号')
a.click()
a.send_keys('18888888888')
sleep(1)
driver.find_elements_by_xpath("//android.widget.EditText")[1].send_keys('123456')
sleep(2)
driver.find_element_by_accessibility_id("登录").click()
# driver.quit()

sleep(5)