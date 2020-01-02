quesiton:
    你想创建一个字典，并且在迭代或序列化这个字典的时候，能够控制元素的顺序
    
solutions:
    需要使用collections 的 OrderedDict类
    

from collections import OrderedDict

d = OrderedDict()
d['f00'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(Key, d[key])
# 输出为"foo 1", "bar 2"  "spam 3"  "grok  4"


序列化输出
import json
json.dumps(d)
# 得到的数据为'{"foo":1, "bar":2, "spam":3, "grok":4}'
    
