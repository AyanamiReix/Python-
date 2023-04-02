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
理解self
1.self和对象指向同一个内存地址，可以认为self就是对象的引用
'''
class Person():
    def __init__(self,hobby):
        self.hobby=hobby  #实例属性定义
        pass
    '''
    定义类
    '''
    def eat(self,name,food):
        '''
            实例方法
            :return
            '''
        print('self=%s'%(id(self)))
        print('%s 喜欢吃 %s,兴趣爱好是 %s'%(name,food,self.hobby))
        pass
    pass

xw=Person('playing games')  #调用的init方法
print('xw=%s'%(id(xw)))
xw.eat('xw','橘子')
print(xw) #直接输出对象，只打印对象的地址信息

#小结 self 特点
#self只有在类中有定义 实例方法的时候才有意义，调用的时候不必传入相应的参数，由解释器自动去指向
#self 名称是可以更改的
#self 指的是 类实例对象本身


'''
魔术方法：
定义：python中内置好的特定方法，一般形式为__xx__
常见的魔术方法
__str__
__new__
__class__
...

'''


#__str__:直接打印对象，输出结果只一串类似id地址的信息


print('-----------Animal()---------------')
class Animal():
    def __init__(self,name,color):
        self.name=name
        self.color=color
        print('---------init函数执行------------')
        pass
    def __str__(self):
        '''

        打印对象 自定义对象的内容格式
        :return:
        '''
        return '%s喜欢的颜色是%s'%(self.name,self.color)
    def __new__(cls, *args, **kwargs):
        '''
        创建对象实例的方法 每调用一次 就会生成一个新的对象 cls是class的缩写
        使用场景：可以控制创建对象的一些属性限定，经常用来做单例模式的时候来使用
        :param args:
        :param kwargs:
        比如有 return object.__new__(cls)
        '''
        print('-----new函数的执行-------')
        return object.__new__(cls) #是真正创建对象实例的
        pass


xiaojie=Animal('小宝','白色')
print(xiaojie)

'''
__new__和__init__的区别
1.__new__类的实例化方法，必须要返回该实例，否则对象就创建不成功
2.__init__用来做数据属性的初始化工作，也可以认为是实例的构造方法，
接受类的实例self 并对其进行构造
3.__new__至少有一个参数是cls 代表要实例化的类，此参数在实例化时由python解释器自动提供
4.__new__函数执行要早于__init__
'''




class Fruit:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        pass

    def __str__(self):
        return '%s的颜色是%s'%(self.name,self.color)
    pass



pg=Fruit('苹果','red')
print(pg)



#证明self就是实例对象本身
class Person:
    def weight(self):
        print(id(self))
        pass
    def __str__(self):
        return
    pass

lm=Person()
print(id(lm))
lm.weight()
print('-------------')



