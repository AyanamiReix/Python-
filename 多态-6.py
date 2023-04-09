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
多态概念:顾名思义，多种状态，多种形态，就是同一种行为 
即 对于不同的子类【对象】 有不同的行为表现
Python 多态语言

实现多态的必须具备的两个前提:
1.继承:多态必须发生在父类和子类之间
2.重写:子类重写父类的方法

'''

#案例演示

class Animal:
    '''
    父类【基类】
    '''
    def say_who(self):
        print('我是一个动物')
        pass
    pass


class Duck(Animal):
    '''
    鸭子类 【子类/派生类】
    '''
    def say_who(self):
        '''
        这里重写父类的方法
        :return:
        '''
        print('我是一只漂亮的鸭子')
        # super().say_who()
        pass
    def walk(self):
        pass
    pass


class Dog(Animal):
    '''
    狗类 【子类/派生类】
    '''
    def say_who(self):
        print('我是一只哈巴狗')
        pass
    def walk(self):
        pass
    pass


class Cat(Animal):
    '''
    猫类 【子类/派生类】
    '''

    def say_who(self):
        print('我是一只小喵喵')
        pass
    def walk(self):
        pass
    pass


class Bird(Animal):
    def say_who(self):
        print('我是一只黄鹂鸟')
        pass
    def walk(self):
        print('蹦蹦跳跳')
    pass


def commonInvoke(obj):
    '''
    统一调用方法
    :param obj: 对象的实例
    :return:
    '''
    obj.say_who()

    pass

# duck1=Duck()
# duck1.say_who()
# cat1=Cat()
# cat1.say_who()

listObj=[Duck(),Dog(),Cat(),Bird()]
for item in listObj:
    '''
    循环去调用函数
    '''
    commonInvoke(item)


'''
总结 
多态的好处:多态可以增加程序的灵活性 增加程序的扩展性
不用关注对象类型本身，而是多态的使用方法：say_who(self)
'''


class Human():
    def say_who(self):
        print('我是人')
        pass

    pass



class student(Human):
    def say_who(self):
        print('我是一年级的小朋友')
        pass
    pass

print('-------第二种多父情况下调用-------')
stu1=student()
stu1.say_who()
listObj2=[Bird(),student()]
for x in listObj2:
    commonInvoke(x)



