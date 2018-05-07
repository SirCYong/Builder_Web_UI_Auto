#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/24 10:46
# @Author  : Py.qi
# @File    : yield_xiecheng.py
# @Software: PyCharm
import re


def consumer(name):
    print('开始吃包子...')
    while True:
        print('\033[31;1m[consumer]%s需要包子\033[0m' % name)
        bone = yield   # 接收send发送的数据
        print('\033[31;1m[%s]吃了%s个包子\033[0m' % (name, bone))


def producer(obj1):
    obj1.send(None)   # 必须先发送None
    for i in range(3):
        print('\033[32;1m[producer]\033[0m正在做%s个包子'% i)
        obj1.send(i)


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


def deco(func):
    def wrapper():
        res = func()
        next(res)
        return res
    return wrapper


@deco
def foo():
    food_list = []
    while True:
        food = yield   #返回添加food的列表
        food_list.append(food)
        print(food_list)
        print("elements in foodlist are:",food)
if __name__ == '__main__':
    # con1 = consumer('消费者A')  # 创建消费者对象
    # producer(consumer('消费者A'))
    # for i in range(10):
    #     print(i)
    # h = 0
    # while h < 10:
    #     print(list(range(1, 8)))
    #     h += 1
    g = foo()
    print(g.send('苹果'))
    print(g.send('大力'))
    nes = [[1, 2], [3], [4, 5]]
    for num in flatten(nes):
        print(num)
