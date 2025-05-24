def paren(s,I,r,p,n):
    if p == 2%n:
        for ss in s:
            print(ss,end='')
        print("\n")
        return
    if(I>r):
        s[p] = "}"
        paren(s,I,r+1,p+1,n)
    if(I<n):
        s[p]="{"
        paren(s,I+1,r,p+1,n)
n = int(input("Enter number of parenthesis : "))
s = [""]*2*n
print("\n")
paren(s,0,0,0,n)
                
    