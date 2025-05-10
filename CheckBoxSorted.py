def CheckBoxSorted(A):
    length = len(A)
    
    if length == 1 or length == 0:
        return True
    
    return A[0] <= A[1] and CheckBoxSorted(A[1:])

a = [1,2,3,5,6,8,2]
if CheckBoxSorted(a):
    print("\nYes given array is sorted")
else:
    print("\nNo given array is not sorted")