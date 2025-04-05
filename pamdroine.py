po = int(input("Enter your number: "))

original_number = po

reversed_number = 0

while po > 0:
    digit = po % 10
    reversed_number = reversed_number * 10 + digit
    po //= 10
    
if original_number ==  reversed_number:
    print(f"{original_number} is a pandroine")
else:
    print(f"{original_number} is not a pandroine")