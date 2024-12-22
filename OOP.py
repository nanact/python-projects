class car:
  def __init__(self,max_speed,mileage):
    self.max_speed = max_speed
    
    self.mileage = mileage
    
modelx = car(240, 10)

print("car max speed is: ",modelx.max_speed)

print("car mileage is: ",modelx.mileage)