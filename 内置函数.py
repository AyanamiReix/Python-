# Python Learning Process
# Name:Ayanami_LJ
# Time:2023/3/16
import random

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

#1.abs取绝对值
print(abs(-5))

#2.round(x,y) 取近似值 y表示精确到几位小数，默认0
print(round(2.55,1))

#3.pow()求指数 求次方
print(pow(3,3))

#4.divmod(a,b) #返回值(a//b,a%b)
print(divmod(7,3))

#5.max()返回给定参数的最大值，参数可以是序列
i=0
listC=[]
while(i<10):
    listC.append(random.random())
    i+=1
    pass
print(listC)
print(max(listC))
print(max(range(1,5)))

#6.sum()求和
print(sum(listC))
print(sum(listC,1))

#7.eval()动态执行字符串的表达
a,c,b=1,2,3
print('动态执行的函数{}'.format(eval('a*b+c-100')))
def testFun():
    print('Ayanami')
    pass
eval('testFun')#没有括号不行
eval('testFun()')#可以调用函数执行

#eval(expression,globals)->globals如果被提供，必须是一个字典对象
print(eval('a+b',{'a':3,'b':10}))


#8.类型转换
'''
chr()数字转字符
bool()
bin()二进制转换
'''
print('----------类型转换---------')
print(bin(10)) #转换二进制
print(hex(32)) #转换十六进制

# 字典的操作
dic=dict()
print(type(dic))
dic['name']='aya'
print(dic)
# bytes()转为字节数组
print(bytes('我喜欢python',encoding='utf-8'))
print(chr(65))
print(bool(0))

#序列操作函数
'''
all():判定可迭代参数是否都为True,对象中的元素除了0、空 False都为True,
所有元素都为True，结果才为True，返回bool类型
any()：判断给定的可迭代参数是否都为False,只要有一个元素为True，结果为True
sort()和sorted()
list.reverse() 只是用来反转，非排序
range(start,stop[,step]) 注:不包括stop，要包括stop请+1
zip()
enumerate(sequence，[start=0]):【中文：枚举】 将一个可遍历的数据对象组合为一个索引序列，如列表、元组或字符串
同时列出数据和数据下表，一般用在for循环当中，返回枚举对象

'''
#all
listA=[]
listA.append(random.random())
listA.append(random.random())
print(all(listC))
listA.append(0)
print(all(listC))
print(all((1,2,0)))
#any
print('-------any-------')
print(any((1,2,0)))
print(any((0,0,0)))
print(any(('',False,0)))
print('---------sort/sorted------------')
print(listC)
#sort
#  list.sort()
# #sort:list的排序方法 直接修改的是原始对象,元组不能使用，因为元组本身不可修改
# print(list)
#sorted
print('----------排序之前---------\n{}'.format(list))
sorted(listC)
print('----------排序之后---------\n{}'.format(list))
#可以看出，sorted不会修改原始数据
list_new=sorted(listC,reverse=False)#默认为False，升序
list_newB=sorted(listC,reverse=True)
print(list_new)
print(list_newB)

#元组也可以使用
tupleA=(35,12,1,24,46,12)
print(sorted(tupleA))

#reverse 函数用于反向列表中的元素怒
listC=[1,6,2,35]
listC.reverse()
print(list)

listA=['name','you','pos']
listB=['aya','mine','lover']
listK=zip(listA)
print(list(listK))
ziplist=zip(listA,listB)
print(list(ziplist))

def printBookInfo():
    books=[]
    id=input('编号')
    bookName=input('书名')
    bookPos=input('位置')
    idlist=id.split(' ') #输入时添加空格，最后根据空格分割，组成列表
    namelist = id.split(' ')
    poslist=id.split(' ')
    bookInfo=zip(idlist,namelist,poslist)
    # print(list(bookInfo))
    for bookItem in bookInfo:
        '''
        遍历图书信息，进行存储
        '''
        dictInfo={'编号':bookItem[0],'书名':bookItem[1],'位置':bookItem[2]}
        books.append(dictInfo)#将字典对象添加到list容器中
        pass
    for item in books:
        print(item)
        pass
    pass
#printBookInfo()


#enumerate给列表等自动赋一个索引值
listObj=['a','b','c'] #注意区别
for item in enumerate(listObj):
    print(item)
for index,item in enumerate(listObj):
    print(item)
    pass
dicObj={}
dicObj['name1']='a'
dicObj['name2']='ab'
dicObj['name3']='abc'
print(dicObj)
for index,item in enumerate(dicObj):
    print(item)
