'''
question: 你需要将一个字符串分割成多个字段，但是分隔符（还有周围的空格）并不是固定的
比如数据驱动中，需要读取excel的数据

solution: 
1 string对象的split()方法只适用于非常简单的字符串分割情形，它并不允许有多个分割符或者分割符周围不确定的空格
2 re.split()
'''

line = 'asdf fjdk; afed,  fjek,asdf, foo'
import re
re.split(r'[;,\s]\s*', line)    #分隔符可以是逗号，分号或者是空格，并且后面紧跟着任意个的空格
