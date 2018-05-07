# -*- coding: utf-8 -*-
import socket
import subprocess
from time import sleep


def start_android_appium(device_name):
    """

    :param device_name:
    :type device_name:
    """
    try:
        if not _is_open('127.0.0.1', 4723):
            # cmd = "start /b appium -a 127.0.0.1 -p 4723" + " --command-timeout 600 --chromedriver-port 9519  --session-override"
            cmd = "start /b appium -a 127.0.0.1 -p 4723  -U " + device_name + " --command-timeout 600 --session-override"
            print(cmd)
            subprocess.call(cmd, shell=True, stdout=open('logs.log', 'w'), stderr=subprocess.STDOUT)
            sleep(5)
            print('开启appium服务成功\n')

        else:
            print('appium服务已开启，不需要开启\n')
            pass
    except Exception as e:
        print(e)


def start_ios_appium(udid):
    try:
        if not _is_open('127.0.0.1', 4723):
            cmd = "appium -a 127.0.0.1 -p 4723 -U " + udid + " --command-timeout 600 --session-override&"
            subprocess.call(cmd, shell=True, stdout=open('logs.log', 'w'), stderr=subprocess.STDOUT)
            sleep(5)
            print('开启appium服务成功\n')
        else:
            print('appium服务已开启，不需要开启\n')
    except Exception as e:
        print(e)


def _is_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        s.shutdown(2)
        return True
    except Exception as e:
        print(e)
        return False
