# ! /user/bin/env python
# # -*- coding: utf-8 -*-

"""
一、反射
1、内置方法
是否类的对象：isinstance(对象名,类名）
2、反射内置函数：把字符串映射成了一个具体的属性，通过字符串来操作类与对象的属性，成为反射
hasattr，getattr，setatrr,delattr (attr是属性的意思）

二、面向对象内置方法
__str__:对象打印时自动触发，打印出对象值，而不是一个内存地址
__del__:在对象被删除时，自动执行
__call__:调用对象的时候自动执行，将本身当做第一个参数传给self

三、元类
1、exec(字符串代码,全局名空间，局部名称空间)用法：执行字符串内的代码，实现自己定制全局作用域和局部作用域
2、元类：类的类，即元类，内置元类type用来专门产生class定义的类的


"""
print("============是否类的对象============")
class Foo:
    pass
foo=Foo()
print(isinstance(foo,Foo))
print(isinstance('abc',str))

print("/n")
print("============反射内置函数：例1============")
class People:
    country='China'
    def __init__(self,name):
        self.name=name
    def tell(self):
        print("{} is aaa".format(self.name))
obj=People('Albert')
# hasattr: 判断某类是否有某个变量/函数属性
print(hasattr(People,'country'))  ## 等同于print('country' in People.__dict__)
print(hasattr(People,'tell'))
# getattr：获取某类是否有某个变量/函数属性，不存在返回None
print(getattr(People,"country1",None))
print(getattr(People,"country",None))
print(getattr(People,"tell",None))
# setattr:设置新的属性的值
setattr(People,'x',111)
print(People.x)
setattr(obj,'age',18)
print(obj.__dict__)
# delattr:删除属性
delattr(obj,'name')
print(obj.__dict__)

print("============反射内置函数：例2============")
class Foo:
    def run(self):
        while True:
            cmd=input("cmd>>: ").strip()
            if hasattr(self,cmd):
                func=getattr(self,cmd)
                func()
            elif cmd=='exit':
                break
    def download(self):
        print('download.....')
    def upload(self):
        print('upload.....')
obj=Foo()
# obj.run()

print("============exec()用法============")
code="""
x=1
y=2
"""
global_dic={}
local_dic={}
exec(code,global_dic,local_dic)
# print(global_dic)
print(local_dic)

print("============元类============")
# 类的类
class Chinese:
    country='China'
    def __init__(self,name):
        self.name=name
    def speak(self):
        print('{} speak Chinese'.format(self.name))
p=Chinese('albert')
print(type(p))
print(type(Chinese))  ## type为元类，用来产生一切class生成的类