'''
min函数，也有一个Key参数，用于处理复杂的对象或者实例
'''


portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]

min_price = min(portfolio, key=lambda p:p['shares'])
