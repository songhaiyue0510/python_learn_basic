# ! /user/bin/env python
# # -*- coding: utf-8 -*-

"""
面向对象的程序设计的三大特性：继承、多肽、封装
一、继承：描述类与类之间的从属关系
1、继承是一种新建类的方式，继承新建的类称为子类或者派生类，被继承的类称为父类、基类、超类，子类会遗传父类的属性
2、继承的优点：减少代码冗余，重用父类的代码
3、python2 中有经典类和新式类之分，python3中全为新式类
4、用 子类名.__bases__查看父类，父类以元祖的形式显示
5、属性查找顺序：对象自己的名称空间 -> 对象所在类的名称空间 -> 对象所在类的父类的名称空间

6、派生就是在继承的基础上定义新的东西，子类定义自己新的属性，如果与父类同名，以子类自己的为准
7、派生有两种方案：（1）直接调用父类的属性 （2）用super()调用父类的属性,返回值是一个对象，不要self

8、经典类与新式类
8.1 新式类：继承object的类，以及该类的子类孙子类
8.2 经典类：没有继承object的类，以及该类的子类、孙子类
备注：python3中没有指定的父类，默认继承object类，所以python3都是新式类

9、多继承属性查找
9.1 菱形结构的继承关系：最后至少两个类都继承一个类
9.2 非菱形结构：继承关系查找从左到右，新式类和经典类没有区别
9.3 菱形结构时，经典类采用深度优先（一条道走到黑），新式类采用广度优先（先试探再迂回）
备注：新式类，属性查找方法 类名.__mro__ 或者 类名.mro()

10、组合：
10.1 解决类与类之间代码冗余的方案
10.2 继承解决类与类之间的从属关系，组合结局类与类之间的交叉关系，也就是什么有什么的关系
10.3 即一个类产生的对象，该对象拥有一个属性，这个属性的值是来自另外一个类的对象

"""
## 继承例子
print("======继承：案例1=========")
class ParentClass1:
    pass
class Parentclass2:
    pass

# 单继承
class SubClass1(ParentClass1):
    pass
class SubClass2(ParentClass1,Parentclass2):
    pass
# 用.__base__查看父类
print(SubClass1.__bases__)
print(SubClass2.__bases__)

print("======继承：案例2，把老师和学生，学生可以自由选择课程，老师可以对学生成绩进行评分=========")

# 原有写法，有冗余代码
class DeepsharePeople:
    school='deepshare'
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

class DeepshareTeacher(DeepsharePeople):
    def modify_score(self):
        print('teacher {} is modifying score'.format(self.name))

class DeepshareStudent(DeepsharePeople):
    def choose(self):
        print('student {} is modifying score'.format(self.name))

tea1=DeepshareTeacher('Albert',18,'male')
stu1=DeepshareStudent('Tim',10,'female')
tea1.modify_score() ## 执行对象的函数属性，不用加变量输入啦
print(tea1.name,tea1.gender)
print(tea1.modify_score)
print(DeepshareStudent.__bases__)
print(tea1.__dict__)

print("======继承：案例3，属性查找顺序=========")
# 属性查找顺序：对象自己的名称空间 -> 对象所在类的名称空间 -> 对象所在类的父类的名称空间
class Foo:
    def f1(self):
        print('Foo.f1')
    def f2(self):
        print('Foo.f2')
        self.f1()
class Bar(Foo):
    def f1(self):
        print('Bar.f1')
obj=Bar()
obj.f2()
## 按照属性查找顺序，Bar中没有f2，到父类找到f2，执行self.f1()时，self为对象本身，故执行Bar中的f1

print("\n")
print("======派生：案例1=========")
# 子类定义自己新的属性，如果与父类同名，以子类自己的为准
class DeepsharePeople:
    school='deepshare'
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def f1(self):
        print('父亲的f1')

class DeepshareTeacher(DeepsharePeople):
    def modify_score(self):
        print('teacher {} is modifying score'.format(self.name))
    def f1(self):
        print('儿子的f1')
