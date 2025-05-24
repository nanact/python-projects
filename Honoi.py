def Honoi(n, a, b, c):
    if n == 1:
        print("Move disk 1 from rod", a, "to rod", b)
        return
    Honoi(n-1,a,c,b)
    
    print("Move disk",n,"From rod",a,"to rod",b)
    
    Honoi(n-1, c , b, a)
    
n = 4
Honoi(n, "A", "C", "B")