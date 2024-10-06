height = int(input("Enter your height in meters"))

weigth = int(input("enter your weigth"))

bmi = weigth / (height)**2

print("your BMI is",bmi)

if bmi < 0:
    print("Bro stop the lying")
    
elif bmi <=  18.8:
    print("You are underweight")

elif bmi <= 24.4:
    print("you are heatly")
    
elif bmi <= 28.8:
    print("you are overweight")
    
elif bmi <= 34.8:
    print("your over overweight")
    
elif bmi <= 39.9:
    print("your are obese")
    
else:
    print("you are the biggest human I will see on this planet")

