# 你有一个字符串形式的方法名称，想通过它调用某个对象的对应方法

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)
        
    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)
        
 
 p = Point(2, 3)
 d = getattr(p, 'distance')(0,0)
 
 # 另外一种方法是使用operator.methodcaller()
 
 import operator
 operator.mechodcaller('distance', 0, 0)(p)
 
 
 # 调用一个方法，实际上是两部独立操作，第一步是查找属性，第二步是函数调用。
 
 # 因此，你需要通过getattr()来查找到这个属性，然后再以函数方式去调用它
 
 # 
 
    
