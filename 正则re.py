'''
特殊字符：
1 .（点）， 默认模式下，可以匹配除了换行的任意字符； 在DOTALL模式时，可以匹配包括换行符的任意字符
2 ^ 匹配字符串的开头，
3 $ 默认模式匹配字符串尾的一个字符， 在MULTILINE模式时，匹配换行符的前一个字符
4 * 对它前面的正则式匹配0-任意次重复， 尽量多的匹配字符串（贪婪匹配），'ab*', 如果'abbbbbbbbbb'的话，得到的不是ab,和a, 而是abbbbbbbbb
5 + 对它前面的正则式匹配1-任意次重复， 尽量多的匹配字符串（贪婪匹配），'ab+', 如果'abbbbbbbbbb'的话，得到的不是ab,abb，而是abbbbbbbbb
6 ? 对它前面的正则式匹配0-1次重复，    尽量多的匹配字符串（贪婪匹配）
7 *? +? ??  
    <.*>匹配的'<a>b<c>’会得到整个字符串，而不是<a>, 在<.*?>将会仅仅匹配到<a>
8 {m} 对它前面的正则式匹配m次 a{6}表示会匹配aaaaaa
9 {m,n} 对它前面的正则式匹配m-n次，尽量多的匹配（贪婪匹配）
10 {m,n}? 对它前面的正则式，尽量少的匹配
11 [] 用于一个字符集合，在i高级和中：
    字符可以单独列出，入[amk]
    可以列出字符范围，[a-z]
    特殊字符在集合中，失去特殊含义。 [(+*)]会匹配 ( + * )
    
 12 | 
    A|B，匹配A或者B
 
 
 二  pattern对象
 1 pattern.search(string)  扫描整个string， 并返回一个相应的匹配对象match；如果没有匹配，则返回None
 2 pattern.match(string) 
 
 pattern.search(string, pos, endpos), 可以指定开始匹配位置和结束匹配位置
 
 三 匹配对象match
 1 匹配对象总有一个布尔值True，如果没有匹配的话，match和search返回None
 2 match.group()
   返回一个或多个匹配的子组，如果只有一个参数，结果是一个字符串，如果有多个参数，结果就是一个元组，每个元素对应一个项。
   
   m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist)
   m.group(0) # 整改匹配字符串, Isaac Newton
   m.group(1) # Isaac
   m.group(2) # Newton
   m.group(0, 1, 2) # ('Isaac Newton', 'Isaac', 'Newton')
   
   
 
 
 
 




















'''
