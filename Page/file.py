# encoding: utf-8
# from time import sleep
import getpass
import shutil
import os


# BeginPath = r"C:\Users\CY\Desktop\lfw"  # 指明被遍历的文件夹
# PurposePath = r"C:\Users\CY\Desktop\new"    # 转换到的文件夹
# count = 0
# path = None
# 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
# for parent, dirNames, fileNames in os.walk(BeginPath):
#     for filename in fileNames:  # 输出文件信息
#         print("path is: " + parent)
#         print("文件名 is: " + filename)
#         count += 1
#         print(count)
#         print("文件路径信息is: " + os.path.join(parent, filename))  # 输出文件路径信息
#         path = os.path.join(parent, filename)
#         print (path)
        # a = parent + '/' + dirName + '/' + filename
        # shutil.copy(path, PurposePath + '\\' + str(count) + '.jpg')

pc_name = getpass.getuser()
BeginPath = r"C:\Users\%s\Desktop" % (str(pc_name))  # 指明被遍历的文件夹
PurposePath = r"C:\Users\%s\Desktop\new"    # 转换到的文件夹
if os.path.exists(PurposePath) is False:    # 有这个目录就没事，没有就增加
    os.makedirs(PurposePath)
file_path = os.path.dirname(os.path.abspath(__file__))  # 当前路径
dir_path = os.path.join(BeginPath, 'lfw')

print(dir_path)
dirs = os.listdir(dir_path)
print(dirs)
Cnt = 0

for Dir in dirs:
    print(Dir)
    dirPath = os.path.join(dir_path, Dir)
    print('DirPath' + dirPath)
    files = os.listdir(os.path.join(dir_path, Dir))
    print(files)
    for file in files:
        Cnt += 1
        print(os.path.join(BeginPath, str(Cnt)+'.jpg'))
        os.rename(os.path.join(dirPath, file), os.path.join(PurposePath, str(Cnt) + '.jpg'))
