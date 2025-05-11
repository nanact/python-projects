def reserseSting(s):
    
    if len(s) == 1:
        return s[0]
    firstchar = s[0]
    
    return reserseSting(s[1:]) + firstchar

s = "Ankit jadis"
print(reserseSting(s))