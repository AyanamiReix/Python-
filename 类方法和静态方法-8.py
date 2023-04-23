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

class People:
    country='us'
    '''
    类方法 用classmethod 来及逆行修饰
    '''
    @classmethod
    def get_country(cls):
        return cls.country #访问类属性
        pass

    @classmethod
    def change_country(cls,data):
        cls.country=data
        pass
    pass


print(People.get_country()) #通过类对象去引用
p=People()
print('实例对象访问 %s'%(p.get_country()))
People.change_country('uk')
print('------------修改之后的数据--------------')
print(People.get_country())




'''
静态方法的概念
类对象所拥有的方法 @staticmethod
为什么要使用静态方法：
静态方法主要存放逻辑性的代码，本身和类以及实例对象没有交互，
也就是说，在静态方法中，不会涉及到类中方法和属性的操作

好处：数据资源能够得到有效的充分利用
'''


print('----------静态方法-------------')
class Fish():
    color='red'
    @staticmethod
    def getdata():
        return Fish.color
    pass

print(Fish.getdata())

fish=Fish()
print(fish.getdata()) #注：一般情况下，我们不会通过实例对象去访问静态方法


#demo 返回当前的系统时间
import  time #引入第三方时间模块
class TimetesT():
    def __init__(self,hour,min,second):
        self.hour=hour
        self.min=min
        self.second=second

    @staticmethod
    def add(x,y):
        return x+y

    @staticmethod
    def showtime():
        return  time.strftime('%H:%M:%S',time.localtime())
    pass

print(TimetesT.showtime())
print(TimetesT.add(1,2))

'''
方法定义的形式可以看出来
1.类方法的第一个参数是类对象cls 进而去引用类对象的属性和方法
用@classmethod修饰
2.实例方法的第一个参数必须是self，通过这个self可以与引用类属性或是类属性，实例属性的优先级最高
3.静态方法不需要定义额外的参数，若要引用属性的话，则可以通过类对象或实例对象引用即可
用@staticmethod修饰
'''


