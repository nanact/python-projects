def powerOf4(number):
    count = 0
    
    if (number & (~(number & (number - 1)))):
        while(number > 1):
            number >>= 1
            count += 1
        
        if(count % 2 == 0):
            return True
        else:
            return False
number = int(input("Enter your number: "))
if powerOf4(number):
    print("It is a number that is a power of 4")
else:
    print("it is not a number that is a power of 4")
    