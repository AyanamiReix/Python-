# Python Learning Process
# Name:Ayanami_LJ
# Time:2023/3/16
import numpy as np
import matplotlib.pyplot as plt
#1.os模块导入
import os

'''
2.os.getcwd()
作用：获取当前的工作路径
'''
print(os.getcwd())

'''
3.os.listdir(path)
作用：传入任意一个path路径，
返回的是该路径下所有文件和目录组成的列表
'''
print('\n----------os.listdir()----------')
path=r'E:\pycharm\python学习以及srt\python 学习' #r来消除转义
print(os.listdir(path))


'''
4.os.walk(path)
含义 ：传入任意一个path路径，深层次遍历指定路径下的所有子文件夹，
返回的是一个由路径、文件夹列表、文件列表组成的元组。
'''
print('\n----------os.walk()----------\n')
path=r'E:\pycharm\pythonProject1'
for path,dirs,files in os.walk(path):
    print(path)
    print(dirs)
    print(files)
    print('\n')



'''
5.os.path.exists(path)
含义：传入一个path路径，判断指定路径下的目录是否存在。
存在返回True，否则返回False；
'''
print('-----------os.path.exists(path)------------')
path5=r'E:\pycharm\python学习以及srt\python 学习'
if os.path.exists(path5):
    print("exist")
    pass
else:
    print('unexist')
    pass

'''
6.os.mkdir(path)
含义：传入一个path路径，创建单层(单个)文件夹；
注意：如果文件夹已经存在，就会报错因此创建文件夹之前，
需要使用os.path.exists(path)函数判断文件夹是否存在；
'''
print('-----------os.mkdir(path)------------')
path6=r'E:\pycharm\python学习以及srt\python 学习\os模块2.py'
def creat_file(path):
    if os.path.exists(path)==False:
        print('指定文件不存在')
        os.mkdir(path)
    else:
        print('当前位置已存在文件夹，创建失败')
creat_file(path6)

'''
6.os.rmdir(path)
含义：传入一个path路径，删除指定路径下的文件夹；
注意：该方法只能删除空文件夹，删除非空文件夹会报错；
'''

# os.rmdir(r'E:\pycharm\python学习以及srt\python 学习\os模块2.py')


'''
8.os.path.join(path1,path2)
含义：传入两个path路径，将该路径拼接起来，形成一个新的完整路径；
'''
print('\n-----------os.path.join(path1,path2)----------')
path8=os.getcwd()
print(path8)

lis=['a.jpg']
for i in lis:
    path_x=os.path.join(path8,i)
    print(path_x)



'''
9.os.path.split(path)
含义：传入一个完整的path路径，将其拆分为绝对路径和文件名2部分；
'''
print('\n--------os.path.split(path)---------')
print(os.path.split(path_x))

'''
10.os.path.dirname(path)
含义：含义：传入一个完整的文件路径，只获取其绝对路径；
'''
print('\n--------os.path.dirname(path)---------')
print(os.path.dirname(path_x))



'''
11.os.path.basename(path)
含义：传入一个完整的文件路径，只获取其文件名；
'''
print('\n--------os.path.basename(path)---------')
print(os.path.basename(path_x))




'''
12.os.path.isdir(path)
含义：传入一个完整的文件路径，判断它是否是文件夹；
是返回True，不是返回False
'''
# def bianli_file(path_files):
#    '''
#    递归遍历路径下的所有文件夹，打印文件
#    :param path_files:
#    :return:
#    '''
#    listRs=os.listdir(path_files) #获取当前路径下所有文件夹
#    for files in listRs:
#        full_path=os.path.join(path_files,files)
#        if os.path.isdir(full_path)==True:
#            bianli_file(full_path)
#            pass
#        else:
#            print(full_path)
#            pass
#        pass
#    else:
#        return
#    pass
#
#
# bianli_file('E:\\QQMusic')
#


'''
13.os.path.isfile(path)
含义：传入一个完整的文件路径，判断它是否是文件；
是返回True，不是返回False
'''
print('\n--------os.path.isfile(path)-------------')
path13=os.getcwd()
listRs=os.listdir(path13)
for files in listRs:
    if os.path.isfile(files):
        print(files)
        pass
    pass

'''
14.os.path.sep
含义：返回当前操作系统的路径分隔符
'''
os.path.sep
print(os.path.sep)



'''
15.os.path.getsize(path)
含义：传入一个完整的文件路径，返回该文件的大小
'''

path15=os.getcwd()
print(os.path.getsize(path15))