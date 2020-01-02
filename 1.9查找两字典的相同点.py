'''
questions:
    
    怎样在两个字典中寻找相同点（比如相同的key，相同的value等）

solutions:
    
    如果序列上的值是不可变的（可哈希），那么可简单利用集合或者生成器来解决问题。
'''
    
 def dedupe(items):
     seen = set()
     for item in items:
         if item not in seen:
             yield item # 返回的是一个生成器，
             seen.add(item)
  
 a = [1,5,2,19,1,5,10]
 list(dedupe(a))
 
 # 上述方法是在序列中元素为hashable的才可用，如果序列中的元素是可以改变的，
    
 def dedupe(items, key=None):
     seen = set()
     for item in items:
         val = item if key is None else key(item)
         if val not in seen:
             yield item # 这里是yield item ,不是 yield value, 返回的不是seen集合
             seen.add(val)
            
 # 这个Key是一个函数，将item 转换成一个不可改变的值
 
 a = [{'x':1, 'y':2}, {'x':1,'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
 list(dedupe(a, key=lambda d: (d['x'], d['y'])))
             
