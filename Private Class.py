class MyClass:
  __privateVar = 43

  def __priMETH ():
    print("I'm inside a function")
  def SayHello(self):
    print("private value is",MyClass.__privateVar)
      
oo = MyClass()
      
oo.SayHello()

oo.__priMETH()