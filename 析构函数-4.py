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
1.析构方法
2.单继承
3.多继承
4.继承的传递
5.重写父类方法
6.调用父类方法
7.多态
8.类属性和实例属性
9.类方法和静态方法

重点：
类的继承
父类的调用
静态方法

难点：
继承与重写
静态方法

'''


'''
析构方法/魔术方法

'''

class Animal:
    def __init__(self,name):
        self.name=name
        print('init被调用')
        pass


    def __del__(self):#就算不写程序也会自动调用
        '''
        当在某个作用域下面 没有被引用的情况下
        解析器会自动调用此函数，来释放内存
        主要应用就是来 操作对象的释放 一旦释放完毕，对象不能再使用
        :return:
        '''
        print('del函数被调用')
        pass
    pass

cat=Animal('cat')




'''
#第一种情况 直接运行
cat=Animal('cat')

#第二种情况 input介入
cat=Animal('cat')
input('程序等待中') #输入后才会调用__del__

#第三种情况:手动删除
cat=Animal('cat')
del cat   #手动删除对象
input('程序等待中') #输入后才会调用__del__

'''




'''
在python中展现面向对象的三大特征：
封装、继承、多态
封装：指的是把内容封装到某个地方，便于后面的使用
需要：把内容封装到某个地方，从另外一个地方去调用被封装内容
对于封装来说，其实就是使用初始化构造方法将内容封装到对象中，
然后通过对象直接或self来获取被封住的内容

继承：和现实中的继承一样， 子可以继承父的内容【属性和行为】
'''

class Animal:
    def eat(self):
        print('吃猫粮呀')
        pass
    def drink(self):
        print('喝suisui')
    pass


class dog(Animal): #继承了Animal父类 此时dog就是子类
    def wwj(self):
        print('狗叫')
        pass
    pass

class cat(Animal):
    def mmj(self):
        print('喵~')
        pass
    pass

d1=dog()
d1.eat() #这是Animal的能力，继承了父的行为

print('------------cat的行为---------------')
c1=cat()
c1.drink()


