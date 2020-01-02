questions:
    怎样在数据字典中执行一些计算操作（最大值，最小值，排序等）
    
    
solutions:

    prices = {
      'ACME': 45.23,
      'AAPL': 612.78,
      'IBM': 205.55,
      'HPQ': 37.20,
      'FB': 10.75
    }
    
    
 为了对字典值执行计算，需要zip()将键值反转过来，
 
 min_price = min(zip(prices.values(), prices.keys()))
 # 输出为(10.75, 'FB')
 max_price = max(zip(prices.values(), prices.keys()))
 # 输出为（612.78， 'AAPL')
 
 # 字典排序
 prices_sorted = sorted(zip(prices.values(), prices.keys()))
