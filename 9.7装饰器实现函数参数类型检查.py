@typeassert(int, int)
def add(x, y):
    return x + y
    
    
    
# 下面是使用装饰器实现@typeassert

from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        if not __debug__:
            return func
     
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).agruments
        
        
            
     
