def add(a, b):
     
    return a + b

def subtract(a, b):
    
    return a - b

def mutliply(a, b):
    
    return a * b

def division(a, b):
    
    return a / b

print("select operator")

print("a. ADD")

print("b. Subtract")

print("c. Mutliply")

print("d. Division")

chocie = input("chose (+, -, * or x, /)")

a = int(input("First number"))

b = int(input("second number"))

if chocie == "+":
    print(add(a, b))

elif chocie == "-":
    print(subtract(a, b))
    
elif chocie == "x" or chocie == "*":
    print(mutliply(a, b))
    
elif chocie == "/":
    print(division(a, b))