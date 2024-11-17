
try:
   number = int(input("Enter a number"))
   print("The value is a ", number)

except ValueError as ex:
    print("Expection: ",ex)