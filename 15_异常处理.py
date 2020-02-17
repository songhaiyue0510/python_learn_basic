# ! /user/bin/env python
# # -*- coding: utf-8 -*-

"""
一、异常
异常由三部分组成：异常的追踪信息、异常的类型、异常的值

二、异常的分类
1 语法异常：SyntaxError
2 逻辑异常
3 索引异常：IndexError
4 键值对的异常：KeyError
5 属性异常：AttributeError
6 0不能被除数异常：ZerDivisionError
7 文件找不到异常：FileNotFoundError
2.8 关闭的文件不能读写异常：ValueError: I/O operation on closed file
2.9 不是整型格式的字符串转化为整型异常：ValueError: invalid literal for int() with base10
2.10 整型不可迭代异常：TypeError: 'int' object is not iterable
2.11 变量名未定义异常： NameError

三、异常处理：没有办法预测，if多分支比异常处理执行效率高
3.1 try ... except ... : try的代码块尝试捕捉异常的代码，except加可以预测/捕获到的异常种类
3.2 try ... except ... else ... : else不能单独使用，必须与except连用，else代码块会在被检测的代码没有出现任何异常的情况下执行
3.3 3.2 try ... except ... else ... finally: 无论有没有异常，finally都会执行，通常放回收资源的代码

四、主动触发异常
1、raise主动触发异常：raise TypeError(string)
2、assert断言：用于判断一个表达式，在表达式条件为 false 的时候触发异常
3、自定义异常：异常也是一个类

"""

print("========异常处理========")
try:
    print('start......')
    x=1
    y=0
    l=[]
    d={"a":1}
    d['b']
    # f=open('a.txt',mode='r',encoding='utf-8')
    print('end...')
## 罗列每种需要捕捉的异常
except NameError:
    print('变量名没有定义')
except KeyError:
    print('字典的key不存在')
except IndexError:
    print('索引超出列表的范围')

## 可以合并三种异常判断，输出结果无法准确判断具体哪一种
# except(NameError,KeyError,IndexError):
#     print('变量名没定义或者字典的key不存在或者索引超出列表范围')

# 万能异常方式
# except Exception:
#     print('万能异常')
else:
    print('没有异常')
finally:
    print('无论是否有异常，都会执行')
    # f.close() ## finally通常放回收资源的代码
print('other.....')

## 主动触发异常
print("\n")
print("========raise主动触发异常========")
print(TypeError)
obj=TypeError('类型错误')
print(obj)
class People:
    def __init__(self,name):
        if not isinstance(name,str):
            raise TypeError('用户名{}必须是str类型'.format(name))
        self.name=name
# p=People(123)
p=People('albert')

print("\n")
print("========assert主动触发异常========")
print('part1......')
print('part2......')
students=['albert','Time']
# students=[]
assert len(students)>0
print('part3....')

print("\n")
print("========自定义异常========")
class RegisterError(BaseException): ## 继承异常的基类 BaseException
    def __init__(self,massage,username):
        self.massage=massage
        self.username=username
    def __str__(self):
        return '{} {}'.format(self.username,self.massage)

obj=RegisterError('注册失败','albert')
print(obj)
## 相当于先初始化对象再打印对象
raise RegisterError('注册失败','albert')