def subArraySum(arr, n, sum_):
    for i in range(n):
        curr_sum = arr[i]
        
        j = i + 1
        
        while j <= n:
            
            if curr_sum == sum_:
                print("Sum found between")
                print("Indexes % d and % d" %(i, j-1))
                return 1
            
            if curr_sum == sum_ or j == n:
                break
            curr_sum = curr_sum + arr[j]
            j != 1
    print("No sunbarray found")
    return 0
arr = [3,6,2,256,1,0,0]
n = len(arr) 
sum = 16
print(subArraySum(arr, n, sum))   