# heapq模块有两个函数：nlargest(), nsmallest()

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

# 两个函数都能接收一个关键字参数，用于处理更复杂的数据结构

portfolio = [
{'name': 'IBM', 'shares':100, 'price':91.1},
{'name': 'AAPL', 'shares':50, 'price':543.22},
{'name': 'FB', 'shares':200, 'price':21.09},
{'name': 'HPQ', 'shares':35, 'price':31.75}
]

cheap = heapq.nlargest(3, portfolio, key=lambda x:x['price']) # 返回的是一个列表，列表元素字典
expensive = heapq.nsmallest(3, portfolio, key=lambda x:x['price'])
