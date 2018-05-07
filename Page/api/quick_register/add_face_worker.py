import getpass
import random
import threading
import unittest
import time
from configparser import ConfigParser
from websocket import create_connection
from Page.api.BuilderBaseFunc import BuilderBaseFunc
from Page.api.builder_api import worker_register, login, upload_file, company_add, employee_register, attendance_login, \
    attendance_instant_add, attendance_card_list, workflow_process_create
from Page.api.quick_register.attendance_machine_quick_register import quick_register
from Page.api.quick_register.random_face_eigenvalues import random_face_eigenvalues
from Page.random_data import get_phone_number, getDistrictCode, get_people_name
from Page.web.get_now_time import get_now_dates, get_pass_dates
from run_path import setting_path, file_path


class AddFaceWorker(unittest.TestCase):
    def setUp(self):
        config = ConfigParser()
        self.path = setting_path()
        self.file_path = file_path('1')
        config.read(self.path)
        ws_url = config.get('testUrl', 'ws_test_url')
        ws = create_connection("ws://%s/wsapi" % ws_url)
        self.ws_driver = BuilderBaseFunc(ws, ws_url)
        self.username = config.get('labor', 'Wuhuigang')
        self.number = 800  # 默认次数
        pass

    def tearDown(self):
        pass

    def test_add_face_worker(self):
        pwd = 123456
        sid = login(self.ws_driver, self.username, pwd)
        i = 0
        while True:
            identity_number = getDistrictCode()
            name = get_people_name()
            sex_str = "男女"
            sex = random.choice(sex_str)
            birthday = get_pass_dates(random.randint(7500, 25550))
            overdue = '2008/08/15-2020/08/15'
            mobile = get_phone_number()
            print(mobile)
            characteristic_value = random_face_eigenvalues()
            user = quick_register(self.ws_driver, sid['data']['sid'], identity_number, name, sex, birthday, overdue, self.file_path, self.file_path, mobile, characteristic_value)
            workflow_process_create(self.ws_driver, sid['data']['sid'], user['data']['user_id'])
            i += 1
            if i > self.number:
                break
            else:
                pass



