'''
question: 现在有多个字典或映射，你想将它们从逻辑上合并成一个单一的映射后， 再执行某些操作，比如查找值或检查某些键是否存在。

solution: collections模块中的ChaimMap类

'''

a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])
