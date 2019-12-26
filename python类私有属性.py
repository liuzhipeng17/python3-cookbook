1 单下划线开头，是内部属性

class A:
  def __init__(self):
      self._internal = 0
      self.public = 1
      
  def public_method(self):
      pass
      
  def _internal_method(self):
      pass
      
      
2 双下划线开头，是私有变量，名称的访问，变成其他形式

class B:
  def __init__(self):
      self.__private = 0
      
  def __private_method(self):
      pass
      
  def public_method(self):
      pass
      self.__private_method()
      

访问B的_private属性的时候，会被重名为_B.__private 

3 __作用在于，这种属性通过继承是无法被覆盖的

class C(B):
  def __init__(self):
      super().__init__()
      self.__private = 1 # 不会覆盖B的__private
      
  def __private_method(self):
      pass
      # 不会覆盖B的__private_method()
    

  
