# ! /user/bin/env python
# -*- coding: utf-8 -*-

"""
类与对象：
1、面向过程与面向对象：
1.1 面向过程的程序设计：优点是复杂的问题流程化、简单化；缺点是可扩展性差，牵一发而动全身；应用场景：一旦完成很少改变的场景
1.2 面向对象的程序设计：优点是解决了程序的扩展性，对某一个对象单独修改，会立刻反应到整个体系中；缺点是编程复杂度高，无法精准的预测问题的处理流程与结果

2、类的用法：类则是一系列对象相似的特征与技能的结合体
2.1 程序中，务必先定义类，后产生对象，定义的时候会立刻执行
2.2 PS
（1）在程序中，特征用变量标识，技能用函数标识
（2）因而类中最常见的无非是：变量和函数的定义
（3）定义类，使用关键字class+空格+类名，类名用大驼峰命名，变量名推荐使用"_"这种方式就是为了区分，类名为名词，函数名为动词

3、对象的用法：类相当于一个模板或者一个工厂，用类可以批量生产对象
3.1 在程序中：先定义类 ==> 调用类 ==> 产生对象
"""

class DeepshareStudent:
    # 用变量表示特征
    school='deepshare'
    # 用函数表示技能
    def __init__(self,x,y,z): ## __init__在调用类的时候自动执行，self必写，给对象初始化，在类创造对象的时候就赋予对象属性以不同的特征
        self.name=x
        self.age=y
        self.gender=z
    def learn(self):  ## self 指类的对象本身
        """
        self 是pycharm自动添加的
        位置参数，必须传值
        """
        print("%s is learning" % self)

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleeping')

    print('========>')

## 类的查看：__dict__，输出为字典形式
name_and_func=DeepshareStudent.__dict__
print(name_and_func)
print(name_and_func['school'])
print(name_and_func['learn']) ## name_and_func['learn']是一个函数的内存地址，加上（）就能调用

name_and_func['learn']('hello')

print('\n')

## 类的查看：class_name.func
print(DeepshareStudent.school)
print(DeepshareStudent.learn)

## 类的修改
DeepshareStudent.school='hello world'
print(DeepshareStudent.school)

## 给类添加属性
DeepshareStudent.country='China'
print(DeepshareStudent.country)

# 删除类的属性
del DeepshareStudent.country
# print(DeepshareStudent.country)

print('\n')
# 先定义类 ==> 调用类 ==> 产生对象，定义了__init__后，即有公共属性又有私有属性
stu1=DeepshareStudent('李依依',18,'male')
print(stu1.name)
print(stu1.school)
stu2=DeepshareStudent('王二',45,'female')
print(stu2.name)
print(stu2.school)
stu3=DeepshareStudent('李三',23,'male')
print(stu3.name)
print(stu3.school)