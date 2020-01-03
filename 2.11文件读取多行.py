with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)
        
 '''
 表达式 lines = (line.strip() for line in f) 执行数据转换操作。 这种方式非常高效，因为它不需要
 预先读取所有数据放到一个临时的列表中。 它仅仅是创建一个生成器，并且每次返回行之前会先执行strip操作。
 
 '''
