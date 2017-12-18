# -*- coding: utf-8 -*-
# auth:cy
import datetime
import os


def screenshot_path() -> object:
    # 截图路径
    now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    path = os.path.dirname(os.path.dirname(__file__))
    return path + '/bug_photo/' + now_time + '.jpg'


def bug_photo(driver):
    driver.get_screenshot_as_file(screenshot_path())


def get_now_dates():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    return now_time


def get_tomorrow_dates():
    tomorrow = (datetime.datetime.now() + datetime.timedelta(days=+1)).strftime('%Y-%m-%d')
    return tomorrow


def get_future_date(number):
    number = int(number)
    pass_dates = (datetime.datetime.now() + datetime.timedelta(days=+number)).strftime('%Y-%m-%d')
    return pass_dates


def get_pass_dates(number):
    number = int(number)
    pass_dates = (datetime.datetime.now() + datetime.timedelta(days=-number)).strftime('%Y-%m-%d')
    return pass_dates

if __name__ == '__main__':
    print(get_future_date(600))