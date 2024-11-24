
def hotel_cost(night):
    return night*140

def Plane_cost(city):
    
    if "Charlotte" == city:
        return 183
    
    elif city == "Tempa":
        return 220
    
    elif city == "Pittsburgh":
        return 220
    
    elif "Los Angeles" == city:
        return 475
    
def rental_car_cost(days):
    if days >= 7:
        return 40*days-50
    
    elif days >= 3:
        return 40*days-20
    
    else:
        return 40*days
    
def trip_cost(night,city,days,Spending_money):
    return rental_car_cost(days)+hotel_cost(night)+Plane_cost(city)+Spending_money


    
print("Post of car rental ",rental_car_cost(5)) 

print("Plane ride cost ",Plane_cost("Los Angeles"))

print("Hotel cost ",hotel_cost(7))

print("Total cost ",trip_cost(3,"Tempa",10,199))
    