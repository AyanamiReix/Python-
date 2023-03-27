# Python Learning Process
# Name:Ayanami_LJ
# Time:2023/3/16
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
'''
set(集合)是python中的一种数据类型，是一个无序且不重复的元素集合
不支持索引和切片，类似于字典，但是只有key 没有value

集合操作函数：
add()
clear()
A.difference(B)->取A-B
A.intersection(B)->取A∩B
A.union(B)->取A∪B
pop()
discard()指定移除元素
updata()两个集合

'''
#创建方式
set1={1,2}
#set
print(set1)
set1.add('python')
print(set1)
set1.clear()
print(set1)
a={12,24,36}
b={24,36,1,44}
print(a.difference(b))    #A-B
print(a.intersection(b))  #交集
print(a.union(b))         #并集
print(a|b)                #并集的第二种操作
#pop就是集合中拿数据并且同时
print('------------------')
print(a)
qudata=a.pop()
print(a)
print(qudata)
#discard 指定移除的元素
a.discard(12)
print(a)
#updata
a.update(b)
print(a)


#练习题
#1.求三组连续自然数的和，求出1-10、20-30、30-45的三个和
#2.100个和尚吃100个馒头，大和尚一人吃三个馒头，小和尚三人吃一个馒头，请问大小和尚各多少人？
#3.指定一个列表，列表里含有唯一一个只出现过一次的数字，写程序找出这个‘独一无二的’数字

def mysum(a,b):
    sum=0
    for item in range(a,b+1):
        sum+=item
        pass
    print(sum)
    pass
mysum(1,10)


def count_member(supply,member):
    sum=0
    small=60
    big=member-small
    sum = big * 3 + 1 / 3 * small
    while sum!=supply:
        if sum>supply:
            small+=3
            pass
        else:
            small-=3
            pass
        big = member - small
        sum = big * 3 + 1 / 3 * small
    print('大和尚个数为%d，小和尚个数为%d'%(big,small))
    pass



count_member(100,60)
list=[1,1,2,2,3,3,5,5,8,8,9,9,9,10,10,7]

def findx(list,a):
    for item in list:
        if item==a:
            return 1
        pass
    return 0

def fun(list):
    listA=[]
    listB=[]
    for item in list:
        if findx(listA,item)==0:
            listA.append(item)
            continue
            pass
        else:
            listB.append(item)
            pass
        pass
    # print(list)
    # print(listA)
    # print(listB)
    key=0
    for item in listA:
        if findx(listB,item)==0:
            key=item
    return key
    pass
print(fun(list))

#
# listA=[]
# for i in list:
#     listA.append(i)
#     pass
# print(listA)
# print(findx(listA,1))



