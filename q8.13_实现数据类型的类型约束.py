
#问题： 你想定义某些属性赋值上有限制的数据结构

#解决方案： 1使用描述器实现一个系统类型和赋值验证框架

class Descriptor:
    def __init__(self,name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)
            
     
     def __set__(self, instance, value):
         instance.__dict__[self.name] = value
         

class Typed(Descriptor):
    expected_type = type(None)
    
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
            
        super().__set__(instance, value)
         
 
 class Unsigned(Descriptor):
     def __set__(self, instance, value):
         if value < 0 :
             raise ValueError('Expected >=0')
         super().__set__(instance, value)
          
 
 class MaxSized(Descriptor):
     def __init__(self, name=None, **opts):
         if 'size' not in opts:
             raise TypeError('missing size option')
         super().__init__(name, **opts)
          
      def __set__(self, instance, value):
          if len(value) >= self.size:
              raise ValueError('size must  be < ' + str(self.size))
          super().__set__(instance, value)
      
# 解决方案：2根据上面的基础构建模块，定义各种不同的数据类型

class Integer(Typed):
    expected_type = int

class UnsignedInteger(Integer, Unsigned):
    pass

class Float(Typed):
    expected_type = float
   
class UnsignedFloat(Float, Unsigned):
    pass

class String(Typed):
    expected_type = str
    
class SizedString(String, Maxsized):
    pass

    
# 解决方案：3根据自定义类型，定义一个类
class Stock:
    name = SizedString('name', size=8)
    shares = UnsignedInteger('share')
    price = UnsignedFloat('price')
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    

          
          
          
          
