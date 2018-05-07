# -*- coding: utf-8 -*-
import os
import re
import subprocess
from time import sleep


def stop_android_appium():
    """

    """
    try:
        cmd = 'taskkill /F /IM node.exe'
        os.popen(cmd)
        print('appium服务关闭')
    except Exception as e:
        print(e)


def stop_ios_appium():
    try:
        for pid in _get_pid_list():
            cmd = "kill " + pid
            subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
    except Exception as e:
        print(e)


def _get_pid_list():
    try:
        cmd = 'lsof -i:4723'
        result = exec_cmd(cmd)
        pid_list = []
        for i in range(len(result)):
            for r in re.findall("node.*?IP", result[i]):
                b = []
                for s in r.split(' '):
                    if s != '':
                        b.append(s)
                pid_list.append(b[1])
        return pid_list
    except Exception as e:
        print(e)
        return []


def exec_cmd(cmd):
    """

    :param cmd:
    :type cmd:
    :return:
    :rtype:
    """
    try:
        r = os.popen(cmd)
        sleep(1)
        result = r.readlines()
        r.close()
        return result
    except Exception as e:
        print(e)


