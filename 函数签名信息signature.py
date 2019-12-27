from inspect import signature

def spam(x, y, z=42):
    pass
    
>>> sig = signature(spam)
>>> print(sig)
# (x, y, z=42)

# sig.bind_partial()方法来执行从指定类型到名称的部分绑定

>>>  bound_types = sig.bind_parital(int, z=int)
>>>  bound_types.arguments
# OrderedDict([('x', <class 'int'>), ('z', <class 'int'>)])  输出是一个有序字典, key是参数名，value是参数类型对象

>>>  bound_values = sig.bind(1, 2, 3)
>>>  bound_values.arguments
# OrderedDict([('x', 1), ('y', 2), ('z', 3)])

for name, value in bound_values.arguments.items():
     if name in bound_types.arguments:
         if not isinstance(value, bound_types.arguments[name]):
             raise TypeError



