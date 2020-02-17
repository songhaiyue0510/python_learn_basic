# ! /user/bin/env python
# # -*- coding: utf-8 -*-

"""
封装：
1、什么是封装：装是把属性存起来，封就是把属性隐藏起来
2、封装变量属性的目的：
（1）严格限制访问者对属性的操作，禁止随意使用，对外部隐藏对内部是开放的，只需要给用户部分接口即可
（2）还可以避免子类覆盖父类的方法
3、封装变量、函数属性：__变量名/函数
4、@property 把函数属性伪装成变量属相
有三个相关联的方法，这三个方法的名字都必须一样，是一个装饰器
（1）第一个方法是一个 getter 函数，它使得 score 成为一个属性。
（2）其他两个方法给score 属性添加了 setter 和 deleter 函数。
备注：需要强调的是只有在 score 属性被创建后， 后面的两个装饰器 @score.setter 和 @score.deleter 才能被定义。


"""
print("====================封装====================")
class Foo:
    __x=111
    def __init__(self,y):
        self.__y=y
    def __f1(self):
    # def f1(self):
        print('Foo f1')
    def f2(self):
        print('Foo f2')
        self.__f1()
        # self.f1()
    def get__y(self):
        print(self.__y)
class Bar(Foo):
    def __f1(self):
    # def f1(self):
        print("Bar.f1")

obj1=Foo(222)
## 报错，外部无法找到被封装的y
# obj.__x
## 内部可以访问被封装的y
obj1.get__y()

## __避免子类覆盖父类属性
print("===========__避免子类覆盖父类属性===========")
obj2=Bar(222)
obj2.f2()

## 封装函数属性，仅保留部分接口
print("\n")
class ATM:
    def put_your_card(self):
        print('插卡')
    def input_pwd(self):
        print('输密码')
    def input_money(self):
        print('输入取款金额')
    def __sent_request(self): ## 封装
        print("向银行系统发请求")
    def __deduct_money(self): ## 封装
        print('扣钱')
    def __update_user_balance(self): ## 封装
        print('更新用户余额')
    def withdraw(self):  ## 开放给用户的接口
        self.__sent_request()
        self.__deduct_money()
        self.__update_user_balance()
obj=ATM()
obj.put_your_card()
obj.withdraw()

## @property 函数使用
print("===========@property 函数使用===========")
print("案例一：没有property函数")
class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
    def bmi(self):
        return self.weight/(self.height*self.height)
albert=People('albert',75,1.80)
print(albert.bmi())

print("案例二：有property函数")
class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
    @property
    def bmi(self):
        return self.weight/(self.height*self.height)
albert=People('albert',75,1.80)
print(albert.bmi)

print("案例三：有property函数的三种方法")
class People:
    def __init__(self,name):
        self.__name=name
    @property
    def name(self):
        print('访问'.center(50,"*"))
        return self.__name
    @name.setter
    def name(self,x):
        print('修改'.center(50,"*"))
        self.__name=x
    @name.deleter
    def name(self):
        print('删除'.center(50,"*"))
        del self.__name
p=People('albert')
print(p.name)
p.name='ALBERT'
print(p.name)
del p.name
print(p.name)