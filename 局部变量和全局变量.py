# Python Learning Process
# Name:Ayanami_LJ
# Time:2023/3/16
import numpy as np
import matplotlib.pyplot as plt

#函数内部的变量优先值最高
#修改全局变量需要global进行声明

name='ayanami'

def fun1():
    name='aya_local'
    print('{}'.format(name))
    pass

fun1()#打印的是aya_local

pro='计算机'
def changeGlobal():
    '''
    要修改全部变量
    :return:
    '''
    pro='市场营销'  #局部变量
    pass

changeGlobal()
print(pro)
#并没有改变全局变量，pro依然是计算机

def changeGlobal_2():
    '''
    改：要修改全部变量
    要声明是global变量
    :return:
    '''
    global pro
    pro = '市场营销'
    pass
changeGlobal_2()
print('-----------------')
print(pro)


#重点：引用
a=1
def fun(x):
    print('x的地址为: {} '.format(id(x)))
    x=2
    print('修改后的地址为: {}'.format(id(x)))
    pass
#调用函数
print('a的地址为:',id(a))
fun(1)
fun(a)
print('传参后a的值为{}'.format(a)) #此处a打印后仍为1，因为a是一个不可变类型，传参后没有改变地址

#可变类型：字典/列表
print('-----------可变类型：列表为例------------')
li=[]
def testRenc(parms):
    print(id(parms))
    li.append([1,2,3])
    print(id(parms))
    pass

print(id(li))
testRenc(li)
print(li)

'''
小结：
1.在python当中，万物皆对象，在函数调用的时候，实参传递的就是对象的引用
2.了解了原理后，就可以更好把控在函数内部的处理是否会影响到函数外部数据变化
3.参数传递是通过对象饮用来完成，即传递地址
'''


'''
匿名函数：
lambda 参数1、参数2、参数3:执行表达式

特点：
1.使用lambda关键字去创建函数
2.没有函数名
3.匿名函数冒号后面的表达式有且只有一个，注意：是表达式，而不是语句
4.匿名函数自带return，return结果就是表达式计算后的结果
'''
print('----------匿名函数-----------')
M=lambda x,y:x*y
#调用方法，通过变量接受，通过变量去调用匿名函数
print(M(1,3))

result=lambda x,y,z:x*y*z
result(1,2,3)
print(result(1,2,3))

'''
if x(> = < .....)y:
       x
else:
       y
以上等价于 x if x(> = < .....)y else y
'''
age=15
print('结婚了' if age>18 else '别生小孩')

compare=lambda x,y:x if x>y else y
print(compare(1,2))
#直接的调用
example1=(lambda x,y:x if x>y else y)(10,16)
print('example1={}'.format(example1))


vars=lambda x:x**2
print(vars(10))
#注：lambda只能实现有限简单逻辑，复杂逻辑只能使用def处理

