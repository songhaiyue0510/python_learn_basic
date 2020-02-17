# ! /user/bin/env python
# -*- coding: utf-8 -*-

"""
1、调用类 ====》产生类的对象，该对象也可以成为类的一个实例，调用过程也成为类的实例化

2、类名.__dict__查看类的名称空间，对象的名称空间 对象名.__dict__，在调用过程产生
备注：寻找对象的独有属性，先从init中找，若没有，则从类的名称空间找，若都没有则报错

3、绑定方法：用对象调用类属性时，拿到的是绑定方法，是绑定到类属性的
备注1：类内部的变量直接给对象使用，都指向同一个内存地址
备注2：类内部的函数，类可以使用，作为一个普通函数，有几个参数就传几个参数
      若绑定给对象使用，谁来调用，就把谁当做第一个参数自动传入

4、对象属性的增删改查

"""

class DeepshareStudent:
    # 用变量表示特征
    school='deepshare'
    name='aaaa'
    # 用函数表示技能
    def __init__(self,name,age,gender): ## __init__在调用类的时候自动执行，self必写，给对象初始化，在类创造对象的时候就赋予对象属性以不同的特征
        self.name=name
        self.age=age
        self.gender=gender
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

stu1=DeepshareStudent('王二',18,'male') ### 类的实例化

print(DeepshareStudent.__dict__)
print('\n')
print(stu1.__dict__)
## 下面两种用法结果一致
print(stu1.__dict__['name'])
print(stu1.name)
print(stu1.school)

## 绑定方法：
print("\n"+"======绑定方法========")
stu1=DeepshareStudent('王二',18,'male')
stu2=DeepshareStudent('王三',19,'male')
# 类内部的函数是绑定给对象使用，查看类和对象的名称空间
print(DeepshareStudent.learn)
print(stu1.learn)
print(stu2.learn)

# 类内部的变量直接给对象使用，查看类和对象的名称空间
print(DeepshareStudent.school)
print(stu1.school)  ## 对象调用learn拿到的是绑定方法，是绑定到类属性的
print(stu2.school)

# 类和对象调用函数
print("\n"+"======类和对象调用函数========")
DeepshareStudent.learn('Albert')
stu1.learn()

## 都叫class，用法的原理也是一样
print(set)
print(dict)
print(set)
print(DeepshareStudent)

### 对象属性的增添删减
print("\n"+"======对象属性的增添删减，与类的增添删减一样========")
class Bar:
    n=1111
    def __init__(self,x):
        self.x=x

# 查看
obj=Bar('abc')
print(obj.__dict__)
print(obj.x)
print(obj.n)

# 添加
obj.abc='abc'
print(obj.abc)

# 修改
obj.abc='123'
print(obj.abc)

# 删除
del obj.abc

### 练习一：实现一个功能，有一个对象，有一个count属性，统计所在的类产生了多少对象
print("======练习一：统计所在类产生多少对象=======")
class Foo():
    count=0
    def __init__(self):
        Foo.count+=1 ## 用self.count不对

obj1=Foo()
obj2=Foo()
obj3=Foo()
print(obj1.count)

print("======练习二：人狗大战=======")
class People:
    def __init__(self,name,aggressivity,life_value=100):
        self.name=name
        self.aggressivity=aggressivity
        self.life_value=life_value
    def bite(self,enemy):
        enemy.life_value-=self.aggressivity
        print("人{}咬了一口狗{},狗掉血{},狗剩余血量{}".format(self.name,enemy.name,self.aggressivity,enemy.life_value))

class Dog:
    def __init__(self,name,dog_type,aggressivity,life_value):
        self.name=name
        self.dog_type=dog_type
        self.aggressivity=aggressivity
        self.life_value=life_value
    def bite(self,enemy):
        enemy.life_value-=self.aggressivity
        print("狗{}咬了一口人{},人掉血{},人剩余血量{}".format(self.name,enemy.name,self.aggressivity,enemy.life_value))

p1=People('张二',60)  ## 调用类，产生类的对象，输入init需要的变量
d1=Dog('小黑','藏獒',200,200)
p1.bite(d1) ## 对象调用内部函数，输入函数需要的变量
d1.bite(p1)