# 

from functools import wraps
import logging


def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging level, name is the logger name, 
    and message is the log message. If name and message aren't specified, they default to 
    the function's module and name
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__
        
        @wraps
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
            
        return wrapper
        
     return decorate
     
     
  # example use
  @logged(logging.DEBUG)
  def add(x,y):
      return x + y
      
  @logged(logging.CRITICAL, 'example'):
  def spam():
      print('spam!')
      
  # 带参数的装饰器，其实最外层的函数logged()接收参数，并将它们作用在内部的装饰器函数上面。
  
  # 内层的函数decorate()接收一个函数作为参数，然后在函数内部放置一个包装器。
  
  # 关键在于，这个包装器是可以使用传递给logged的参数logmsg
