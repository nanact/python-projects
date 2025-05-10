def MaxElementArray(a):
    length = len(a)
    
    if length == 1:
        return a[0]
    
    return max(a[0],MaxElementArray(a[1:]))
a = [1,2,3,5,6,10235,778]

print("The largerst is" ,MaxElementArray(a))