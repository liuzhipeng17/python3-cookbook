'''
question: 你想构造一个字典，是从另外字典的子集，或者从它演化而来

solution: 
1 字典推导式
2 dict((元组序列))
'''
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}


p1 = {key:value for key, value in prices.items() if value >200}
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key, value in prices.items() if key in tech_names}

t = ((key,value) for key, value in prices.items() if value > 200)
p3 = dict(t)
