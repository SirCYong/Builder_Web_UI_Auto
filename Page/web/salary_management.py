# -*- coding: utf-8 -*-
import os
import re
from time import sleep
from openpyxl import load_workbook
from Page.BankCardNumber import get_bank_card_number
from Page.Element import get_element, get_elements, is_element_present_3s
from Page.random_data import setting_input_time
from Page.web.get_now_time import get_now_dates, bug_photo
from Page.web.into_level import into_one_level, into_two_level
from run_path import test_report_path


def new_payroll(driver, payroll_name, money):
    # 薪资管理
    try:
        into_one_level(driver, '工程面板')
        sleep(1)
        into_two_level(driver, '薪资管理')
        get_element(driver, ('xpath', "//button[@class='btn btn-primary']")).click()
        # 工程名称
        get_element(driver, ('xpath', "//select[@id='kkkk']/option[2]")).click()
        # 输入工资月份
        get_now_dates()
        setting_input_time(driver)
        r = r'\d{4}-\d{2}'
        text = re.findall(r, get_now_dates())
        get_element(driver, ('xpath', "//input[@class='form-control form-n-y-1']")).send_keys(text)
        # 工资单名称
        get_element(driver, ('id', 'createProllNameAll')).clear()
        sleep(0.2)
        get_element(driver, ('id', 'createProllNameAll')).send_keys(payroll_name)
        # 确定按钮
        get_element(driver, ('xpath', "//button[@class='btn btn-primary proll-btn-com']")).click()
        sleep(1)
        # 增加最后一个人
        get_elements(driver,
                     ('xpath', "//div[@id='createrProll']/div[3]/div[1]/div[2]/div/div[1]/div/div/div/span[2]"))[
            -1].click()
        sleep(0.5)
        get_element(driver, ('xpath', "//a[contains(text(),'移除')]")).click()
        sleep(1)
        if is_element_present_3s(driver, ('xpath', "//tr[1]/td[7]/input"), 3):
            print("移除失败")
            assert False
        else:
            pass
        get_elements(driver,
                     ('xpath', "//div[@id='createrProll']/div[3]/div[1]/div[2]/div/div[1]/div/div/div/span[2]"))[
            -1].click()
        get_element(driver, ('xpath', "//tr[1]/td[5]/a")).click()
        get_elements(driver, ('xpath', "//input[@class='form-control']"))[1].send_keys(get_bank_card_number()[2:18])
        get_element(driver, ('xpath', "//button[contains(text(),'确定')]")).click()
        # 发放金额
        get_element(driver, ('xpath', "//input[@class='pay-money']")).send_keys(money)
        sleep(3)
        get_element(driver, ('xpath', "//button[contains(text(),'保存')]")).click()
        sleep(0.5)
        get_element(driver, ('xpath', "//table[@id='project-proll-release']/tbody/tr[1]/td[7]/a[1]")).click()
        assert is_element_present_3s(driver, ('xpath', "//input[@class='pay-money']"), 3), "保存失败"
        sleep(3)
        get_element(driver, ('xpath', "//button[contains(text(),'保存')]")).click()
        sleep(0.5)
        get_element(driver, ('xpath', "//table[@id='project-proll-release']/tbody/tr[1]/td[7]/a[2]")).click()
        sleep(3)
        report = os.path.join(test_report_path(), payroll_name + '.xls')
        import win32com.client
        sleep(1)
        excel = win32com.client.gencache.EnsureDispatch('Excel.Application')
        sleep(0.1)
        wb = excel.Workbooks.Open(report)
        sleep(2)
        wb.SaveAs(report + 'x', FileFormat=51)
        wb.Close()
        excel.Application.Quit()
        # 删除旧的xls
        sleep(0.5)
        os.remove(report)
        new_report = os.path.join(test_report_path(), payroll_name + '.xlsx')
        wb1 = load_workbook(filename=new_report)
        sheets = wb1.get_sheet_names()  # 获取所有的表格
        print(sheets)
        sheets_first = sheets[0]  # 获取第一个表
        ws1 = wb1.get_sheet_by_name(sheets_first)
        print(ws1['F2'].value)
        assert money == ws1['F2'].value, "下载文件内容显示不正确"
        os.remove(new_report)
    except Exception as e:
        bug_photo(driver)
        print(e)
        assert False


