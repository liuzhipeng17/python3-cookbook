# question:调用父类一个已经被覆盖的方法

# solution: 使用super()函数

class A:
    def spam(self):
        print('A.spam')
        
class B(A):
    def spam(self):
        print('B.spam')
        super().spam() # 会调用A.spam()
        

# super()函数，常用的用法，在__init__确保父类的init被执行了

class A:
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1
