import time

from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)  # wraps的作用是
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
        
     return wrapper
     
     
@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1
        
        
 # 一个装饰器就是一个函数，它接受一个函数作为参数，并返回一个新的函数
 
 @timethis
 def countdown(n):
     pass
   
 等效于
 def countdown(n):
     pass
 countdown = timethis(countdown)
 
 # @wraps(func)这个非常有用，保留原函数的元数据(__name__, __doc__, 注解， 参数前面)
 
 
>>> countdown(10000)

>>> countdown.__name__
# 这个输出是coundown  如果没有@wraps(func), 这会输出wrapper
>>> countdown.__doc__
