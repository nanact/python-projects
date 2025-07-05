def equilibriunPoint(arr):
    leftSideSum = 0
    rightSideSum = 0
    n = len(arr)
    
    for i in range(n):
        leftSideSum = 0
        rightSideSum = 0
        for j in range(i):
            leftSideSum += arr[j]
        for j in range(i+1, n):
            rightSideSum += arr[j]
        if leftSideSum == rightSideSum:
            return i
    return -1
arr = [-7,1,5,2,-4,3,0]
print("Element :", arr[equilibriunPoint(arr)])      