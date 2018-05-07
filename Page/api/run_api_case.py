import getpass
import random
import threading
import unittest
import time
from configparser import ConfigParser
from multiprocessing import Process

from websocket import create_connection

from Page.api.BuilderBaseFunc import BuilderBaseFunc
from Page.api.builder_api import worker_register, login, upload_file, company_add, employee_register, attendance_login, \
    attendance_instant_add, attendance_card_list
from Page.random_data import get_phone_number
from run_path import setting_path


class run_all_api_case(unittest.TestCase):
    def setUp(self):
        config = ConfigParser()
        self.path = setting_path()
        self.file_path = r'C:\Users\%s\Desktop\UIAutotest\Page\file\1.jpg' % (str(getpass.getuser()))
        config.read(self.path)
        ws_url = config.get('testUrl', 'ws_test_url')
        ws = create_connection("ws://%s/wsapi" % ws_url)
        self.ws_driver = BuilderBaseFunc(ws, ws_url)
        self.mobile = get_phone_number()
        self.number = 30  # 默认次数
        self.i = 1
        self.operation = 18888888888
        pass

    def tearDown(self):
        pass

    def test_worker_register(self):
        t = time.time()
        # 多线程
        # while 1:
        #     one = threading.Thread(target=worker_register, args=self.mobile)
        #     one.start()
        #     one.join()
        #     i += 1
        #     if i > number:
        #         break
        # 多进程
        while True:
            p1 = Process(target=worker_register, args=(self.ws_driver, get_phone_number(),))
            p2 = Process(target=worker_register, args=(self.ws_driver, get_phone_number(),))
            p3 = Process(target=worker_register, args=(self.ws_driver, get_phone_number(),))
            p4 = Process(target=worker_register, args=(self.ws_driver, get_phone_number(),))
            p1.start()
            p2.start()
            p3.start()
            p4.start()
            p1.join()
            p2.join()
            p3.join()
            p4.join()

            self.i += 1
            if self.i > self.number:
                break
        print(time.time() - t)

    def test_upload_file(self):
        while True:
            mobile = get_phone_number()
            sid = login(self.ws_driver, worker_register(self.ws_driver, mobile))
            p1 = Process(target=upload_file, args=('back', sid))
            p2 = Process(target=upload_file, args=('face', sid))
            p1.start()
            p2.start()
            p1.join()
            p2.join()
            self.i += 1
            if self.i > self.number:
                break

    def test_employee_register(self):
        sid = login(self.operation)
        new_company_id = company_add(sid)
        t = time.time()
        while True:
            p1 = Process(target=employee_register, args=(new_company_id,))
            p2 = Process(target=employee_register, args=(new_company_id,))
            p3 = Process(target=employee_register, args=(new_company_id,))
            p4 = Process(target=employee_register, args=(new_company_id,))
            p1.start()
            p2.start()
            p3.start()
            p4.start()
            p1.join()
            p2.join()
            p3.join()
            p4.join()
            self.i += 1
            if self.i > self.number:
                break
        print(time.time() - t)

    def test_attendance_instant_add(self):
        attendance_dict = attendance_login()
        card_list = attendance_card_list()
        random.choice(card_list)
        t = time.time()
        while True:
            p1 = Process(target=attendance_instant_add, args=(attendance_dict, card_list[0]))
            p2 = Process(target=attendance_instant_add, args=(attendance_dict, card_list[1]))
            p3 = Process(target=attendance_instant_add, args=(attendance_dict, card_list[2]))
            p4 = Process(target=attendance_instant_add, args=(attendance_dict, card_list[3]))
            p1.start()
            p1.join()
            p2.start()
            p3.start()
            p4.start()

            p2.join()
            p3.join()
            p4.join()
            self.i += 1
            if self.i > self.number:
                break
        print(time.time() - t)


