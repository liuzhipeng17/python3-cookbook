d ={
  'a': [1,2,3],
  'b': [4,5]
}

e = {
  'a': {1,2,3},
  'e': {4,5}
}

可以采用collections模块中的defaultdict来构造这样的字典。
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(3)


创建一个多值映射字典很简单，可以自己实现，但是比较麻烦

d ={}
for key, value in paris:
    if key not in d:
        d[key] = value
        
    d[key].append(value)

如果使用defaultdict就比较简单
from collections import defaultdict

d = defaultdict(list)
for key, value in paris:
    d[key].append(value)
