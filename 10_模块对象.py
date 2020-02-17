# ! /user/bin/env python
# -*- coding: utf-8 -*-

import a.x1,a.y1

"""
1、产生一个包的名称空间
2、执行包下的__init__.py文件，将产生的名字存放于包的名称空间中
3、在当前执行文件中拿到一个名字a，该名字指向包的名称空间
"""

a.x1.func1()
a.y1.func2()

print(a.x1.func1)
print(a.y1.func2)