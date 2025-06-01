def getMaxLength(a, a_size):
    counter = 0
    maxOnes  = 0
    
    for i in range(0, a_size):
        if (a[i] == 0):
            counter = 0
        
        else:
            counter += 1
            maxOnes = max(maxOnes, counter)
    return maxOnes
a = [1,1,0,0,1,0,1,0,1,1,1,1]
a_size = len(a)
print("Max 1 :",getMaxLength(a, a_size))    
    