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
多继承概念
'''

class Superman:
    def fly(self):
        print('超人会飞')
        pass
    pass


class Human():
    def __init__(self,height):
        self.height=height
        print('身高是%dcm'%self.height)


class qiqi(Superman,Human):
    pass

Qi=qiqi(158)
Qi.fly()

'''
问题是，当多个父类当中存在相同方法的时候，应该去调用哪一个类
'''

class D(object):
    def ptt(self):
        print('D.eat')
        pass
    pass

class C(D):
    def ptt(self):
        print('C.eat')
        pass
    pass

class B(D):
    pass


class A(B,C):
    pass

a=A()
a.ptt() #这边发现继承的是C的eat
print(A.__mro__)
'''
复盘 a.eat() (广度优先遍历)
首先到A里面查找，若A没有，则到B里面查找，
若B没有，则去C类中查找，若C没有，则去D，若还是没有，则报错
最终: A->B->C->D

多继承的顺序:
print(X.__mor__)
'''
class E(C,B):
    pass
print('------E的广度优先遍历为-------')
print(E.__mro__)

'''
间接节点继承
'''

class GrandFather():
    def eat(self):
        print('吃的方法')
        pass
    pass


class Father(GrandFather):
    def eat(self): #因为父类中已经存在这样的方法，在这里相当于方法覆盖了
        print('爸爸经常吃海鲜')
    pass

class Son(Father):
    pass


son=Son()
print(Son.__mro__)
son.eat() #此方法是从 GrandFather继承过来的


'''
重写和调用父类方法
重写父类的方法
子类中，有一个和父类相同名字的方法，子类中会覆盖
为什么要重写，父类的方法已经不满足子类的需要，那么子类就可以重写

'''
class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def bark(self):
        print('汪汪叫...')
        pass

    def __str__(self):
        return '{}的颜色是{}'.format(self.name,self.color)
    pass

class KeJi(Dog,A):
    def __init__(self,name,color):
        '''
        父类 Dog 同样有init函数，这时候如果调用父类 则会报错 因为被覆盖了
        针对这种诉求，我们有如下改进方法
        利用 Dog.__init__()
        '''
        # Dog.__init__(self,name,color)
        super().__init__(name,color) #super是自动找到父类，进而调用方法，上面是手动寻找
        #扩展其他属性
        self.height=90
        self.wegiht=20
        pass


    def bark(self):
        super().bark()
        print('喵喵叫')

    def ptt(self):
        '''
        这边是 super函数的调用顺序测试
        调用A后 同样符合广度优先遍历
        :return:
        '''
        super().ptt()

    pass

kj=KeJi('keji','red')
kj.bark()
print(kj.height)
print(kj)
print(kj.ptt())

