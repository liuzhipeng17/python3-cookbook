'''
question:
    你想在字符串中搜索和匹配指定的文本模式
    
solution:
    1 str.replace()
    
    2 re.sub()

'''

text = 'yeah, but no, but yeah, but no, but yeah'
text.replace('yeah', 'yep')


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# 你想将时间格式改成2012-11-27
import re
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2',text)

#sub函数中的第一个参数是被匹配的模式，第二个参数是替换的模式。 
#反斜杠\3指向前面模式的捕获组号
