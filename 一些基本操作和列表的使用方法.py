# Python Learning Process
# Name:Ayanami_LJ
# Time:2023/3/16
import numpy as np
import matplotlib.pyplot as plt
#首字母变大写/消除空格/地址/查找find（x）
# name='lj'
# print(name.capitalize())
# a='      ff         '
# print(a.strip())
# print(a.rstrip())
# print(a.lstrip())
# a=40
# b=40
# print(id(a))
# print(id(b))
#
# #查找
# data='ad jijiawj'
# print(data.find('j'))
# print(data.index('j'))
# #find与index的区别，find没找到返回-1，index则报错
#
# #判断是否以某个值为开头/结尾，是则返回T,不是返回F
# print(data.startswith('b'))
# print(data.endswith('j'))
#
# #大小写转化
# print(data.upper()) #转换大写
# print(data.lower()) #转换小写
#
#
# #统计出现次数
# print(data.count('a'))
#
#
#
# #切片
# #string[start:end:step]
# #关键：start包含，end不包含 左闭右开
# string='I am your father'
# print(string[0:])
# print(string[2:5:1])
# print(string[:10])
# #倒叙输出 负号表示方向
# print(string[::-1])
#

'''
list：python当中非常重要的数据结构，是一种有序的数据集合
#特点：
1支持增删改查
2.列表中的数据可以变化，但地址不会改变
3.用[]来表示数据类型，数据项之间用逗号分割，注：数据项可以是任何类型的数据
4.支持索引和切片
'''

li=[1,2,3,'nihao']
print(len(li)) #len可以获取列表对象中的数据个数
str='dawdadaw'
print(len(str))
print(type(li))
#查找

listA=['abcd',775,12.23,True]
print(listA[1::-1])
print(listA*2)

#增加
listA.append([1,2,3,])
print(listA)
#插入操作，指定位置
listA.insert(1,'a')
print(listA)
#list()强制类型转换
data=list(range(9))
print(type(data))
listA.extend(data)  #extend 拓展 批量添加
print(listA)

listA.extend([1,2,3,4]) #注意和append的一个区分
print(listA)
print('------------------------')

listB=list(range(10,30))
print(listB)
print(len(listB))
#删除操作
del listB[0]
print(len(listB))

#批量删除操作 ：使用索引 slice
del listB[10:]
print(listB)
print(len(listB))

#list.remove 移除指定项 参数是数据值
listB.remove(11)
print(listB)
print(len(listB))

#list.pop :移除指定项 参数是索引值（下标）
listB.pop(2)
print(listB)

#list.index(data,start,end) start-end是指查找范围
print(listB.index(18,1,10))

