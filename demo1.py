# Python Learning Process
# Name:Ayanami_LJ
# Time:2023/3/16
import random

import numpy as np
import matplotlib.pyplot as plt

#逻辑运算符
a,b,c,d=23,10,18,15
print(a+b>c and a==24)
print(a+b>c or a==24)
print('------------')
print( not a<b)

print(not 2>1 and 1<4 and 2<3 )
name=input("请输入姓名:")
classpro='haha'
print("%s%s"%(name,classpro))
print('Name是：{}'.format(name))

#判断语句与循环控制
score=int(input("请输入你的成绩："))
if score>90:
    print("A")
    pass
elif score>60 and score<90:
    print('B')
else:
    print('SB')
    pass
# 猜拳小游戏
# 0：石头，1：✂，2：布

#input('[0：石头，1：✂，2：布]')
result=str('0')
while result!='你赢了，好厉害哦':
    player = str(input("请出拳:"))
    sta = 0
    if player == '石头':
        sta = 0
        pass
    elif player == '剪刀':
        sta = 1
        pass
    else:
        sta = 2
        pass
    systerm_player = random.randint(0, 2)
    if systerm_player == 0:
        com_player = '石头'
        pass
    elif systerm_player == 1:
        com_player = '剪刀'
        pass
    else:
        com_player = '布'
    print("系统出招为：{}".format(com_player))
    result = '结果'
    if player == com_player:
        result = "平局"
        pass
    elif sta == 0 and systerm_player == 1:
        result = '你赢了，好厉害哦'
        pass
    elif sta == 0 and systerm_player == 2:
        result = '我的评价是，不如群友'
        pass
    elif sta == 1 and systerm_player == 2:
        result = '你赢了，好厉害哦'
        pass
    elif sta == 1 and systerm_player == 0:
        result = '我的评价是，不如群友'
        pass
    elif sta == 2 and systerm_player == 0:
        result = '你赢了，好厉害哦'
        pass
    elif sta == 2 and systerm_player == 1:
        result = '我的评价是，不如群友'
        pass
    print('{}'.format(result))
    pass
pass





a,b=1,9
while b>=1:
    a=1
    while a<=b:
        print("%d*%d=%d"%(a,b,a*b),end=' ')
        a+=1
        pass
    print()
    b-=1
    pass


#2n-1
b=1
r=int(input('请输入三角形的高:'))
#num(*)=10-2b
while b<=r:
    temp1=r-b
    temp2=2*b-1
    while temp1>0:

        print(' ',end='')
        temp1 = temp1-1
        pass
    while temp2>0:
        print('*',end='')
        temp2=temp2-1
    print()
    b=b+1
    pass







