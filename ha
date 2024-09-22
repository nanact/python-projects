import time
import keyword
name = input("what is your name: ")
print("that is a good name",name)
age = float(input("how old are you: "))
if age < 18:
    print("you are below 18")
else:
    print("you are old")
country = input("what is you country: ")
print("processing data")
time.sleep(3)
print("\n your name is: ",name,"\n your age is: ",age,"\n you come from: ",country)
print(keyword.kwlist)