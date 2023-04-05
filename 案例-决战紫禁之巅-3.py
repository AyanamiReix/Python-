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

问题分析
决战紫禁之巅有两个人物，小罗和小琪
属性：1.玩家的名字 2.玩家的血量
方法：
   normal attack()
   thump()
   resume()
   __str__显示玩家状态
'''

class Role():
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp


    def normal_attack(self,enemy):
        '''

        普通攻击：对方 hp-10
        :param enemy:敌人
        :return:
        '''
        enemy.hp-=10
        info = '%s对%s发起了普通攻击' % (self.name, enemy.name)
        print(info)
        pass


    def thump(self,enemy):
        '''

        重击：对方 hp-15
        :param enemy:敌人
        :return:
        '''
        enemy.hp -= 15
        info='%s对%s发起了重击'%(self.name,enemy.name)
        print(info)
        pass

    def recover(self):
        '''
        恢复：自身 hp+10
        :return:
        '''
        self.hp+=10
        info = '%s吃药，补了10滴血' % (self.name)
        print(info)
        pass

    def __str__(self):
        return 'Name:%s  HP:%s'%(self.name,self.hp)
    pass

#创建两个实例化对象

Jie=Role('罗爹大坏蛋',100)
Qi=Role('可怜的群友宝宝',100)

#while 循环
import time #导入时间函数库
while True:
    if Qi.hp<=0 or Jie.hp<=0:
        #满足条件退出循环
        if Qi.hp <= 0:
            print('%s死了，是个 菜鸡'%Qi.name)
            pass
            break
        else:
            print('%s死了，是个 菜鸡', Jie.name)
            break
            pass
        pass
    Jie.normal_attack(Qi)
    print(Jie)
    print(Qi)
    print('-----------------------')
    time.sleep(1)
    Jie.thump(Qi)
    print(Jie)
    print(Qi)
    print('-----------------------')
    time.sleep(1)
    Qi.recover()
    print(Jie)
    print(Qi)
    time.sleep(1)
    pass
print('对战结束')

