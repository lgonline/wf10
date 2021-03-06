#!/usr/bin/env python
# encoding: utf-8

"""
@author: liugang9
@software: PyCharm
@file: test__dict__demo.py
@time: 2017/10/26 18:26
"""

class cls:
    clsvar = 1
    def __init__(self):
        self.insvar = 2

#创建类的实例ins1和ins2
ins1 = cls()
ins2 = cls()

#用实例1为类变量重新赋值并打印
print '#'*10
ins1.clsvar = 20
print cls.clsvar     #输出结果为1
print ins1.clsvar    #输出结果为20
print ins2.clsvar    #输出结果为1

#用类名为类变量重新赋值并打印
print '#'*10
cls.clsvar = 10
print cls.clsvar     #输出结果为10
print ins1.clsvar    #输出结果为20
print ins2.clsvar    #输出结果为10

#这次直接给实例1没有在类中定义的变量赋值
print '#'*10
ins1.x = 11
print ins1.x         #输出结果为11

#然后再用类名给类中没有定义的变量赋值
print '#'*10
cls.m = 21
print cls.m          #输出结果为21

#再创建一个实例ins3，然后打印一下ins3的变量
print '#'*10
ins3 = cls()
print ins3.insvar    #输出结果为2
print ins3.clsvar    #输出结果为10
print ins3.m         #输出结果为21
print ins3.x         #报错AttributeError: cls instance has no attribute 'x'