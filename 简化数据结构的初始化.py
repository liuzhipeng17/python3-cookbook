#1 question:写了很多用作数据结构的类，不想写太多烦人的__init__函数

#2 solution:

import math

class Structure1:
     _fields = []
     
     def __init__(self, *args):
         if len(args) != len(self._fields):
             raise TypeError('Expected {} arguments'.format(len(self._fields)))
             
         for name, value in zip(self._fields, args):
             setattr(self, name, value) # 动态添加init函数的赋值
             
             
#然后使用你的类继承这个基类
class Stock(Structure1):
      _fields = ['name', 'shares', 'price']
      
class  Point(Structure1):
      _fields = ['x', 'y']
      
class Circle(Structure1):
      _fields = ['radius']
      
#使用这些类的示例

s = Stock('ACME', 50, 91.1)
p = Point(2,4)
c = Circle(4.5)
s2 = Stock('ACME',50) # 会抛出异常
