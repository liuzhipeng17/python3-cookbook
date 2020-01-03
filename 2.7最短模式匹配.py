
'''
question: 查找最短的可能匹配
这个问题一般出现需要匹配一对分隔符之间的文本的时候（比如引号包含的字符串）。
'''

import re
str_pat = re.compile(r'"(.*)"')
text1 = 'Computer says "no."'
str_pat.findall(text1)  #['no.1']
text2 = 'Computer says "no." Phone says "yes."'
str_pat.findall(text2) # ['no." Phone says "Yes.']， 最长匹配

# 最短匹配，需要？修饰。
str_pat = re.compile(r'"(.*?)"')
str_pat.findall(text2) # 输出结果为['no.', 'yes.']


# 最长匹配变成最短匹配，方法是在* 或者+ 后面，加上？
