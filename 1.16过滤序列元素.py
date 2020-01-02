'''
question: 你有一个数据序列，想利用一些规则从中提取出需要的值或者缩短序列

solution: 
1 最简单的过滤序列方式：列表推导；如果输入非常大的时候，会产生一个非常大的结果集，占用大量内存。
2 生成器表达式过滤；过滤规则不能过于复杂
3 如果过滤规则过于复杂，可使用filter()函数
'''

#1 列表表达式过滤
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
[n for n in mylist if n>0]

#2 生成器表达式
pos = (n for n in mylist if n > 0)

#3 内建的filter函数
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))  # filter没有key参数
