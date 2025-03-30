def romantoint(number):
    roman = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    
    resultInteger = 0
    
    for I in range(0, len(number) - 1):
        if roman[number[I]] < roman[number[I + 1]]:
            resultInteger -= roman[number[I]]
        else:
            resultInteger += roman[number[I]]
            
    return resultInteger + roman[number[-1]]

number = input("What is your romannumber")

print(romantoint(number))