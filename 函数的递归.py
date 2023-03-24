# Python Learning Process
# Name:Ayanami_LJ
# Time:2023/3/16
import numpy as np
import matplotlib.pyplot as plt
'''
递归函数必须有明确的结束条件：递归出口
递归优点：
1.逻辑、定义简单明了
递归缺点：
1.容易导致栈溢出
'''

def jiecheng(x):
    sum=1
    for item in range(x+1):
        if item>0:
            sum*=item
            pass
        pass
    print(sum)
    pass

jiecheng(5)


#递归的方式求阶乘
def fac(x):
   if x==1:
       return 1
   else:
       return fac(x-1)*x

print(fac(5))


#os模块：文献操作模块
import os #引入文献操作模块
#递归案例：模拟实现树形结构的遍历
def find_file(file_Path):
    listRs=os.listdir(file_Path)  #得到该路径下面所有的文件夹
    for fileitem in listRs:
        full_path=os.path.join(file_Path,fileitem)#获取完整的文件路径
        if os.path.isdir(full_path):  # 判断是否是文件夹
            find_file(full_path)  # 如果是一个文件夹，再次去递归
            pass
        else:
            print(fileitem)
            pass
        pass
    else:
        return
    pass


#调用搜索文件对象
#先给一个文件路径
find_file('E:\\QQMusic')


print(os.getcwd())
path='E:\\pycharm'
print(os.listdir(path))








