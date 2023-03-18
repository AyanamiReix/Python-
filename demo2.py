# Python Learning Process
# Name:Ayanami_LJ
# Time:2023/3/16
import numpy as np
import matplotlib.pyplot as plt

#1.打印前100个整数值
sum=0
for data in range(101):
    sum+=data
    pass
print('{}'.format(sum))
print('sum=%d'%(sum))
print('------------------')


#2.求50-200所有整数和
#注意：以下运算的区别，分别为精确计算，取整计算，取余计算
# print(11/2)  精确
# print(11//2) 取整
# print(11%2)  取余

sum=0
for data in range(50,201):  #结尾不取
    if data%2==0:
        sum+=data
        pass
    pass
print('{}'.format(sum))


#3.break的使用和continue的使用
sum=0
for data in range(50,201): #break的使用
    if sum>5000:
        break
        pass
    if data%2==0:
        sum+=data
        pass
    pass
print('{}'.format(sum))
sum=0

#continue：打印1-100所有奇数
for data in range(1,100):
    if data%2==0:
        continue
        pass
    print(data)
    pass



for data in 'i hate the world':
    if data=='w':
        continue #break
        pass
    print(data,end='')



#4.for循环打印99乘法表
for i in range(10):
    for j in range(1,i+1):
        print('%d*%d=%d   '%(i,j,i*j),end='')
        pass
    print('')
    pass



#5.for-else ：例如登录账号密码，几次输错封锁账号
account ='ayanami'
password='123'
for i in range(2):
    zh=str(input("请输入您的账号"))
    mm=input("请输入您的密码")
    #判断
    if account==zh and password==mm:
        print("登陆成功")
        pass
    break
    pass
else:
    print('您的账号已经锁定...')
#while-else 同理


#6.猜年龄小游戏
# 1.允许用户最多尝试3次
# 2.每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y or y，就继续让其猜3次，N就推出程序
# 3.如果猜对了，就直接退出
import  random
answer=random.randint(0,99)
print(answer)
i=0
index='Y'
while index=='Y' or 'y' :
    while i <= 2:
        player = int(input("请输入你的猜测值:"))
        if player == answer:
            print("猜对了好棒")
            index='N'
            break
            pass
        elif player>answer:
            print("猜大了")
            i += 1
            pass
        else:
            print("猜小了")
            i += 1
            pass
        pass
    else:
        index=input("三次机会已经耗尽，想继续猜测吗？[Y/y:继续，N/n:终止]")
        if index=='Y' or 'y':
            i=0
            continue
            pass
else:
    print("游戏结束")




