# -*- coding: utf-8-*-
# auth cy
import getpass
import unittest
import sys
from BeautifulReport import BeautifulReport
sys_path = r'C:\Users\%s\Desktop\builder_webui_autotest' % (str(getpass.getuser()))
sys.path.append(sys_path)
from configparser import ConfigParser
from Page.web.get_now_time import get_now_dates
from Page.web.send_mail import send_mail
from run_path import run_path, test_report_path, setting_path


class RunAllCase(unittest.TestCase):
    def setUp(self):
        self.case_path = run_path()  # 测试用例的路径
        self.report_path = test_report_path()  # 报告存放路径
        print(self.report_path, '\n', self.case_path)

    def tearDown(self):
        pass

    def test_run_all_case(self):
        print(self.case_path)
        discover = unittest.defaultTestLoader.discover(self.case_path, "test_*", top_level_dir=None)
        print(discover)
        result = BeautifulReport(discover)
        a = result.report(filename='测试报告', description='执行测试报告', log_path=self.report_path)
        if a is None:
            config = ConfigParser()
            config.read(setting_path())
            mail_to_list = {config.get('mail', 'to_list'), config.get('mail', 'to_list1'),
                            config.get('mail', 'to_list2')}  # 收件人(列表)
            # mail_to_list = [config.get('mail', 'to_list')]  # 收件人(列表)
            mail_title = str(get_now_dates()) + 'WebUI测试报告'
            for i in range(1):  # 发送1封，填写1 就是list中的人，每人发一封
                if send_mail(mail_to_list, mail_title, 'Please check the attachment.', config.get('mail', 'user'),
                             config.get('mail', 'pass')):  # 邮件主题和邮件内容
                    print("done!")
                else:
                    print("failed!")
        else:
            pass
