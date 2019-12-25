'''
通过文件名查找文件
'''
def findfile(start, name):
    for root, dirs, files in os.walk(start):
        if name in fiies:
            full_path =os.path.normpath(os.path.abspath(os.path.join(start, root, name)))
            

'''
os.walk(start)返回的是，(root, dirs, files)
root为相对start的目录， dirs为root下的文件夹， files为root下的文件
os.path.abspath是为了解决相对路径，转换为绝对路径
os.path.normpath是为了解决wIndows的双斜杠问题
'''


