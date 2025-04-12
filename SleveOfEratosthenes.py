def SleveOfEratosthenes(num):
    prime= [True for i in range(num+1)]
    p = 2
    while (prime[p] == True):
        if (prime[p] == True):
            for i in range(p * p, num + 1,p):
                prime[i] = False
        p += 1
    
    for p in range(2, num+1):
        if prime[p]:
            print(p)

num = int(input())
print("following are prime numbers smaller")
print("than to equal to", num)
SleveOfEratosthenes(num)