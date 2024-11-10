
#the product of an integer and all the integers below it

def factorial(x):
    '''This is a recusize function to find the factorail of an number'''
    
    if x==0 or x==1:
        return 1
    
    else:
        return x*factorial(x - 1)
  
#doc is to call the single quotation in the fun  
print(factorial.__doc__)

print("the factorail of 0 is ",factorial(0))

print("the factorail of 1 is ",factorial(1))

print("the factorail of 23 is ",factorial(23))

print("the factorail of 34 is ",factorial(34))
    
