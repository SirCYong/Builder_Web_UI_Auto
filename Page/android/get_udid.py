# -*- coding: utf-8 -*-
from Page.android.stop_appium import exec_cmd


def get_android_udid():
    """

    :return:
    :rtype:
    """
    try:
        cmd = 'adb devices'
        result = exec_cmd(cmd)
        a = result[1].split('\t')
        return a[0]
    except Exception as e:
        print(e)

        return False


def get_ios_udid():
    """

    :rtype:
    :return:
    :rtype:
    """
    try:
        result = exec_cmd('system_profiler SPUSBDataType | grep "Serial Number:.*" | sed s#".*Serial Number: "##')
        udid = result[len(result)-1]
        udid = udid[:udid.find('\n')]
        return udid
    except Exception as e:
        print(e)
        return False


def get_android_version():
    try:
        cmd = 'adb shell getprop ro.build.version.release'
        result = exec_cmd(cmd)
        a = result[0].split('\t')
        return a[0][:3]
    except Exception as e:
        print(e)
        return False


def android_7_uninstall():
    try:
        cmd = 'adb uninstall io.appium.android.ime'
        exec_cmd(cmd)
    except Exception as e:
        print(e)
        return False
if __name__ == '__main__':
    a = get_android_version()
    print(a)
    print(type(a))