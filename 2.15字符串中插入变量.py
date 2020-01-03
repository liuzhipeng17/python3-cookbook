'''
question: 你想创建一个内嵌变量的字符串， 变量被它的值所表示的字符串替换掉

solution: format()

'''

s = '{name} has {n} messages.'
b = s.format(name='Guido', n=37)
