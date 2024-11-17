#bye bye

valid = False

while not valid:
    try:
        n = input(int("Enter a number: "))
        
        while n%2 == 0:
            print("bye bye")
        valid = True       
    except ValueError:
        print('invaild')
        