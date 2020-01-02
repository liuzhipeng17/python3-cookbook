
questions:
    你有一个字典列表，你想根据某个或某几个字段来排序列表
    
solutions:
    通过使用operator模块的itemgetter函数。
    
rows = [
  {'fname': 'Brian', 'lname': 'Jones', 'uid':1003},
  {'fname': 'David', 'lname': 'Beazley', 'uid':1002},
  {'fname': 'John', 'lname': 'Cleese', 'uid':1001},
  {'fname': 'Big', 'lname': 'Jones', 'uid':1004},
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

rows_by_lfname = sorted(rows, key=itemgetter('lname','fname')) #

rows_by_lfname = sorted(rows, key=lambda u: (u['lname'],u['fname']))
