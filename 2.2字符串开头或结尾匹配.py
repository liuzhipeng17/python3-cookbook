'''
question: 你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀,url等
solution: str.startswith(),  str.endswith()

'''
filename = 'spam.txt'
filename.endswith('.txt')# True
filename.startswith('file:') #False

# 如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中，然后传给startswith()或endswith()

import os

filenames = os.listdir('.')
[name for name in filenames if name.endswith(('.c', '.h'))]
any(name.endswith('.py') for name in filenames)

