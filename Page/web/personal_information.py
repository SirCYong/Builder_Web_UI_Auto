# -*-coding:utf-8 -*-
# auth CY

import datetime
import random
from time import sleep

from Page.Element import get_element, get_elements, is_element_present, get_element_3s
from Page.random_data import getCompanyName, random_str, get_org_no, getPeopleName, get_mobile, setting_input_time
from Page.web.get_now_time import bug_photo, get_now_dates, get_pass_dates, get_tomorrow_dates


def work_experience(driver):
    company_name = getCompanyName()
    project_name = company_name[2:-4] + '工程'
    start_date = get_pass_dates(random.randint(300, 400))
    end_date = get_pass_dates(random.randint(100, 299))
    information = "上士闻道勤而行之；中士闻道若存若亡；下士闻道大笑之，不笑不足以为道。执行是一日复一日的"
    try:
        if is_element_present(driver, ('xpath', "//i[@data-target='#mo-work-add']")):
            get_element(driver, ('xpath', "//i[@data-target='#mo-work-add']")).click()
        else:
            get_element(driver, ('xpath', "//div[@data-target='#mo-work']")).click()
            get_element(driver, ('xpath', "//div[@data-target='#mo-work-add' and contains(text(),'添加工作经验')]")).click()
        get_elements(driver, ('xpath', "//div[@class='col-sm-6']/input[@placeholder='']"))[1].send_keys(company_name)
        sleep(1)
        setting_input_time(driver)
        get_elements(driver, ('xpath', "//input[@data-max-time='']"))[2].send_keys(start_date)
        end_date_element = "//input[@data-min-time='%s']" % start_date
        get_element(driver, ('xpath', end_date_element)).send_keys(end_date)
        get_elements(driver, ('xpath', "//div[@class='col-sm-6']/input[@placeholder='']"))[2].send_keys(project_name)
        get_element(driver, ('xpath', "//div[@class='col-sm-6']/textarea[@class='form-control']")).send_keys(
            information)
        get_elements(driver, ('xpath', "//button[contains(text(),'完成')]"))[1].click()
        sleep(0.5)
        element = "//h4[contains(text(),'%s')]" % company_name

        assert is_element_present(driver, ('xpath', element))
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def personal_certificate(driver, file_path):
    sleep(3)
    try:
        if is_element_present(driver, ('xpath', "//i[@data-target='#mo-book-add']")):
            get_element(driver, ('xpath', "//i[@data-target='#mo-book-add']")).click()
        else:
            get_element(driver, ('xpath', "//div[@data-target='#mo-book']")).click()
            get_element(driver, ('xpath', "//div[@data-target='#mo-book-add' and contains(text(),'添加证书')]")).click()
        work_type = "//div[1]/div[1]/select[@class='form-control']/option[%s]" % str(random.randint(2, 39))
        get_elements(driver, ('xpath', work_type))[0].click()
        certificate_number = random_str() + get_org_no()[:-3]
        get_element(driver, ('xpath', "//input[@placeholder='请输入工种证书号']")).send_keys(certificate_number)
        level_education = "//div[3]/div[1]/select[@class='form-control']/option[%s]" % str(random.randint(2, 11))
        get_elements(driver, ('xpath', level_education))[0].click()
        setting_input_time(driver)
        get_element(driver, ('xpath', "//input[@placeholder='选择日期不得晚于当前日期']")).send_keys(
            get_pass_dates(random.randint(200, 400)))
        get_element(driver, ('xpath', "//input[@placeholder='选择日期大于等于领证日期']")).send_keys(
            get_pass_dates(random.randint(50, 199)))
        get_element(driver, ('xpath', "//input[@placeholder='选择日期大于使用开始日期']")).send_keys(get_tomorrow_dates())
        get_element(driver, ('xpath', "//div[7]/div[1][@class='col-sm-6']/input")).send_keys('政府')
        if len(get_elements(driver, ('xpath', "//input[@name='file']"))) == 2:
            get_elements(driver, ('xpath', "//input[@name='file']"))[0].send_keys(file_path)
            get_elements(driver, ('xpath', "//input[@name='file']"))[1].send_keys(file_path)
        else:
            get_elements(driver, ('xpath', "//input[@name='file']"))[-2].send_keys(file_path)
            get_elements(driver, ('xpath', "//input[@name='file']"))[-1].send_keys(file_path)
        # 利用js 获取当前元素位置
        driver.execute_script("arguments[0].scrollIntoView();",
                              get_element(driver, ('xpath', "//button[contains(text(),'提交')]")))
        sleep(0.5)
        get_element(driver, ('xpath', "//button[contains(text(),'提交')]")).click()
        element = "//h4[contains(text(),'%s')]" % certificate_number
        assert is_element_present(driver, ('xpath', element)), "添加证书失败"
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def add_education_experience(driver):
    sleep(3)
    try:
        if is_element_present(driver, ('xpath', "//i[@data-target='#mo-edu-add']")):
            get_element(driver, ('xpath', "//i[@data-target='#mo-edu-add']")).click()
        else:
            get_element(driver, ('xpath', "//div[@data-target='#mo-edu']")).click()
            get_element(driver, ('xpath', "//div[@data-target='#mo-edu-add' and contains(text(),'添加教育经历')]")).click()
        work_type = "//div[1]/div[1]/select[@class='form-control']/option[%s]" % str(random.randint(1, 10))
        get_elements(driver, ('xpath', work_type))[1].click()
        get_element(driver, ('xpath', "//input[@placeholder='专业']")).send_keys('建筑')
        start_dates = get_pass_dates(random.randint(200, 300))
        end_dates = get_pass_dates(random.randint(50, 199))
        setting_input_time(driver)
        get_element(driver, (
            'xpath', "//input[@placeholder='' and @class='form-control input-sm form-date val-start-date']")).send_keys(
            start_dates)
        get_elements(driver, ('xpath', "//input[@placeholder='' and @class='form-control input-sm form-date']"))[
            -1].send_keys(end_dates)
        school_name = getCompanyName()[2:-4] + '学校'
        get_element(driver, ('xpath', "//input[@placeholder='学校名称']")).send_keys(school_name)
        get_elements(driver, ('xpath', "//button[contains(text(),'完成')]"))[2].click()
        title = school_name + '(' + start_dates + '——' + end_dates + ')'
        element = "//h4[contains(text(),'%s')]" % title
        assert is_element_present(driver, ('xpath', element))
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def family_information(driver):
    sleep(3)
    try:
        get_element(driver, ('xpath', "//div[@data-target='#mo-home']")).click()
        get_element(driver, ('xpath', "//input[@data-duplex-changed='show1']")).click()
        get_elements(driver, ('xpath', "//div[@class='pi-plane-con-text']/input"))[0].clear()
        get_elements(driver, ('xpath', "//div[@class='pi-plane-con-text']/input"))[0].send_keys('2')
        setting_input_time(driver)
        # 结婚日期
        get_elements(driver, ('xpath', "//div[@id='marry']/input"))[0].send_keys(
            get_pass_dates(100))
        get_elements(driver, ('xpath', "//div[@class='pi-plane-con-text']/input"))[1].send_keys(getPeopleName())
        get_elements(driver, ('xpath', "//div[@class='pi-plane-con-text']/input"))[2].send_keys(get_mobile())
        relation_element = "//div[2]/div/div[6]/select/option[%s]" % str(random.randint(2, 8))
        get_element(driver, ('xpath', relation_element)).click()
        len_province = len(get_elements(driver, ('xpath', "//div[2]/div/div[7]/select/option")))
        province_element = "//div[2]/div/div[7]/select/option[%s]" % str(random.randint(2, len_province))
        get_element(driver, ('xpath', province_element)).click()
        sleep(1)
        len_city = len(get_elements(driver, ('xpath', "//div[2]/div/div[8]/select/option")))
        city_element = "//div[2]/div/div[8]/select/option[%s]" % str(random.randint(2, len_city))
        get_element(driver, ('xpath', city_element)).click()
        sleep(1)
        len_district = len(get_elements(driver, ('xpath', "//div[2]/div/div[9]/select/option")))
        district_element = "//div[2]/div/div[9]/select/option[%s]" % str(random.randint(1, len_district))
        get_element(driver, ('xpath', district_element)).click()
        get_element(driver, ('xpath', "//div[2]/div/div[10]/input")).send_keys('塔克拉玛干')
        get_element(driver, ('xpath', "//div[2]/div/div[11]/input")).send_keys('厄尔')
        get_elements(driver, ('xpath', "//button[contains(text(),'保存')]"))[1].click()
        assert get_element(driver, ('id', "LAY_demo2")).text == '更新成功'
        a = get_element(driver, ('id', "LAY_demo2")).text
        print(a)
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False


