medical_cause=input("did you have a medical cause Y or N: ")

atten = int(input("enter the attendance of the student: "))

if medical_cause == 'Y': 
  print ("You are allowed")
  
elif medical_cause == "n":
    if atten >= 75:
        print("allowed")
    else:
        print("not allowed")
        
else:
    print("error at line 1820 if coditional statement is not config, motion cannot attribute ")