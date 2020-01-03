'''
question: 你想去掉文本字符串开头，结尾或者中间不想要的字符，比如空白
solution: 
1 strip()
2 replace() 
3 正则表达式
'''
s = ' hello world \n'
s.strip()
# strip()方法只能删除开始或者结尾的字符。 默认情况下， 这些方法会去除空白字符，但是也可指定其他的字符
t = '-----hello====='
t.lstrip('-')  # 'hello====='
t.strip('-=')  # 'hello'

# strip()不会对字符串原来产生影响，只是返回处理后的字符串
# 如果想要去除掉中间的空白字符，可采用replace()
s = ' hello    world \n'
s.replace(' ', '')

# 或者用re
import re
re.sub('\s+', ' ', s)


