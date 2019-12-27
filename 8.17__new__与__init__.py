# 你想创建一个实例，但是希望绕过__init__()方法

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
 
 # 下面演示如何不调用__init__()方法来创建这个实例
 
 d = Date.__new__(Date)
 
 d.year # 会报错，因为没有d没有year属性
 
 data = {'year':2012, 'month':8, 'day':28}
 for key, value in data.items():
     setattr(d, key, value)
     
 
 
# 从这里可以看出__new__ 和__init__的区别

1）__new__ 返回的是一个实例， 

2）__init__返回的是None

3）__new__ 并没有对属性进行赋值，__init__有赋值
  
