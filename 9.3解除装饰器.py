# 一个装饰器已经作用于一个函数上，你想撤销他，直接访问原始的未包装的那个函数

@somedecorator
def add(x, y):
    return x + y
    
    
>>> orig_add = add.__wrapped__
>>> orig_add(3, 4)


# __wraped__访问未包装的原始函数，前提是在包装器上正确使用@wraps

# 如果有多个包装器，访问__wrapped__属性的行为是不可预知的，应避免这么做。
