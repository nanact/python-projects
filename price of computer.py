class Computer:
  def __init__(self):
      self.__maxprice = 100
      
  def sell(self):
      print("We are selling the computer for the max price of {}".format(self.__maxprice))
      
  def setMaxPrice(self,price):
      self.__maxprice = price
      
c = Computer()

c.sell()

c.__maxprice = 10000

c.sell()

c.setMaxPrice(1000)

c.sell()