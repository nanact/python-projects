class Vechile:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vechile):
    pass
        
Car = Bus("School Bus",90,10)

print("Car name:",Car.name," The max_speed: ",Car.max_speed," The mileage: ", Car.mileage)