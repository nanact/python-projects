def print_factors(number):
    print("The factor of", number, "are")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
            
number = int(input("What is your number"))

print_factors(number)