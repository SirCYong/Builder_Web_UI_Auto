# -*- coding: utf-8 -*-
import os
import random
from faker import Factory

from run_path import test_report_path

fake = Factory().create('zh_CN')
print(fake.phone_number())
print(fake.name())
print(fake.address())
print(fake.email())
report = os.path.join(test_report_path(), '59017-12工资单.xls')
os.remove(report)