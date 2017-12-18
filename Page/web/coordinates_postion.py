# -*- coding:utf-8 -*-
# author: cy
import win32gui
import win32api
from time import sleep
import win32clipboard as w
import win32con


def click_position(hwd, x_position, y_position):
    """
    鼠标左键点击指定坐标
    :param hwd:
    :param x_position:
    :param y_position:
    :return:
    """
    # 将两个16位的值连接成一个32位的地址坐标
    long_position = win32api.MAKELONG(x_position, y_position)
    # win32api.SendMessage(hwnd, win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP, long_position)
    # 点击左键
    win32api.SendMessage(hwd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    win32api.SendMessage(hwd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)


def getText():
    # 读取剪切板
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d


def setText(aString):
    # 写入剪切板
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString.encode(encoding='gbk'))
    w.CloseClipboard()


def input_content(hwd, content, is_enter):
    """
    从站贴板中查找输入的内容
    :param hwd:
    :param content:
    :param sleep:
    :param is_enter 是否要在最后输入enter键,内容与enter之间间隔一秒
    :return:
    """
    setText(content)
    sleep(0.3)
    click_keys(hwd, win32con.VK_CONTROL, 86)
    if is_enter:
        sleep(1)
        click_keys(hwd, win32con.VK_RETURN)


def click_keys(hwd, *args):
    """
    定义组合按键
    :param hwd:
    :param args:
    :return:
    """
    for arg in args:
        win32api.SendMessage(hwd, win32con.WM_KEYDOWN, arg, 0)
    for arg in args:
        win32api.SendMessage(hwd, win32con.WM_KEYUP, arg, 0)


