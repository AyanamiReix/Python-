# Python Learning Process
# Name:Ayanami_LJ
# Time:2023/3/16
import numpy as np
import matplotlib.pyplot as plt
'''
元组：是一个不可变的序列，创建后不能作任何改变
1.不可变
2.用（）创建元组类型，数据项用逗号分隔
3.可以是任何的类型
4.元组中只有一个元素时，要加上逗号，不然解释器会当作整形处理
5.支持切片操作
'''

#元组的创建 不能进行修改
tupleA=()
print(type(tupleA))
tupleA=('AABB',89.92,'dad',[1,2,3])
print(tupleA)
tupleB=('123',) #当元组中只有一个数据项的时候，要加，
print(type(tupleB))


#元组的查询
for item in tupleA:
    print(item,end=' ')
    pass
print('\n--------')
#切片操作
print(tupleA[0])
print(tupleA[0:])
print(tupleA[::-2]) #反方向，每隔两个取一次，负号只代表方向

#注意：tupleA[0,1,2,3,4]等价于tupleA[-5,-4,-3,-2,-1] （这边指的是索引下标）

#注：可以对元组中的列表进行修改

tupleC=(1,2,3,['a',1,351])
tupleC[3][0]=111
print(tupleC)

tupleD=tuple(range(10))
print(tupleD)
print(tupleD.count(9)) #统计元素出现的次数


'''
字典：数据类型，字典是由 键值对 组成的集合，通常使用键来访问数据
，效率非常高，和list一样支持对数据的添加、修改、删除操作
特点：
1.不是序列类型，没有下标概念，是一个无需的 键值集合，是内置的高级数据类型
2.用{}来表示字典对象，每个键值用逗号分隔
3，键 必须是不可变的类型 【元组、字符串】值可以是任意的类型
4.每个键 必须是唯一的，如果重复，后者会覆盖前者
'''
print('\n---------------------------------字典：\n')
#字典创建
a={}
print(type(a))
#添加字典数据
# dictA={}
dictA={'pro':'艺术','school':'北京电影学院'}
print(a)
dictA['name']='Ayanami' #key:value
dictA['age']='100'
dictA['pos']='Lover'
print(dictA)
print(len(dictA))

print(dictA['name'])
dictA['school']='南农'
print(dictA)

#(key:value)=item
#获取所有键
print(dictA.keys())
#获取所有的值
print(dictA.values())
#获取所有键值对
print(dictA.items())
#遍历所有键值对
for item in dictA.items():
    print(item)
    pass

for key,value in dictA.items():
    print("key=%s,value=%s"%(key,value))
    pass

#添加操作： dict.update({'something'}:data)
dictA.update({'height':1.80})
print(dictA)

#删除操作:通过指定键进行删除
del dictA['name']
dictA.pop('age')
print(dictA)

#对字典进行排序操作
print('--------------\n排序:\n')
#1.按照key排序
print(sorted(dictA.items(),key=lambda d:d[0]))


#合并 适用对象：字符串、list、tuple
strA='sb把'
strB='uu'
print(strA+strB)
listA=list(range(10))
listB=list(range(10))
print(listA+listB)
tupleA=tuple(range(3))
tupleB=tuple(range(4,6))
print(tupleA+tupleB)


#in 对象是否存在 结果是一个bool类型的数据
print('--------------\n对象是否存在')
print('s' in strA)
print(3 in tupleA)
#字典判断的是键
print('name' in dictA)
print('pos' in dictA)