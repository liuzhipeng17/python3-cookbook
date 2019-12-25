'''
模块导入
graphics/
    __init__.py
    primitive/
        __init__.py
        line.py
        fill.py
        text.py
    formats/
        __init__.py
        png.py
        jpg.py

'''
1 __init__.py非空
如果你执行了语句import graphics， 文件graphics/__init__.py将被导入,建立graphics命名空间的内容。
像import graphics.format.jpg这样导入，文件graphics/__init__.py和文件graphics/formats/__init__.py将在文件graphics/formats/jpg.py导入之前导入。

大部分时候,__init__.py空着就好。 

# graphics/formats/__init__.py
from . import png
from . import jpg

这样，就可以import graphics.formats， 代替import graphics.formats.png


2 __all__ 控制全部导入时的内容

# somemodule.py
def spam():
    pass

def grok():
    pass

blah = 42
# Only export 'spam' and 'grok'
__all__ = ['spam', 'grok']


3 相对导入 

mypackage/
    __init__.py
    A/
        __init__.py
        spam.py
        grok.py
    B/
        __init__.py
        bar.py
        
 如果模块mypackage.A.spam要导入同目录下的模块grok，它应该包括的import语句如下
 from . import grok 
 
 如果模块mypackage.A.spam要导入不同目录下的模块B.bar，它应该使用的import语句如下：
 from ..B import bar  # 注意这里..B，表示../B
 
 最后，相对导入只适用于在合适的包中的模块。尤其是在顶层的脚本的简单模块中，它们将不起作用。
 
 如果包的部分，作为脚本执行，会报错
 
 python mypackage/A/spam.py
 
 另一方面，如果你使用Python的-m选项来执行先前的脚本，相对导入将会正确运行。 例如：

% python3 -m mypackage.A.spam # Relative imports work

