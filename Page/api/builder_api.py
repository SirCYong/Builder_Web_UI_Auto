# coding:utf-8
import datetime
import os
import random
import threading
import time
import requests
from Page.random_data import get_phone_number, get_people_name, \
    get_company_name, get_org_no, random_str
from Page.web.get_now_time import get_now_dates, get_now_time, get_future_date, get_pass_dates


def worker_register(ws_driver, mobile):
    print(mobile)
    phone_code_parameter = {
        "command": {
            "path": "employee.consumer.RegPhoneVerifyCode"
        },
        "parameters": {
            "username": mobile
        }
    }
    ws_driver.web_socket_request(phone_code_parameter)

    parameter = {
        "command": {
            "path": "employee.consumer.WorkerRegister"
        },
        "parameters": {
            "username": mobile,
            "password": "123456",
            "code": "11111"
        }
    }
    result = ws_driver.web_socket_request(parameter)
    print(result)
    assert result['code'] == 1000
    assert result['msg'] == '成功:注册'
    return mobile


def login(ws_driver, username, password):
    print(username)
    parameter = {
        "command": {
            "path": "employee.consumer.Login"
        },
        "parameters": {
            "username": username,
            "password": password
        }
    }
    result = ws_driver.web_socket_request(parameter)
    print(result['data']['sid'])
    assert result['msg'] == '成功:登录'
    assert result['code'] == 1000
    return result


def upload_file(id_card, result, url):
    http_parameter_face = {
        "command": "personalIdUpdate",
        "sid": result['data']['sid'],
        "type": ['imageface']
    }
    sys_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(sys_path, "1.jpg")
    files = {'img': ('1.jpg', open(file_path, 'rb'), 'image/jpeg')}
    add_url = 'http://' + url + '/upload_file/'

    http_parameter_back = {
        "command": "personalIdUpdate",
        "sid": result['data']['sid'],
        "type": ['imageback']
    }
    # thread.start_new_thread(requests.post(url=add_url, data=http_parameter_face, files=files))
    if id_card == 'face':
        t = time.time()
        a = requests.post(url=add_url, data=http_parameter_face, files=files)
        print(a.status_code)
        print(a.text)
        c = eval(a.text)
        assert c['msg'] == '成功'
        assert c['code'] == 1000
        print(time.time() - t)
    elif id_card == 'back':
        t = time.time()
        b = requests.post(url=add_url, data=http_parameter_back, files=files)
        print(b.status_code)
        print(b.text)
        c = eval(b.text)
        assert c['msg'] == '成功'
        assert c['code'] == 1000
        print(time.time() - t)
    else:
        print('input ERROR')


def employee_register(ws_driver, company_id, mobile=get_phone_number()):
    code_parameter = {
        "command": {
            "path": "employee.consumer.RegPhoneVerifyCode"
        },
        "parameters": {
            "username": mobile
        }
    }
    ws_driver.web_socket_request(code_parameter)
    real_name = get_people_name()
    phone_code_parameter = {
        "command": {
            "path": "employee.consumer.EmployeeRegister"
        },
        "parameters": {
            "username": mobile,
            "real_name": real_name,
            "password": "123456",
            "code": "11111",
            "company_id": company_id['data']['company_id'],
            "captcha_code": "tttt",
        }
    }
    result = ws_driver.web_socket_request(phone_code_parameter)
    assert result['code'] == 1000
    assert result['msg'] == '成功:公司职员注册'
    return result


def company_add(ws_driver, result):
    requestDict = {
        "command": {
            "path": "employer.consumer.CompanyAdd"
        },
        "parameters": {
            "sid": result['data']['sid'],
            "address_form": {
                "province": '浙江省'
            },
            "company_form": {
                "name": get_company_name(),
                "org_no": get_org_no(),
                "credit_no": random_str(18)
            }
        }
    }
    result = ws_driver.web_socket_request(requestDict)
    return result


def attendance_login(ws_driver):
    attendance_parameter = {
        "command": {
            "path": "project.consumer.AttendanceMachineAuthentication"
        },
        "parameters": {
            "attendance_machine_name": "hpface固定ipc测试",
            "secret_key": "123456"
        }
    }
    result = ws_driver.web_socket_request(attendance_parameter)
    return result


def attendance_instant_add(ws_driver, result, card_num):
    attendance_parameter = {
        "command": {
            "path": "project.consumer.AttendanceInstantAdd"
        },
        "parameters": {
            "attendance_instant_form": [
                {
                    "card_num": card_num,
                    "type": random.randint(1, 2),
                    "day": get_now_dates(),
                    "time": get_now_time()
                }
            ],
            "sid": result['data']['sid']
        }
    }
    result = ws_driver.web_socket_request(attendance_parameter)
    assert result['code'] == 1000
    assert result['msg'] == '成功:操作'


def attendance_card_list(ws_driver):
    parameter = {
        "command": {
            "path": "employer.consumer.AttendanceCardList"
        },
        "parameters": {
            "sid": 1
        }
    }
    result = ws_driver.web_socket_request(parameter)
    a = result['data']['attendace_cards']
    card_list = []
    for i in range(len(a)):
        card_list.insert(i, a[i]['ic_card_num'])
    return card_list


def workflow_process_create(ws_driver, sid, worker_id, number=1):
    # 签订用工合同
    if number:
        start_day = get_pass_dates(2)
    else:
        start_day = get_future_date(1)
    parameter = {
        "command": {
            "path": "workflow.consumer.ProcessCreate"
        },
        "parameters": {
            "sid": sid,
            "flow_name": "sign_worker_contract",

            "worker_contract": {
                "team_id": 1,
                "worktype_id": 1,
                "term_type": 1,  # 非固定期限
                "worker_id": worker_id,  # ** 单人**
                "start_day": start_day,
                "finish_day": get_future_date(300),
                "pay_day": 15,
                "morning_time_on_duty": "8:30",
                "morning_time_off_duty": "11:30",
                "afternoon_time_on_duty": "12:00",
                "afternoon_time_off_duty": "18:00",
                "payment_method": 1,
            },
            "work_time_pay": [{
                "time_unit": "小时",
                "pay_mount": 20,
            }]
        }
    }
    result = ws_driver.web_socket_request(parameter)
    assert result['msg'] == '成功'


def set_user_group(ws_driver, sid, user_id, group_name):
    # 给职员设置角色
    parameter = {
        "command":
            {
                "path": "employer.consumer.SetUserGroup"
            },
        "parameters":
            {
                "sid": sid,
                "user_id": [user_id],
                "group_name": group_name
            }
    }
    result = ws_driver.web_socket_request(parameter)
    print(result)


def company_list(ws_driver, sid):
    # 查询公司
    parameter = {
        "command":
            {
                "path": "employer.consumer.CompanyList"
            },
        "parameters":
            {
                "sid": sid}
    }
    result = ws_driver.web_socket_request(parameter)
    return result


if __name__ == '__main__':
    # mobile = get_phone_number()
    t = time.time()
    i = 1
    attendance_card_list()

    print(time.time() - t)