tea1=DeepshareTeacher('Albert',18,'male')
tea1.f1()

print("======派生：案例2，init函数部分相同=========")
class DeepsharePeople:
    school='deepshare'
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def f1(self):
        print('父亲的f1')
    def info(self):
        print("""
        ====个人信息
        姓名：{}
        年龄：{}
        性别：{}""".format(self.name,self.age,self.gender))

class DeepshareTeacher(DeepsharePeople):
    def __init__(self,name,age,gender,level,salary):
      # 方法一：
        # self.name=name
        # self.age=age
        # self.gender=gender
      # 方法二：
      #   DeepsharePeople.__init__(self,name,age,gender) ## 用类来调用，没有自动传值，要把self
      # 方法三：
        super().__init__(name,age,gender)
        self.level=level
        self.salary=salary
    def modify_score(self):
        print('teacher {} is modifying score'.format(self.name))
    def f1(self):
        print('儿子的f1')
    def info(self):
      # 方法二
      #   DeepsharePeople.info(self)
      # 方法三：
        super().info()
        print("""
        等级：{}
        薪资：{}""".format(self.level,self.salary))
tea1=DeepshareTeacher('Albert',18,'male','10','3.1')
print(tea1.level,tea1.salary)
tea1.info()

print('\n')
print("======经典类vs新式类=========")
class Foo:
    pass
print(Foo.__bases__)  ## python3没有指定父类，默认继承object类

print('\n')
print("======多继承关系查找=========")
## python均为新式类，采用广度优先方式查找
class A(object):
    def test(self):
        print('from A ')
class B(A):
    # def test(self):
    def test1(self):
        print('from B ')
class C(A):
    def test1(self):
    # def test(self):
        print('from C ')
class D(B):
    def test1(self):
    # def test(self):
        print('from D')
class E(C):
    # def test(self):
    def test1(self):
        print('from E')
class F(D,E):
    pass
f1=F()
f1.test()
## 下两种方法一致
print(F.__mro__)
print(F.mro())

print('\n')
print("======多继承关系查找：当有super()时=========")

### 正常理解：super().f1()在A中没有找到，在父类X中没有找到，应该报错，但这里严格按照mro的继承顺序，从C-A-X-B的顺序查找，最终在B中找到f1
class X:
    def test(self):
        print('x')
    # def f1(self):
    #     print('XF')
class A(X):
    def test(self):
        print('1 打印一下，代码先经过这里')
        super().f1()
        print('3 再打印一下，代码最后经过这里')
class B:
    def f1(self):
        print('2 再经过这里from B')
class C(A,B):
    pass
c=C()
c.test()
print(C.__mro__)

print('\n')
print("=============================组合================================")
## 即一个类产生的对象，该对象拥有一个属性，这个属性的值是来自另外一个类的对象
class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day
    def tell_birth(self):
        print("出生年月日{}-{}-{}".format(self.year,self.mon,self.day))
class DeepsharePeople:
    school='deepshare'
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
class DeepshareTeacher(DeepsharePeople):
    def __init__(self,name,age,gender,level,salary):
        super().__init__(name,age,gender)
        self.level=level
        self.salary=salary
    def change_score(self):
        print('teacher {} is changing score'.format(self.name))
class DeepshareStudent(DeepsharePeople):
    def __init__(self,name,age,gender,course):
        super().__init__(name,age,gender)
        self.course=course
    def choose(self):
        print('student {} chose course'.format(self.name))

tea1=DeepshareTeacher('albert',18,'male',10,3.1)
date_obj=Date(2000,1,1)
date_obj.tell_birth()
tea1.birth=date_obj
print(tea1.birth)
tea1.birth.tell_birth()
tea1.change_score()
stu1=DeepshareStudent('张三',16,'male','AI')
stu1.birth=Date(2002,3,3)
stu1.birth.tell_birth()