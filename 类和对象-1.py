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
面向对象编程:oop[object oriented progarmming] 是一种python的编程思路
面向过程：按照业务逻辑写代码
类结构：
1.类名
2.属性：一组数据
3.行为：允许对进行操作的方法

class 类名:(建议大头命名法)
      属性
      方法
定义类和对象：

'''

class Human:
    '''
    对应人的特征
    '''
    name='aya' #类属性
    age=20
    '''
    对应人的行为
    '''
    def __init__(self):
        self.name1='ayanami' #实例属性
    def eat(self):
        print('文静地')
        pass
    def face(self):
        print('beautiful')
        pass
    pass

#创建一个对象[类的实例化]
ayanam=Human()
ayanam.eat() #调用函数
ayanam.face()
print(ayanam.name)

'''
实例方法:在类的内部，使用def关键字来定义，
第一个默认参数是self（名字可以是其他的名字，但位置必须被占用）
实例方法是归于 类的实例所有 

'''

class person:
    def eat(self):
        print('傻狗')
        pass
    pass

xq=person()
xq.name='xqq'
xq.sex='female'
print('{}的性别是{}'.format(xq.name,xq.sex))

#改进方法
class person2:
    def __init__(self):
        '''
        统一声明实例属性
        __init__在创建新类的时候默认被调用（自动执行）
        '''
        self.name='汪琪'
        self.sex='female'
        self.age=20
        pass

xq=person2()
print(xq.name)

'''
__init__传参
如果只是默认调用，那么每次被调用时创建的对象属性都一样，所以我们可以传属性参数
def __init__(self，feature1,feature2,...):
'''

class person3:
    '''
            传多个属性，使类更通用
            :param name:
            :param sex:
            :param age:
            '''
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age

        pass
    def eat(self,food):
        print(self.name+'喜欢吃'+food)
    pass
print('------------传多个属性参数------------')
qq=person3('汪琪','female','22')
print(qq.name,qq.sex,qq.age)
qq.eat('好吃的')

'''
总结 __init__
1.python 自带的内置函数 魔术方法
2.是一个初始化的方法，用来定义实例属性和初始化数据，创建对象时自动调用
3.运用传参的机制可以让我们定义功能更加方便
'''






