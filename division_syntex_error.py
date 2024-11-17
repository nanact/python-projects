
try:
   num1,num2 = eval(input("Enter two number saparated by a comma"))

   Result = num1 / num2
   
   print("Result is",Result)
   
except ZeroDivisionError:
    print("Error with division with 0")
    
except SyntaxError:
    print("Comma is missing, Enter input like this 1, 2")
    
except:
    print("worng input")
    
else:
    print("no expections")