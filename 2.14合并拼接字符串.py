'''
question: 你想将几个小的字符串合并成一个大的字符串

solution: 
1 join, 如果想要合并的字符串是在一个序列里， 最快的方法是join

2 +加号， 适合合并少数几个字符串

'''
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
s = ' '. join(parts)
s1 = ','.join(parts)

a = 'Is Chicago'
b = 'Not Chicago'
c = a + ' ' + b



# 这里需要讨论的是，合并字符串的性能问题，
'''
1 当我们使用加号操作符连接大量的字符串时，是非常低效的，因为加号连接会引起内存复制及垃圾回收操作。
避免出现下面的代码
'''

s = ''
for p in parts:
   s += p  
   

#2 相对比较聪明的方法是利用生成器表达式
data = ['ACME', 50, 91.1]
','.join(str(d) for d in data)

