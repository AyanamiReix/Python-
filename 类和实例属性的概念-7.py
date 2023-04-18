# Python Learning Process
# Name:Ayanami_LJ
# Time:2023/3/16
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import math
from scipy import stats
import random

'''
类属性就是类对象所拥有的属性
'''

class Student:
    name='Aya' #属于类属性  student类对象所拥有的
    num=13
    def __init__(self,age,name):
        self.age=age
        self.name=name#实例属性
        pass
    pass



lm=Student(18,'K')
print(lm.name)  #通过实例对象去访问类属性
print(lm.age)
print('--------通过类对象Student去访问 name------------')
print(Student.name)
# print(Student.age) #这边会报错
'''
小结：
类属性可以被类对象和实例对象共同访问使用
实例属性只能由实例对象所访问,当实例属性和类属性同时存在，优先选择/输出实例属性
'''

lm.num=7 #通过实例对象，对类属性进行修改，可以吗？不可以！！
print(lm.num)
print('---------xh的num-----------')
xh=Student(28,'H')
print(xh.num)  #可以发现并没有修改

#正确修改类属性方法:通过类对象去修改
print('---------类对象修改后----------')
Student.num=20
print(xh.num)