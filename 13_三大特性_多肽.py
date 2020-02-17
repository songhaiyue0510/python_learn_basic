# ! /user/bin/env python
# # -*- coding: utf-8 -*-

"""
多肽
1、多态性：可以在不用考虑的对象具体类型的前提下，而直接使用对象下的方法
多态, 不同的 子类对象调用 相同的 父类方法，产生 不同的 执行结果，可以增加代码的外部 调用灵活度，
多态以 继承 和 重写 父类方法 为前提
多态是调用方法的技巧，不会影响到类的内部设计
参考链接：https://www.cnblogs.com/onefine/p/10499390.html
2、鸭子类型：定义两个没有关系的类，规范一致，解耦合
3、类的绑定方法
3.1 类的绑定方法：应该用类来调用，并且自动将类作为第一个参数传入，参数叫做cls，@classmethod
3.2 类的非绑定方法： @staticmethod
"""

print("==========没有多态时：=============")
#
class ArmyDog(object):
    def bite_enemy(self):
        print('追击敌人')

class DrugDog(object):
    def track_drug(self):
        print('追查毒品')

class Person(object):
    def work_with_army(self, dog):
        dog.bite_enemy()

    def work_with_drug(self, dog):
        dog.track_drug()

p = Person()
p.work_with_army(ArmyDog())
p.work_with_drug(DrugDog())

print('\n')
print("==========有多态时：例1=============")
class Dog(object):
    def work(self):
        pass

class ArmyDog(Dog):
    def work(self):
        print('追击敌人')

class DrugDog(Dog):
    def work(self):
        print('追查毒品')

class Person(object):
    def work_with_dog(self, dog):  # 只要能接收父类对象，就能接收子类对象
        dog.work()  # 只要父类对象能工作，子类对象就能工作。并且不同子类会产生不同的执行效果。

p = Person()
p.work_with_dog(ArmyDog())
p.work_with_dog(DrugDog())

print("==========有多态时：例2=============")
class ArmyDog(object):
    def work(self):
        print('追击敌人')

class DrugDog(object):
    def work(self):
        print('追查毒品')

class Person(object):
    def work_with_dog(self, dog):
        dog.work()

p = Person() ## 调用类 == 产生对象
p.work_with_dog(ArmyDog()) ## 对象调用函数
p.work_with_dog(DrugDog())

print("==========类的绑定方法=============")
import settings
class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def tell(self):
        print("{} {}".format(self.name,self.age))
    @classmethod   ## 加了这段话，自动把类当做第一个参数传入，后续再87行括号会自动将类当做第一个参数传入
    def read_from_conf(x): ## 不需要自动传值，则去掉self
        return People(settings.NAME,settings.AGE)

p=People.read_from_conf()
p.tell()

print("==========类的非绑定方法=============")
import settings
import hashlib
import time
class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def tell(self):
        print("{} {}".format(self.name,self.age))

    @classmethod   ## 加了这段话，自动把类当做第一个参数传入，后续再87行括号会自动将类当做第一个参数传入
    def read_from_conf(cls): ## 不需要自动传值，则去掉self
        return People(settings.NAME,settings.AGE)
    @staticmethod  ## 将create_id变成普通方法，即非绑定方法或者静态方法
    def create_id():
        m=hashlib.md5()
        m.update(str(time.clock()).encode('utf-8'))
        return m.hexdigest()

p=People('albert',18)
print(p.create_id)
print(p.create_id())