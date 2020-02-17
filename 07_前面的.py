# ! /user/bin/env python
# -*- coding: utf-8 -*-
#------------------------------# break使用 # ----------------------------------
# albert_age=18
# while True:
#     guess=int(input(">>: "))
#     if guess>albert_age:
#         print('偏大')
#     elif guess<albert_age:
#         print('偏小')
#     else:
#         print('correct')
#         break

#------------------------------# 无参装饰器 # ----------------------------------
import time
def index(): ## 有返回值
    time.sleep(1)
    print('welcome')
    return 1
def home(name): ## 无返回值
    time.sleep(2)
    print('welcome %s' %name)

def timer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print(stop_time-start_time)
        return res
    return wrapper

index=timer(index) # 新的index=wrapper
home=timer(home)   # 新的home=wrapper

home('Albert')
index()

## 无参装饰器：常用使用方法
import time

def timer(func): # 装饰器也是一个函数，先定义后使用
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print(stop_time-start_time)
        return res
    return wrapper

@timer # 在被装饰对象正上方单独一行添加，相当于执行index=timer(index)
def index(): ## 有返回值
    time.sleep(1)
    print('welcome')
    return 1

@timer # 在被装饰对象正上方单独一行添加，相当于执行index=timer(index)
def home(name): ## 无返回值
    time.sleep(2)
    print('welcome %s' %name)

home('Albert')
index()

## 无参装饰器模板
def outer(func):
    def inner(*args,**kwargs):
        """
        这里写装饰器逻辑
        :param args: 任意位置参数
        :param kwargs: 任意关键参数
        :return: 一个函数对象
        """
        res=func(*args,**kwargs)
        return res
    return inner