weather = (1,0,0,0,1,0,0)
sundy = 0
rainy = 0
for i in range(0,7):
    if(weather[i] == 0):
        rainy += 1
        
    else:
        sundy += 1
        
if sundy > rainy:
    print("Good weather")
    
else:
    print("bad weather")
    