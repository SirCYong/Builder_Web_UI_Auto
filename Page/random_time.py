import datetime
import os
import random
import time

import pymysql
from sshtunnel import SSHTunnelForwarder


# def gen_dates(bdate, days):
#     day = datetime.timedelta(days=1)
#     print(day)
#     for i in range(days):
#         yield bdate + day * i
    # today = datetime.date.today()
    # print(today)
    # return today


def Hours():
    time = random.randint(1, 1000)
    print(time)
    #   小时
    hours = time % 24
    print(hours)
    return hours


def Minute():
    time = random.randint(1, 1000)
    #   分
    minute = time % 60
    print(minute)
    return minute


def Second():
    #   秒
    second = random.randint(1, 800) % 60
    print(second)
    return second


def Type():
    # 进出
    my_type = random.randint(4, 5) % 3
    return my_type


def get_user_id(db):
    server = SSHTunnelForwarder(
        ssh_address_or_host=('dev.zlddata.cn', 22),  # 指定ssh登录的跳转机的address
        ssh_username='root',  # 跳转机的用户
        ssh_password='Hdfds*&2156gda',  # 跳转机的密码
        remote_bind_address=('127.0.0.1', 3306))
    server.start()
    myConfig = pymysql.connect(
        user="root",
        passwd="Hkdff*79231lgfj",
        host="127.0.0.1",
        db=db,
        port=server.local_bind_port)
    sql = "select user_id from employee_worker"
    cursor = myConfig.cursor()
    cursor.execute(sql)
    #  使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    sum_user_id = len(data)
    print("总共 '%d'人" % sum_user_id)
    cursor.close()
    return sum_user_id


def get_time():
    start_time = 0*60*60
    # while start_time < 23*60*60:
    start_time = start_time + random.randint(60, 3600)
    a = time.localtime(start_time)
    change_time = time.strftime("%H:%M:%S", a)
    # if int(time.strftime("%H", a)) == 23 and int(time.strftime("%M", a)) >= 30:
    return change_time


def user_sql(db,my_sql):
    server = SSHTunnelForwarder(
        ssh_address_or_host=('dev.zlddata.cn', 22),  # 指定ssh登录的跳转机的address
        ssh_username='root',  # 跳转机的用户
        ssh_password='Hdfds*&2156gda',  # 跳转机的密码
        remote_bind_address=('127.0.0.1', 3306))
    server.start()
    myConfig = pymysql.connect(
        user="root",
        passwd="Hkdff*79231lgfj",
        host="127.0.0.1",
        db=db,
        port=server.local_bind_port)
    sql = my_sql
    cursor = myConfig.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    cursor.close()


def connect_mysql(username, password, host, data_base, port):
    server = SSHTunnelForwarder(
        ssh_address_or_host=('dev.zlddata.cn', 22),  # 指定ssh登录的跳转机的address
        ssh_username='root',  # 跳转机的用户
        ssh_password='Hdfds*&2156gda',  # 跳转机的密码
        remote_bind_address=('127.0.0.1', 3306))
    server.start()
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    con = pymysql.connect(username, password, host, data_base, port)
    curs = con.cursor()
    return con, curs


def close_mysql(con, curs):
    curs.close()
    con.close()


def zldtest():
    con, curs = connect_mysql('root', 'Hkdff*79231lgfj', '127.0.0.1', 'zldtest', 'server.local_bind_port')
    return con, curs


def perftest():
    con, curs = connect_mysql('root', 'Hkdff*79231lgfj', '127.0.0.1', 'perftest', 'server.local_bind_port')
    return con, curs

if __name__ == '__main__':
    db = 'perftest'
    sql = """select * from workflow_request"""
    # user_sql(db, sql)
    # get_time()
    Type()