#coding:utf-8
import os
from time import sleep

import shutil

file_path = os.path.dirname(os.path.abspath(__file__))
BeginPath = r"C:\Users\CY\Desktop\lfw"  # 指明被遍历的文件夹
PurposePath = r"C:\Users\CY\Desktop\new"    # 转换到的文件夹夹
count = 0
# path = None
# 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
for parent, dirNames, fileNames in os.walk(BeginPath):
    # for dirName in dirNames:  # 输出文件夹信息
    #     print("path is: " + parent)
    #     print("子目录 is: " + dirName)
    for filename in fileNames:  # 输出文件信息
        print("path is: " + parent)
        print("文件名 is: " + filename)
        sleep(0.1)
        count += 1
        print(count)
        print("文件路径信息is: " + os.path.join(parent, filename))  # 输出文件路径信息
        path = os.path.join(parent, filename)
        shutil.copy(path, PurposePath + '\\' + str(count) + '.jpg')
        # os.rename(path, PurposePath)