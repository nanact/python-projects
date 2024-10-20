print("prime numbers")

lower = int(input("Enter the lower: "))

upper = int(input("Enter the the upper: "))

for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)