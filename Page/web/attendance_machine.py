# -*- coding: utf-8 -*-
# auth: cy
import random
from time import sleep

from selenium.webdriver.common.keys import Keys

from Page.Element import get_element, get_elements, is_element_present
from Page.web.get_now_time import bug_photo
from Page.web.into_level import into_two_level, into_one_level


def attendance_machine(driver, people):
    global name1_text
    into_two_level(driver, '设备管理')
    driver.find_element_by_xpath("//a[contains(text(),'考勤卡')]").click()
    name_text = []
    num = random.randint(100000, 999999)
    driver.find_element_by_xpath("//button[contains(text(),'新增')]").click()
    get_element(driver, ('xpath', "//input[@placeholder='请输入4-10位考勤卡号']")).send_keys(num)
    get_element(driver, ('xpath', "//span[@class='select2-selection__placeholder']")).click()
    get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(people)
    sleep(0.5)
    get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(Keys.ENTER)
    driver.find_element_by_xpath("//button[contains(text(),'确定')]").click()
    if is_element_present(driver, ('xpath', "//div[contains(text(),'该用户已绑定考勤卡')]")):
        # 解绑考勤卡
        sleep(7)
        get_element(driver, ('xpath', "//input[@placeholder='请输入考勤卡号或姓名筛选']")).send_keys(people)
        get_elements(driver, ('xpath', "//button[contains(text(),'筛选')]"))[0].click()
        for i in range(len(get_elements(driver, ('xpath', "//*[@id='kqk-table']/tbody/tr"))), 0, -1):
            unbind_element = "//*[@id='kqk-table']/tbody/tr[%d]/td[4]/a" % i
            get_element(driver, ('xpath', unbind_element)).click()
            get_element(driver, ('xpath', "//*[@id='k']/form/div[4]/button[3]")).click()
            assert is_element_present(driver, ('xpath', "//i[@class='layui-layer-ico layui-layer-ico1']")), "解绑考勤卡失败"
        sleep(0.5)
        # 输入空格 查看全部
        get_element(driver, ('xpath', "//input[@placeholder='请输入考勤卡号或姓名筛选']")).clear()
        get_element(driver, ('xpath', "//input[@placeholder='请输入考勤卡号或姓名筛选']")).send_keys(' ')
        sleep(0.5)
        get_elements(driver, ('xpath', "//button[contains(text(),'筛选')]"))[0].click()
        driver.find_element_by_xpath("//button[contains(text(),'新增')]").click()
        get_element(driver, ('xpath', "//input[@placeholder='请输入4-10位考勤卡号']")).send_keys(num)
        get_element(driver, ('xpath', "//span[@class='select2-selection__placeholder']")).click()
        get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(people)
        sleep(0.5)
        get_element(driver, ('xpath', "//input[@class='select2-search__field']")).send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//button[contains(text(),'确定')]").click()
    if is_element_present(driver, (
            'xpath',
            "html/body/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div[2]/ul/li[1]/a")):
        get_element(driver, (
            'xpath',
            "html/body/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div[2]/ul/li[1]/a")).click()
        sleep(0.5)
        element_len = get_elements(driver, ('xpath', "//*[@id='kqk-table']/tbody/tr"))
        for i in range(1, len(element_len) + 1):
            element = "//*[@id='kqk-table']/tbody/tr[%d]/td[2]" % i
            name_text.insert(i, get_element(driver, ('xpath', element)).text)
        assert str(num) in name_text, "考勤卡添加失败1"
    else:
        element_len_now = get_elements(driver, ('xpath', "//*[@id='kqk-table']/tbody/tr"))
        for i in range(1, len(element_len_now)):
            element = "//*[@id='kqk-table']/tbody/tr[%d]/td[2]" % i
            name_text.insert(i, get_element(driver, ('xpath', element)).text)
        assert str(num) in name_text, "考勤卡添加失败2"
    name1_text = []
    for h in range(1, len(get_elements(driver, ('xpath', "//*[@id='kqk-table']/tbody/tr"))) + 1):
        element = "//*[@id='kqk-table']/tbody/tr[%d]/td[3]" % h
        if get_element(driver, ('xpath', element)).text != '-':
            name1_text.insert(h, get_element(driver, ('xpath', element)).text)
    if is_element_present(driver, (
            'xpath',
            "html/body/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div[2]/ul/li[4]/a")):
        get_element(driver, (
            'xpath',
            "html/body/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div[2]/ul/li[4]/a")).click()
        sleep(0.5)
    sleep(1)
    get_element(driver, ('xpath', "//input[@placeholder='请输入考勤卡号或姓名筛选']")).send_keys(str(name1_text[0]))
    get_elements(driver, ('xpath', "//button[contains(text(),'筛选')]"))[0].click()
    assert name1_text[0] == get_element(driver,
                                        ('xpath', "//*[@id='kqk-table']/tbody/tr/td[3]")).text, "考勤卡筛选成功,or 筛选失败"
    # 解绑考勤卡
    get_element(driver, ('xpath', "//input[@placeholder='请输入考勤卡号或姓名筛选']")).clear()
    get_element(driver, ('xpath', "//input[@placeholder='请输入考勤卡号或姓名筛选']")).send_keys(num)
    get_elements(driver, ('xpath', "//button[contains(text(),'筛选')]"))[0].click()
    get_element(driver, ('xpath', "//*[@id='kqk-table']/tbody/tr/td[1]/input")).click()
    sleep(0.5)
    driver.find_elements_by_xpath("//button[contains(text(),'删除')]")[0].click()
    get_elements(driver, ('xpath', "//button[contains(text(),'确定')]"))[3].click()
    get_element(driver, ('id', 'success')).click()
    if is_element_present(driver, (
            'xpath',
            "//div[contains(text(),'考勤卡不存在或无法删除已经绑定用户的考勤卡，请重新选择用户,或者先解绑')]")):
        sleep(7)
        try:
            # get_element(driver, ('xpath', "//button[contains(text(),'取消')]")).click()
            get_element(driver, ('xpath', "//*[@id='kqk-table']/tbody/tr/td[4]/a")).click()
            get_element(driver, ('xpath', "//*[@id='k']/form/div[4]/button[3]")).click()
            get_element(driver, ('xpath', "//*[@id='kqk-table']/tbody/tr/td[1]/input")).click()
            get_elements(driver, ('xpath', "//button[contains(text(),'删除')]"))[0].click()
            get_elements(driver, ('xpath', "//button[contains(text(),'确定')]"))[3].click()
            get_element(driver, ('id', 'success')).click()
        except Exception as e:
            bug_photo(driver)
            print(e)
    assert is_element_present(driver, ('id', "LAY_demo2")), "删除考勤卡失败"


def attendance_machine_login(driver):
    into_one_level(driver, '工程面板')
    sleep(1)
    get_elements(driver, ('xpath', "//a[contains(text(),'设置')]"))[1].click()
    into_two_level(driver, '考勤机设置')
    get_elements(driver, ('xpath', "//i[@class='glyphicon glyphicon-facetime-video']"))[0].click()
    # 得到selenium打开的浏览器的所有句柄
    all_hand = driver.window_handles
    # 切换句柄
    driver.switch_to_window(all_hand[-1])
    get_element(driver, ('id', 'firstname')).clear()
    sleep(0.5)
    get_element(driver, ('id', 'firstname')).send_keys('hpface固定ipc测试')
    get_element(driver, ('id', 'lastname')).send_keys('123456')
    get_element(driver, ('xpath', "//button[@class='btn btn-primary']")).click()
    sleep(0.5)
    if get_element(driver, ('id', 'LAY_demo2')).text == '成功:订阅':
        pass
    else:
        bug_photo(driver)
        assert False
    driver.close()
    driver.switch_to_window(all_hand[0])