def basic_information(driver):
    sleep(3)
    try:
        get_element(driver, ('xpath', "//div[@data-target='#mo-basic']")).click()
        get_element(driver, ('xpath', "//button[@class='btn btn-primary btn-sm']/i")).click()
        len_element = len(get_elements(driver, ('xpath', "//div[@id='selectWorkType']/div")))
        for i in range(1, len_element, 3):
            element = "//div[@id='selectWorkType']/div[%s]/div/div[1]" % i
            get_element(driver, ('xpath', element)).click()
            sleep(0.1)
        get_element(driver, ('xpath', "//a[contains(text(),'确定')]")).click()
        # 省
        len_province = len(get_elements(driver, ('xpath', "//div[12]/select/option")))
        province_element = "//div[12]/select/option[%s]" % str(random.randint(2, len_province))
        get_element(driver, ('xpath', province_element)).click()
        sleep(0.2)
        # 市
        len_city = len(get_elements(driver, ('xpath', "//div[13]/select/option")))
        city_element = "//div[13]/select/option[%s]" % str(random.randint(2, len_city))
        get_element(driver, ('xpath', city_element)).click()
        sleep(0.2)
        # 区
        len_district = len(get_elements(driver, ('xpath', "//div[14]/select/option")))
        district_element = "//div[14]/select/option[%s]" % str(random.randint(2, len_district))
        get_element(driver, ('xpath', district_element)).click()
        get_element(driver, ('xpath', "//textarea[@type='text']")).send_keys('潘松区88号')
        get_elements(driver, ('xpath', "//button[contains(text(),'保存')]"))[0].click()
        assert get_element(driver, ('id', "LAY_demo2")).text == '更新成功'
        a = get_element(driver, ('id', "LAY_demo2")).text
        print(a)
    except Exception as e:
        print(e)
        bug_photo(driver)
        assert False
