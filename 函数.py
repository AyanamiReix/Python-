# Python Learning Process
# Name:Ayanami_LJ
# Time:2023/3/16
import numpy as np
import matplotlib.pyplot as plt



def printInfo():
    '''
    这个函数是用来...
    :return:
    '''
    print('Hello World')
    pass
printInfo()

#输出不同人的信息（通过传参来解决）
def infomation(name,height,weight,hobby):
    '''
    这是打印某个人信息的函数
    :param name:
    :param height:
    :param weight:
    :param hobby:
    :return:
    '''
    print("%s的身高为%dcm"%(name,height))
    print("%s的体重是%dkg"%(name,weight))
    print('%s的爱好为%s'%(name,hobby))
    pass
infomation('Ayanami',168,53,'Love')

'''
参数的分类：
必选参数、默认参数[缺省参数]、可选参数、关键词参数
参数：为了得到外部数据的
'''
# 必选参数
def sum(data):  #注意不需要指定类型，区别C语言
    sum=0       #形参，定义时候不占内存地址
    while data>=0:
        sum+=data
        data-=1
        pass
    return sum
sum1=sum(100)
print(sum1)

#必选参数，必须填写实参
def qiuhe(a,b):
    sum=a+b
    print(sum)
    pass
qiuhe(1,2)

#缺省参数，如果未复制，就会用定义时给的默认值
def sum_1(a=1,b=5):
    sum=(a+b)
    print(sum)
    pass
sum_1()
sum_1(33) #53,b采用默认值
print('------可变参数-------')
#可变参数(当参数的个数不确定时使用，比较灵活)
def get_st(*args):
    '''
    计算累加和

    :param args:可变长的参数类型
    :return:
    '''
    print(args)
    result=0
    for item in args:
        result+=item
        pass
    print('result=%d'%result)
    pass


get_st(1,)
get_st(1,2)


#传一个可变元组（关键词可选参数）
print('----------双星号---------------')
def fun_dic(**dic):
    print(dic)
    pass
dicA={'name':'Ayanami','pos':'my ex'}
fun_dic(**dicA)
fun_dic(name='Ayanami',pos='ex')

#组合传参
print('--------组合传参--------')
def com_fun(*tuplE,**dic):
    '''
    可选参数必须放到关键字可选参数之前
    可选参数；接受的是元组类型
    关键字可选参数；接受的是字典类型
    :param tuplE:
    :param dic:
    :return:
    '''
    print(tuplE)
    print(dic)
    pass
#def com_fun(**dic,*tuplE):这个不行！！！！
com_fun(1,2,3,4)
com_fun(name='Aya')
com_fun(1,2,3,4,name='Aya')





