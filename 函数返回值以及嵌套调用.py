# Python Learning Process
# Name:Ayanami_LJ
# Time:2023/3/16
import numpy as np
import matplotlib.pyplot as plt
'''
概念：函数执行完以后会返回一个对象
类型:可以返回任意类型，返回值类型应该取决于return后面的类型
用途：给调用方返回数据
在一个函数体内可以出现多个return值，但是只能返回一个return
如果在一个函数体内执行了了return，意味着函数就推出了，return后面的代码语句将不会执行
'''
def sum(a,b):
    sum=a+b
    return sum#将计算的结果返回
    pass

print(sum(10,30))

#返回列表
def calculate(num):
    li=[]
    result=0
    i=1
    while i<=num:
        result+=i
        i+=1
        pass
    li.append(result)
    return li
print(calculate(5))



#返回元组
def returntuple():
    '''
    返回元组类型的数据
    :return:
    '''
    return 1,2,3
    pass
a=returntuple()
print(a)

#返回字典
def returndic():
    '''
    返回元组类型的数据
    :return:
    '''
    return {'name':'aya'}
    pass
a=returndic()
print(type(a))


#函数的嵌套调用

def fun1():
    print('-----fun1 start------')
    print('-----fun1 end------')
    pass

def fun2():
    print('-----fun2 start------')
    fun1()
    print('-----fun2 end------')
    pass

fun2()
'''
函数的分类：根据函数的返回值和函数的参数
1.有参数无返回值
2.有参数有返回值
3.无参数有返回值
4.无参数无返回值
'''

#写函数，接受n个数字，求这些参数数字的和
def fun_sum(*num):
    sum = 0
    for item in num:

       sum+=item
       pass
    print(sum)
    return sum
fun_sum(1,3,14,1,3,4,)

#写函数，找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表

def fun_jishu(list):
    i = 1
    listA=[]
    for items in list:
       if i%2==1:
           listA.append(items)
       i += 1
       pass
    pass


    return listA

list=[1,23,4,2,25,1,2,13,5]
print(fun_jishu(list))

def jishu(con):
    listA=[]
    index=1
    for i in con:
        if index%2==1:
            listA.append(i)
            pass
        index+=1
        pass
    return listA


print(jishu([1,2,3,4,5,67,]))

'''
#写函数，检查穿入字典的每一个value的长度，如果大于2，那么仅保留前
两个长度的内容，并将新的内容返回给调用者.
p.s:字典中的value只能是字符串或列表
'''

def check_dic_value(dic):
    '''

    :param dic:
    :return:
    '''
    dicA={}
    for key,value in dic.items():
        if len(value)>2:
            dicA[key]=value[:2]
            pass
        else:
            dicA[key]=value
            pass
        pass
    return dicA

def creat_dic(**dic):
    print(dic)
    return dic
dicB=creat_dic(name='aya',school='njau',hobby='games',love=[1,2,3,4])
print(dicB)
dictA={}
dictA=check_dic_value(dicB)
print(dictA)