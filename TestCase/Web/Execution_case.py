# -*- coding: utf-8-*-
# auth cy
import unittest

from Page.web import HTMLTestRunner_screenshot
from run_path import run_path, test_report_path

case_path = run_path()  # 测试用例的路径
report_path = test_report_path()  # 报告存放路径
print(report_path, '\n', case_path)

if __name__ == "__main__":
    discover = unittest.defaultTestLoader.discover(case_path, "test_*.py", top_level_dir=None)
    print(discover)
    run = HTMLTestRunner_screenshot.HTMLTestRunner(title="测试报告",
                                                   description="测试用例参考",
                                                   stream=open(report_path + "\\result.html", "wb"),
                                                   verbosity=2,
                                                   retry=0)
    run.run(discover)
