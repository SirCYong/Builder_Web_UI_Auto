# -*- coding: utf-8 -*-
import getpass
import sys
sys_path = r'C:\Users\%s\Desktop\builder_webui_autotest' % (str(getpass.getuser()))
sys.path.append(sys_path)
# sys.path.append(r'C:\Users\CY\Desktop\builder_webui_autotest')
import random
import pymysql.cursors
import time
from Page.random_time import Type
from Page.web.get_now_time import get_pass_dates, get_now_dates

fmt = '%Y-%m-%d %H:%M:%S'  # 格式化时间
begin_time = get_now_dates() + " 00:00:01"  # 当前日期初始时间
end_time = get_now_dates() + " 23:59:59"  # 当前日期结束时间
now_time = time.strftime(fmt, time.localtime())  # 当前时间
# 将其转换为时间数组
timeArray_begin = time.strptime(begin_time, fmt)
# timeArray_end = time.strptime(end_time, fmt)
# timeArray_now = time.strptime(now_time, fmt)

# 转换为时间戳:
timeStamp_begin = int(time.mktime(timeArray_begin))
# timeStamp_end = int(time.mktime(timeArray_end))
# timeStamp_now = int(time.mktime(timeArray_now))
# timeStamp_end - timeStamp_now # 不能大于当前时间戳
# one = timeStamp_begin + random.randint(28800, 34200)
# two = timeStamp_begin + random.randint(41400, 43200)
# three = timeStamp_begin + random.randint(46800, 48600)
# four = timeStamp_begin + random.randint(64800, 79200)
# otherStyleTime = time.strftime("%H:%M:%S", time.localtime(one))
conn = pymysql.connect(
    host='mongodb.zldhz.com',
    user='zldtest',
    password='Khfdf*7123gdUIUYf',
    port=3306,
    database='zldtest',
    cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
number = 4  # 增加几次考勤
all_user_sql = "select *  from auth_user_groups a where a.group_id in (9, 6, 5, 4, 8)"
cur.execute(all_user_sql)
rel = cur.fetchall()
h = 0
for user in rel:
    print(user)
    for i in range(number):
        change_time = time.strftime("%H:%M:%S", time.localtime(timeStamp_begin + random.randint(28800, 34200))), \
                      time.strftime("%H:%M:%S", time.localtime(timeStamp_begin + random.randint(41400, 43200))), \
                      time.strftime("%H:%M:%S", time.localtime(timeStamp_begin + random.randint(46800, 48600))), \
                      time.strftime("%H:%M:%S", time.localtime(timeStamp_begin + random.randint(64800, 79200)))
        sql = "insert into " \
              "project_attendanceinstant" \
              "(day, time, type, longitude,latitude,capture_image,screen_image,attendance_machine_id, user_id, operator_id )" \
              "VALUES ('%s','%s','%s', '', '', '', '',1,'%s', NULL)" % \
              (get_now_dates(), change_time[i], Type(i), user['user_id'])
        print(sql)
        try:
            cur.execute(sql)
        except Exception as e:
            h += 1
            print('有' + str(h) + '条数据插入失败')
            print(e)
            pass
        conn.commit()
conn.close()
