num = int(input("enter the number"))

t = num 

numlen = 0

while t > 0 :
    
    numlen = numlen + 1
    
    t = t//10
    
if  numlen >= 4:
       numlen = numlen // 2
       
       chk = 0
       
       while num > 0:
           ram = num % 10
           
           if chk == numlen:
               midone = ram
           elif chk == (numlen - 1):
               midtwo = ram
               
           num = int(num/10)
            
           chk = chk + 1    
           
prod = midone * midtwo
       
print("the product of mig dight are: ")
           
           
    
    
