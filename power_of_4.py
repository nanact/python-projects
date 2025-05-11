n = int(input("Enter your number : "))

def checkIfpower(n):
    if (n<=0):
        return False
    if(n==1):
        return True
    if (n%4==0):
        return checkIfpower(n/4)
    return False

if (checkIfpower(n)):
    print("Power of 4")
else:
    print("Power not a  of 4")