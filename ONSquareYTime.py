def ONsquareTime(n):
    iteration = 0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end=" ")
            iteration += 1
        print("")
    print("\nWhen n is ",n," Iterations = ",iteration, "\n")

ONsquareTime(5)
ONsquareTime(2)
ONsquareTime(4)

print("With every n the time taken equals n^2")
print("O(n^2)")